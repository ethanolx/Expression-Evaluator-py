'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
from enum import Enum


# Enum of all valid tree traversal orders (dfs)
class TreeTraversalOrder(Enum):
    IN_ORDER = 'In-Order'
    PRE_ORDER = 'Pre-Order'
    POST_ORDER = 'Post-Order'
