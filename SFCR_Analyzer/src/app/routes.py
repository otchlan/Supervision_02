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

from src.analyzer.pdfanalyze2 import process_pdf

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
    path = data.get("path", "")
    company = data.get("company", "")

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

