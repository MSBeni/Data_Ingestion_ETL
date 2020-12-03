import pandas as pd
import numpy as np
import sqlite3

# Make connection between the system and the Database
conn = sqlite3.connect('rides.db', detect_types=sqlite3.PARSE_DECLTYPES)

# Defining Parameters
params = {
    'vendor': 'VeriFone',
}
# Query to read the distance form the table where the vendor condition applies
sql = 'SELECT distance FROM rides WHERE vendor = :vendor'

# Reading all the data in Database with specific distance
datb = pd.read_sql(sql, conn, params=params)

print(f"The mean of the Distances is: {np.mean(datb['distance'])}")

