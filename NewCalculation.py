import pandas as pd
import pandas_datareader.data as web
import numpy as np
import xlrd
import datetime
import math



time_frame = 10
risk_free_rate = 0.0152
portfolio_ticker = ['ACN', 'DIS', 'COST', 'INTC', 'JPM',	'V', 'XOM', 'JNJ', 'BSX', 'CPB']
portfolio_distribution = [0.1371,	0.1009,	0.1941,	0.0645,	0.0577,	0.2613,	0.00, 0.1236, 0.0546, 0.0063]
filename = "data.csv"

def processData(timeFrame, RFR, ticker, filename):

    #CONSTS
    time_frame = timeFrame
    risk_free_rate = RFR
    portfolio_ticker = ticker
    portfolio_dict = dict(zip(portfolio_ticker, portfolio_distribution))


    def string_date(t):
        x = datetime.datetime(t[0], t[2], t[1])
        return x.strftime("%d-%m-%Y")

    #open excel file and create dataframe
    loc = (filename)

    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)

    data = pd.DataFrame()


    tupledates = list(map(lambda x: xlrd.xldate_as_tuple(x, 0), sheet.col_values(0)[1:]))
    dates = list(map(lambda x: string_date(x), tupledates))

    data["date"] = dates

    for i in range(1, len(sheet.row_values(0))):
        ticker = sheet.cell_value(0, i)
        data[ticker] = sheet.col_values(i)[1:]

    data.set_index(['date'], inplace=True)


    #create dataframe with only min and max data
    min_max = data.iloc[[0, -1]]

    #take max - min data and convert it into a list
    avg_returns = list((min_max / min_max.shift(-1)).iloc[0])
    avg_returns = list(map(lambda x: (x ** (1/time_frame) - 1), avg_returns))

    #get returns table with numpy
    allReturns = data / data.shift(-1) - 1

    #use returns table to get standard deviation
    std_dev_list = allReturns.std(axis = 0, skipna = True)
    std_dev_list = list(map(lambda x: x * math.sqrt(12), std_dev_list))


    #calculate excess returns
    excessReturns = pd.DataFrame()

    for ticker in portfolio_ticker:
        excessReturns[ticker] = (allReturns.loc[:, ticker] - allReturns.loc[:, ticker].mean())


    #calculate covariance with excess returns
    cov_matrix = pd.DataFrame()

    #create index header
    cov_matrix[""] = portfolio_ticker
    cov_matrix.set_index('', inplace=True)

    #Fill covariance table
    for col in range(len(portfolio_ticker)):
        new_col = []
        for row in range(len(portfolio_ticker)):
            if row > col:
                new_col.append((excessReturns[portfolio_ticker[row]] * excessReturns[portfolio_ticker[col]]).sum()/120)
            else:
                new_col.append(np.nan)
        cov_matrix[portfolio_ticker[col]] = new_col

    #Use covariance table to find 2 * cov() * w(x) * w(y)
    adv_cov_matrix = pd.DataFrame()

    #create index header
    adv_cov_matrix[""] = portfolio_ticker
    adv_cov_matrix.set_index('', inplace=True)

    #Fill secondary covariance table
    for col in range(len(portfolio_ticker)):
        new_col = []
        for row in range(len(portfolio_ticker)):
            if row > col:
                new_col.append(cov_matrix.iloc[row, col] * 2 * portfolio_dict[portfolio_ticker[row]] * portfolio_dict[
                    portfolio_ticker[col]])
            else:
                new_col.append(np.nan)
        adv_cov_matrix[portfolio_ticker[col]] = new_col
    print(adv_cov_matrix)


    #find stocks weight^2 and Std_Dev^2
    stdDevSq_list = [sd ** 2 for sd in std_dev_list]

    return avg_returns, stdDevSq_list, adv_cov_matrix

def calculateValues(portfolio_distribution, avg_returns, stdDevSq_list, adv_cov_matrix):

    # get individual component and portfolio returns
    individual_components = []
    for i in range(len(avg_returns)):
        individual_components.append(avg_returns[i] * portfolio_distribution[i])

    portfolio_return = (sum(individual_components))

    #Use calculated values to find portfolio SD
    weightSq_list = [w ** 2 for w in portfolio_distribution]
    portfolioSD = (sum([weightSq_list[i] * stdDevSq_list[i] for i in range(len(stdDevSq_list))])
                        + adv_cov_matrix.sum().sum()) ** 0.5


    #Calculate Sharpe Ratio
    Sharpe_Ratio = (portfolio_return - risk_free_rate) / portfolioSD

    return portfolio_return, portfolioSD, Sharpe_Ratio


#######################################################################################################################
# #THINGS THAT YOU MIGHT WANT TO SEE:
# # 1. INITIAL DATA TABLE
# print(data)
#
# #2. Average Returns From Start Date to End Date Specified
# print(avg_returns)
#
# #3. RETURNS DATA TABLE (Data Table of Differences)
# print(allReturns)
#
#4. PORTFOLIO RETURNS
# print("portfolio return: ", portfolio_return)
#
# #5. TABLE OF EXCESS RETURNS (X - X mean)
# print(excessReturns)
#
# #6. COVARIANCE MATRIX
# print(cov_matrix)
#
# #7. Secondary Covariance Matrix (2 * W(x) * W(y) * Initial Covariance)
# print(adv_cov_matrix)
#
#8. PORTFOLIO STANDARD DEVIATION
# print("Portfolio SD: ", portfolioSD)

#9 SHARPE RATIO
# print("Sharpe Ratio: ", Sharpe_Ratio)

# import needed modules
# import quandl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# empty lists to store returns, volatility and weights of imiginary portfolios
port_returns = []
port_volatility = []
stock_weights = []

best_SR = 0

# set the number of combinations for imaginary portfolios
num_assets = len(portfolio_ticker)
num_portfolios = 50000

avg_returns, stdDevSq_list, adv_cov_matrix = processData(time_frame, risk_free_rate, portfolio_ticker, filename)

# populate the empty lists with each portfolios returns,risk and weights
for single_portfolio in range(num_portfolios):
    weights = np.random.random(num_assets)
    weights /= np.sum(weights)


    returns, volatility, SR = calculateValues(weights, avg_returns, stdDevSq_list, adv_cov_matrix)
    if SR > best_SR:
        best_SR = SR
        best_index = single_portfolio

    port_returns.append(returns)
    port_volatility.append(volatility)
    stock_weights.append(weights)

# a dictionary for Returns and Risk values of each portfolio
portfolio = {'Returns': port_returns,
             'Volatility': port_volatility}

# extend original dictionary to accomodate each ticker and weight in the portfolio
for counter,symbol in enumerate(portfolio_ticker):
    portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]

# make a nice dataframe of the extended dictionary
df = pd.DataFrame(portfolio)

# get better labels for desired arrangement of columns
column_order = ['Returns', 'Volatility'] + [stock+' Weight' for stock in portfolio_ticker]

# reorder dataframe columns
df = df[column_order]
print("Sharpe Ratio:", best_SR)
print(df.loc[best_index])

# plot the efficient frontier with a scatter plot
plt.style.use('seaborn')
df.plot.scatter(x='Volatility', y='Returns', figsize=(10, 8), grid=True)
plt.xlabel('Volatility (Std. Deviation)')
plt.ylabel('Expected Returns')
plt.title('Efficient Frontier')

plt.plot(df.loc[best_index]['Volatility'], df.loc[best_index]['Returns'],'*', label='Optimum Point', markersize=np.sqrt(300.), c='g')
lgnd = plt.legend(loc="upper left", numpoints=1, fontsize=10)

lgnd.legendHandles[0]._legmarker.set_markersize(20)


plt.show()