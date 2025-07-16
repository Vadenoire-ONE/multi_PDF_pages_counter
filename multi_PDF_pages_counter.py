# -*- coding: utf-8 -*-
import os
from PyPDF2 import PdfReader

def count_pdf_pages_in_folder(folder_path):
    """
    Подсчитывает общее количество страниц во всех PDF файлах в папке и подпапках
    """
    total_pages = 0
    pdf_files_count = 0
    pdf_files_info = []
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files_count += 1
                file_path = os.path.join(root, file)
                try:
                    reader = PdfReader(file_path)
                    pages_count = len(reader.pages)
                    total_pages += pages_count
                    pdf_files_info.append({
                        'file': file,
                        'path': file_path,
                        'pages': pages_count
                    })
                    print(f"OK {file}: {pages_count} страниц")
                except Exception as e:
                    print(f"ОШИБКА при чтении файла {file}: {e}")
    
    return pdf_files_count, total_pages, pdf_files_info

def generate_report(folder_path):
    """
    Генерирует подробный отчет о PDF файлах в папке
    """
    print(f"Анализ папки: {folder_path}")
    print("=" * 60)
    
    pdf_count, total_pages, files_info = count_pdf_pages_in_folder(folder_path)
    
    print("\n" + "=" * 60)
    print("ИТОГОВЫЙ ОТЧЕТ")
    print("=" * 60)
    print(f"Найдено PDF файлов: {pdf_count}")
    print(f"Общее количество страниц: {total_pages}")
    
    if files_info:
        print(f"Среднее количество страниц на файл: {total_pages/pdf_count:.1f}")
        
        # Топ-5 самых больших файлов
        sorted_files = sorted(files_info, key=lambda x: x['pages'], reverse=True)
        print("\nСамые объемные файлы:")
        for i, file_info in enumerate(sorted_files[:5], 1):
            print(f"{i}. {file_info['file']}: {file_info['pages']} страниц")

# Использование
if __name__ == "__main__":
    # Текущая папка где находится скрипт
    folder_path = "."
    
    # Проверяем существование папки
    if os.path.exists(folder_path):
        generate_report(folder_path)
    else:
        print(f"Папка {folder_path} не найдена!")
