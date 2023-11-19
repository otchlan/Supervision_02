import requests

from duckduckgo_search import DDGS

COMPANIES = [
        {"name": "NATIONALE-NEDERLANDEN TUnŻ S.A.", "url": "https://www.nn.pl"},
        {"name": "TU ALLIANZ ŻYCIE POLSKA S.A.", "url": "https://www.allianz.pl"},
        {"name": "UNIQA TU na ŻYCIE S.A.", "url": "https://www.uniqa.pl"},
        {"name": "PKO ŻYCIE TU S.A.", "url": "https://www.pkoubezpieczenia.pl"},
        {"name": "PZU ŻYCIE SA", "url": "https://www.pzu.pl"},
        {"name": "TUW REJENT-LIFE", "url": "https://www.rejentlife.com.pl"},
        {"name": "STUnŻ ERGO HESTIA SA", "url": "https://www.ergohestia.pl"},
        {"name": "TUnŻ WARTA S.A.", "url": "https://www.warta.pl"},
        {"name": "TU INTER-ŻYCIE POLSKA S.A.", "url": "https://www.interpolska.pl"},
        {"name": "COMPENSA TU na ŻYCIE S.A. Vienna Insurance Group", "url": "https://www.compensa.pl"},
        {"name": "GENERALI ŻYCIE T.U. S.A.", "url": "https://www.generali.pl"},
        {"name": "TUnŻ CARDIF POLSKA S.A.", "url": "https://www.cardif.pl"},
        {"name": "UNUM ŻYCIE TUiR S.A.", "url": "https://www.unum.pl"},
        {"name": "VIENNA LIFE TU na ŻYCIE S.A. Vienna Insurance Group", "url": "https://www.viennalife.pl"},
        {"name": "SALTUS TU ŻYCIE SA", "url": "https://www.saltus.pl"},
        {"name": "AEGON TU na ŻYCIE S.A.", "url": "https://www.aegon.pl"},
        {"name": "SIGNAL IDUNA ŻYCIE POLSKA TU S.A.", "url": "https://www.signal-iduna.pl"},
        {"name": "TU na ŻYCIE EUROPA S.A.", "url": "https://www.tueuropa.pl"},
        {"name": "OPEN LIFE TU ŻYCIE S.A.", "url": "https://www.openlife.pl"},
        {"name": "SANTANDER ALLIANZ TU na ŻYCIE S.A.", "url": "https://www.santander.allianz.pl"},
        {"name": "POCZTOWE TUnŻ S.A.", "url": "https://www.pocztowenazycie.pl"},
        {"name": "POLSKI GAZ TUW na ŻYCIE", "url": "https://www.polskigaztuw.pl"},
        {"name": "CA ŻYCIE TU S.A.", "url": "https://www.ca-ubezpieczenia.pl"}
    ]


 
KEYWORDS = "sfcr" 


def search(url):
    with DDGS() as ddgs:
        return [
            result for result in ddgs.text(
                f"sfcr site:{url} filetype:pdf", max_results=1000
            )
        ]


KEYWORDS = ["Sprawozdanie z badania", 
"Sprawozdanie niezależnego biegłego rewidenta z badania", 
"Opinia niezależnego biegłego rewidenta",
"Sprawozdanie biegłego rewidenta z badania"]

def search_statement(url):
    with DDGS() as ddgs:
        try:
            ret = set(())
            for keyword in KEYWORDS:
                res = {
                    result for result in ddgs.text(
                        f"\"{keyword}\" site:{url} filetype:pdf", max_results=100
                    )
                }
                ret |= res
            return ret
        except:
            return [
                result for result in ddgs.text(
                    f"\"sprawozdanie z badania\" site:{url} filetype:pdf", max_results=100
                )
            ]
        
def get_file(url):
    response = requests.get(url)
    response.raise_for_status()  

    return response.content

print(search_statement("pzu.pl"))