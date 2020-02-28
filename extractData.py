import pandas_datareader.data as web
import pandas as pd

def extractData(stocks, start, end):

    source = 'yahoo'

    data = pd.DataFrame()

    for symbol in stocks:
        try:
            data[symbol] = web.DataReader(symbol, data_source=source, start=start, end=end)['Adj Close']
        except:
            error = f"Ticker Symbol {symbol} cannot be found"
            print(error)

    data = data.asfreq('M', method='pad')
    print(data)


stocks = ['ACN', 'DIS', 'COST', 'INTC', 'JPM',	'V', 'XOM', 'JNJ', 'BSX', 'CPB']
start = '2010-01-01'
end = '2016-01-01'
extractData(stocks, start, end)