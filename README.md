# Stock Portfolio Tracker
This repository contains Python and Google script codes that enable the automated collation of stock price data, and the creation of tables and graphs for a portfolio-tracking website. 

The project relies on two programs:
1. <a href="https://github.com/msivadasan/portfolio_tracker/blob/main/download_stock_rev.py"> download_stock_rev.py </a>:  This is Python code that undertakes the following tasks: 
    
    (a) Reads in a list of stock ticker symbols, purchase date, and initial investment from the Google spreadsheet <a href="https://docs.google.com/spreadsheets/d/1zWlWkkUg2dMRr47atKf_LoSQJQfcNj0zesH7uCwK4Co/edit?usp=sharing/" target="_blank">Portfolio Info</a>. (This could be modified to a local csv file.)

    (b) Fetches stock price data (from an initial date up to the current date) using Yahoo! Finance API  for all of the ticker symbols.

    (c) Plots graphs of stock prices and investment value (based on initial investment and subsequent price movements).

    (d) Saves the latest stock data in a csv file (pv.csv).

The Windows task scheduler is used to run batch file daily around 7:30 PM (after New York financial markets have closed). The.bat file has the following commands:

call %cd%\Anaconda3\Scripts\activate.bat

cd "%path-to-directory%"

python "%path-to-code%\download_stock_rev.py"

For help with setting up the Windows task scheduler, see this <a href="https://stackoverflow.com/questions/4437701/run-a-batch-file-with-windows-task-scheduler"> StackExchange post </a>. 

2. <a href="https://github.com/msivadasan/portfolio_tracker/blob/main/update_csv.gs"> update_csv.gs</a>: Google script with a time trigger set to run daily in the Google spreadsheet <a href="https://docs.google.com/spreadsheets/d/1zWlWkkUg2dMRr47atKf_LoSQJQfcNj0zesH7uCwK4Co/edit?usp=sharing/" target="_blank">Portfolio Info</a> around 9:30PM (to leave a sufficient gap for the <a href="https://github.com/msivadasan/portfolio_tracker/blob/main/download_stock_rev.py"> download_stock_rev.py </a> program to have been run by the Windows task scheduler around 7:30PM).  This code updates the stock price information with the data from pv.csv (created in step 1(d) above). 

The table with information on the stock portfolio in the Google spreadsheet <a href="https://docs.google.com/spreadsheets/d/1zWlWkkUg2dMRr47atKf_LoSQJQfcNj0zesH7uCwK4Co/edit?usp=sharing/" target="_blank">Portfolio Info</a>, as well as the graphs created by   <a href="https://github.com/msivadasan/portfolio_tracker/blob/main/download_stock_rev.py"> download_stock_rev.py </a> can be linked to a webpage, which would serve as a dynamically (daily) updated portfolio-tracking website.  I linked these to my Google sites <a href= "https://sites.google.com/view/madhavsivadasan/projects/stock-portfolio-tracker" target="_blank"> portfolio tracker page </a>.

 



        


