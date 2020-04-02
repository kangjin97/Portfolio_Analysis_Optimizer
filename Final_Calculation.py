import numpy as np
import matplotlib.pyplot as plt
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
    return data


# Extract Data from yahoo finance
stocks = ['ACN', 'DIS', 'COST', 'INTC', 'JPM','V', 'XOM', 'JNJ', 'BSX', 'CPB']
start = '2010-01-01'
end = '2016-01-01'

dt = extractData(stocks, start, end)

main_df = pd.DataFrame(dt)


# inputting mean for any missing data just in case (data cleaning)
def impute(df, col, method):
    if method == "mean":  # impute missing values with column mean
        df[col].fillna(value=df[col].mean(), inplace=True)
    elif method == "zero":  # impute missing values with zero
        df[col].fillna(value=0, inplace=True)
    else:  # in this case, method will be the name of the asset to be substituted with
        df[col].fillna(value=df[method], inplace=True)
        # substitute values with the performance of related asset at specific timestep
    return df


to_impute = main_df.columns[main_df.isna().any()].tolist()

for col in to_impute:
    main_df = impute(main_df, col, "mean")


# Define function to calculate returns, volatility
def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    # calculates portfolio performance and volatility

    # sum of all equities' mean * weighted average for a given portfolio for annual returns
    returns = np.sum(mean_returns * weights) * 12

    # Standard deviation of portfolio (using dot product against covariance, weights)
    # 252 trading days

    # The standard deviation of a two-asset portfolio is calculated by squaring the weight of the first asset
    # and multiplying it by the variance of the first asset, added to the square of the weight of the second asset,
    # multiplied by the variance of the second asset.

    # 1. Multiply covariance matrix with weights
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(12)
    # std=np.sqrt(sum(np.dot(cov_matrix, weights)))* np.sqrt(252)
    return std, returns


# Define function to generate {num_portfolios} number of random portfolios
def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate):
    # generates portfolios with randomised weights
    # Initialize array of shape N x 3 to store our results, for 1. portfolio std dev 2. return 3. sharpe ratio
    # where N is the number of portfolios we're going to simulate
    results = np.zeros((num_portfolios, 3))

    # Array to store the weights of each equity
    weights_record = []
    for i in range(num_portfolios):
        # Randomly assign floats to our all the equities

        # numpy.random.random() is one of the function for doing random sampling in numpy.
        # It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0)
        weights = np.random.random(len(mean_returns))
        # Normalize/convert to all to the scale of 0 to 1. (out of 100%)
        weights /= np.sum(weights)
        # Append each possible allocation into the list
        weights_record.append(weights)

        # Pull the standard deviation, returns from our function above using
        # the weights, mean returns generated in this function
        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)

        # Store output
        results[i, 0] = portfolio_std_dev
        results[i, 1] = portfolio_return
        # Sharpe ratio
        results[i, 2] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record


def simulate_ef_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate):
    # obtain results of all possible portfolios' std dev & return, and each asset's weights
    results, weights = random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate)

    # obtain list of asset names
    asset_names = mean_returns.index.tolist()

    # returns position/index of the max portfolio Sharpe ratio
    max_sharpe_idx = np.argmax(results, axis=0)[2]

    # obtain the associated standard deviation, annualized return w the index of the maximum sharpe ratio
    sdp, rp = results[max_sharpe_idx, 0], results[max_sharpe_idx, 1]

    # to obtain the allocation of the portfolio associated with max Sharpe ratio
    # 1. get the portfolio from the weights array w the index of the max sharpe ratio
    # 2. assign the asset_names as index
    # 3. left with one column and name it allocation
    max_sharpe_allocation = pd.DataFrame(weights[max_sharpe_idx], index=asset_names, columns=['allocation'])

    # since the allocation is on the scale from 0-1, *100 to get percentage
    max_sharpe_allocation.allocation = [round(i * 100, 2) for i in max_sharpe_allocation.allocation]

    # transpose the table so that the assets become headers
    max_sharpe_allocation = max_sharpe_allocation.T


    # obtain portfolio index with the min volatility - standard deviation
    min_vol_idx = np.argmin(results, axis=0)[0]

    # obtain the associated standard deviation, annualized return w the index of the min volatility
    sdp_min, rp_min = results[min_vol_idx, 0], results[min_vol_idx, 1]
    min_vol_allocation = pd.DataFrame(weights[min_vol_idx], index=asset_names, columns=['allocation'])
    min_vol_allocation.allocation = [round(i * 100, 2) for i in min_vol_allocation.allocation]
    min_vol_allocation = min_vol_allocation.T

    msr = results[max_sharpe_idx][2]
    print("Maximum Sharpe Ratio:", round(msr, 2))

    print("-" * 80)
    print("Maximum Sharpe Ratio Portfolio Allocation\n")
    print("Annualised Return:", round(rp, 2))
    print("Annualised Volatility:", round(sdp, 2))
    print("\n")
    print(max_sharpe_allocation)
    print("-" * 80)
    print("Minimum Volatility Portfolio Allocation\n")
    print("Annualised Return:", round(rp_min, 2))
    print("Annualised Volatility:", round(sdp_min, 2))
    print("\n")
    print(min_vol_allocation)

    plt.figure(figsize=(10, 7))

    # x = volatility, y = annualized return, color mapping = sharpe ratio
    plt.scatter(results[:, 0], results[:, 1], c=results[:, 2], cmap='YlGnBu', marker='o', s=10, alpha=0.3)
    plt.colorbar()
    plt.scatter(sdp, rp, marker='*', color='r', s=500, label='Maximum Sharpe ratio')
    plt.scatter(sdp_min, rp_min, marker='*', color='g', s=500, label='Minimum volatility')
    plt.title('Simulated Portfolio Optimization based on Efficient Frontier')
    plt.xlabel('annualised volatility')
    plt.ylabel('annualised returns')
    plt.legend(labelspacing=0.8)
    plt.show()


# Get monthly percentage change of assets
main_df = main_df.pct_change().dropna()


# Get mean returns and covariance matrix of assets within the given time frame
mean_returns = main_df.mean()
cov_matrix = main_df.cov()


# Calculate efficient frontier based on risk-free rate and number of portfolios
num_portfolios = 1000
risk_free_rate = 0.0152
simulate_ef_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate)