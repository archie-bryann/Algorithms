# YouTube: Depth First Search (DFS) Explained - Algorithm, Examples and Code
# pseudocode

# preorder traversal
# first values visited
marked = [False] * G.size()
def dfs_pre(G, v):
    visit(v)
    marked[v] = True
    for w in G.neighbors(v):
        if not marked[w]:
            dfs_pre(G, w)


# postorder traversal
# get the values after there are no more neigbours
marked = [False] * G.size()
def dfs_post(G, v):
    marked[v] = True
    for w in G.neighbors(v):
        if not marked[w]:
            dfs_post(G, w)
    visit(v)