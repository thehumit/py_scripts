import pandas as pd

df = pd.read_csv("../ex02/hh_sorted.csv")

def find_grade(a):
    b = ""
    if a.find("Junior") != -1:
        b += "Junior"
    if a.find("Middle") != -1:
        if b:
            b += "/Middle"
        else:
            b += "Middle"
    if a.find("Senior") != -1:
        if b:
            b += "/Senior"
        else:
            b += "Senior"
    if not b:
        b = "-"
    return (b)

df.name = df.name.apply(lambda x: find_grade(x))
df.to_csv("hh_positions.csv", index=False, quoting=csv.QUOTE_ALL)
