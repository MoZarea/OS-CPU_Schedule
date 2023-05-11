from operator import add

def detect(process, allocation, request, work):
	""" TODO: Implement a selected deadlock detection algorithm, 
		detect: receives processes, allocations, requests, and work 
		and returns true if a deadlock is detected otherwise false.   """

if __name__=='__main__':
	'''
	n=int(input('Enter number of processes: '))
	process=list(range(n))

	r=int(input('Enter number of resources: '))

	allocation=input('Enter allocation: ').split()
	request=input('Enter request: ').split()
	available=input('Enter available resources: ')
	'''

	process=[0, 1, 2, 3, 4]
	allocation=[[0, 1, 0], [2, 0, 0], [3, 0, 3], [2, 1, 1], [0, 0, 2]]
	request=[[0, 0, 0], [2, 0, 2], [0, 0, 0], [1, 0, 0], [0, 0, 2]]
	available=[0, 0, 0]

	detect(process, allocation, request, available)


