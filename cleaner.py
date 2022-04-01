improt pandas as pd

df = pd.read_csv("/Users/tquintan/Desktop/piscine_ds/day00/ex03/hh_sorted.csv")

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

jobs = df.name.apply(lambda x: find_grade(x))