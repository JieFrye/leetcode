class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        Note applying the above rules simultaneously requires
        the use of other integers
        die -> live use 3
        live -> die use 2
        '''
        if not board or len(board) == 0:
            return
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0:
                    if self.count(board,i,j) == 3:
                        # die -> live
                        board[i][j] = 3
                if board[i][j] == 1:
                    live = self.count(board,i,j)
                    if live < 2 or live > 3:
                        # live -> die
                        board[i][j] = 2
        # update the board
        for i in range(len(board)):
            for j in range(len(board[0])):
                # note that some cell has not changed
                if board[i][j] == 2 or board[i][j] == 3:
                    board[i][j] -= 2


    def count(self, board, i, j):
        '''
        count the number of live cells in the eight neighbors
        '''
        c = 0
        directions = [[0, -1], [0,1], [-1,0], [1,0], \
                      [1, -1], [1,1], [-1,-1], [-1,1]]
        for d in directions:
            row = i + d[0]
            col = j + d[1]
            if (row >= 0 and row < len(board) and \
                col >= 0 and col < len(board[0]) and \
                (board[row][col] == 1 or board[row][col] == 2)):
                c += 1
        return c

board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(board)
sol = Solution()
sol.gameOfLife(board)
print(board)
