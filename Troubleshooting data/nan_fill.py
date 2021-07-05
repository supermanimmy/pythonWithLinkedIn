"""Working with nan and filling missing data"""

import pandas as pd
import numpy as np
val = float('nan') # also np.nan
###print(val)

#print(val == float('nan')) #False

#print (pd.isnull(val)) # True

values = pd.Series([1.2, 2.3, float('nan'), 4.5])
#pd.isnull is ufunc

#print(pd.isnull(values)) 
# True
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool

"""Filling missing data"""

values = pd.Series([1., 2., np.nan, 4., 5., np.nan, 7.0])

#fillna will na with a given value
#fillna will return a new Series (use inplace=True to mutate the object)

#print(values.fillna(5.))

#YOu can use computed value

avg = values.mean() #mean is 'nan aware'
#print(values.fillna(avg))

print(values.interpolate(inplace=True))
