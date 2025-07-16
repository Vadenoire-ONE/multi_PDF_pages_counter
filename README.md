# Multi-PDF Page Counter

A simple Python script to recursively scan a directory, count the total number of pages in all PDF files, and generate a summary report.

## Overview

This script is designed to help users quickly assess the volume of PDF documents in a folder and its subfolders. It iterates through all files, identifies PDFs, counts their pages, and provides a consolidated report. This is particularly useful for tasks like estimating printing costs, digital archiving, or data analysis of document collections.

## Features

*   **Recursive Scanning:** Scans the script's current directory and all of its subdirectories.
*   **Page Counting:** Accurately counts the pages of each `.pdf` file.
*   **Real-time Logging:** Provides a live log in the console, showing which files are being processed and their page counts.
*   **Robust Error Handling:** Gracefully skips corrupted, password-protected, or unreadable PDF files and reports the error without crashing.
*   **Comprehensive Summary:** Generates a final report with:
    *   Total number of PDF files found.
    *   Grand total of all pages.
    *   Average pages per file.
*   **Top 5 Report:** Lists the top 5 largest documents by page count, making it easy to spot the most voluminous files.

## Requirements

*   Python 3.x
*   `PyPDF2` library

### Installation

1.  Make sure you have Python 3 installed.
2.  Install the required `PyPDF2` library using pip:
    ```bash
    pip install PyPDF2
    ```

## How to Use

1.  Place the `multi_PDF_pages_counter.py` script into the root folder you want to analyze.
2.  Open a terminal or command prompt in that folder.
3.  Run the script:
    ```bash
    python multi_PDF_pages_counter.py
    ```
4.  The script will automatically start scanning and will print the results directly to the console when finished.

## How It Works: Step-by-Step Algorithm

The script follows a clear and logical process to achieve its goal:

1.  **Initialization**: The script starts by initializing counters for the total number of pages and the total number of PDF files to zero. It also creates an empty list to store details of each processed PDF.

2.  **Directory Traversal**: It uses Python's built-in `os.walk('.')` function to "walk" through the directory tree, starting from the current directory (`.`) where the script is located. This process visits every folder and subfolder.

3.  **File Identification**: In each directory, it loops through all the files. For each file, it checks if the filename (converted to lowercase) ends with the `.pdf` extension.

4.  **PDF Processing and Page Counting**: If a PDF file is identified:
    *   A `try...except` block is used to handle potential errors.
    *   **Try**: It attempts to open the file using the `PdfReader` from the `PyPDF2` library.
    *   It retrieves the number of pages by checking the length of the `reader.pages` object (`len(reader.pages)`).
    *   This page count is added to the `total_pages` grand total.
    *   Details about the file (name, path, page count) are stored for the final report.
    *   A success message (`OK {file}: {pages} страниц`) is printed to the console.
    *   **Except**: If `PyPDF2` fails to read the file (e.g., the file is encrypted, corrupted, or not a valid PDF), it catches the exception, prints an error message (`ОШИБКА...`), and continues to the next file without stopping the program.

5.  **Report Generation**: After the script has scanned all files and folders, it prints a final, formatted summary report containing:
    *   The total number of PDF files found.
    *   The grand total of all pages from all valid files.
    *   The calculated average number of pages per file.
    *   A sorted list of the **Top 5 largest files** by page count.

## Sample Output

*Note: The script's console output is in Russian.*

```
Анализ папки: .
============================================================
OK annual-report-2023.pdf: 150 страниц
OK project_proposal.pdf: 25 страниц
ОШИБКА при чтении файла corrupted-file.pdf: PdfReadError('File has not been decrypted')
OK user_manual_v1.pdf: 312 страниц
OK small-document.pdf: 4 страниц

============================================================
ИТОГОВЫЙ ОТЧЕТ
============================================================
Найдено PDF файлов: 4
Общее количество страниц: 491
Среднее количество страниц на файл: 122.8

Самые объемные файлы:
1. user_manual_v1.pdf: 312 страниц
2. annual-report-2023.pdf: 150 страниц
3. project_proposal.pdf: 25 страниц
4. small-document.pdf: 4 страниц
```