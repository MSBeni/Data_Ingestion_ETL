import pyarrow.parquet as pp

table = pp.read_table('taxi.parquet')
df = table.to_pandas()

print(df.dtypes)
print(df.head(10))
