import numpy as np
import pandas as pd
def fun(df):
    #file = open('model.txt', 'w')
    diff = []
    per = []
    tot = 0
    count = 0
    for i in range(1,len(df)):
        if(df['Close'][i-1] > df['Open'][i-1] and df['Close'][i] < df['Open'][i]):
            count = count + 1
            tot = tot+1
        elif(df['Close'][i-1] > df['Open'][i-1] and df['Close'][i] > df['Open'][i]):
            diff1 = df['Close'][i] - df['Open'][i]
            per1 = diff1/df['Open'][i]
            diff.append(diff1)
            per.append(per1)
            tot = tot+1
            i = i+1
    avg_diff = sum(diff)/len(diff)
    avg_per = sum(per)/len(per)
    return [avg_diff, avg_per, tot, count]