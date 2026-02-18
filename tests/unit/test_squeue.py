from src.squeue import SQueue

def test_squeue():
    squeue = SQueue()
    squeue.push(1)
    squeue.push(2)
    assert squeue.peek() == 1
    assert squeue.pop() == 1
    assert not squeue.empty()
    assert squeue.pop() == 2
    assert squeue.empty()