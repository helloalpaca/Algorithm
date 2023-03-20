"""
class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
"""

answer_preorder = ""
answer_inorder = ""
answer_postorder = ""

def preorder(root, trees):
    if root != ".":
        global answer_preorder
        answer_preorder += root
        preorder(trees[root][0], trees)
        preorder(trees[root][1], trees)

def inorder(root, trees):
    if root != ".":
        global answer_inorder
        inorder(trees[root][0], trees)
        answer_inorder += root
        inorder(trees[root][1], trees)

def postorder(root, trees):
    if root != ".":
        global answer_postorder
        postorder(trees[root][0], trees)
        postorder(trees[root][1], trees)
        answer_postorder += root

def solution(N, edges):
    trees = {}
    for i in range(N):
        trees[edges[i][0]] = [edges[i][1], edges[i][2]]

    preorder("A", trees)
    inorder("A", trees)
    postorder("A", trees)
    return answer_preorder + "\n" + answer_inorder + "\n" + answer_postorder

if __name__ == '__main__':
    N = int(input())
    edges = []

    for _ in range(N):
        edges.append(input().split())

    print(solution(N, edges))