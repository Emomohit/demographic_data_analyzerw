# 🏥 Medical Data Visualizer

A data analysis and visualization project that explores medical examination data to identify relationships between cardiac disease, body measurements, blood markers, and lifestyle choices.

*(Note: Although the repository name is `demographic_data_analyzerw`, the code contained inside belongs to the Medical Data Visualizer project!)*

This project is part of the **Data Analysis with Python** curriculum from [freeCodeCamp](https://www.freecodecamp.org/).

## 📈 What it Does
This script generates two complex visualizations to analyze patient data:
1. **Categorical Plot (`draw_cat_plot`)**: 
   - Adds an `overweight` column calculated from BMI.
   - Normalizes cholesterol and gluc levels.
   - Uses Seaborn's `catplot` to chart the counts of good and bad outcomes for various categorical features, split by whether the patient has cardiovascular disease (`cardio`).
2. **Correlation Heat Map (`draw_heat_map`)**: 
   - Cleans the data by filtering out absurd blood pressure and height/weight values (removing extreme percentiles).
   - Calculates the correlation matrix for all variables.
   - Plots a Seaborn heatmap masking the upper triangle, providing a clear color-coded view of which health factors are most correlated.

## 🛠️ Technologies Used
- **Python 3**
- **Pandas:** For reading data and manipulating columns (adding overweight, normalizing values).
- **Seaborn:** For generating the categorical charts and heatmaps.
- **Matplotlib:** For rendering the figures.

## 🚀 How to Run
1. Ensure you have the required libraries installed:
   ```bash
   pip install pandas seaborn matplotlib
   ```
2. Run the main script to generate the plots:
   ```bash
   python main.py
   ```
3. To run the tests and verify the logic:
   ```bash
   python test_module.py
   ```
