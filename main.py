def get_tickers():
    file_tickers = './data/tickers.txt'
    with open(file_tickers, 'r') as file:
        lines = file.readlines()
    return {l.replace('_SPB', '') for l in lines}

def get_ticker_financials():
    import requests
    from lxml import html
    import financial_sources

    page = requests.get(financial_sources.url_financials)
    source_code = html.fromstring(page.content) 

    for key, value in financial_sources.locators.items():
        print(key, ':', source_code.xpath(value.substitute(index=financial_sources.indexes[0]))[0].text)

def analysis():
    # tickers = get_tickers()
    # for ticker in tickers:
        ticker = 'BMRN'
        # financials = get_ticker_financials()
        get_ticker_financials()
        print(ticker, end='')

if __name__ == "__main__":
    analysis()