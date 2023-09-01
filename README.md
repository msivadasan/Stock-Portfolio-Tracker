# portfolio_tracker
This repository contains Python and Google script codes that enable the automated collation of stock price data, and the creation of tables and graphs for a portfolio-tracking website. 

The project relies on three programs:
1. download_stock_rev.py:  This is Python code that undertakes the following tasks: 
    (a) Reads in a list of stock ticker symbols, purchase date, and initial investment from a Google spreadsheet (PORTFOLIO_INFO.gsheet) (This could be modified to a local csv file.)
    (b) Fetches stock price data (from an initial date up to the current date) using Yahoo! Finance API  for all of the ticker symbols
    (c) Plots graphs of stock prices and investment value (based on initial investment and subsequent price movements)
    (d) Saves the latest stock data in a csv file (pv.csv).
2. Google script to be run on PORTFOLIO_INFO.gsheet, which updates the stock price information with the data pv.csv (created in step 1.(d) above).   
        
   


