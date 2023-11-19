from flask import request, jsonify, send_file
import requests
import os

# Assuming 'app' is imported from your 'app' module
from app import app, cross_origin

# Other imports
from .util import COMPANIES, search, get_file
from scrapper.app import find_pdf_links, build_site_map

import logging
logging.basicConfig(level=logging.DEBUG)

import pdfplumber
import pandas as pd
import numpy as np
from openpyxl import load_workbook

import tarfile

import shutil

def clear_directory(directory_path):
    """
    Clear all files and subdirectories in a specified directory.

    Args:
    directory_path (str): Path of the directory to clear.
    """
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            logging.error(f'Failed to delete {file_path}. Reason: {e}')

def create_archive(source_dir, archive_path):
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

    logging.info(f"Archive created at {archive_path}")

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

def process_pdf(file_name):
    file_path = os.path.join('/app', 'input', f'{file_name}')

    tables_dict = {}
    tableNumber = 0
    pageNumber = 0
    tables_set = ['02.01.02','05.01.02', '05.01.02.01', '05.01.02.02','05.02.01', '05.02.01.01', '05.02.01.02', '05.02.01.03', '05.02.01.04', '05.02.01.05', '05.02.01.06','12.01.02', '12.01.02.01','17.01.02', '17.01.02.01','19.01.21', '19.01.21.01', '19.01.21.02', '19.01.21.03', '19.01.21.04','22.01.21', '22.01.21.01','23.01.01', '23.01.01.01', '23.01.01.02','25.01.21', '25.01.21.01', '25.01.21.02', '25.01.21.03', '25.01.21.04', '25.01.21.05','25.02.21', '25.02.21.01', '25.02.21.02', '25.02.21.03', '25.02.21.04', '25.02.21.05','25.03.21', '25.03.21.01', '25.03.21.02', '25.03.21.03', '25.03.21.04', '25.03.21.05','28.01.01', '28.01.01.01', '28.01.01.02', '28.01.01.03', '28.01.01.04', '28.01.01.05','28.02.01', '28.02.01.01', '28.02.01.02', '28.02.01.03', '28.02.01.04', '28.02.01.05',]

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

@app.route('/sitemap', methods=['POST'])
@cross_origin()
def sitemap():
    data = request.json
    url = data.get("url", "")


    links = search(url)
#    links = build_site_map(url, url) 

    data = {
        'links': links,
    }

    return jsonify(data)


@app.route('/companies', methods=['GET'])
@cross_origin()
def companies():
    data = {
        'companies': COMPANIES,
    }

    return jsonify(data)


@app.route('/analyze', methods=['POST'])
@cross_origin()
def analyze():
    logging.debug("Received request for /analyze")
    data = request.json
    url = data.get('url', '')

    if url:
        logging.info(f"Downloading file from URL: {url}")
        r = requests.get(url)
        if r.status_code == 200:
            filename = url.split('/')[-1] if '/' in url else 'downloaded_file'

            # Save file to the input directory in the Docker container
            input_dir = os.path.join('/app', 'input', filename)
            os.makedirs(os.path.dirname(input_dir), exist_ok=True)

            with open(input_dir, 'wb') as file:
                file.write(r.content)
                logging.info(f"File saved to {input_dir}")

            # Call the processing function from pdfanalyze2.py
            process_pdf(filename)

            # Create a tar.gz archive of the output directory
            archive_name = f"/app/output/{filename}.tar.gz"
            create_archive('/app/output', archive_name)

            # Clear the input and output directories
            clear_directory('/app/input')
            clear_directory('/app/output')

            return jsonify({"Status": "OK", "Message": f"File processed. Archive created at {archive_name}"})
        else:
            logging.error(f"Failed to download the file. Status code: {r.status_code}")
            return jsonify({"Status": "Error", "Message": "Failed to download the file"})
    else:
        logging.warning("No URL provided in the request")
        return jsonify({"Status": "Error", "Message": "No URL provided"})

        # zip_file to spakowane pliki w
        #return send_file(zip_file, mimetype="file/zip")

        #funk find_pdf_links
        #wyslij pliki .csv

if __name__ == '__main__':
    app.run(debug=True)

