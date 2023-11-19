import os
import pdfplumber
import pandas as pd
import numpy as np
from openpyxl import load_workbook
from excel_writer import write_to_excel


def pad_dataframe(dframe, total_columns):
    additional_cols = total_columns - dframe.shape[1]
    empty_cols = pd.DataFrame(np.nan, index=dframe.index, columns=[f'Empty_{z}' for z in range(additional_cols)])
    return pd.concat([empty_cols, dframe], axis=1)

def print_table(search_text, merged_tables):
    if search_text in merged_tables:
        print(f"Merged table for {search_text}:")
        print(merged_tables[search_text])
    else:
        print(f"No table found for {search_text}.")


file_name = 'UNIQA 2021'
file_extension = 'pdf'

# Assuming that the file_path is correctly pointing to the file in the 'docs' directory
file_path = os.path.join('/app', 'docs', f'{file_name}.{file_extension}')

tables_dict = {}
tableNumber = 0
pageNumber = 0
tables_set = ['02.01.02',
              '05.01.02', '05.01.02.01', '05.01.02.02',
              '05.02.01', '05.02.01.01', '05.02.01.02', '05.02.01.03', '05.02.01.04', '05.02.01.05', '05.02.01.06',
              '12.01.02', '12.01.02.01',
              '17.01.02', '17.01.02.01',
              '19.01.21', '19.01.21.01', '19.01.21.02', '19.01.21.03', '19.01.21.04',
              '22.01.21', '22.01.21.01',
              '23.01.01', '23.01.01.01', '23.01.01.02',
              '25.01.21', '25.01.21.01', '25.01.21.02', '25.01.21.03', '25.01.21.04', '25.01.21.05',
              '25.02.21', '25.02.21.01', '25.02.21.02', '25.02.21.03', '25.02.21.04', '25.02.21.05',
              '25.03.21', '25.03.21.01', '25.03.21.02', '25.03.21.03', '25.03.21.04', '25.03.21.05',
              '28.01.01', '28.01.01.01', '28.01.01.02', '28.01.01.03', '28.01.01.04', '28.01.01.05',
              '28.02.01', '28.02.01.01', '28.02.01.02', '28.02.01.03', '28.02.01.04', '28.02.01.05',
              ]

table_settings = {
    "vertical_strategy": "lines",  # or 'explicit' or 'lines'
    "horizontal_strategy": "lines"
}

with pdfplumber.open(file_path) as pdf:
    for page in pdf.pages:
        pageNumber += 1
        page_content = page.extract_text()

        for search_text in tables_set:
            if search_text in page_content:
                print(f'Extracting page {pageNumber} for {search_text}')
                page_tables = page.extract_tables(table_settings)

                for table in page_tables:
                    print(f'Extracting table {tableNumber}')
                    df = pd.DataFrame(table[1:], columns=table[0])

                    if search_text not in tables_dict:
                        tables_dict[search_text] = [df]
                    else:
                        tables_dict[search_text].append(df)

                    tableNumber += 1

max_columns_dict = {search_text: 0 for search_text in tables_set}
merged_tables_dict = {}

for search_text, table_list in tables_dict.items():
    # Compute the maximum number of columns for each search_text
    for df in table_list:
        max_columns_dict[search_text] = max(max_columns_dict[search_text], df.shape[1])

    all_rows = []
    for df in table_list:
        padded_df = pad_dataframe(df, max_columns_dict[search_text])
        all_rows.extend(padded_df.values.tolist())  # Convert DataFrame to list of rows and extend the list

    # Create a new DataFrame from the list of rows
    if all_rows:
        merged_tables_dict[search_text] = pd.DataFrame(all_rows, columns=[f'Column_{i}' for i in
                                                                          range(max_columns_dict[search_text])])
    else:
        merged_tables_dict[search_text] = pd.DataFrame()


print(f"Total tables extracted: {tableNumber}")

for search_text, merged_table in merged_tables_dict.items():
    if not merged_table.empty:
        output_csv_filename = os.path.join('/app', 'output', f"{file_name}-{search_text}.csv")
        merged_table.to_csv(output_csv_filename, index=False)
        print(f"Saved table for '{search_text}' as '{output_csv_filename}'")
    else:
        print(f"No table to save for '{search_text}' (empty table).")


# Example to print tables for a specific search_text
specific_search_text = '02.01.02'  # For example
print_table(specific_search_text, merged_tables_dict)

# Writing to excel file
#print('Writing to Excel')
#write_to_excel(file_name, merged_tables_dict)



