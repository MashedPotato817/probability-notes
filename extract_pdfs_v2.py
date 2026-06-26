# -*- coding: utf-8 -*-
import pdfplumber
import os

pdf_files = [
    "笔记 2026年6月16日.pdf",
    "2021-2022_答案解析.pdf",
    "2022-2023_答案解析.pdf",
    "2023-2024_答案解析.pdf",
    "期末考试试卷.pdf"
]

# 输出到文件
with open("pdf_content.txt", "w", encoding="utf-8") as f:
    for pdf_file in pdf_files:
        try:
            with pdfplumber.open(pdf_file) as pdf:
                f.write(f"\n{'='*80}\n")
                f.write(f"文件: {pdf_file}\n")
                f.write(f"页数: {len(pdf.pages)}\n")
                f.write(f"{'='*80}\n")
                
                for i, page in enumerate(pdf.pages):
                    text = page.extract_text()
                    if text:
                        f.write(f"\n--- 第{i+1}页 ---\n")
                        f.write(text)
                        f.write("\n")
                        
                # 提取表格
                f.write(f"\n--- 表格提取 ---\n")
                for i, page in enumerate(pdf.pages):
                    tables = page.extract_tables()
                    if tables:
                        for j, table in enumerate(tables):
                            f.write(f"\n第{i+1}页 表格{j+1}:\n")
                            for row in table:
                                f.write(str(row) + "\n")
                                
        except Exception as e:
            f.write(f"读取 {pdf_file} 时出错: {e}\n")
            import traceback
            f.write(traceback.format_exc())

print("PDF内容已提取到 pdf_content.txt")