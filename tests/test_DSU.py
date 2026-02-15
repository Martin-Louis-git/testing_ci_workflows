from src.DSU import DSU

def test_dsu_init():
    dsu = DSU(5)
    assert dsu.parent == list(range(5))
    assert dsu.rank == [1] * 5

def test_dsu_find():
    dsu = DSU(5)
    assert dsu.find(0) == 0
    assert dsu.find(4) == 4

def test_dsu_union():
    dsu = DSU(5)
    assert dsu.union(0, 1) == True
    assert dsu.find(0) == 1
    assert dsu.union(1, 2) == True
    assert dsu.find(2) == 1