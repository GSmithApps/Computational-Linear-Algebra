import pandas as pd
import numpy as np

def get_data(dataset_switch = 'linear'):
    """
    try the following switches:
    linear
    exponential
    even_spacing
    pups
    """

    # making our dataset with a few different switches or options
    if dataset_switch == 'linear':
        from sklearn.datasets import make_regression
        X,y = make_regression(
            n_samples=100,
            n_features=1,
            random_state = 11,
            noise = 10
        )
        X = X[:,0]
    elif dataset_switch == 'exponential':
        from sklearn.datasets import make_regression
        X,_ = make_regression(
            n_samples=100,
            n_features=1,
            random_state = 11,
            noise = 10
        )
        X = X[:,0]
        from numpy.random import default_rng
        rng = default_rng()
        vals = rng.standard_normal(100)/2
        y = np.power(3,X) + vals
    elif dataset_switch == 'even_spacing':
        X = np.linspace(-2.0, 3.0, num=100)
        y = 40*X
    elif dataset_switch == 'pups':
        pups_df = pd.read_csv('pupSlice.csv',header=None)
        X = np.arange(1,3024+1)
        y = pups_df[0].values

    import pandas as pd

    df = pd.DataFrame({
        'x':X,
        'y':y
    })

    return df.sort_values(by=['x'])

