#! /usr/bin/env python
#coding=utf-8

class node:
	def __init__(self, s):
		self.data = s
		self.left = None
		self.right = None

def build_tree():
	tree_data = ['A','B','C','D','E','F','G','H','I']
	node_list = []

	for i in range(0, len(tree_data)):
		if(i == 0):
			root = node(tree_data[i])
			root.left = node(tree_data[i*2+1])
			root.right = node(tree_data[i*2+2])
			node_list.append(root)
			node_list.append(root.left)
			node_list.append(root.right)
		else:
			if((i*2+1) >= len(tree_data)):
				break
			node_list[i].left = node(tree_data[i*2+1])
			node_list.append(node_list[i].left)
			if((i*2+2) >= len(tree_data)):
				break		
			node_list[i].right = node(tree_data[i*2+2])
			node_list.append(node_list[i].right)
	return root

def dfs(root):
	if(root == None):
		return 
	print("data: ", root.data)
	dfs(root.left)
	dfs(root.right)

root = build_tree()
dfs(root)


