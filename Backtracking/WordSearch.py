# Word Search

# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

class Solution:
    def exist(self, board, word: str) -> bool:
        '''
        ideas: dfs
        '''
        def search(board, word, d, i, j, m, n):
            if i<0 or i==m or j<0 or j==n or word[d] != board[i][j]:
                return False
            # no return False yet and found all char in word
            if d == len(word) - 1:
                return True
            # same letter cell may not be used again
            curr = board[i][j]
            board[i][j] = 0
            # word[d] = board[i][j] so move on to next char
            found = search(board, word, d+1, i+1, j, m, n) or \
                    search(board, word, d+1, i-1, j, m, n) or \
                    search(board, word, d+1, i, j-1, m, n) or \
                    search(board, word, d+1, i, j+1, m, n)
            board[i][j] = curr
            return found

        if len(board) == 0:
            return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if search(board, word, 0, i, j, m, n):
                    return True
        return False

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = 'SEE'

sol = Solution()
print(sol.exist(board, word))
