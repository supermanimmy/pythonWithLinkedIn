"""Working with SQL database"""
import sqlite3

conn = sqlite3.connect('rides.db', detect_types=sqlite3.PARSE_DECLTYPES)
conn.row_factory = sqlite3.Row

# What's the average ride distance for VeriFone?
params = {
    'vendor': 'VeriFone',
}

sql = 'SELECT distance FROM rides WHERE vendor = :vendor'

# df = pd.read_sql(sql, conn, params=params)
# avg_distance = df['distance'].mean()
# print(f'average distance: {avg_distance:.2f}miles')

cur = conn.cursor()
cur.execute(sql, params)
total, count = 0,0
for row in cur:
    total += row['distance']
    count += 1

avg_distance = total/count
print(f'average distance: {avg_distance:.2f} miles')

# avg_distance = total / count
# print(f'average distance: {avg_distance:.2f}miles')
