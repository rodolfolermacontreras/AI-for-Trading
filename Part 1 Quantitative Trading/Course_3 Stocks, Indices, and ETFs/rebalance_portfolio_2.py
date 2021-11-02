def rebalance_portfolio(returns, index_weights, shift_size, chunk_size):
    """
    Get weights for each rebalancing of the portfolio.

    Parameters
    ----------
    returns : DataFrame
        Returns for each ticker and date
    index_weights : DataFrame
        Index weight for each ticker and date
    shift_size : int
        The number of days between each rebalance
    chunk_size : int
        The number of days to look in the past for rebalancing

    Returns
    -------
    all_rebalance_weights  : list of Ndarrays
        The ETF weights for each point they are rebalanced
    """
    assert returns.index.equals(index_weights.index)
    assert returns.columns.equals(index_weights.columns)
    assert shift_size > 0
    assert chunk_size >= 0
    
    #TODO: Implement function
    all_rebalance_weights=[] 
    
    
    numDays=len(returns)
   
    for end_date in range(chunk_size, numDays, shift_size): 
        
        start_date = end_date-chunk_size  
        
        #Extract the partial return of the latest chunk of time
        period_returns = returns.iloc[(start_date):end_date,] 
        #period_returns = returns.iloc[(start_date):-1,:] 
        
        #check whether there are enough non-null days, if not, skip that day
        if (period_returns.shape[0]- chunk_size <0):
        #if (end- chunk_size <0):
            continue
            
        covariance_returns = get_covariance_returns(period_returns)
        
        
        period_weights = index_weights.iloc[end_date-1,] #up to but before end_date, exclude return on end_date
        #ind_weights = index_weights.iloc[shift-1,].mean()
        
        #Re-compute optimal weights
        #optimal_weights = get_optimal_weights(covariance_returns,period_weights,end_date) 
        optimal_weights = get_optimal_weights(covariance_returns,period_weights,scale=2) 
        
        #Append optimized weights to the output list
        all_rebalance_weights.append(optimal_weights)

    
    return all_rebalance_weights


project_tests.test_rebalance_portfolio(rebalance_portfolio)