from app import app, request,  jsonify, cross_origin 

from .util import COMPANIES, search, get_file

from scrapper.app import find_pdf_links, build_site_map



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
def analyze():
    data = request.json
    url = data.get('url', '')
    path = data.get("path", "")
    company = data.get("company", "")

    new_path = get_file(url, path, company)

    return jsonify({
        "Path": new_path
    })


if __name__ == '__main__':
    app.run(debug=True)

