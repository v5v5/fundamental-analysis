def get_tickers():
    file_tickers = './data/tickers.txt'
    with open(file_tickers, 'r') as file:
        lines = file.readlines()
    return {l.replace('_SPB', '') for l in lines}

def analysis():
    tickers = get_tickers()
    for ticker in tickers:
        print(ticker, end='')

analysis()