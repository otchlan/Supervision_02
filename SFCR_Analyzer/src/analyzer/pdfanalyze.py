import os
import pdfplumber
import pandas as pd
import numpy as np


def pad_dataframe(dframe, total_columns):
    additional_cols = total_columns - dframe.shape[1]
    empty_cols = pd.DataFrame(np.nan, index=dframe.index, columns=[f'Empty_{z}' for z in range(additional_cols)])
    return pd.concat([empty_cols, dframe], axis=1)

current_dir = os.path.dirname(__file__)  # Gets the directory where the script is located
src_dir = os.path.dirname(current_dir)  # Moves up to the 'src' directory
project_dir = os.path.dirname(src_dir)  # Moves up to the main project directory
file_path = os.path.join(project_dir, 'docs', 'ALLIANZ 2021.pdf')

#file_path = "c:/supervision_source/strona_air.pdf"  # Replace with your file path
tables = []
tables_dict = {}
tableNumber = 0
pageNumber = 0
tables_set = ['02.01.02', '05.01.02', '05.01.02.01', '05.01.02.02', '05.02.01', '05.02.01.01', '05.02.01.02',
              '05.02.01.03', '05.02.01.04', '05.02.01.05', '05.02.01.06', '5.05.01.02', '12.01.02', '12.01.02.01',
              '17.01.02.01']

table_settings = {
    "vertical_strategy": "lines",  # or 'explicit' or 'lines'
    "horizontal_strategy": "lines"
}

max_columns = 0

with pdfplumber.open(file_path) as pdf:
    for page in pdf.pages:
        pageNumber += 1
        page_content = page.extract_text()

        for search_text in tables_set:
            if search_text in page_content:
                print(f'Extracting page {pageNumber}')
                # Extract tables from each page
                page_tables = page.extract_tables(table_settings)
                for table in page_tables:
                    print(f'Extracting table {tableNumber}')
                    df = pd.DataFrame(table[0:], columns=table[0])
                    tables_dict[search_text].append(df)
                    if df.shape[1] > max_columns:
                        max_columns = df.shape[1]
                    tableNumber += 1

print(f'Tables extracted: {tableNumber}')

merged_tables = []
i = 0

while i < len(tables):
    current_table = tables[i]
    #print(f'Current table: {i}')

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

merged_table_final = []

for i, df in enumerate(merged_tables):
    df_reset = df.reset_index(drop=True)
    if df.shape[1] == max_columns:
        merged_table_final.append(df_reset)
    else:
        merged_table_final.append(pad_dataframe(df_reset, max_columns))

print('Final table : ')
print(merged_table_final)

all_rows = []
for df in merged_table_final:
    df = pad_dataframe(df, max_columns)  # Ensure padding is applied correctly
    all_rows.extend(df.values.tolist())  # Extend the list with the DataFrame's rows

# Create a new DataFrame from the list of rows
final_df = pd.DataFrame(all_rows, columns=[f'Column_{i}' for i in range(max_columns)])

filename = f'final_table_{tableNumber}.csv'
final_df.to_csv(filename, index=False)
print(f'Saved: {filename}')
print(final_df)




