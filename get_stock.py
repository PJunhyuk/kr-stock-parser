import time
time_start = time.time()

import os
import argparse as ap

import pandas as pd

import functions

parser = ap.ArgumentParser()
parser.add_argument('-n', "--stockName", help="Name of Stock")
parser.add_argument('-v', "--visualize", help="Visualizer on/off")
args = vars(parser.parse_args())

if args["stockName"] is None:
    stock_name = '카카오'
else:
    stock_name = args["stockName"]

if args["visualize"] is None:
    is_visualize = False
else:
    is_visualize = True

if not os.path.isfile('./code_df.csv'):
    functions.save_as_csv()
    print('save complete!')
    print('Time required(s): ' + str(time.time() - time_start))
code_df = pd.read_csv('./code_df.csv')
# print(code_df)
# print(type(code_df))

url = functions.get_url(stock_name, code_df)

df = pd.DataFrame()

for page in range(1, 41):
    pg_url = '{url}&page={page}'.format(url=url, page=page)
    df = df.append(pd.read_html(pg_url, header=0)[0], ignore_index=True)

df = df.dropna()

# Remove except 'date, close'
df = df.drop(df.columns[[2, 3, 4, 5, 6]], axis=1)

# Translate names of column in df to Korean
df = df.rename(columns = {'날짜': 'date', '종가': 'close'})

# Convert date to date-format, close to int
df['date'] = pd.to_datetime(df['date'])
df['close'] = df['close'].astype(int)

# Sort: ascending
# df = df.sort_values(by=['date'], ascending=True)
df = df.iloc[::-1]
df = df.reset_index(drop=True)

print(df.head())
print('Time required(s): ' + str(time.time() - time_start))

if is_visualize is True:
    functions.draw_plot(stock_name, df)
