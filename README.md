# python-heap

> [!WARNING]
> This implementation is inspired by a homework assignment from [15-213](https://www.cs.cmu.edu/~213/) at Carnegie Mellon University. It is intended for educational purposes only and is not suitable for production use.

[![CI](https://github.com/icaoberg/python-heap/actions/workflows/ci.yml/badge.svg)](https://github.com/icaoberg/python-heap/actions/workflows/ci.yml)
[![Release Status](https://img.shields.io/badge/release-v0.1-red.svg)](https://github.com/icaoberg/python-heap)
[![GitHub issues](https://img.shields.io/github/issues/icaoberg/python-heap.svg)](https://github.com/icaoberg/python-heap/issues)
[![GitHub forks](https://img.shields.io/github/forks/icaoberg/python-heap.svg)](https://github.com/icaoberg/python-heap/network)
[![GitHub stars](https://img.shields.io/github/stars/icaoberg/python-heap.svg)](https://github.com/icaoberg/python-heap/stargazers)
[![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://www.gnu.org/licenses/quick-guide-gplv3.en.html)

A simple naive implementation of a [heap](https://en.wikipedia.org/wiki/Heap_(data_structure)) in Python, providing both `MinHeap` and `MaxHeap`.

The purpose of this repo is to serve as an example of how to set up a GitHub Actions workflow.

## Definition

> A heap is a complete binary tree in which the value at the root is the minimum (min-heap) or maximum (max-heap) value in the tree, and both subtrees are also heaps.

— Paul E. Black, *[heap](https://xlinux.nist.gov/dads/HTML/heap.html)*, Dictionary of Algorithms and Data Structures [online], NIST.

## When to Use

A heap is the right structure when you repeatedly need the smallest or largest element with O(log n) insert and O(log n) removal:

- **Priority queues** — operating system schedulers and event-driven simulations use a min-heap to always process the highest-priority (lowest-value) task next.
- **Dijkstra's shortest path** — the algorithm uses a min-heap to greedily extract the unvisited node with the smallest tentative distance.
- **Heap sort** — inserting all elements into a max-heap and popping them in order produces a sorted list in O(n log n).
- **Median maintenance** — pairing a max-heap (lower half) and a min-heap (upper half) lets you track the running median in O(log n) per insertion.
- **K largest / K smallest** — a min-heap of size k efficiently tracks the k largest elements seen in a stream without storing the entire dataset.

## Requirements

- Python 3.6+

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/icaoberg/python-heap.git
cd python-heap
pip install -r requirements.txt
```

## Usage

### MinHeap

```python
from Heap import MinHeap

h = MinHeap()
h.push(5)
h.push(3)
h.push(7)
h.push(1)
h.push(4)

print(h.size())     # 5
print(h.peek())     # 1  (minimum)
print(h.pop())      # 1
print(h.peek())     # 3
print(h.is_empty()) # False
print(len(h))       # 4
```

### MaxHeap

```python
from Heap import MaxHeap

h = MaxHeap()
h.push(5)
h.push(3)
h.push(7)
h.push(1)
h.push(4)

print(h.size())     # 5
print(h.peek())     # 7  (maximum)
print(h.pop())      # 7
print(h.peek())     # 5
print(h.is_empty()) # False
print(len(h))       # 4
```

### Methods

Both `MinHeap` and `MaxHeap` share the same interface:

| Method | Description |
|--------|-------------|
| `push(element)` | Insert an element into the heap |
| `pop()` | Remove and return the root element (min or max) |
| `peek()` | Return the root element without removing it |
| `random(n)` | Populate the heap with `n` random integers |
| `is_empty()` | Return `True` if the heap has no elements |
| `size()` | Return the number of elements |
| `tolist()` | Return a copy of the internal array representation |

## Testing

```bash
pytest tests.py
```

## Support

If you found this project helpful, consider buying me a coffee!

[![Buy Me a Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/icaoberg)

## Copyright

Copyright © [icaoberg](https://github.com/icaoberg) at [Carnegie Mellon University](https://www.cmu.edu). All rights reserved.
