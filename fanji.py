#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
梵基投资

@author: czs
"""

import pandas as pd
import numpy as np

df = pd.read_excel('/Users/czs/Desktop/INPUT.xlsx')

df=df.set_index('Symbol',inplace=False)

df=df.drop(index=['JPY','Futures'])

df=df.replace('-',np.NaN,inplace=False)
df=df.dropna(how='any', subset=['Exchange'])


df['Total']=df.groupby('Symbol').sum()['Comm/Fee']
df['Total']=df.Total.mask(df.Total.diff().eq(0))
df.to_excel('OUTPUT_Cui.xlsx')