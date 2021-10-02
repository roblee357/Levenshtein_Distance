from Levenshtein import distance as lev
import pandas as pd
import itertools

# This program calculates the Levenshtein distance of the first 10 most popular website
# against the next 90 most popular websites.

# I. Preprocess data
# 1. Read urls from CSV
# Source https://ahrefs.com/blog/most-visited-websites/
# Formatted in Excel to csv
websites = pd.read_csv('websites.csv')
# 2. Remove protocal and Top-level Domain
mid_url = websites['Domain'].str.split('.').str[:-1].str[-1:].tolist()
## print(mid_url)
# 3. Flatten
flat_list = list(itertools.chain(*mid_url))
## print(flat_list)

print(lev(flat_list[0],flat_list[1]))
first_run = True
line = ""

for i in range(10):
##    print(i)
    
    if first_run:
        line += ','+','.join(flat_list[10:100]) + '\n'
        first_run = False
    line += flat_list[i] + ','
    for ii in range(10,100):
        # Use lev() to calc distance
        line += str(lev(flat_list[i],flat_list[ii]))+','
    line += '\n'

# write csv file which can be formatted again in Excel
with open('output.csv', 'w') as fout:
    fout.write(line)
    
