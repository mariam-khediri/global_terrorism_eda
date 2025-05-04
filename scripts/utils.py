def clean_data(df):
    import pandas as pd # type: ignore

    # Fill NaNs
    df['nkill'] = df['nkill'].fillna(0)
    df['nwound'] = df['nwound'].fillna(0)

    # Create casualties column
    df['casualties'] = df['nkill'] + df['nwound']

    # Drop rows with missing location
    df = df.dropna(subset=['city', 'provstate'])

    # Replace 0s in month/day
    df['imonth'] = df['imonth'].replace(0, 1)
    df['iday'] = df['iday'].replace(0, 1)

    return df 