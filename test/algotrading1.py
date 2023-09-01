# %%
import pandas as pd
import numpy as np
import yfinance as yf
s = "HCLTECH.NS"

# %%
data = yf.download(s, start="2022-12-07", end="2022-12-08",interval="5m")

# %%
import statistics
def fun(df):
    #file = open('model.txt', 'w')
    diff = []
    diff_pre = []
    per_pre = []
    per = []
    tot = 0
    count = 0
    i = 1
    while i < len(df):
        if(df['Close'][i-1] > df['Open'][i-1] and df['Close'][i] < df['Open'][i]):
            
            tot = tot+1
            i=i+1
        elif(df['Close'][i-1] > df['Open'][i-1] and df['Close'][i] > df['Open'][i]):
            diff1 = df['Close'][i] - df['Open'][i]
            per1 = diff1/df['Open'][i]
            diff.append(diff1)
            #diff_pre.append()
            per.append(per1)
            count = count + 1
            diff1 = df['Close'][i-1] - df['Open'][i-1]
            per1 = diff1/df['Open'][i-1]
            per_pre.append(per1)
            diff_pre.append(diff1)
            tot = tot+1
            i = i+2
        else:
            i = i+1
    avg_diff = sum(diff)/len(diff)
    avg_per = sum(per)/len(per)
    #per.sort()
    #diff.sort()
    median_per = statistics.median(per)
    median_diff = statistics.median(diff)
    return [diff, per, diff_pre, per_pre, avg_diff, avg_per, tot, count, median_per, median_diff, len(df)]

# %%
list1 = fun(data)
print(list1[4:])
print(len(list1[0]))
#print(list(zip(list1[2], list1[0])))
tup = list(zip(list1[2], list1[0]))
print(tup)
#tup1 = tup.sort(key =lambda x: x[1])
sorted(tup, key= lambda x:x[1])
print(tup)


# %%
#print(tup[1[1]])

# %%
data2 = yf.download(s, start="2022-12-08", end="2022-12-09", interval="5m")
#print(data2.tail())
balance = 200000
no_of_shares = balance/data2['Open'][0]
req_diff = 140/no_of_shares
tmp = []
count = 0
for i in range(0, len(list1[0])):
    if(tup[i][1] >= req_diff):
        tmp.append(tup[i][0])
        count = count + 1
if(len(tmp) == 0):
    median_tmp = 0
else:
    median_tmp = statistics.median(tmp)
print(median_tmp)
print(balance)
print(len(data2))


# %%
balance = 200000
print(balance)
count = 0
i = 0
while i < len(data2)-1:
    if(data2['Close'][i] - data2['Open'][i] >= median_tmp):
        #print(1)
        #print(balance)
        count = count + 1
        num = balance/data2['Open'][i]
        balance = balance + ((data2['Close'][i+1] - data2['Open'][i+1])*num)
        i=i+2
    else:
        i = i+1
print(count)
print(balance)
balance = 200000
print(balance)
count = 0
i = 0
while i < len(data2)-1:
    if(data2['Close'][i] - data2['Open'][i] >= 0):
        #print(1)
        #print(balance)
        count = count + 1
        num = balance/data2['Open'][i]
        balance = balance + ((data2['Close'][i+1] - data2['Open'][i+1])*num)
        i=i+2
    else:
        i = i+1
print(count)
print(balance)



# %%
import mplfinance as plt

# %%
data['MA10'] = data['Close'].rolling(10).mean()
data['MA13'] = data['Close'].rolling(13).mean()
data.dropna(inplace=True)
#data.index.strftime("%m/%d/%Y, %r")
#data.index.format()
#type(data.index)
#data.DatatimeIndex.strftime()

# %%
#x = data.index
#plt.plot(data.index,data[['Close','MA15']])
#data.plot(show_nontrading=False)
plt.plot(data,mav=(10,13))
#data[['Close','MA15']].plot(figsize=(32,16))

# %%
balance = 200000
initial_balance = balance
profit = 0
stock = 0
for i in range(0,len(data)):
    if(data['MA10'][i] > data['MA13'][i] and balance > data['Close'][i] and data['MA10'][i]):
        if(stock==0):
            stock +=1
        elif(stock*data['Close'][i] < balance):
            balance = balance-(stock*data['Close'][i])
            stock+=stock
        else:
            stock+= (balance/data['Close'][i])
            balance = balance%data['Close'][i]
    # elif(data['MA10'][i] < data['MA13'][i] and stock > 0):
    #     if(stock == 1):
    #         stock=0
    #         balance+=data['Close'][i]
    #     else:
    #         if(stock%2 == 1):
    #             stock = stock/2
    #             balance+= stock*data['Close'][i]
    #             stock+=1
    #         else:
    #             stock = stock/2
    #             balance+= stock*data['Close'][i]
    elif(data['MA10'][i] < data['MA13'][i] and stock > 0):
        balance+= stock*data['Close'][i]
        stock = 0
print(balance-initial_balance)



# %%



