import pandas as pd

from earthflux.processing import annual_carbon_summary


def test_annual_carbon_summary():
    df = pd.DataFrame(
        {
            "Year": [2022, 2022, 2023],
            "GPP": [100.0, 150.0, 200.0],
            "Reco": [60.0, 70.0, 120.0],
        }
    )

    result = annual_carbon_summary(df)

    assert result.loc[0, "GPP"] == 250.0
    assert result.loc[0, "Reco"] == 130.0
    assert result.loc[0, "NEP"] == 120.0
    assert result.loc[1, "NEP"] == 80.0
