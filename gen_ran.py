import sys
import os
import numpy as np
import pandas as pd

arguments = sys.argv
number_of_trials = int(arguments[1])

if not os.path.exists('out'):
    os.makedirs('out')

path = os.getcwd() + '\out'

randomList = np.random.randint(0, 10, size=(number_of_trials, 100))
c = 1

df = pd.DataFrame()

for list in randomList:
    col_name = 'trial {}'.format(c)
    df[col_name] = list
    c+=1

df.to_csv('{}\{} trials.csv'.format(path, number_of_trials))