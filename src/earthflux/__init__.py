"""EarthFlux: lightweight tools for environmental carbon-flux data processing."""

from .io import load_flux_data
from .metrics import calculate_nep
from .processing import annual_carbon_summary

__all__ = [
    "load_flux_data",
    "calculate_nep",
    "annual_carbon_summary",
]

__version__ = "0.1.0"
