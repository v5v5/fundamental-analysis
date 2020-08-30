# Create virtual environment
py -m venv .venv
# Activate virtual environment
./venv/Scripts/Activate.ps1
# Install all module requirements
py create_requirements

pip install -r requirements.txt

# Algorithm 
1. Select next company ticker from tickers list 'tickers.txt' (for example, MOMO)
2. Select next financial indicator from financial indicators list below (for example, Sales growth past 5 years)
3. Get financials data from links:
- https://www.marketwatch.com/investing/stock/ccl/financials
- https://www.marketwatch.com/investing/stock/ccl/financials/balance-sheet
- https://www.marketwatch.com/investing/stock/ccl/financials/cash-flow

to calculate certain indicator value

4. Calculate the indicator for the ticker and fill the indicator value in the table

| Ticker    | Sales growth past 5 years |
| -         | -                         |
| MOMO      | Value 0                   |
| TSLA      | Value 1                   |
| ...       | ...                       |
| EPAM      | Value n                   |

5. Goto 2. while all indicators will be calculated
6. Goto 1. while all tickers will be handled

7. Select next indicator to sort the table
8. Sort the table by the indicator value by descending or ascending depends on indicator (for example, for Sales growth past 5 years - BY DESCENDING, it means THE BIGGER THE BETTER) and get and save index of place for each ticker
9. Goto 7. while all indicators will be handled

10. Select next ticker
11. Calculate sum of places for certain ticker and save as ticker points
12. Goto 10.

13. Sort of result table by ticker points

# Know about financials indicators
Request to google 'financial indicators of company'
links to help:
- https://www.scoro.com/blog/financial-kpis-for-financial-kpi-dashboard/
- https://www.investopedia.com/financial-edge/0910/6-basic-financial-ratios-and-what-they-tell-you.aspx

Fundamental indicators list:
- Sales growth past 5 years (DESC, the bigger the better)
- ...
Technical indicators list:
- Performance for last three month (ASC, the lower the better)
- Performance for last month (ASC, the lower the better)
- Performance for last week (ASC, the lower the better)
- ...