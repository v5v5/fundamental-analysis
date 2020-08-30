# create virtual environment
py -m venv .venv
# activate virtual environment
./venv/Scripts/Activate.ps1
# install all module requirements
py create_requirements

pip install -r requirements.txt

# algorithm 
1. select next company ticker from tickers list 'tickers.txt' (for example, MOMO)
2. select next financial indicator from financial indicators list below (for example, Sales growth past 5 years)
3. get financials data from links:
- https://www.marketwatch.com/investing/stock/ccl/financials
- https://www.marketwatch.com/investing/stock/ccl/financials/balance-sheet
- https://www.marketwatch.com/investing/stock/ccl/financials/cash-flow

to calculate certain indicator value

4. calculate the indicator for the ticker and fill the indicator value in the table

| Ticker    | Sales growth past 5 years |
| -         | -                         |
| MOMO      | Value 0                   |
| TSLA      | Value 1                   |
| ...       | ...                       |
| EPAM      | Value n                   |

5. goto 2. while all indicators will be calculated
6. goto 1. while all tickers will be handled

7. select next indicator to sort the table
8. sort the table by the indicator value by descending or ascending depends on indicator (for example, for Sales growth past 5 years - BY DESCENDING, it means THE BIGGER THE BETTER) and get and save index of place for each ticker
9. goto 7. while all indicators will be handled

10. select next ticker
11. calculate sum of places for certain ticker and save as ticker points
12. goto 10.

13. sort of result table by ticker points

# know about financials indicators
request to google 'financial indicators of company'
links to help:
- https://www.scoro.com/blog/financial-kpis-for-financial-kpi-dashboard/
- https://www.investopedia.com/financial-edge/0910/6-basic-financial-ratios-and-what-they-tell-you.aspx

indicators list:
- Sales growth past 5 years
- ...