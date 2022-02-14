with open('file1.txt') as F1,open('file2.txt') as F2:
	for L1,L2 in zip(F1,F2):
		L1=L1.strip()
		L2=L2.strip()
		print(L1+L2)