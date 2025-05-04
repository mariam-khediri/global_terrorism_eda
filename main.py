from scripts.load_data import load_dataset # type: ignore
# Step 1: explore the raw data

#load data
"""df=load_dataset("data/raw_data.csv")

#explore the data
print("\n dataset info:")
print(df.info())

print("\n sample rows:")
print (df.head())"""

# interpretation :

""" ==>as a first step discovering our raw data : it contains 181691 rows and 135 columns 
too many columns , they might be redundant or irrelevent for our eda 
now we will modify the load_data.py to select columns and clean"""


# step 2: explore the filtered data

"""df=load_dataset("data/raw_data.csv")

# Summary"""
"""print("\n Cleaned Dataset Info:")
print(df.info())

print("\n Sample Data:")
print(df.head())"""

# interpretation :
""" now we have 181691 rows and only 14 columns
most features have missing or null values
==> next step we will clean and prepare our data for eda""" 

# Step 3 : explore clean data

from scripts.utils import clean_data # type: ignore

df = load_dataset("data/raw_data.csv")
df = clean_data(df) 

#df.to_excel("output/cleaned_data.xlsx", index=False)

# Step 4 featture engineering
#print(df[['nkill', 'nwound', 'casualties']].head())

"""from scripts.eda_visuals import plot_top_countries_by_casualties
plot_top_countries_by_casualties(df)
"""
"""from scripts.eda_visuals import plot_attack_type_impact
plot_attack_type_impact(df)
"""

"""from scripts.eda_visuals import plot_terrorism_trends
plot_terrorism_trends(df)"""

from scripts.eda_visuals import (
    plot_attack_type_impact,
    plot_terrorism_trends,
    plot_top_countries,
    plot_global_heatmap
)

#plot_attack_type_impact(df)
#plot_terrorism_trends(df)
#plot_top_countries(df)
plot_global_heatmap(df)