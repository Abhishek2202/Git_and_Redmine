def SumTriangle(A):
    if len(A)==0:
       return A
    else:
        return A[0] + SumTriangle(A[1:])       

A = [ 1, 2, 3, 4]
(SumTriangle(A))