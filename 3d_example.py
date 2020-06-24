from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('sachin.xlsx')
df = df[df['Runs'] != 'DNB']
df = df[df['Runs'] != 'TDNB']
df = df[df['Mins'] != '-']
df = df[df['BF'] != '-']

runs = df['Runs'].values
mins = df['Mins'].values
bf = df['BF'].values

figure = plt.figure(figsize=(10,6))
#ax = Axes3D(figure)
#ax.hist(runs,mins,bf)
plt.hist(mins)
plt.show()
