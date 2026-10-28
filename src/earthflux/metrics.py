"""Carbon-flux metric calculations."""

from numbers import Real


def calculate_nep(gpp: Real, reco: Real) -> float:
    """Calculate net ecosystem production.

    EarthFlux uses the convention:

        NEP = GPP - Reco

    Parameters
    ----------
    gpp
        Gross primary productivity.
    reco
        Ecosystem respiration.

    Returns
    -------
    float
        Net ecosystem production.
    """
    return float(gpp - reco)
