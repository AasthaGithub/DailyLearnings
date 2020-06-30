#backtracking
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = '$'
        
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word
        
        rowNum = len(board)
        colNum = len(board[0])
        
        matchedWords = []
        
        def backtracking(row, col, parent):    
            
            letter = board[row][col]
            currNode = parent[letter]
            
            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)
            # Before the EXPLORATION, mark the cell as visited 
            board[row][col] = '#'
            
            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset     
                if newRow < 0 or newRow >= rowNum or newCol < 0 or newCol >= colNum:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)
        
            # End of EXPLORATION, we restore the cell
            board[row][col] = letter
        
            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)
        
        return matchedWords    



#dfs trie
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
      
		#	1. build trie with all words list
		#	2. start scanning matrix, move in all four directions and check if such combination exists in the trie
		#	3. make sure you donot return when result is found ( case: words = [cat, cattle ] )
		
        ## TIME COMPLEXICITY : O(M(4x3^(L-1))) ## (M is the number of cells in the board and L is the maximum length of words.)
		## SPACE COMPLEXICITY : O(N) ##
	    
        def dfs(i, j, curr, currNode):
            ch = board[i][j]
            if( ch not in currNode.children or (i, j) in visited ):
                return
            if currNode.children[ch].endOfWord:
                res.add(curr)
                # return                            # edge case
            visited.add((i,j))
            for x,y in directions:
                if 0 <= i + x < m and 0 <= j + y < n:
                    dfs( i + x, j + y, curr + board[i + x][j + y], currNode.children[ch])
            visited.remove((i,j))   # edge case
        
        # buid trie data structure
        my_trie = Trie()
        [ my_trie.insert(word) for word in words ]
        rootNode = my_trie.get_rootNode()
        
        m, n = len(board), len(board[0])
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        res = set()                     
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = set()
                dfs(i, j, board[i][j], rootNode)
        return res
    
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.rootNode = TrieNode()
    
    def get_rootNode(self):
        return self.rootNode
    
    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        currNode = self.rootNode
        for idx, ch in enumerate(word):
            if( ch not in currNode.children ):
                currNode.children[ch] = TrieNode()
            currNode = currNode.children[ch]        
        currNode.endOfWord = True
        
        
#reduce 
from functools import reduce
from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # create trie
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        
        for word in words:
            reduce(dict.__getitem__,word,trie)[END] = word
        
        res = set()
        def findstr(i,j,t):
            if END in t:
                res.add(t[END])
                # return
            letter = board[i][j]
            board[i][j] = ""
            if i > 0 and board[i-1][j] in t:
                findstr(i-1,j,t[board[i-1][j]])
            if j>0 and board[i][j-1] in t:
                findstr(i,j-1,t[board[i][j-1]])
            if i < len(board)-1 and board[i+1][j] in t:
                findstr(i+1,j,t[board[i+1][j]])
            if j < len(board[0])-1 and board[i][j+1] in t:
                findstr(i,j+1,t[board[i][j+1]])
            board[i][j] = letter
            
            return 
        
        for i, row in enumerate(board):
            for j, char in enumerate(row):
                if board[i][j] in trie:
                    findstr(i,j,trie[board[i][j]])
        return res
