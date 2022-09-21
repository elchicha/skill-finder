import cloudscraper


base_url = "https://www.indeed.com/jobs"
search_term = "customer support director"
location = "san francisco, ca"

scraper = cloudscraper.create_scraper()


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0",
    "Referer" : "https://www.indeed.com/"
    }

    
def get_search_params(search_term, location):
    params = {"q": search_term, "l": location}
    return params


def get_search_results(url, search, loc):
    params = get_search_params(search, loc)
    resp = scraper.get(url, params=params, headers=headers)
    return resp

raw_html = get_search_results(base_url, search_term, location)
print(raw_html)

