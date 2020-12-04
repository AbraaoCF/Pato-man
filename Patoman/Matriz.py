import os

main_dir = os.path.split(os.path.abspath(__file__))[0]
matriz = open(os.path.join(main_dir,"matriz.txt"), "r")

Matriz = [[]]
i = 0

for j in matriz.read():
	if(j == '\n'):
		Matriz.append([])
		i += 1
	else: Matriz[i].append(int(j))

def mat():
    newMat=[[0]*len(Matriz[0]) for i in range(len(Matriz))]
    for i in range(len(Matriz)):
        for j in range(len(Matriz[0])):
            newMat[i][j]=Matriz[i][j]
    return newMat
