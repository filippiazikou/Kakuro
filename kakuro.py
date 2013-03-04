from parse import *
from csp import *
from utils import *
from csp_search import *


#Change to appropriate puzzle!
puzzle = puzzle3

#Change to value: bt - btmrv - fc - fcmrv
algorithm = "bt"


class Kakuro(CSP):
	def __init__(self):
		self.parse_data()
		CSP.__init__(self,self.Variables, self.DomainDict, self.NeighborsDict, self.has_conflict) 
		
	def has_conflict(self, var, val, assignment):
		#numbers in the same column or line must differ
		#print assignment
		for neighbor in self.NeighborsDict[var]:
			if neighbor in assignment:
				if assignment[neighbor] == val:
					return True 
		#check for the sum 
		for sum_element in self.Sums:
			if var in sum_element[1]:
				if (algorithm == "bt" or algorithm == "btmrv"):
					s=val
					counter=1
				else:
					s=0
					counter=0
				for Xsum in sum_element[1]:
					if Xsum in assignment:
						s = s + assignment[Xsum]
						counter =counter +1
				#if all neighbors are in assignment
				if (counter==len(sum_element[1]) and s!=sum_element[0]):
					return True
				#if not all neighbors in assignment yet
				if (counter<len(sum_element[1]) and s>=sum_element[0]):
					return True
		return False 
		
	def parse_data(self):
		#print "~~~PUZZLE~~~"
		self.Variables = []
		for i, line in enumerate(puzzle):
			#print line
			for j, element in enumerate(line):
				if element == '_':
					var1 = str(i)
					if len(var1) == 1:
						var1 ="0"+var1
					var2 = str(j)
					if len(var2) == 1:
						var2 ="0"+var2
					self.Variables.append("X"+var1+var2)
					
		#print "~~~VARIABLES~~~"
		#print self.Variables

		#print "~~~DOMAIN~~~"
		self.DomainDict = {}
		for element in self.Variables:
			self.DomainDict[element]=[]
			for i in range(1,10):
				self.DomainDict[element].append(i)
				
		#print self.DomainDict
		#print "~~~SUMS~~~"
		self.Sums = []
		for i, line in enumerate(puzzle):
			for j, element in enumerate(line):
				if (element != '_' and element != '*'):
					#down - column
					if (element[0] != ''):
						x = []
						for k in range(i+1, len(puzzle)):
							if (puzzle[k][j] != '_'):
								break
							var1 = str(k)
							if len(var1) == 1:
								var1 ="0"+var1
							var2 = str(j)
							if len(var2) == 1:
								var2 ="0"+var2
							x.append("X"+var1+var2)
						self.Sums.append((element[0],x))
					#right - line
					if (element[1] != ''):
						x = []
						for k in range(j+1, len(puzzle[i])):
							if (puzzle[i][k] != '_'):
								break
							var1 = str(i)
							if len(var1) == 1:
								var1 ="0"+var1
							var2 = str(k)
							if len(var2) == 1:
								var2 ="0"+var2
							x.append("X"+var1+var2)
						self.Sums.append((element[1],x))
						
		#print self.Sums
		#print "~~NEIGHBORS DICTIONARY~~"
		self.NeighborsDict = {}
		for element in self.Variables:
			self.NeighborsDict[element]=[]
			for sum_element in self.Sums:
				if element in sum_element[1]:
					self.NeighborsDict[element]+=sum_element[1]
					del self.NeighborsDict[element][self.NeighborsDict[element].index(element)]
		#print self.NeighborsDict				


solution = Kakuro()

print "~~~RESULT~~~"
if algorithm == "fc":
	result = backtracking_search(solution, inference=forward_checking)
if algorithm == "bt":
	result = backtracking_search(solution)
if algorithm == "btmrv":
	result = backtracking_search(solution, select_unassigned_variable=mrv)
if algorithm == "fcmrv":
	result = backtracking_search(solution, select_unassigned_variable=mrv, inference=forward_checking)
#result = backtracking_search(solution)
for i, line in enumerate(puzzle):
	string =""
	for j, element in enumerate(line):
		if element == '*':
			string = string+"[*]\t"
		elif element =='_':
			var1 = str(i)
			if len(var1) == 1:
				var1 ="0"+var1
			var2 = str(j)
			if len(var2) == 1:
				var2 ="0"+var2
			var="X"+var1+var2
			string = string+"["+str(result[var])+"]\t"
		else:
			string=string+str(element[0])+"/"+str(element[1])+"\t"
	print string
#print result