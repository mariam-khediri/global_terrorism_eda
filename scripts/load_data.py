import pandas as pd # type: ignore

def load_dataset(path: str) -> pd.DataFrame:
    # loads the dataset from the given path and returns a pandas dataframe
    
    try:
        df=pd.read_csv(path, encoding='latin1')
        print(f"loaded dataset with shape:{df.shape}")

        selected_cols=[
            'iyear', 'imonth', 'iday', 'country_txt', 'region_txt', 'provstate', 'city',
            'attacktype1_txt', 'targtype1_txt', 'weaptype1_txt', 'nkill', 'nwound',
            'summary', 'gname'
        ]
        
        df =df[selected_cols]
        print(f"filtered dataset shape:{df.shape}")
        return df
    except Exception as e:
        print(f"failed to load dataset:{e}")
        return pd.DataFrame()




