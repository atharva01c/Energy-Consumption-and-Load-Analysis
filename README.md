<h1>⚡ Energy Consumption & Load Analysis using Python</h1>

This project analyzes hourly electricity consumption data to identify usage patterns, peak load hours, and energy demand trends. Using Python, NumPy, Pandas, and Matplotlib, the project demonstrates how raw energy data from Excel files can be transformed into meaningful visual insights to support data-driven energy optimization decisions.

This project is particularly relevant for roles in energy analytics, data science, and sustainability-focused organizations.


<h2>🎯 Objectives</h2>

Analyze hourly electricity consumption data

Identify peak energy demand hours

Calculate key statistical metrics (mean, max, min)

Visualize energy usage trends using charts

Demonstrate real-world data handling using Excel input


<h2>🛠️ Tech Stack</h2>

Python

NumPy – Numerical computations

Pandas – Data loading and preprocessing

Matplotlib – Data visualization

Excel (.xlsx) – Data source


<h2>📊 Dataset Description</h2>

The dataset contains hourly electricity consumption values.

Column	Description
Hour	Hour of the day (0–23)
Energy_Consumption	Electricity usage in kWh
▶️ How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/energy-consumption-analysis.git
cd energy-consumption-analysis

2️⃣ Create & Activate Virtual Environment (Recommended)
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install numpy pandas matplotlib openpyxl

4️⃣ Run the Analysis
python energy_analysis.py


<h2>📈 Output & Visualizations</h2>

The script generates:

Line plot showing hourly energy consumption

Bar chart showing load distribution

Peak load visualization highlighting maximum demand hour

These visualizations help understand:

Low-demand periods (late night)

High-demand periods (morning and evening)

Peak energy usage trends


<h2>🔍 Key Insights</h2>

Energy consumption is lowest during late-night hours

Demand rises significantly during morning and evening

Peak electricity usage occurs during evening hours

Such insights can assist in load balancing and energy optimization
