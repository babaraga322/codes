class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def column(matrix, i):
            return [row[i] for row in matrix]
        
        def sq(matrix,i,j):
            res=[]
            for x in range(i,i+3):
                for y in range(j,j+3):
                    res+=[matrix[x][y]]
            return res
                
        
        
        for i in range(9):
            temp = [val for val in board[i] if val!='.']
            if len(temp)!=len(set(temp)):
                return False
            
        for j in range(9):
            temp = [val for val in column(board,j) if val!='.']
            if len(temp)!=len(set(temp)):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                temp = [val for val in sq(board,i,j) if val!='.']
                
                if len(temp)!=len(set(temp)):
                    return False
        return True
            