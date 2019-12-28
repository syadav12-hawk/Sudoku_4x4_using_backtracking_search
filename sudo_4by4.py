global bt_flag

bt_flag=0


def dom_find(puz,i,j):
	dom=[]
	f_dom=[]
	t_puz=[]
	t_puz=puz
	#print(t_puz)

	univ_dom=[1,2,3,4]
	for k in univ_dom:
		flag1=0
		for c in [0,1,2,3]:
			if (k==t_puz[i][c]):
				flag1=1
				break
		if(flag1==0):
			dom.append(k)

	for l in dom:
		flag2=0
		for r in [0,1,2,3]:
			if (l==t_puz[r][j] and r!=i):
				flag2=1
				break
		if (flag2==0):		
			f_dom.append(l)

	#print(f_dom)

	return f_dom;


#Enter the Sudoku Table
#print("Enter the sudoku table")
#puz=[]
#for i in [1,2,3,4]:
#	row=[]
#	for j in [1,2,3,4]:
#		row.append(int(input()))
#	puz.append(row)

puz=[[0, 2, 1, 0], [3, 0, 0, 0], [0, 0, 0, 1], [0, 3, 4, 0]]
print(puz)


def back_track(puz,prob,k):
	global bt_flag
	(i,j)=prob[k]
	print(puz)
	if bt_flag==1:
		t=puz[i][j]
		puz[i][j]=0
		dom=dom_find(puz,i,j)
		print(dom," ", k)
		if len(dom)==1:
			back_track(puz,prob,k-1)
		else:
			bt_flag=0
			for m in dom:
				if t==m:
					continue
				puz[i][j]=m
				if k<len(prob)-1:
					back_track(puz,prob,k+1)
				return
	else:
		dom=dom_find(puz,i,j)
		print(dom," ", k)
		if len(dom)==0:
			bt_flag=1
			back_track(puz,prob,k-1)
		else:
			puz[i][j]=dom[0]
			if k<len(prob)-1:
				back_track(puz,prob,k+1)
			else:
				return


def sudoku_solver(puz):
	prob=[]
	que=[]

	for i in [0,1,2,3]:
		for j in [0,1,2,3]:
			if puz[i][j]==0:
				prob.append((i,j))
	back_track(puz,prob,0)
	print(puz)






sudoku_solver(puz)





#Sudoku Solver Fuction Using BackTracking Search
