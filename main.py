from scripts.load_data import load_dataset # type: ignore

#load data
df=load_dataset("data/raw_data.csv")

#explore the data
print("\n dataset info:")
print(df.info())

print("\n sample rows:")
print (df.head())

# as a first step discovering our raw data : it contains 181691 rows and 135 columns 
# too many columns , they might be redundant or irrelevent for our eda 
#now we will modify the load_data.py to select columns and clean
