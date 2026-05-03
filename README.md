# INFO5574_finalproject_gold_nflx
Final project: data and analysis for studying the relationship between historical gold prices and Netflix (NFLX) stock performance.

## Data sources
- **Gold prices (USD)**
  - Source: World Gold Council – historical gold price data (Yearly_Avg sheet).
  - Content: Gold prices per troy ounce in multiple currencies since 1978.
  - This project uses the USD-denominated series.
  - https://goldprice.org/

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
