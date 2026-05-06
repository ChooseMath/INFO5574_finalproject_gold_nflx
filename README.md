# INFO5574_finalproject_gold_nflx
Final project: data and analysis for studying the relationship between historical gold prices and Netflix (NFLX) stock performance.

## Data sources
- **Gold prices (GLD: SPDR® Gold Shares)**
  - **Source:** State Street Global Advisors / Yahoo Finance (`GLD`).
  - **Content:** Daily Net Asset Value (NAV) and Adjusted Close prices from 2004 onward. 
  - *Note: We utilize GLD rather than spot gold to perfectly align the trading calendar with the US stock market, eliminating microstructure noise.*

- **Netflix stock prices (NFLX)**
  - Source: Kaggle – historical daily Netflix stock price dataset.
  - Content: Daily Open, High, Low, Close, Adjusted Close, and Volume from 2002 onward.
  - This project uses the Adjusted Close price.
  - https://www.kaggle.com/datasets/henryshan/netflix-stock-price

## What we do

Part 1: Data preprocessing

As data lead, my responsibilities in this repo are:

1. **Load and clean raw data**
   - Read the World Gold Council Excel file and select the Yearly_Avg sheet.
   - Handle the irregular header rows and extract the date column and the USD gold price column.
   - Read the Netflix daily price CSV and parse the `Date` column as a time index.

2. **Aggregate to annual series**
   - Convert daily Netflix Adjusted Close prices to **annual average prices**.
   - Convert yearly gold prices to a clean annual USD series (year-end dates).
   - Extract the calendar year and build two tables:  
     - `Year`, `Gold_USD_mean`  
     - `Year`, `NFLX_AdjClose_mean`

3. **Merge and export**
   - Merge the gold and Netflix annual tables on the `Year` column.
   - Save the merged dataset as:

   ```text
   data/combined_gold_nflx_yearly.csv
   ```

   with columns:
   - `Year`
   - `Gold_USD_mean`
   - `NFLX_AdjClose_mean`

This merged CSV is the input for the other team members, who will perform statistical analysis and create visualizations in separate notebooks.


Part 3: Visualization and insights

As the visualization lead, my responsibilities in this repo are:

1. **Generate time-series visualizations**
   - Create a dual-axis line chart to compare annual gold prices and Netflix stock prices.
   - Use the Year column as the x-axis and plot both variables with separate y-axes for clarity.
   - Highlight long-term trends and major fluctuations.
2. **Analyze relationships between variables**
   - Create a scatter plot of Gold_USD_mean vs NFLX_AdjClose_mean.
   - Fit a linear regression line to visualize the overall relationship.
   - Observe whether the relationship appears linear and identify any outliers.
3. **Compute and visualize correlation**
   - Calculate the correlation matrix between gold prices and Netflix stock prices.
   - Generate a heatmap to present the correlation coefficient in a clear and interpretable way.
4. **Interpret results and provide insights**
   - Summarize key findings from the visualizations.
   - Discuss whether the relationship is positive, negative, or weak.
   - Clarify that correlation does not imply causation.
   - Identify possible external factors (e.g., macroeconomic trends, market growth) influencing both variables.
These visualizations are used to support the statistical analysis results and provide intuitive insights into the relationship between the two variables.
