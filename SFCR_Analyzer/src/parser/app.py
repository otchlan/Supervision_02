import PyPDF2
import re
from docx import Document
import os

# Funkcja do ekstrakcji tekstu ze strony PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return text

# Funkcja do ekstrakcji tekstu z dokumentu .docx


# Funkcja do sprawdzania, czy struktura z załącznika znajduje się w pliku PDF
def check_structure_in_pdf(pdf_text, structure):
    structure_found = {}
    for section in structure:
        # Pomijanie kodu sekcji (np. "C.5 ") i wzięcie tylko tekstu po pierwszej spacji
        section_text = ' '.join(section.split(' ')[1:])
        if re.search(re.escape(section_text), pdf_text, re.IGNORECASE):
            structure_found[section] = True
        else:
            structure_found[section] = False
    return structure_found

# Funkcja do wyświetlania tabel z pliku .docx
def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        text = []  # Lista do przechowywania tekstu
        for table in doc.tables:
            for i, row in enumerate(table.rows):
                if i == 0:
                    continue  # Pomijanie pierwszego wiersza
                if len(row.cells) > 2:
                    text.append(row.cells[2].text.strip())  # Dodawanie tekstu do listy
        return text
    except Exception as e:
        print(f"Błąd podczas ekstrakcji tabeli z pliku .docx: {e}")
        return []  # Zwracanie pustej listy w przypadku błędu

def check_toc_structure_in_pdf(pdf_path, structure, toc_pages):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            toc_text = ' '.join([reader.pages[i].extract_text() for i in toc_pages])
            structure_found = {section: re.search(re.escape(section), toc_text, re.IGNORECASE) is not None for section in structure}
            return structure_found
    except Exception as e:
        print(f"Błąd podczas przetwarzania pliku PDF: {e}")
        return {}

def extract_toc_from_pdf(pdf_path, toc_pages):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            toc_text = ''
            for page_num in toc_pages:
                toc_text += reader.pages[page_num].extract_text() + '\n'
            return toc_text
    except Exception as e:
        print(f"Błąd podczas ekstrakcji spisu treści z pliku PDF: {e}")
        return ""

def to_frontend():
    # Ścieżki do plików
    current_dir = os.path.dirname(__file__)  # Katalog, w którym znajduje się skrypt
    project_dir = os.path.dirname(os.path.dirname(current_dir))  # Główny katalog projektu
    pdf_path = os.path.join(project_dir, 'docs', 'NN TUNZ 2021.pdf')  # Pełna ścieżka do pliku PDF

    docx_path = os.path.join(current_dir, 'Zal2.docx')  # Ścieżka do pliku .docx w tym samym katalogu co skrypt

    # Ekstrakcja struktury z załącznika nr 2
    structure = extract_text_from_docx(docx_path)
    for line in structure:
        print(line)

    # Wywołanie funkcji
    #try:
    #    wyciagnij_tabele_z_docx(docx_path)
    #except FileNotFoundError:
    #    print(f"Nie znaleziono pliku: {docx_path}")
    #except Exception as e:
    #    print(f"Wystąpił błąd: {e}")


    print("---")
    print("---")
    print("---")


    # Zakres stron, na których znajduje się spis treści (zakładając, że znajduje się na stronach 0-4)
    toc_pages = range(0, 5)  # Zaktualizuj zakres stron zgodnie z rzeczywistym rozmieszczeniem spisu treści

    # Wywołanie funkcji
    toc_text = extract_toc_from_pdf(pdf_path, toc_pages)
    print("Spis treści z pliku PDF:")
    print(toc_text)


    print("---")
    print("---")
    print("---")


    structure = extract_text_from_docx(docx_path)
     try:
         pdf_text = ' '.join(extract_text_from_pdf(pdf_path))
     except FileNotFoundError:
         print(f"Nie znaleziono pliku PDF: {pdf_path}")
         pdf_text = ""

     structure_check = check_structure_in_pdf(pdf_text, structure)

     # Tworzenie tabeli wyników
     table_results = []
     for section in structure:
         section_text = ' '.join(section.split(' ')[1:])  # Pomijanie kodu sekcji
         found_text = "znaleziona" if structure_check.get(section, False) else "nie znaleziona"
         table_results.append({'section': section_text, 'status': found_text})

     return table_results
