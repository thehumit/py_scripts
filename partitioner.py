import pandas as pd
import csv

df = pd.read_csv("../ex03/hh_positions.csv")
dates = pd.to_datetime(df.created_at)
unique = dates.map(lambda t: t.date()).unique()

def extract_unique_date_df(df, dates, unique):
    dates = dates.map(lambda x: x.date())
    for i in unique:
        indexes = dates[dates == i].index
        df_ret = df.iloc[indexes]
        df_ret.to_csv(str(i) + ".csv", index=False, quoting=csv.QUOTE_ALL)

extract_unique_date_df(df, dates, unique)
