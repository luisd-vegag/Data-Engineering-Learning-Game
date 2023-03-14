import dask.dataframe as dd

# Define a function to read CSV files using Dask


def read_csv_files(files):
    df = dd.read_csv(files, assume_missing=True)
    results = df.compute()
    return results
