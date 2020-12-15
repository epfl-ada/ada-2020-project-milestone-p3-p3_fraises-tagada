import pandas as pd
import numpy as np
import datetime as dt
import statsmodels.formula.api as smf

def bootstrap(df, func, n_boots=1000):
    '''
    General bootstrapping method
    Inputs : df -> dataFrame on which to work
             func -> function that computes the value to bootstrap
             n_boots -> number of samples for bootstrapping
    Outputs : values -> all the computed values
              CI -> confidence interval of the values
    '''
    # Store values of each sample here
    values = []
    
    # Randomly sample n times -> obtain n values
    for n in range(n_boots):
        
        # Obtain random sample
        inds = np.random.randint(df.shape[0], size = (df.shape[0]))
        sample = df.iloc[inds]
        
        # Compute value for this sample and store
        val = func(sample)
        values.append(val)
    
    # Compute confidence interval from stored values
    CI = [np.percentile(values,2.5), np.percentile(values, 97.5)]
    
    return values, CI


def compute_search_rates(df_, formula):
    
    df = df_.copy()
    # First we transform the datetime to ordinal values
    df.date = pd.to_datetime(df.date)
    df.date = df.date.map(dt.datetime.toordinal)

    # Standardize date
    date_mean = df.date.mean()
    date_std = df.date.std()
    df.date = (df.date - date_mean) / date_std

    # Make search_conducted be 0 or 1
    df.search_conducted =  df.search_conducted.astype(int)

    # Compute the search rates using a logistic regression

    model = smf.logit(formula = formula, data = df).fit()

    search_rates = model.predict()
    
    return search_rates, model


def load_data_to_pickle(data_url, filename):
    '''
    Load the data from internet and stores it in your folder as a pickle-rick
    To read pickle : pd.read_pickle(filename)
    Input : data_url -> url to the big data
    '''
    # Load data (can take some time)
    df = pd.read_csv(data_url, compression='zip')
    
    # Save to pickle format
    df.to_pickle(filename)
    
    # Informative print
    print('pickle-rick reporting for duty')