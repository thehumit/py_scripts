import pandas as pd
import csv

df = pd.read_csv("../ex02/hh_sorted.csv")

def counter(df):
    titles = ["Junior", "Middle", "Senior"]
    df_ret = pd.DataFrame(columns = ("name", "count"))

    for i, word in enumerate(titles):
        df_ret.loc[i] = {"name":word, "count":df["name"].str.count(word).sum()}
    return(df_ret)

tmp = counter(df)
tmp.to_csv("hh_positions.csv", index=False, quoting=csv.QUOTE_ALL)
