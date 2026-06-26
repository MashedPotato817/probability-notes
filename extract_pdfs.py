import pdfplumber
import os
import sys

# 设置UTF-8编码输出
sys.stdout.reconfigure(encoding='utf-8')

pdf_files = [
    "笔记 2026年6月16日.pdf",
    "2021-2022_答案解析.pdf",
    "2022-2023_答案解析.pdf",
    "2023-2024_答案解析.pdf",
    "期末考试试卷.pdf"
]

all_content = {}

for pdf_file in pdf_files:
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = ""
            for i, page in enumerate(pdf.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n=== 第{i+1}页 ===\n"
                    text += page_text
            all_content[pdf_file] = text
            print(f"\n{'='*60}")
            print(f"文件: {pdf_file}")
            print(f"{'='*60}")
            print(text)
    except Exception as e:
        print(f"读取 {pdf_file} 时出错: {e}")