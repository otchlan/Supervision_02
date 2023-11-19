from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = [r for r in ddgs.text(f"\"Sprawozdanie z badania\"site:www.warta.pl filetype:pdf ")]

    print(results)
