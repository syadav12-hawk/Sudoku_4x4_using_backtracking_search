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
	global que
	global pre_prob
	(i,j)=prob[k]
	print(puz)
	if bt_flag==1:
		t=puz[i][j]
		puz[i][j]=0
		dom=dom_find(puz,i,j)
		print(dom,"is the dom of ", k)
		if len(dom)==0:
			pre_prob[k]=[]
			back_track(puz,prob,k-1)
		else:
			
			count=0
			mod_dom=[]
			for f in pre_prob.keys():
				if f==k:
					print(pre_prob[f], ' ',f)
					for w in dom:
						flag4=0
						for v in pre_prob[f]:
							if v==w:
								flag4=1
								break
						if flag4==1:
							continue
						else:
							mod_dom.append(w)
					print('Modified dom', mod_dom)
					if len(mod_dom)==0:
						bt_flag=1
						puz[i][j]=0
						pre_prob[k]=[]
						back_track(puz,prob,k-1)
					else:
						bt_flag=0
						for x in mod_dom:
							puz[i][j]=x
							pre_prob[k].append(x)
							if k<len(prob)-1:
								back_track(puz,prob,k+1)
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
