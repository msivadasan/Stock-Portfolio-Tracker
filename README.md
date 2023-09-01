# portfolio_tracker
This repository contains Python and Google script codes that enable the automated collation of stock price data, and the creation of tables and graphs for a portfolio-tracking website. 

The project relies on two programs:
1. download_stock_rev.py:  This is Python code that undertakes the following tasks: 
    
    (a) Reads in a list of stock ticker symbols, purchase date, and initial investment from a Google spreadsheet (<a href="https://docs.google.com/spreadsheets/d/1zWlWkkUg2dMRr47atKf_LoSQJQfcNj0zesH7uCwK4Co/edit?usp=sharing/" target="_blank">Portfolio Info</a>
) 
(This could be modified to a local csv file.)

    (b) Fetches stock price data (from an initial date up to the current date) using Yahoo! Finance API  for all of the ticker symbols

    (c) Plots graphs of stock prices and investment value (based on initial investment and subsequent price movements)

    (d) Saves the latest stock data in a csv file (pv.csv).

The Windows task scheduler is used (along with a bat file with the command  ...\AppData\Local\Microsoft\WindowsApps\python3.exe "...\download_stock_rev.py") to run this program daily at 7:30 PM (after New York financial markets have closed). For help with setting up the Windows task scheduler, see this <a href="https://stackoverflow.com/questions/4437701/run-a-batch-file-with-windows-task-scheduler"> StackExchange post </a>. 

2. update_csv.ps: Google script with a trigger that  run in Google spreadsheet <a href="https://docs.google.com/spreadsheets/d/1zWlWkkUg2dMRr47atKf_LoSQJQfcNj0zesH7uCwK4Co/edit?usp=sharing/" target="_blank">Portfolio Info</a>
, which updates the stock price information in sheet "updated" with the data pv.csv (created in step 1.(d) above). 

The graphs created by  download_stock_rev.py are linked in the Google sites <a href= "https://sites.google.com/view/madhavsivadasan/projects/stock-portfolio-tracker" target="_blank"> portfolio tracker page </a>.

 



        


