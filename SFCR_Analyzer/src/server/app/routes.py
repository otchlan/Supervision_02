from app import app, jsonify, cross_origin 


from scrapper.app import find_pdf_links



@app.route('/sitemap', methods=['GET'])
@cross_origin()
def sitemap():

    data = {
        'message': 'Mapa witryny',
        'status': 'success'
    }

    return jsonify(data)

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url', '')

    analysis_result = {
        'url': url,
        'analysis': 'Tutaj będą wyniki analizy'
    }

    return jsonify(analysis_result)

if __name__ == '__main__':
    app.run(debug=True)

