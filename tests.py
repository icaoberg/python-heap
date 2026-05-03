import pytest
from Heap import MinHeap, MaxHeap

# --- MinHeap ---

def test_minheap_empty():
    h = MinHeap()
    assert h.is_empty()
    assert h.size() == 0
    assert len(h) == 0

def test_minheap_push():
    h = MinHeap()
    for i, val in enumerate([5, 3, 7, 1, 4]):
        h.push(val)
        assert h.size() == i + 1

def test_minheap_peek():
    h = MinHeap()
    for val in [5, 3, 7, 1, 4]:
        h.push(val)
    assert h.peek() == 1

def test_minheap_pop_order():
    h = MinHeap()
    for val in [5, 3, 7, 1, 4]:
        h.push(val)
    result = [h.pop() for _ in range(h.size() + 1) if not h.is_empty()]
    assert result == sorted(result)

def test_minheap_pop_empty():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.pop()

def test_minheap_peek_empty():
    h = MinHeap()
    with pytest.raises(IndexError):
        h.peek()

def test_minheap_random():
    h = MinHeap()
    h.random(10)
    assert h.size() == 10
    assert h.peek() == 0

def test_minheap_random_invalid():
    h = MinHeap()
    h.random(0)
    assert h.is_empty()

def test_minheap_tolist():
    h = MinHeap()
    h.push(1)
    h.push(2)
    result = h.tolist()
    result.append(99)
    assert h.size() == 2

def test_minheap_repr():
    h = MinHeap()
    h.push(1)
    assert "MinHeap" in repr(h)

# --- MaxHeap ---

def test_maxheap_empty():
    h = MaxHeap()
    assert h.is_empty()
    assert h.size() == 0
    assert len(h) == 0

def test_maxheap_peek():
    h = MaxHeap()
    for val in [5, 3, 7, 1, 4]:
        h.push(val)
    assert h.peek() == 7

def test_maxheap_pop_order():
    h = MaxHeap()
    for val in [5, 3, 7, 1, 4]:
        h.push(val)
    result = [h.pop() for _ in range(h.size() + 1) if not h.is_empty()]
    assert result == sorted(result, reverse=True)

def test_maxheap_pop_empty():
    h = MaxHeap()
    with pytest.raises(IndexError):
        h.pop()

def test_maxheap_peek_empty():
    h = MaxHeap()
    with pytest.raises(IndexError):
        h.peek()

def test_maxheap_random():
    h = MaxHeap()
    h.random(10)
    assert h.size() == 10
    assert h.peek() == 9

def test_maxheap_repr():
    h = MaxHeap()
    h.push(1)
    assert "MaxHeap" in repr(h)
