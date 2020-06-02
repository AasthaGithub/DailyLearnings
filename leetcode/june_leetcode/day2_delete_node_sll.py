#to delete a node if access given to current node only    
    
    node.val = node.next.val;
    node.next = node.next.next;
