from src.QStack import QStack

def test_qstack_innit():
    stack = QStack()
    assert stack.empty() == True

def test_qstack_empty():
    stack = QStack()
    assert stack.empty() == True
    stack.push(1)
    assert stack.empty() == False
    stack.pop()
    assert stack.empty() == True

def test_qstack_push_pop_peek():
    stack = QStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3
    assert stack.pop() == 3
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1
    assert stack.pop() == 1
    assert stack.peek() == -1
    assert stack.pop() == -1