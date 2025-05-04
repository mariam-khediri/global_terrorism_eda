# 🌍 Global Terrorism Data EDA Project

This project performs **Exploratory Data Analysis (EDA)** on the [Global Terrorism Database (GTD)](https://www.start.umd.edu/gtd/), focusing on identifying patterns, trends, and regional differences in global terrorist activities from 1970 to 2017.

---

## 📦 Dataset Description

- **Source**: Global Terrorism Database (by START/University of Maryland)
- **Size**: ~135 columns and ~181,000 rows
- **Period Covered**: 1970–2017
- **Features**:
  - Date and location of attacks (`iyear`, `imonth`, `iday`, `country_txt`, `region_txt`, `provstate`, `city`)
  - Attack type (`attacktype1_txt`)
  - Target type (`targtype1_txt`)
  - Weapon type (`weaptype1_txt`)
  - Casualties (`nkill`, `nwound`)
  - Perpetrator group (`gname`)
  - Incident summary

---

## 🛠 Data Cleaning

- Filtered dataset to include **14 key columns** for analysis
- Replaced `0` in month/day with `1` to fix date parsing
- Handled missing values and NaNs
- Created a new column: `casualties = nkill + nwound`

---

## 📊 Exploratory Data Analysis (EDA)

We analyzed terrorism data from multiple angles:

1. **Most Frequent Attack Types**  
   - Bar chart showing top 10 attack types by number of casualties

2. **Terrorism Trends Over the Years**  
   - Line plot showing number of attacks and casualties from 1970–2017

3. **Top Affected Countries**  
   - Bar chart showing countries with the most attacks

4. **Global Heatmap of Attacks**  
   - Interactive choropleth map showing geographic distribution of incidents

---

## 📁 Project Structure

```

eda\_gtd/
│
├── data/
│   └── globalterrorismdb.csv        # Raw dataset
│
├── output/
│   └── figures/                     # Saved plots (HTML & PNG)
│
├── scripts/
│   ├── load\_data.py                 # Data loading and filtering
│   ├── utils.py                     # Helper functions (e.g., date fix, casualty calc)
│   └── eda\_visuals.py               # Plotting and EDA visualizations
│
├── main.py                          # Main script to run the analysis
└── README.md                        # Project summary (this file)

````

---

## ▶️ How to Run

1. Clone the repo:
```bash
git clone https://github.com/<your-username>/global_terrorism_eda.git
cd global_terrorism_eda
````

2. Install requirements:

```bash
pip install pandas matplotlib seaborn plotly
```

3. Run the analysis:

```bash
python main.py
```

4. Visualizations will be saved in:
   `output/figures/`

---

## 📈 Example Visuals

> Check the `output/figures/` folder for:

* `attack_type_impact.png`
* `top_countries.png`
* `terrorism_trends.png`
* `global_terror_heatmap.html` (interactive)

---

## 📌 Credits

* Dataset: [GTD - National Consortium for the Study of Terrorism and Responses to Terrorism (START)](https://www.start.umd.edu/gtd/)

