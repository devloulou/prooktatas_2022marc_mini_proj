import pandas as pd
import psycopg2

# Series, DataFrame, Panel

# Series - adatbázis táblának 1 oszlopa -> 1 dimenziós tömb
# DataFrame - adatbázis tábla - 2 dimenziós

# [[],[],[],
# [],[],[],
# [],[],[]]

# Panel - 3 dimenziós tömb

csv_path = r"C:\WORK\Prooktatás\mini_project\data\circuits.csv"

df = pd.read_csv(csv_path)

print(df.columns.to_list())

print(df.head(3))

print(df['circuitId'])

print(df[['circuitId', 'circuitRef', 'circuitId', 'circuitRef', 'circuitId', 'circuitRef', 'circuitId', 'circuitRef']])

#print(df['circuitId', 'circuitRef', 'circuitId', 'circuitRef', 'circuitId', 'circuitRef', 'circuitId', 'circuitRef'])
#print(df[['circuitId', 'alt']])

print(df[['circuitId']])

def my_func(x):
    return x * 2

print(df['circuitId'].apply(my_func))

df['circuitId'] = df['circuitId'].apply(my_func)

df['ez_az_oszlop_neve'] = "ez_az_oszlop_ertéke"

print(".----------------------------.")

print(df['circuitId'])

print(".----------------------------.")
print(".----------------------------.")
print(df['ez_az_oszlop_neve'] )