from earthflux.metrics import calculate_nep


def test_calculate_nep():
    assert calculate_nep(500, 300) == 200.0


def test_calculate_nep_negative():
    assert calculate_nep(200, 300) == -100.0
