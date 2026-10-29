"""Input/output utilities for EarthFlux."""

from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = ("Year", "GPP", "Reco")


def load_flux_data(filepath: str | Path) -> pd.DataFrame:
    """Load a flux CSV file and validate required columns.

    Parameters
    ----------
    filepath
        Path to a CSV file containing at least Year, GPP, and Reco.

    Returns
    -------
    pandas.DataFrame
        Validated flux data.

    Raises
    ------
    FileNotFoundError
        If the input file does not exist.
    ValueError
        If one or more required columns are missing.
    """
    path = Path(filepath)

    if not path.exists():
        raise FileNotFoundError(f"Flux file not found: {path}")

    df = pd.read_csv(path)

    missing = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df
