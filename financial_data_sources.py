from string import Template

statement_income = 'Income Statement'
statement_balance_sheet = 'Balance Sheet'
statement_cash_flow = 'Cash Flow Statement'

url_income_statement = Template(
    'https://www.marketwatch.com/investing/stock/${ticker}/financials')
url_balance_sheet = Template(
    'https://www.marketwatch.com/investing/stock/${ticker}/financials/balance-sheet')
url_cash_flow_statement = Template(
    'https://www.marketwatch.com/investing/stock/${ticker}/financials/cash-flow')

urls = {
    statement_income: url_income_statement,
    statement_balance_sheet: url_balance_sheet,
    statement_cash_flow: url_cash_flow_statement,
}

indexes = [6, 5, 4, 3, 2]

sales_revenue = Template(
    '//td[normalize-space()="Sales/Revenue"]/../td[${index}]')
cost_of_goods_sold = Template(
    '//td[normalize-space()="Cost of Goods Sold (COGS) incl. D&A"]/../td[${index}]')
depreciation_amortization_expense = Template(
    '//td[normalize-space()="Depreciation & Amortization Expense"]/../td[${index}]')
gross_income = Template(
    '//td[normalize-space()="Gross Income"]/../td[${index}]')
sga_expense = Template(
    '//td[normalize-space()="SG&A Expense"]/../td[${index}]')
equity_in_affiliates_pretax = Template(
    '//td[normalize-space()="Equity in Affiliates (Pretax)"]/../td[${index}]')
non_operating_income_expense = Template(
    '//td[normalize-space()="Non Operating Income/Expense"]/../td[${index}]')
non_operating_interest_income = Template(
    '//td[normalize-space()="Non-Operating Interest Income"]/../td[${index}]')
interest_expense = Template(
    '//td[normalize-space()="Interest Expense"]/../td[${index}]')
pretax_income = Template(
    '//td[normalize-space()="Pretax Income"]/../td[${index}]')
income_tax = Template('//td[normalize-space()="Income Tax"]/../td[${index}]')
consolidated_net_income = Template(
    '//td[normalize-space()="Consolidated Net Income"]/../td[${index}]')
minority_interest_expense = Template(
    '//td[normalize-space()="Minority Interest Expense"]/../td[${index}]')
net_income = Template('//td[normalize-space()="Net Income"]/../td[${index}]')
eps_basic = Template('//td[normalize-space()="EPS (Basic)"]/../td[${index}]')
eps_diluted = Template(
    '//td[normalize-space()="EPS (Diluted)"]/../td[${index}]')
ebitda = Template('//td[normalize-space()="EBITDA"]/../td[${index}]')

total_current_assets = Template(
    '//td[normalize-space()="Total Current Assets"]/../td[${index}]')
total_assets = Template(
    '//td[normalize-space()="Total Assets"]/../td[${index}]')
total_liabilities = Template(
    '//td[normalize-space()="Total Liabilities"]/../td[${index}]')
common_equity_total = Template(
    '//td[normalize-space()="Common Equity (Total)"]/../td[${index}]')
total_shareholders_equity = Template(
    '//td[normalize-space()="Total Shareholders\' Equity"]/../td[${index}]')
accumulated_minority_interest = Template(
    '//td[normalize-space()="Accumulated Minority Interest"]/../td[${index}]')
total_equity = Template(
    '//td[normalize-space()="Total Equity"]/../td[${index}]')
liabilities_shareholders_equity = Template(
    '//td[normalize-space()="Liabilities & Shareholders\' Equity"]/../td[${index}]')

net_operating_cash_flow = Template(
    '//td[normalize-space()="Net Operating Cash Flow"]/../td[${index}]')
net_investing_cash_flow = Template(
    '//td[normalize-space()="Net Investing Cash Flow"]/../td[${index}]')
net_financing_cash_flow = Template(
    '//td[normalize-space()="Net Financing Cash Flow"]/../td[${index}]')
free_cash_flow = Template(
    '//td[normalize-space()="Free Cash Flow"]/../td[${index}]')


def indicator_name() -> str:
    # return '//tr/td[1]/text()[normalize-space()!=""]'
    return '//tr/td[1]'


def locator_template(locator_name: str) -> Template:
    return Template(f'//td[normalize-space()="{locator_name}"]/../td[${{index}}]')


locators_income_statement = {
    'Sales/Revenue': sales_revenue,
    'Cost of Goods Sold (COGS) incl. D&A': cost_of_goods_sold,
    'Depreciation & Amortization Expense': depreciation_amortization_expense,
    'Gross Income': gross_income,
    'SG&A Expense': sga_expense,
    'Equity in Affiliates (Pretax)': equity_in_affiliates_pretax,
    'Interest Expense': interest_expense,
    'Pretax Income': pretax_income,
    'Income Tax': income_tax,
    'Consolidated Net Income': consolidated_net_income,
    'Minority Interest Expense': minority_interest_expense,
    'Net Income': net_income,
    'EPS (Basic)': eps_basic,
    'EPS (Diluted)': eps_diluted,
    'EBITDA': ebitda,
}

locators_balance_sheet = {
    'Total Current Assets': total_current_assets,
    'Total Assets': total_assets,
    'Total Liabilities': total_liabilities,
    'Common Equity (Total)': common_equity_total,
    'Total Shareholders\' Equity': total_shareholders_equity,
    'Accumulated Minority Interest': accumulated_minority_interest,
    'Total Equity': total_equity,
    'Liabilities & Shareholders\' Equity': liabilities_shareholders_equity,
}

locators_cash_flow_statement = {
    'Net Operating Cash Flow': net_operating_cash_flow,
    'Net Investing Cash Flow': net_investing_cash_flow,
    'Net Financing Cash Flow': net_financing_cash_flow,
    'Free Cash Flow': free_cash_flow,
}

locators = {
    statement_income: locators_income_statement,
    statement_balance_sheet: locators_balance_sheet,
    statement_cash_flow: locators_cash_flow_statement,
}
