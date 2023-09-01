"""
Created on Sun Oct 17 16:23:29 2021
@author: Madhav Sivadasan
"""
########################################################################################
#Import various python libraries/programs
import pandas as pd
import datetime as dt
from datetime import date
from datetime import datetime
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.lines as mlines
from matplotlib.dates import DateFormatter
########################################################################################
#How to read in a sheet from google sheets: https://towardsdatascience.com/read-data-from-google-sheets-into-pandas-without-the-google-sheets-api-5c468536550 
# Read from sheet #https://docs.google.com/spreadsheets/d/1zWlWkkUg2dMRr47atKf_LoSQJQfcNj0zesH7uCwK4Co/edit?usp=sharing
sheet_id = "1zWlWkkUg2dMRr47atKf_LoSQJQfcNj0zesH7uCwK4Co"
sheet_name = "Stocks"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dd=pd.read_csv(url, parse_dates=['PurchaseDate'],dayfirst=True) #Reads in data from "url" into a dataframe 
dd=dd.dropna(axis='rows') ##To drop columns/rows with missing values
tickers=dd[["Ticker"]]
dop=dd[["PurchaseDate"]]
inv=dd[["Investment"]]
########################################################################################
def myfigures(matrix, col, counter, legend1, legend2, legendon, name):
    fig, ax=plt.subplots()
    ax.plot(matrix[:,0].astype(np.datetime64), matrix[:,4], label=legend2)
    ax.xaxis.set_tick_params(rotation=60, labelsize=8)
    date_form = DateFormatter("%m-%d-%y")
    ax.xaxis.set_major_formatter(date_form)
    tmin=min(matrix[:,4])
    tmax=max(matrix[:,4])
    plt.vlines(dop.iloc[counter,0],tmin,tmax)
    plt.title((dd.iloc[counter,0]))
    blck_line = mlines.Line2D([], [], color='black', markersize=15, label=legend1)
    first_legend = plt.legend(handles=[blck_line], loc='lower left')
    # Add the legend manually to the current Axes.
    if legendon==1:
        plt.gca().add_artist(first_legend)
        plt.legend(loc='upper right')
    cc=str(name)+str(ii)+ str(".png")
    plt.savefig(cc, bbox_inches='tight')
    print("This is Fig:", counter)
    plt.show()
###########################################################################
##This is code to import stock price data from Yahoo Finance    
##I follow advice from "How to download from Yahoo! Finance: https://pythonrepo.com/repo/ranaroussi-yfinance-python-finance"
invvalues={}
for ii in range (0, len(dop)):
    today = date.today()
    xx = yf.download(tickers=tickers.iloc[ii,0], start=datetime(2021, 1, 1), end=today)
    print(xx)
    xx['ticker']=str(tickers.iloc[ii,0]) #Adds the ticker symbol as column 1 in dataframe

    #######################################################################################
    #Here I plot graphs for each of the stocks
    #Information on how to plot: https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html 
    # Documentation on matplotlib: https://matplotlib.org/stable/users/index.html
    #https://stackoverflow.com/questions/13187778/convert-pandas-dataframe-to-numpy-array/ 
    kk=xx.reset_index() #This is to change the first column of dates to an ordinary variable
    ##To plot from 30 days before purchase date
    temp=dop.iloc[ii,0] - dt.timedelta(days=30)
    trunckk = kk[kk['Date'] >= (temp)] # trunckk has prices from pdate-30 to today
    purchprice= kk[kk['Date'] == dop.iloc[ii,0]].iloc[0,4]
    tr2kk=kk[kk['Date'] >= dop.iloc[ii,0]]
    invv=tr2kk[['Date']]
    name="InvestValue" +str(ii)
    invv[name]=(tr2kk['Close']*(inv.iloc[ii,0])/purchprice)
    ivdfname="ivdf"+str(ii)
    invvalues[ivdfname]=invv
    npaa = trunckk.to_numpy()
    #https://stackoverflow.com/questions/1574088/plotting-time-in-python-with-matplotlib
    #dates = matplotlib.dates.date2num(npaa["Date"])
    legend2="Stock Price"
    legend1="Purchase Date"
    myfigures(npaa, 4, ii, legend1, legend2, 1, "fig")

################################################################################
##The code below merges data for the different stocks.I do a merge by date to allow for different purchase dates for different stocks (i.e., I merge by the date across stocks)
dfallinv=invvalues['ivdf0']
for ii in range (1,len(dop)):
    name="ivdf"+str(ii)
    n2="InvestValue"+str(ii)
    dfallinv=pd.merge(dfallinv, invvalues[name], how='outer', left_on='Date', right_on='Date')
################################################################################
## The code below plots portfolio value graphs for each of the stocks.  I am not showing these on the webpage currently for each stock, but I could use if needed
dfvv = dfallinv.to_numpy()
for ii in range (0,len(dop)):
    #https://stackoverflow.com/questions/1574088/plotting-time-in-python-with-matplotlib
    #dates = matplotlib.dates.date2num(npaa["Date"])
    fig, ax=plt.subplots()
    ax.plot(dfvv[:,0].astype(np.datetime64), dfvv[:,ii+1], label="Portfolio Value")
    ax.xaxis.set_tick_params(rotation=60, labelsize=8)
    date_form = DateFormatter("%m-%d-%y")
    ax.xaxis.set_major_formatter(date_form)
    tmin=min(dfvv[:,ii+1])
    tmax=max(dfvv[:,ii+1])
    plt.vlines(dop.iloc[ii,0],tmin,tmax)
    plt.title((dd.iloc[ii,0]+str(":Portfolio Value")))
    blck_line = mlines.Line2D([], [], color='black', markersize=15, label='Purchase Date')
    cc=str("vfig")+str(ii)+ str(".png")
    plt.savefig(cc, bbox_inches='tight')
    plt.show()
################################################################################
#The code below adds the values across each of the stocks, and then plots the figure of the portfolio value
dfallinv['PValue']=dfallinv['InvestValue0']
for ii in range (1,len(dop)):
    dfallinv['PValue']=dfallinv['PValue']+dfallinv["InvestValue"+str(ii)]
   
dfvv = dfallinv.to_numpy()
fig, ax=plt.subplots()
ax.plot(dfvv[:,0].astype(np.datetime64), dfvv[:,len(dop)+1], label="PortfolioValue")
ax.xaxis.set_tick_params(rotation=60, labelsize=8)
date_form = DateFormatter("%m-%d-%y")
ax.xaxis.set_major_formatter(date_form)
tmin=min(dfvv[:,len(dop)+1])
tmax=max(dfvv[:,len(dop)+1])
plt.vlines(dop.iloc[ii,0],tmin,tmax)
plt.title(("Overall Portfolio Value"))
cc=str("pvfig")+str(".png")
plt.savefig(cc, bbox_inches='tight')
plt.show()
##########################################################################
#This code collects the information for each stock for the latest trading date
pv= dfallinv.iloc[[0,-1]]
lasttdate=pv['Date'].iloc[1]
for ii in range (0,len(dop)):
    nn='InvestValue'+str(ii)
    pv = pv.rename(columns={nn: dd.iloc[ii,0]})
    pv.round({dd.iloc[ii,0]:2})
pv.round({"PValue":2})
pv = pv.rename(columns={"PValue": "Overall Portfolio Value"})
pvt=pv.set_index("Date").transpose()
pvt['II']=np.arange(len(pvt))
pvt=pvt.reset_index().set_index("II")
pvt["Purchase Date"]=dop
column_indices = [0,1,2]
new_names = ['Stock','Initial Value',"Latest Trade Value"]
old_names = pvt.columns[column_indices]
pvt.rename(columns=dict(zip(old_names, new_names)), inplace=True)
pvt['Latest Trade Date']=lasttdate
pvt=pvt[['Stock',"Purchase Date", 'Initial Value','Latest Trade Date', "Latest Trade Value"]]
pvt.to_csv("pv.csv", index=False, float_format='%.2f')
####################################################################
