#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deid_gate · 发布前脱敏硬闸 (Life Plugin System)

在你把任何草稿提交到公开仓库 / 发到平台之前，扫一遍常见敏感模式：
邮箱 / 电话 / 金额 / 附件直链 / 网盘链 / 账户凭证，以及可选的自定义姓名黑名单。

用法：
  python3 deid_gate.py --gate FILE
      只校验：命中敏感 → 退出码 1（拦截发布）；干净 → 退出码 0。

  python3 deid_gate.py --sanitize FILE --out OUT
      生成脱敏版（命中处替换为占位符）并打印一份命中报告。

  python3 deid_gate.py --gate FILE --names "张示例,示例公司A"
      额外把你自己的真实姓名/公司/客户名加入黑名单（不写进脚本，避免敏感入库）。

注意：这是"够用"的第一道闸，不是万能。它目前**抓不到**：未列入黑名单的真实姓名、
即时通讯号、证件号、银行卡号、物理地址、commit message、文件名。这些仍需人工复核。
"""
import sys
import re
import argparse

PATTERNS = [
    ("邮箱",      re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}"), "<EMAIL_REDACTED>"),
    ("电话/号码", re.compile(r"(?<!\d)(?:\+?\d[\d\-\s]{8,}\d)(?!\d)"),               "<PHONE_REDACTED>"),
    ("金额",      re.compile(r"(?:[$€£¥]\s?\d[\d,]*(?:\.\d+)?|(?:USD|EUR|RMB|CNY|人民币|美元)\s?\d[\d,]*(?:\.\d+)?|\d[\d,]*(?:\.\d+)?\s?(?:元|美金|刀))"), "<AMOUNT_REDACTED>"),
    ("附件直链",  re.compile(r"https?://\S+\.(?:pdf|xlsx?|docx?|zip|rar)(?:\?\S*)?", re.I), "<ATTACHMENT_URL_REDACTED>"),
    ("网盘/IM链", re.compile(r"https?://\S*(?:dingtalk|aliyun|yunpan|lark|feishu)\S*", re.I), "<ATTACHMENT_URL_REDACTED>"),
    ("账户/凭证", re.compile(r"(?:account|账户|api[_\-]?key|token|secret)\s*[:：=]\s*\S+", re.I), "<ACCOUNT_REDACTED>"),
]


def build_name_pattern(names):
    names = [n.strip() for n in names if n.strip()]
    if not names:
        return None
    return ("姓名/公司名", re.compile("|".join(re.escape(n) for n in names)), "<NAME_REDACTED>")


def preview(m):
    g = m.group(0)
    return "*" * len(g) if len(g) <= 4 else g[:2] + "*" * (len(g) - 4) + g[-2:]


DATE_RE = re.compile(r"^\+?\d{4}[-/]\d{1,2}[-/]\d{1,2}")  # ISO 日期，避免被电话规则误报


def scan(text, patterns):
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        for name, rx, _ph in patterns:
            for m in rx.finditer(line):
                if name == "电话/号码" and DATE_RE.match(m.group(0).strip()):
                    continue  # 日期不是电话
                hits.append((i, name, preview(m)))
    return hits


def sanitize(text, patterns):
    for _name, rx, ph in patterns:
        text = rx.sub(ph, text)
    return text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate")
    ap.add_argument("--sanitize")
    ap.add_argument("--out")
    ap.add_argument("--names", default="")
    args = ap.parse_args()

    patterns = list(PATTERNS)
    np = build_name_pattern(args.names.split(",")) if args.names else None
    if np:
        patterns.append(np)

    path = args.gate or args.sanitize
    if not path:
        ap.error("需 --gate FILE 或 --sanitize FILE")

    with open(path, encoding="utf-8") as f:
        text = f.read()

    hits = scan(text, patterns)
    print(f"脱敏闸扫描：{path}")
    if hits:
        print(f"❌ gate 不过：命中 {len(hits)} 处敏感模式")
        for ln, name, pv in hits[:50]:
            print(f"   L{ln:<5}{name:<12}{pv}")
    else:
        print("✅ gate 通过：未命中敏感模式")

    if args.sanitize:
        out = args.out or (path + ".脱敏.md")
        with open(out, "w", encoding="utf-8") as f:
            f.write(sanitize(text, patterns))
        print(f"已写脱敏版 → {out}")

    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main()
