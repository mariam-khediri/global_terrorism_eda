# %%
import pandas as pd # type: ignore
import matplotlib.pyplot as plt# type: ignore
import seaborn as sns# type: ignore

# sample data
data={
    'country':['iraq','afganistan','pakistan','india', 'somalia'],
    'attacks':[2450,1750,1500,900,800]
}

# create a dataframe
df=pd.DataFrame(data)

# plot
plt.figure(figsize=(10,6))
sns.barplot(x='country',y='attacks', data=df,palette='rocket')
plt.title('sample terrorism attack by country', fontsize=16)
plt.xlabel('country', fontsize=14)
plt.ylabel('number of attacks', fontsize=14)
plt.show()

