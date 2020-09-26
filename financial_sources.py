from string import Template

url_financials = Template('https://www.marketwatch.com/investing/stock/${ticker}/financials')
url_balance_sheet = Template('https://www.marketwatch.com/investing/stock/${ticker}/financials/balance-sheet')
url_cash_flow = Template('https://www.marketwatch.com/investing/stock/${ticker}/financials/cash-flow')

urls = {
    'Income Statement': url_financials,
    'Balance Sheet': url_balance_sheet,
    'Cash Flow Statement': url_cash_flow
}

indexes = [6,5,4,3,2]

sales_revenue = Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[1]/td[${index}]')
cost_of_goods_sold = Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[3]/td[${index}]')
depreciation_amortization_expense = Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[5]/td[${index}]')
gross_income = Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[9]/td[${index}]')
sga_expense = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[1]/td[${index}]')
non_operating_income_expense = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[8]/td[${index}]')
non_operating_interest_income = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[9]/td[${index}]')
interest_expense = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[11]/td[${index}]')
pretax_income = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[15]/td[${index}]')
income_tax = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[18]/td[${index}]')
consolidated_net_income = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[26]/td[${index}]')
minority_interest_expense = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[27]/td[${index}]')
net_income = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[28]/td[${index}]')

total_current_assets = Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[20]/td[${index}]')
total_assets = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[16]/td[${index}]')
total_liabilities = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[24]/td[${index}]')
common_equity_total = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[30]/td[${index}]')
total_shareholders_equity = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[39]/td[${index}]')
accumulated_minority_interest = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[41]/td[${index}]')
total_equity = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[42]/td[${index}]')
liabilities_shareholders_equity = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[43]/td[${index}]')

net_operating_cash_flow = Template('//*[@id="maincontent"]/div[1]/table[1]/tbody/tr[16]/td[${index}]')
net_investing_cash_flow = Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[13]/td[${index}]')
net_financing_cash_flow = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[17]/td[${index}]')
free_cash_flow = Template('//*[@id="maincontent"]/div[1]/table[3]/tbody/tr[23]/td[${index}]')

locators = {
    'Sales/Revenue': sales_revenue,
    'Cost of Goods Sold (COGS) incl. D&A': cost_of_goods_sold,
    'Depreciation & Amortization Expense': depreciation_amortization_expense,
    'Gross Income': gross_income,
    'SG&A Expense': sga_expense,
    'Interest Expense': interest_expense,
    'Pretax Income': pretax_income,
    'Income Tax': income_tax,
    'Consolidated Net Income': consolidated_net_income,
    'Minority Interest Expense': minority_interest_expense,
    'Net Income': net_income,
    'EPS (Basic)': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[38]/td[${index}]'),
    'EPS (Diluted)': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[41]/td[${index}]'),
    'EBITDA': Template('//*[@id="maincontent"]/div[1]/table[2]/tbody/tr[44]/td[${index}]'),

    'Total Current Assets': total_current_assets,
    'Total Assets': total_assets,
    'Total Liabilities': total_liabilities,
    'Common Equity (Total)': common_equity_total,
    'Total Shareholders\' Equity': total_shareholders_equity,
    'Accumulated Minority Interest': accumulated_minority_interest,
    'Total Equity': total_equity,
    'Liabilities & Shareholders\' Equity': liabilities_shareholders_equity,

    'Net Operating Cash Flow': net_operating_cash_flow,
    'Net Investing Cash Flow': net_investing_cash_flow,
    'Net Financing Cash Flow': net_financing_cash_flow,
    'Free Cash Flow': free_cash_flow,
}
