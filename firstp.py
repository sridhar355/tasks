class ListDict:
	
	def __init__(self):
		pass
	
	def addElementToList(self,lst,a):
		
		lst.append(a)
	def addElementToDict(self,dict,b,c):
		
		dict[b]=c
	def printObject(self,lst,dict):
		print("list",lst)
		print("dictionary",dict)