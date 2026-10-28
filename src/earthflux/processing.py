"""Processing and aggregation routines."""

import pandas as pd

from .metrics import calculate_nep


def annual_carbon_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Aggregate GPP and Reco by year and calculate annual NEP.

    Parameters
    ----------
    df
        DataFrame containing Year, GPP, and Reco columns.

    Returns
    -------
    pandas.DataFrame
        Annual GPP, Reco, and NEP values.
    """
    required = {"Year", "GPP", "Reco"}
    missing = sorted(required.difference(df.columns))

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    annual = (
        df.groupby("Year", as_index=False)
        .agg(
            GPP=("GPP", "sum"),
            Reco=("Reco", "sum"),
        )
        .sort_values("Year")
        .reset_index(drop=True)
    )

    annual["NEP"] = [
        calculate_nep(gpp, reco)
        for gpp, reco in zip(annual["GPP"], annual["Reco"])
    ]

    return annual
