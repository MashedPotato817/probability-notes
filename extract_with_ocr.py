# -*- coding: utf-8 -*-
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# 方法1: 使用pypdf提取
from pypdf import PdfReader

pdf_files = [
    "笔记 2026年6月16日.pdf",
    "2021-2022_答案解析.pdf",
    "2022-2023_答案解析.pdf",
    "2023-2024_答案解析.pdf",
    "期末考试试卷.pdf"
]

print("="*80)
print("使用pypdf提取PDF内容")
print("="*80)

for pdf_file in pdf_files:
    try:
        reader = PdfReader(pdf_file)
        print(f"\n{'='*60}")
        print(f"文件: {pdf_file}")
        print(f"页数: {len(reader.pages)}")
        print(f"{'='*60}")
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                print(f"\n--- 第{i+1}页 ---")
                print(text[:2000] if len(text) > 2000 else text)  # 限制输出长度
    except Exception as e:
        print(f"读取 {pdf_file} 时出错: {e}")

print("\n" + "="*80)
print("检查PDF是否为扫描件...")
print("="*80)

# 检查PDF是否有可提取的文字
for pdf_file in pdf_files[:1]:  # 只检查第一个文件
    try:
        reader = PdfReader(pdf_file)
        total_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                total_text += text
        print(f"\n{pdf_file}:")
        print(f"提取的文字长度: {len(total_text)}")
        if len(total_text) < 100:
            print("可能是扫描PDF，需要OCR处理")
        else:
            print("成功提取文字内容")
    except Exception as e:
        print(f"检查 {pdf_file} 时出错: {e}")