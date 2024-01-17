# every node in a tree shd hv atmost 2 nodes (0,1,2)
# Types 
    # > Full BT / Strictly BytesWarning - must hv 2 chl exept leaf
    # > Almost complete BT / Incomplete BT - must hv 2 chl in all d lvls except in last lvl but  filled from left to ri8
    # > Complete BT / Perfect BT - must hv 2 chl in all d lvls / 2^L nodes
    # > Left skewed BT - every node sld hv only left children
    # > Ri8 skewed BT - every node sld hv only ri8 children
# Representation 
# 1. linear nd seq - using array
# 2. linear nd seq - using list

# using Array 
# > root node index 0
# > Left child - placed at > 2i+1 (i is position of parent)
# > Right child - placed at > 2i+2

# using List
# {[adrss of prv][data][adrss of prv]} 

# Construction of tree with inorder and postorder 
# Inorder - Left root ri8 (B A C)
# postorder - left ri8 root (B C A)

# Post order > root
# Inorder > Ri8/left 

