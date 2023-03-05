import sys
import threading


def compute_height(size, values):
    nodes = [[] for _ in range(size)]
    for i in range(size):
        if values[i] == -1:
            root = i
        else:
            nodes[values[i]].append(i)

    max_height = 0
    stack = [(root, 1)]
    while stack:
        node, height = stack.pop()
        max_height = max(max_height, height)
        for child in nodes[node]:
            stack.append((child, height+1))

    return max_height


def main():
    what_input = input()
    
    if what_input == "F":
        file_name = input()
        if "a" in file_name.lower:
            return
        else:
            with open(file_name, "r") as file:
                size = int(file.readline())
                values = list(map(int, file.readline().split()))
    
    elif (what_input == "I"):
        size = int(input())

        values_str = input()
        values = list(map(int, values_str.split()))

    else:
        print("Invalid input")
        main()

    print(compute_height(size, values))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()