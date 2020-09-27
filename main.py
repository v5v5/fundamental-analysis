def get_tickers():
    file_tickers = './data/tickers.txt'
    with open(file_tickers, 'r') as file:
        lines = file.read().splitlines()
        return {l.replace('_SPB', '') for l in lines}


def format_number(number: str) -> float:
    if (number == '-'):
        raise ValueError()

    n = number.replace(
        '(', '-'
    ).replace(
        ')', ''
    ).replace(
        'B', ''
    ).replace(
        'M', ''
    ).replace(
        ',', ''
    ).replace(
        '%', ''
    )

    f = float(n)

    if ("B" in number):
        f *= 1e+9
    elif ("M" in number):
        f *= 1e+6

    return f


def get_ticker_financials(ticker):
    import requests
    from lxml import html
    import financial_data_sources

    print(f'--- TICKER: {ticker} ---')
    for statement_name, url in financial_data_sources.urls.items():
        print(f'--- STATEMENT: {statement_name} ---')
        link = url.substitute(ticker=ticker)

        try:
            page = requests.get(link)
        except:
            print(f'Can not get page from url {link}')
            continue
        content = html.fromstring(page.content)

        # locators = financial_sources.locators[statement_name]
        locators = content.xpath(financial_data_sources.indicator_name())
        # for locator_name, locator_xpath in locators.items():
        for locator in locators:
            locator_name = locator.text_content().strip()
            year_index = financial_data_sources.indexes[0]
            # xpath = locator_xpath.substitute(index=year_index)
            locator_template = financial_data_sources.locator_template(locator_name)
            locator_xpath = locator_template.substitute(index=year_index)
            # TODO save locator_name
            # ...
            # TODO save xpath (locator_xpath)
            # ...
            try:
                value = content.xpath(locator_xpath)[0].text_content()
            except Exception:
                print(f'{locator_name}: NOT EXISTS')
                continue

            try:
                number = format_number(value)
            except ValueError:
                print(f'{locator_name}: -')
                continue
            except:
                print(f'{locator_name}: CAN NOT FORMAT THE VALUE \'{value}\'')
                continue

            print(f'{locator_name}: {number}')


def analysis():
    # tickers = get_tickers()
    # for ticker in tickers:
    # ticker = 'CMA'
    ticker = 'TSLA'
    get_ticker_financials(ticker)


if __name__ == "__main__":
    analysis()
