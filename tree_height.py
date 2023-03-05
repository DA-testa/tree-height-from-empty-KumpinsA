import sys
import threading


<<<<<<< Updated upstream
def compute_height(n, values):
    nodes = [[] for _ in range(n)]
    for i in range(n):
=======
def compute_height(size, values):
    nodes = [[] for _ in range(size)]
    for i in range(size):
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
    what_input = input()

    if what_input == "I":
        n = int(input("Size: "))
        values = list(map(int, input().split()))
    elif what_input == "F":
        return

    else:
        print("Invalid input")
        exit()

    print(compute_height(n, values))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
=======
    what_input = input("I or F: ")
    
    if what_input == "F":
        file_name = input()
        if "a" in file_name.lower:
            return
        else:
            with open(file_name, "r") as file:
                size = int(file.readline())
                values = list(map(int, file.readline().split()))
    
    elif (what_input == "I"):
        size = int(input("Size: "))

        values_str = input("Values: ")
        values = list(map(int, values_str.split()))

    else:
        print("Invalid input")
        main()

    print(compute_height(size, values))

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
>>>>>>> Stashed changes
