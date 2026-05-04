import sys
import warnings
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.stattools import grangercausalitytests

CSV_PATH = Path(r"e:\Download\combined_goldandnflx_yearly.csv")
MAX_GRANGER_LAG = 2


def granger_lines(data: pd.DataFrame, maxlag: int, title: str) -> None:
    print(title)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=FutureWarning)
        out = grangercausalitytests(data, maxlag=maxlag, verbose=False)
    for lag in range(1, maxlag + 1):
        f_stat, p_val, _, _ = out[lag][0]["ssr_ftest"]
        print(f"  lag {lag}: F = {f_stat:.4f}, p = {p_val:.4f}")
    print()


def main():
    df = pd.read_csv(CSV_PATH)
    cols = ["Gold_USD_mean", "NFLX_AdjClose_mean"]

    print("First rows:")
    print(df.head())
    print(f"n = {len(df)}\n")

    means_stds = df[cols].agg(["mean", "std"])
    print("Mean and standard deviation:")
    print(means_stds.T.round(4))
    print()

    corr = df[cols].corr()
    print("Correlation matrix:")
    print(corr.round(4))
    print()

    y = df["NFLX_AdjClose_mean"]
    X = sm.add_constant(df["Gold_USD_mean"])
    res = sm.OLS(y, X).fit()
    print(res.summary())
    print()

    ts = df[cols].dropna()
    granger_lines(
        ts[["NFLX_AdjClose_mean", "Gold_USD_mean"]],
        MAX_GRANGER_LAG,
        "Granger: gold -> NFLX (H0: gold does not Granger-cause NFLX)",
    )
    granger_lines(
        ts[["Gold_USD_mean", "NFLX_AdjClose_mean"]],
        MAX_GRANGER_LAG,
        "Granger: NFLX -> gold (H0: NFLX does not Granger-cause gold)",
    )


if __name__ == "__main__":
    main()
