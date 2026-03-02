import math

class Node:
    def __init__(self, value=None):
        self.value = value      
        self.children = []

def alpha_beta(node, depth, alpha, beta, maximizing_player):
    
   
    if depth == 0 or not node.children:
        return node.value

    if maximizing_player:
        max_eval = -math.inf
        
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            
            if beta <= alpha:
                break   
        
        return max_eval

    else:
        min_eval = math.inf
        
        for child in node.children:
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            
            if beta <= alpha:
                break
            return min_eval



if __name__ == "__main__":
    
    root = Node()
    
    left = Node()
    right = Node()
    
    left.children = [Node(3), Node(5)]
    right.children = [Node(6), Node(9)]
    
    root.children = [left, right]
    
    result = alpha_beta(root, depth=2, alpha=-math.inf, beta=math.inf, maximizing_player=True)
    
    print("Best value:", result)
 
