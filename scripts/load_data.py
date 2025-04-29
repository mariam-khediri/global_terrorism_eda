import pandas as pd # type: ignore

def load_dataset(path: str) -> pd.DataFrame:
    # loads the dataset from the given path and returns a pandas dataframe
    
    try:
        df=pd.read_csv(path, encoding='latin1')
        print(f"loaded dataset with shape:{df.shape}")
        return df
    except Exception as e:
        print(f"failed to load dataset:{e}")
        return pd.DataFrame()




