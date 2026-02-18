from src.DSU import DSU
from src.QStack import QStack
from src.squeue import SQueue

def test_QStack_DSU():
    stack:QStack = QStack()    

    dsu1:DSU = DSU(2)
    dsu2:DSU = DSU(3)
    dsu3:DSU = DSU(4)
    dsu4:DSU = DSU(5)

    stack.push(dsu1)
    stack.push(dsu2)
    stack.push(dsu3)
    stack.push(dsu4)

    assert stack.pop() == dsu4

    assert stack.peek() == dsu3

def test_squeue_DSU():
    squeue:SQueue = SQueue()

    dsu1:DSU = DSU(2)
    dsu2:DSU = DSU(3)
    dsu3:DSU = DSU(4)
    dsu4:DSU = DSU(5)

    squeue.push(dsu1)
    squeue.push(dsu2)
    squeue.push(dsu3)
    squeue.push(dsu4)

    assert squeue.pop() == dsu1

    assert squeue.peek() == dsu2