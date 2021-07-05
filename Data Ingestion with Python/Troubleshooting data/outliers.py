"""Finding outliers manually"""
import pandas as pd
import sqlite3

#Load data from database

conn = sqlite3.connect('rides.db')

df = pd.read_sql('SELECT * FROM rides', conn)
conn.close()
print(df.head())



#Print 90% quantile of trips, 7.06
print('.9 percentile', df['trip_distance'].quantile(.90))

#Print max distance

print('max distance', df['trip_distance'].max()) #max distance 932.9

#distance over 100 is unrealistic, lets find and change them

mask = (df['trip_distance'] > 100)
print(len(df[mask])) # 7 Trips over 100 miles.

#Change all rides over 100miles to .99 percentile

fill_value = df['trip_distance'].quantile(.99)
print('fill value = ', fill_value)# fill value =  19.480200000000004
df.loc[mask, 'trip_distance'] = fill_value
print('max after fix' , df['trip_distance'].max()) #max after fix 35.57


