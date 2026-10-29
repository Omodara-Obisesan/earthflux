from pathlib import Path

from earthflux import annual_carbon_summary, load_flux_data

example_file = Path(__file__).with_name("example_flux.csv")

df = load_flux_data(example_file)
summary = annual_carbon_summary(df)

print(summary)
