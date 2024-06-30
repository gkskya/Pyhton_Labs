def heapifyDown(H, i):
    n = len(H) - 1
    while 2*i <= n:
        j = 2*i
        if j+1 <= n and H[j+1] > H[j]:
            j += 1
        if H[i] >= H[j]:
            break
        H[i], H[j] = H[j], H[i]
        i = j
        
def heapify_up(H, i):
    while i > 1 and H[i//2] < H[i]:
        H[i], H[i//2] = H[i//2], H[i]
        i //= 2

def build_heap(H):
    n = len(H) - 1
    for i in range(n//2, 0, -1):
        heapifyDown(H, i)
    return H

def bottom_up_heap_construction(A):
    n = len(A) - 1
    H = [0] * (n+1)
    H[1:] = A[1:]
    build_heap(H)
    
    print("Beginning Array:", A[1:])
    print("Array after heapify:", H[1:])
    
    root_node = H[1]
    print("root node:", root_node)
    
    level_2_nodes = [H[2], H[3]]
    print("2. level nodes:")
    print(level_2_nodes)
    
    level_3_nodes = [H[4], H[5], H[6], H[7]]
    print("3. level nodes:")
    print(level_3_nodes)
    print()
    
    return H[1:]

A = [0, 2, 9, 7, 6, 5, 8, 10]
bottom_up_heap_construction(A)

A = [0, 12, 11, 13, 5, 6, 7]
bottom_up_heap_construction(A)

