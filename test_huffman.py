import huffman_logic as h

m = h.build_huffman_lengths([5, 9, 12, 13, 25] , 5)

print(m)

k = h.get_canonical_map(m)

print(k)