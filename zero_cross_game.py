import sys

def check_pattern(mat):
    masterlist = []
    for i in range(3):
        list = []
        for j in range(3):
            if len(masterlist)<=3:
                list.append(mat[i][j])
            elif len(masterlist)<=6:
                list.append(mat[j][i])
            else
        masterlist.append(list)

    list1=[mat[0][0],mat[1][0],mat[2][0]]
