import pandas as pd
import pytest

from earthflux.io import load_flux_data


def test_load_flux_data(tmp_path):
    filepath = tmp_path / "flux.csv"
    pd.DataFrame(
        {
            "Year": [2022, 2023],
            "GPP": [500.0, 550.0],
            "Reco": [300.0, 350.0],
        }
    ).to_csv(filepath, index=False)

    df = load_flux_data(filepath)

    assert list(df.columns) == ["Year", "GPP", "Reco"]
    assert len(df) == 2


def test_missing_required_column(tmp_path):
    filepath = tmp_path / "flux.csv"
    pd.DataFrame(
        {
            "Year": [2022],
            "GPP": [500.0],
        }
    ).to_csv(filepath, index=False)

    with pytest.raises(ValueError, match="Missing required columns"):
        load_flux_data(filepath)
