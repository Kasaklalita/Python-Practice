from .second import mirror


def test_mirror():
    assert mirror(2, 45) == [10, 15]
    assert mirror(0, 0) == [0, 0]
    assert mirror(6, 45) == [6, 15]
