# EarthFlux

EarthFlux is a small Python package for processing environmental carbon-flux
data. The first version focuses on a simple, testable workflow:

1. Load and validate flux data.
2. Calculate net ecosystem production (NEP).
3. Produce annual carbon-flux summaries.

The project is intentionally small so it can serve as a software-engineering
foundation that can later grow into a more complete Earth-system analysis
library.

## Installation

Clone the repository and enter the project directory:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
cd earthflux
```

Create and activate a virtual environment.

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

Install EarthFlux in editable mode with development tools:

```bash
python -m pip install --upgrade pip
pip install -e ".[dev]"
```

## Quick start

```python
from earthflux import load_flux_data, annual_carbon_summary

df = load_flux_data("examples/example_flux.csv")
summary = annual_carbon_summary(df)

print(summary)
```

Expected output:

```text
   Year    GPP   Reco    NEP
0  2021  220.0  150.0   70.0
1  2022  320.0  205.0  115.0
2  2023  340.0  215.0  125.0
```

## Run the tests

```bash
pytest
```

## Run the example

```bash
python examples/quickstart.py
```

## Current project structure

```text
earthflux/
├── .github/
│   └── workflows/
│       └── tests.yml
├── examples/
│   ├── example_flux.csv
│   └── quickstart.py
├── src/
│   └── earthflux/
│       ├── __init__.py
│       ├── io.py
│       ├── metrics.py
│       └── processing.py
├── tests/
│   ├── test_io.py
│   ├── test_metrics.py
│   └── test_processing.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Roadmap

### v0.1

- CSV loading and validation
- NEP calculation
- Annual carbon-flux summaries
- Automated tests
- Continuous integration

### v0.2

- Timestamp parsing and temporal quality checks
- Missing-value handling
- Flux-unit validation
- Multiple-site support
- Logging
- Type checking

### v0.3

- NEE/GPP/Reco sign-convention support
- Carbon-budget calculations
- Yield and NECB support
- Plotting utilities
- Command-line interface

### Later

- xarray and NetCDF support
- Parallel processing
- Configuration files
- Docker
- API service
- Cloud deployment

## Scientific convention

The initial implementation uses:

```text
NEP = GPP - Reco
```

Before applying the package to observational datasets, verify that the sign
conventions and units of the input data match this definition.

## License

MIT
