[![Build Status](https://travis-ci.com/username/repo_name.svg?branch=master)](https://travis-ci.com/username/repo_name)


# Supervision_hack 3 - SF_CRacker

## Rozruch:
Uruchomienie aplikacji za pomocą Docker:
```
docker-compose up -d --build
```

## Interfejs:
Po uruchomieniu Docker'a aplikacja dostępna jest pod adresem:
[http://localhost:3000/](http://localhost:3000/)

## Architektura aplikacji:
- **Frontend**: Znajduje się w folderze `frontend`. Zawiera całą logikę interfejsu użytkownika.
- **Backend**: Znajduje się w folderze `SFCR_Analyzer`. Zawiera logikę przetwarzania danych.

## Funkcjonalności:
- **Wyszukiwanie plików PDF**: Wykorzystuje silnik DuckDuckGo do szybkiego wyszukiwania plików PDF.
- **Eksport tabel z PDF do CSV**: Wyciąganie tabel z dokumentów PDF i zapisywanie ich jako pliki CSV.
- **Sprawdzanie zawartości sprawozdań**: Porównywanie zawartości sprawozdań na podstawie Załącznika nr 2.
- **Lista zakładów**: Przygotowana lista aktualnych zakładów ubezpieczeń.
- **Porównanie tabel rocznych**: Tabele przygotowane do porównywania danych z różnych lat.
- **Eksport obrazów tabel do uczenia maszynowego**: Wykorzystanie biblioteki img2table do przetwarzania obrazów tabel na dane do uczenia maszynowego.

## Narzędzia:
- **Analizator (analyzer)**:
  - `pdfanalyze2.py`: Wyciąga główne tabele ze sprawozdań i zapisuje je w formacie CSV.
  - `excel_writer.py`: Tworzy arkusze kalkulacyjne na podstawie plików CSV dla analizy rok do roku.
  - `DEF_BILANS-global.xlsx`: Szablon do generowania tabel bilansowych.
- **Parser (parser)**:
  - `app.py`: Wyciąga strukturę do sprawdzenia z dokumentu "Załącznik nr 2{...}.docx", następnie porównuje ją z pierwszymi stronami dokumentów PDF.
