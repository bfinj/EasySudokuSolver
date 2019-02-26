class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        while True:
            for i in range(9):
                for j in range(9):
                    temp = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                    if board[i][j] not in temp:
                        ans = []
                        top = i / 3
                        left = j / 3
                        for tem in temp:
                            if tem not in board[i] and tem not in [board[k][j] for k in range(9)]:
                                ap = 1
                                for k in range(3):
                                    for l in range(3):
                                        if tem == board[top*3+k][left*3+l]:
                                            ap = 0
                                if ap == 1:
                                    ans.append(tem)
                        board[i][j] = "".join(ans)
            con = 0
            for i in range(9):
                for j in range(9):
                    if len(board[i][j]) != 1:
                        con = 1
                        break
            if con == 0:
                break
