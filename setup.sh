#!/bin/bash

# Tworzenie głównego katalogu projektu
mkdir -p SFCR_Analyzer

cd SFCR_Analyzer

# Tworzenie podkatalogów
mkdir -p data
mkdir -p docs
mkdir -p src
mkdir -p tests

# Tworzenie struktury modułów w src/
cd src
mkdir -p scrapper
mkdir -p downloader
mkdir -p parser
mkdir -p analyzer
mkdir -p utils

# Tworzenie plików __init__.py dla każdego modułu
touch scrapper/__init__.py
touch downloader/__init__.py
touch parser/__init__.py
touch analyzer/__init__.py
touch utils/__init__.py

# Tworzenie plików specyficznych dla modułów
touch parser/text_parser.py
touch parser/image_parser.py
touch parser/table_parser.py
touch analyzer/completeness_checker.py
touch analyzer/auditor_opinion_analyzer.py
touch analyzer/change_analyzer.py
touch utils/utils.py

# Powrót do głównego katalogu SFCR_Analyzer
cd ..

# Tworzenie plików w głównym katalogu
touch requirements.txt
touch README.md

# Tworzenie plików testowych
cd tests
touch test_scrapper.py
touch test_downloader.py
touch test_parsers.py
touch test_analyzers.py

echo "Struktura projektu SFCR_Analyzer została utworzona."
