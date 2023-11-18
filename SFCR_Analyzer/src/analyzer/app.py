import PyPDF2
import re
from docx import Document

# Funkcja do ekstrakcji tekstu ze strony PDF
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        for page in reader.pages:
            text.append(page.extract_text())
        return text


# Funkcja do ekstrakcji tekstu z dokumentu .docx
def extract_text_and_contents_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = []
        contents = []

        for page_num, page in enumerate(reader.pages):
            page_text = page.extract_text()
            text.append(page_text)

            # Wyszukaj potencjalne wpisy spisu treści na stronie
            if re.search(r'(Spis treści|Contents|Rozdział)', page_text, re.IGNORECASE):
                contents.append((page_num + 1, page_text))

        return text, contents

# Funkcja do sprawdzania, czy struktura z załącznika znajduje się w pliku PDF
def check_structure_in_pdf(pdf_text, structure):
    structure_found = {}
    for section in structure:
        if re.search(re.escape(section), pdf_text, re.IGNORECASE):
            structure_found[section] = True
        else:
            structure_found[section] = False
    return structure_found

def extract_text_from_docx(docx_path):
    try:
        doc = Document(docx_path)
        for table in doc.tables:
            for row in table.rows:
                if len(row.cells) > 2:  # Sprawdzenie, czy wiersz ma co najmniej 3 komórki
                    print(row.cells[2].text)  # Wydrukowanie tekstu z trzeciej komórki
    except Exception as e:
        print(f"Błąd podczas ekstrakcji tabeli z pliku .docx: {e}")

def find_pages_with_keyword(pdf_path, keyword):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        forms_pages = []

        for i, page in enumerate(reader.pages):
            tekst = page.extract_text()
            if tekst and re.search(keyword, tekst, re.IGNORECASE):
                forms_pages.append(i)

        return forms_pages


def find_and_display_pages_with_keyword(pdf_path, keyword):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        pages_with_keyword = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and re.search(keyword, text, re.IGNORECASE):
                pages_with_keyword.append(i)
                print(f"--- Page {i + 1} ---")
                print(text)
                print("\n\n")

        return pages_with_keyword


# Ścieżki do plików
pdf_path = 'NNTUNZ2021.pdf'
docx_path = 'z2-struktura.docx'

# Wywołanie funkcji
try:
    extract_text_from_docx(docx_path)
except FileNotFoundError:
    print(f"Nie znaleziono pliku: {docx_path}")
except Exception as e:
    print(f"Wystąpił błąd: {e}")

# Ekstrakcja struktury z załącznika nr 2
#TODO dwa razy się wyświetla struktura - czy to problem z wyświetlaniem, czy z funkcją
#structure = extract_text_from_docx(docx_path)


# Wyszukaj strony z formularzami ilościowymi
forms_pages = find_pages_with_keyword(pdf_path, 'Formularze ilościowe')

print("Strony zawierające 'Formularze ilościowe':", forms_pages)

# Search for pages with "Quantitative Templates" and display their content
#find_and_display_pages_with_keyword(pdf_path, 'Quantitative Templates')


# Ekstrakcja tekstu z pliku PDF
#pdf_text, pdf_contents = extract_text_and_contents_from_pdf(pdf_path)

#print("Spis treści:")
#for page_num, content in pdf_contents:
#    print(f"Strona --- {page_num}:")
#    print("--- content")
#    print(content)
#    print("---")

# Sprawdzenie, czy struktura z załącznika znajduje się w pliku PDF
#structure_check = check_structure_in_pdf(pdf_text, structure)

# Wydruk wyników sprawdzenia dla każdej sekcji
#for section, found in structure_check.items():
#    print(f"Sekcja '{section}': {'znaleziona' if found else 'nie znaleziona'}")
