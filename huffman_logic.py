# huffman_logic.py - TO BE COMPLETED 
import heapq


def build_huffman_lengths(freqs, limit):
    class Node:
        def __init__(self, freq, symbol=None, left=None, right=None):
            self.freq = freq
            self.symbol = symbol
            self.left = left
            self.right = right
        def __lt__(self, other):
            return self.freq < other.freq

    heap = []
    nodes = [None] * limit

    for i, f in enumerate(freqs):
        if f > 0:
            node = Node(f, i)
            nodes[i] = node
            heapq.heappush(heap, node)

    if len(heap) == 1:
        only = heap[0]
        return [1 if f > 0 else 0 for f in freqs]

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        parent = Node(left.freq + right.freq, None, left, right)
        heapq.heappush(heap, parent)

    root = heap[0]

    lengths = [0] * limit

    def dfs(node, depth):
        if not node:
            return
        if node.symbol is not None:
            lengths[node.symbol] = depth
            return
        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)

    return lengths


def get_canonical_map(lengths:list):
    
    map = {}

    sorted_lengths = sorted(enumerate(lengths), key=lambda x: (x[1] , x[0]))

    code = 0
    previous_length = 0

    for i , length in sorted_lengths :
        code = code << (length - previous_length)
        map[i] = format(code, f'0{length}b')
        code += 1
        previous_length = length
   
    return map