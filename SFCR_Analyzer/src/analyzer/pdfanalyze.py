import os
import pdfplumber
import pandas as pd

current_dir = os.path.dirname(__file__)  # Gets the directory where the script is located
src_dir = os.path.dirname(current_dir)  # Moves up to the 'src' directory
project_dir = os.path.dirname(src_dir)  # Moves up to the main project directory
file_path = os.path.join(project_dir, 'docs', 'AEGON 2022.pdf')


# file_path = "./SFCR_Analyzer/docs/AEGON 2022.pdf"  # Replace with your file path
tables = []
tableNumber = 0
pageNumber = 0

with pdfplumber.open(file_path) as pdf:
    for page in pdf.pages:
        pageNumber += 1

        table_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "lines"
        }

        print(f'Extracting page {pageNumber}')
        # Extract tables from each page
        page_tables = page.extract_tables(table_settings)
        for table in page_tables:
            print(f'Extracting table {tableNumber}')
            df = pd.DataFrame(table[1:], columns=table[0])
            tables.append(df)
            tableNumber += 1

print(f'Tables extracted: {tableNumber}')

merged_tables = []
i = 0

while i < len(tables) - 2:
    current_table = tables[i]
    print(f'Current table: {i}')

    if current_table.empty:
        i += 1
        continue

    # Add your logic here to check if the next table is a continuation
    # For example, check if the headers are the same
    while i + 1 < len(tables) and not tables[i].empty and not tables[i+1].empty and tables[i + 1].iloc[0].equals(current_table.iloc[0]):
        # Merge tables
        print(f'Merging tables {i} and {i+1}')
        current_table = pd.concat([current_table, tables[i + 1][1:]])
        i += 1

    merged_tables.append(current_table)
    i += 1

print(f'Tables merged: {len(merged_tables)}')





