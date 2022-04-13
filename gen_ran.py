import sys
import os
import numpy as np
import pandas as pd

# To run file 
# py gen_ran.py number_of_trials_here
# eg py gen_ran.py 10, for 10 trials

# Pandas config
pd.io.formats.excel.ExcelFormatter.header_style = None

# Getting arguments
arguments = sys.argv
number_of_trials = int(arguments[1])

# make output folder if not existing
if not os.path.exists('out'):
    os.makedirs('out')

# Get cwd
path = os.getcwd() + '\out'

# Generating randint
# generates random ints list between 0-9 in shape of trials x 100
randomList = np.random.randint(0, 10, size=(number_of_trials, 100))
c = 1 # Counter

# Make dataframe
df = pd.DataFrame()

# Add list as col to df
for list in randomList:
    col_name = 'Trial {}'.format(c)
    df[col_name] = list
    c+=1

# Outputting file
# df.to_csv('{}\{} trials.csv'.format(path, number_of_trials))
df.to_excel('{}\{} Trials.xlsx'.format(path, number_of_trials), sheet_name='{} Trials'.format(number_of_trials))