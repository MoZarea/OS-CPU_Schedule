from operator import add

def detect(process, allocation, request, available):
	n = len(process)
	finished = [False] * n
	count = n
	sequence = "Sequence: "
	for i in range(n):
		if request[i]==[0]*3:
			finished[i]=True
			count -= 1
			available = list(map(add, available, allocation[i]))
			allocation[i] = [0] * 3
			printState(allocation, request, available)
			sequence += "P{} -> ".format(i)
	while count != 0:
		safe = False
		for i in range(n):
			if finished[i] == False and request[i] <= available:
				available = list(map(add, available, allocation[i]))
				request[i] = [0] * 3
				allocation[i] = [0] * 3
				finished[i] = True
				safe = True
				sequence += "P{} -> ".format(i)
				count -= 1
				break
		printState(allocation, request, available)
		if not safe:
			break
	if(count != 0):
		print("\nDeadlock detected!")
	else:
		print("\nNo Deadlock has been detected.")
		sequence += "finished"
		print(sequence)
	
def printState(allocation, request, available):
	width = 12
	print("".ljust(width, " ")+"Allocation".ljust(width, " ")+"Request".ljust(width, " ")+"Available".ljust(width, " ")+"\n")
	for i in range(len(allocation)):
		print("P{}".format(i).ljust(width, " ")+('  '.join(map(str, allocation[i]))).ljust(width, " ")+('  '.join(map(str, request[i]))).ljust(width, " ")+(('  '.join(map(str, available)) + "\n") if i == 0 else "\n"))


if __name__=='__main__':
	process=[0, 1, 2, 3, 4]
	allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
	request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
	available=[0, 0, 0]
	printState(allocation, request, available)
	detect(process, allocation, request, available)