
import pytest

from earthflux.weather import download_weather


def test_invalid_latitude(tmp_path):
    """Latitude outside the valid range should be rejected."""

    with pytest.raises(ValueError, match="Latitude"):
        download_weather(
            latitude=100,
            longitude=-92.3341,
            start_date="2025-01-01",
            end_date="2025-01-31",
            output_file=tmp_path / "weather.csv",
        )


def test_invalid_longitude(tmp_path):
    """Longitude outside the valid range should be rejected."""

    with pytest.raises(ValueError, match="Longitude"):
        download_weather(
            latitude=38.9517,
            longitude=-200,
            start_date="2025-01-01",
            end_date="2025-01-31",
            output_file=tmp_path / "weather.csv",
        )


def test_invalid_date_range(tmp_path):
    """Start date must not come after the end date."""

    with pytest.raises(ValueError, match="Start date"):
        download_weather(
            latitude=38.9517,
            longitude=-92.3341,
            start_date="2025-02-01",
            end_date="2025-01-01",
            output_file=tmp_path / "weather.csv",
        )
