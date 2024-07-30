#26/07/2024

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

df1 = pd.read_csv('/Users/muskansudiksha/Desktop/df1', index_col=0) 
df2 = pd.read_csv('/Users/muskansudiksha/Desktop/df2') 

#plt.style.use('bmh')
#df1['A'].hist()
df1.plot(kind='hist')
df1.plot.box()


