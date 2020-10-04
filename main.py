def get_tickers():
    file_tickers = './data/tickers.txt'
    with open(file_tickers, 'r') as file:
        lines = file.read().splitlines()
        return {l.replace('_SPB', '') for l in lines}


def format_number(number: str) -> float:
    if number == '-':
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

    if "B" in number:
        f *= 1e+9
    elif "M" in number:
        f *= 1e+6

    return f

import save_data

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
        locators = content.xpath(financial_data_sources.indicator_name())
        locators_names = list(
            map(lambda locator: locator.text_content().strip(), locators))
        locators_templates = {(locator_name, financial_data_sources.locator_template(locator_name))
            for locator_name in locators_names}
        save_data.save_locator_template(statement_name, locators_templates)

        for locator_name, locator_template in locators_templates:
            for year_index in financial_data_sources.indexes:
                locator_xpath = locator_template.substitute(index=year_index)
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
                save_data.save_financial_value(ticker, locator_name, number)

# tickers = get_tickers()
tickers = {'RIG','AMD'}

def collect_financials_names():
    count = len(tickers)
    for ticker in tickers:
        print(f'ticker count = {count/len(tickers)*100}%')
        count -= 1
        get_ticker_financials(ticker)
    print(f"analisys completed. ticker count = {count/len(tickers)*100}%'")

def analysis():
    pass

if __name__ == "__main__":
    collect_financials_names()
    # save_data.print_financial_statement_parameters()
