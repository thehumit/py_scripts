import glob
import pandas as pd
import csv

files = glob.glob("*.csv")
data_frame = pd.DataFrame()
content = []

for filename in files:
    df = pd.read_csv(filename, index_col=None)
    content.append(df)


data_frame = pd.concat(content)
data_frame.sort_values(by=["created_at"], inplace=True)
data_frame.to_csv("hh_positions.csv", index=False, quoting=csv.QUOTE_ALL)
