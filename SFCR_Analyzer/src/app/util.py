import requests

from duckduckgo_search import DDGS


COMPANIES = [
    {"code": "10", "name": "NATIONALE-NEDERLANDEN TUnŻ S.A.", "url": "https://www.nn.pl"},
    {"code": "11", "name": "TU ALLIANZ ŻYCIE POLSKA S.A.", "url": "https://www.allianz.pl"},
    {"code": "24", "name": "UNIQA TU na ŻYCIE S.A.", "url": "https://www.uniqa.pl"},
    {"code": "27", "name": "PKO ŻYCIE TU S.A.", "url": "https://www.pkoubezpieczenia.pl"},
    {"code": "28", "name": "PZU ŻYCIE SA", "url": "https://www.pzu.pl"},
    {"code": "42", "name": "TUW REJENT-LIFE", "url": "https://www.rejentlife.com.pl"},
    {"code": "49", "name": "STUnŻ ERGO HESTIA SA", "url": "https://www.ergohestia.pl"},
    {"code": "50", "name": "TUnŻ WARTA S.A.", "url": "https://www.warta.pl"},
    {"code": "53", "name": "TU INTER-ŻYCIE POLSKA S.A.", "url": "https://www.interpolska.pl"},
    {"code": "55", "name": "COMPENSA TU na ŻYCIE S.A. Vienna Insurance Group", "url": "https://www.compensa.pl"},
    {"code": "56", "name": "GENERALI ŻYCIE T.U. S.A.", "url": "https://www.generali.pl"},
    {"code": "57", "name": "TUnŻ CARDIF POLSKA S.A.", "url": "https://www.cardif.pl"},
    {"code": "59", "name": "UNUM ŻYCIE TUiR S.A.", "url": "https://www.unum.pl"},
    {"code": "62", "name": "VIENNA LIFE TU na ŻYCIE S.A. Vienna Insurance Group", "url": "https://www.viennalief.pl"},
    {"code": "68", "name": "SALTUS TU ŻYCIE SA", "url": "https://www.saltus.pl"},
    {"code": "69", "name": "AEGON TU na ŻYCIE S.A.", "url": "https://www.aegon.pl"},
    {"code": "80", "name": "SIGNAL IDUNA ŻYCIE POLSKA TU S.A.", "url": "https://www.signal-iduna.pl"},
    {"code": "82", "name": "TU na ŻYCIE EUROPA S.A.", "url": "https://www.tueuropa.pl"},
    {"code": "93", "name": "OPEN LIFE TU ŻYCIE S.A.", "url": "https://www.openlife.pl"},
    {"code": "95", "name": "SANTANDER ALLIANZ TU na ŻYCIE S.A.", "url": "https://www.santander.allianz.pl"},
    {"code": "1209", "name": "POCZTOWE TUnŻ S.A.", "url": "https://www.pocztowenazycie.pl"},
    {"code": "1431", "name": "POLSKI GAZ TUW na ŻYCIE", "url": "https://www.polskigaztuw.pl"},
    {"code": "1448", "name": "CA ŻYCIE TU S.A.", "url": "https://www.ca-ubezpieczenia.pl"},
];


 
KEYWORDS = "sfcr" 

def search(url):
    with DDGS() as ddgs:
        return [
            result for result in ddgs.text(
                f"sfcr site:{url} filetype:pdf", max_results=1000
            )
        ]



def get_file(url, path, company):
    response = requests.get(url)
    response.raise_for_status()  

    new_path = f"{os.path.abspath(path)}/SFCR_{company.code}_{company.name}.pdf"

    with open(new_path, 'wb') as f:
        f.write(response.content)

    return new_path

