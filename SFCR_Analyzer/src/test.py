from duckduckgo_search import DDGS

with DDGS() as ddgs:
    results = [r for r in ddgs.text(f"site:www.allianz.pl filetype:pdf ")]
    print(results)
