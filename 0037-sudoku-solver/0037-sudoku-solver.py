class Solution(object):
    def solveSudoku(self, board):
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    val = board[r][c]
                    row[r].add(val)
                    col[c].add(val)
                    s = (r//3)*3+(c//3)
                    box[s].add(val)
        def bt(r,c):
            if r==9:
                return True
            if c==9:
                return bt(r+1,0)
            if board[r][c]!='.':
                return bt(r,c+1)
            s=(r//3)*3+(c//3)
            for i in range(1,10):
                i=str(i)
                if i not in row[r] and i not in col[c] and i not in box[s]:
                    row[r].add(i)
                    col[c].add(i)
                    box[s].add(i)
                    board[r][c]=i
                    if bt(r,c+1):
                        return True
                    row[r].remove(i)
                    col[c].remove(i)
                    box[s].remove(i)
                    board[r][c]='.'
            return False
        return bt(0,0)