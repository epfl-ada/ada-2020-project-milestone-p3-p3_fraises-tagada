import pandas as pd
import numpy as np

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
