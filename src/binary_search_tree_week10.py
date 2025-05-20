class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def build_complete_bst(sorted_values):
    def helper(left, right):
        if left > right:
            return None
        mid = (left + right) // 2
        node = Node(sorted_values[mid])
        node.left = helper(left, mid - 1)
        node.right = helper(mid + 1, right)
        return node
    return helper(0, len(sorted_values) - 1)

def build_perfect_bst(sorted_values):
    # Hanya bekerja jika jumlah node = 2^h - 1 (contoh: 7 node)
    return build_complete_bst(sorted_values)  # Perfect BST adalah Complete BST dengan semua level terisi penuh

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.value))
        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")

# Input dari pengguna
nodes = []
print("Masukkan 7 nilai untuk node (pisahkan dengan spasi):")
input_values = input().split()
nodes = [int(val) for val in input_values[:7]]  # Ambil 7 nilai pertama

if len(nodes) != 7:
    print("Harap masukkan tepat 7 nilai!")
    exit()

# Urutkan nilai untuk memastikan Complete/Perfect BST
sorted_values = sorted(nodes)
complete_bst = build_complete_bst(sorted_values)
perfect_bst = build_perfect_bst(sorted_values)  # Sama dengan Complete BST jika node = 7

print("\nComplete BST:")
print_tree(complete_bst)

print("\nPerfect BST (sama dengan Complete BST karena 7 node = 2^3-1):")
print_tree(perfect_bst)
