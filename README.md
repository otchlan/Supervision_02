Supervision_hack 3 -> task 02: #SF_CRacker

# Rozruch:
docker-compose up -d --build

po odpaleniu się docker'a wejść na
http://localhost:3000/

Frontend aplikacji odzielony jest od backendu aplikacji
Cała logika FE znajduje się w folderze: **frontend**
Funkcjonalności aplikacji
Funkcjonalności

- Szybkie wyszukiwanie plików PDF dzięki silnikowi duckduckgo
- Wycąganie tabel z PDFów i zapisywanie ich w postaci CVS
- Sprawdzanie zawartości sprawozdania na podstawie Załącznika nr. 2
- Przygotowana lista aktualnych zakładów
- Przygotowane tabele pod porównywanie poprzednich lat
- Wyciąganie z PDFów obrazów tabeli i przygotowanie takowych danych do uczenia maszynowego (wykorzystujemy nową bibloteke img2table)
- Cała logika BE znajduje się w folderze: **SFCR_Analyzer**

Narzędzia do przetwarzania plików znajdują się w folderze **src**
Wewnątrz tego folderu znajdują się foldery:
**analyzer** który zawiera pliki
- pdfanalyze2.py - plik zawiera kod który wyciąga główne tabele ze sprawozdań i zapisuje je w formacie .csv
- excel_writer.py - towrzy na podstawie plików .csv arkusz kalkulacyjny który można potem wykorzystać do analizy zprawozdań rok do roku
- DEF_BILANS-global.xlsx - szablon z którego wychodzi każda tabela bilansowa
**parser** który zawiera:
- app.py - plik wyciąga strukturę do sprawdzenia z "Załączkik nr 2{...}.docx", następnie pobiera kilka pierwszych stron z .pdf i porównuje, czy zgadza się.
