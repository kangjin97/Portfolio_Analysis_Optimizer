import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import pandas as pd

def extractData(stocks, start, end):
    global progress
    progress = 0

    source = 'yahoo'

    data = pd.DataFrame()

    for symbol in stocks:
        try:
            data[symbol] = web.DataReader(symbol, data_source=source, start=start, end=end)['Adj Close']
        except:
            error = f"Ticker Symbol {symbol} cannot be found"
            return error

    data = data.asfreq('M', method='pad')
    return data


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


# Define function to calculate returns, volatility
def portfolio_annualised_performance(weights, mean_returns, cov_matrix):
    # sum of all equities' mean * weighted average for a given portfolio for annual returns
    returns = np.sum(mean_returns * weights) * 12

    # 1. Multiply covariance matrix with weights
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(12)

    return std, returns


# Define function to generate {num_portfolios} number of random portfolios
def random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate, progress_bar):
    global progress
    # generates portfolios with randomised weights

    # Initialize array of shape N x 3 to store our result
    results = np.zeros((num_portfolios, 3))

    # Array to store the weights of each equity
    weights_record = []
    for i in range(num_portfolios):
        progress += 1
        progress_bar["value"] = progress
        progress_bar.update()


        # It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0)
        weights = np.random.random(len(mean_returns))
        # Normalize/convert to all to the scale of 0 to 1. (out of 100%)
        weights /= np.sum(weights)
        # Append each possible allocation into the list
        weights_record.append(weights)

        portfolio_std_dev, portfolio_return = portfolio_annualised_performance(weights, mean_returns, cov_matrix)

        # Store output
        results[i, 0] = portfolio_std_dev
        results[i, 1] = portfolio_return
        # Sharpe ratio
        results[i, 2] = (portfolio_return - risk_free_rate) / portfolio_std_dev
    return results, weights_record


def simulate_ef_random(mean_returns, cov_matrix, num_portfolios, risk_free_rate, progress_bar):
    global progress
    progress_bar["value"] = progress
    # obtain results of all possible portfolios' std dev & return, and each asset's weights
    results, weights = random_portfolios(num_portfolios, mean_returns, cov_matrix, risk_free_rate, progress_bar)

    # obtain list of asset names
    asset_names = mean_returns.index.tolist()

    # returns position/index of the max portfolio Sharpe ratio
    max_sharpe_idx = np.argmax(results, axis=0)[2]

    # obtain the associated standard deviation, annualized return w the index of the maximum sharpe ratio
    sdp, rp = results[max_sharpe_idx, 0], results[max_sharpe_idx, 1]

    # Obtain the allocation of the portfolio associated with max Sharpe ratio
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

    outputDisplay = "Maximum Sharpe Ratio: " + str(round(msr,
                                                         2)) + "\n" + "-" * 80 + "\n" + "Maximum Sharpe Ratio Portfolio Allocation\n\n" + "Annualised Return: " + str(
        round(rp, 3)) + "\n" + "Annualised Volatility: " + str(round(sdp, 3)) + "\n\n" + str(
        max_sharpe_allocation) + "\n" + "-" * 80 + "\n" + "Minimum Volatility Portfolio Allocation\n\n" + "Annualised Return: " + str(
        round(rp_min, 3)) + "\n" + "Annualised Volatility: " + str(
        round(sdp_min, 3)) + "\n\n" + str(min_vol_allocation) + "\n"

    f = plt.figure(figsize=(10, 7))
    plt.scatter(results[:, 0], results[:, 1], c=results[:, 2], cmap='YlGnBu', marker='o', s=10, alpha=0.3)
    plt.colorbar()
    plt.scatter(sdp, rp, marker='*', color='r', s=500, label='Maximum Sharpe ratio')
    plt.scatter(sdp_min, rp_min, marker='*', color='g', s=500, label='Minimum volatility')
    plt.title('Simulated Portfolio Optimization based on Efficient Frontier')
    plt.xlabel('annualised volatility')
    plt.ylabel('annualised returns')
    plt.legend(labelspacing=0.8)

    progress = 0
    progress_bar["value"] = progress
    progress_bar.update()

    return f, outputDisplay