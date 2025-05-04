import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_top_countries_by_casualties(df):
    top_countries = df.groupby('country_txt')['casualties'].sum().sort_values(ascending=False).head(10)

    print("\nTop 10 Countries by Total Casualties:")
    print(top_countries)

    plt.figure(figsize=(12, 6))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='Reds_r')
    plt.title('Top 10 Countries by Total Casualties (Killed + Wounded)', fontsize=16)
    plt.xlabel('Total Casualties')
    plt.ylabel('Country')
    plt.tight_layout()

    plt.savefig("output/figures/top10_countries_casualties.png")
    plt.show()

def plot_attack_type_impact(df):
    attack_counts = df['attacktype1_txt'].value_counts().head(10)
    attack_causalties= df.groupby('attacktype1_txt')['casualties'].sum().sort_values(ascending=False).head(10)

    #print tables
    print("\n top 10 attack types by frequency:")
    print(attack_counts)

    print('\n top 10 attack types by total causalities:')
    print(attack_causalties)

    #plot frequency
    plt.figure(figsize=(12,5))
    sns.barplot(x=attack_counts.values, y=attack_counts.index, palette='Blues_r')
    plt.title('top 10 attack types by frequency', fontsize=14)
    plt.xlabel('number of attacks')
    plt.ylabel('attack type')
    plt.tight_layout()
    plt.savefig('output/figures/top10_attack_types_frequency.png')
    plt. show()

    # plot causalties
    plt.figure(figsize=(12,6))
    sns.barplot(x=attack_causalties.values, y= attack_causalties.index , palette='Oranges_r')
    plt.title('top 10 attack type by total causlties', fontsize=14)
    plt.xlabel ('total causalties')
    plt.ylabel('attack type')
    plt.tight_layout()
    plt.savefig('output/figures/top10_attack_types_casualties.png')
    plt.show()


def plot_terrorism_trends(df: pd.DataFrame):
    # Group by year, count number of rows (attacks), and sum casualties
    yearly = df.groupby('iyear').agg({
        'casualties': 'sum'
    })
    yearly['attacks'] = df.groupby('iyear').size()

    # Plot
    plt.figure(figsize=(14,6))
    sns.lineplot(data=yearly, x=yearly.index, y='attacks', label='Number of Attacks')
    sns.lineplot(data=yearly, x=yearly.index, y='casualties', label='Number of Casualties')
    plt.title("Terrorism Trends Over Time (1970–2017)", fontsize=16)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Count", fontsize=12)
    plt.legend()
    plt.tight_layout()

    # Save the plot
    output_path = "output/figures/trends_over_time.png"
    plt.savefig(output_path)
    print(f"Saved trends plot to: {output_path}")


def plot_top_countries(df: pd.DataFrame, top_n=10):
    # Count number of attacks per country
    top_countries = df['country_txt'].value_counts().head(top_n)

    # Plot
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
    plt.title(f"Top {top_n} Countries by Number of Terrorist Attacks", fontsize=14)
    plt.xlabel("Number of Attacks", fontsize=12)
    plt.ylabel("Country", fontsize=12)
    plt.tight_layout()

    # Save the plot
    output_path = f"output/figures/top_{top_n}_countries.png"
    plt.savefig(output_path)
    print(f"Saved top countries plot to: {output_path}")
    plt.close()


import plotly.express as px

def plot_global_heatmap(df: pd.DataFrame):
    # Count attacks per country
    country_counts = df['country_txt'].value_counts().reset_index()
    country_counts.columns = ['country', 'attacks']

    # Create interactive choropleth
    fig = px.choropleth(
        country_counts,
        locations='country',
        locationmode='country names',
        color='attacks',
        color_continuous_scale='Reds',
        title='Global Distribution of Terrorist Attacks',
    )

    # Save HTML output
    output_path = "output/figures/global_terror_heatmap.html"
    fig.write_html(output_path)
    print(f"Interactive heatmap saved to: {output_path}")




