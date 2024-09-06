import sys
pyScriptName = sys.argv[0]
outputfile='outputScrollSaw.txt' #Final file containing sequences that passed ScrollSaw
def WriteList(txtFile,list):
	fileObj = open(txtFile, "w")
	for i in list:
		fileObj.write(i)
		fileObj.write('\n')
	fileObj.close()

def WriteList2(txtFile,list):
	fileObj = open(txtFile, "a")
	for i in list:
		fileObj.write(i)
		fileObj.write('\n')
	fileObj.close()

def Write_name_values(txtFile,name,listvalues):
	fileObj = open(txtFile, "a")
	fileObj.write('>')
	fileObj.write(name)
	fileObj.write('\n')
	kkkk=str(len(listvalues))
	fileObj.write('*')
	fileObj.write(kkkk)
	fileObj.write('\n')
	for k in listvalues:
		kk=str(k)
		fileObj.write(kk)
		fileObj.write(', ')
	fileObj.write('\n')
	fileObj.close()		

def write_report(r, filename):    
	with open(filename, "w") as input_file:
		for k, v in r.items():
			line = '{}, {}'.format(k, v) 
			print(line, file=input_file)
	
import itertools
comb=list(itertools.combinations(range(3), 2)) #generating a list with all possible pairs of taxonomic groups. The total number of taxonomic groups must be specified here (17 in our study, 3 for testing dataset)
numbercomb=len(comb)

totalnumber=0
ScrollSawsequence=[]

for k in comb:
	tax1=str(k[0])
	tax2=str(k[1])
	if len(tax1) == 1:
		tax1='0'+tax1
	if len(tax2) == 1:
		tax2='0'+tax2
	sequenceList=[]
	NameDistances=('%s_%s.phy.dist' %(tax1,tax2))
	dataFileName=NameDistances# generating names of files needed for the ScrollSaw analysis (outputs of Tree-Puzzle program, see Supplementary Methods for details)

	sequenceList=[]#List containing all sequence names
	fileObj = open(dataFileName, 'r')
	fileObj.readline()
	for l in fileObj:
		if l[0].isdigit():
			r = l.split('  ')
			r=l.split()
			name=r.pop(0)
			sequenceList.append(name)
	fileObj.close()

	fileObj = open(dataFileName, 'r')
	numsekv=int(fileObj.readline()) # reading the first line containing the number of sequences. This is followed by verification of the number of sequences
	if numsekv == len(sequenceList):
		print ('Everything is fine. The number of sequences is ', numsekv)
	else:
		print ('There is an error somewhere, the number of sequences does not match')
	fileObj.close()

	values=[]
	valuesFragm=[]
	name=''
	result={}
	ListOfNames=[]

	def lowest(valueList,name,tax1,tax2):#definition of the function that finds the lowest value
		minimalValue=0.0
		minimalSequence=''
		if name[0:2]  == (tax1): # determine whether a value belonging to a sequence from taxonomic group 1 is being compared
			for i in enumerate(valueList):
				if valueList[i[0]] != 0:
					p=[i[0]]
					p=int(p[0]) # p is the order of values in the list
					k=sequenceList[p] # k indicates which sequence corresponds to p
					if k[0:2] == (tax2):# considers only sequence values belonging to taxon 2
						if minimalValue:
							if valueList[i[0]]<minimalValue:
								minimalValue=valueList[i[0]]
								minimalSequence=k
						else:
								minimalValue=valueList[i[0]]
								minimalSequence=k						
		elif name[0:2]  == (tax2): # sequences from taxonomic group 2
			for i in enumerate(valueList):
				if valueList[i[0]] != 0:
					p=[i[0]]
					p=int(p[0]) # p is the order of values in the list
					k=sequenceList[p] # k indicates which sequence corresponds to p
					if k[0:2] == (tax1):# considers only sequence values belonging to taxon 1
						if minimalValue:
							if valueList[i[0]]<minimalValue:
								minimalValue=valueList[i[0]]
								minimalSequence=k
						else:
								minimalValue=valueList[i[0]]
								minimalSequence=k			
		it=[minimalSequence,minimalValue]
		return it		
	
	fileObj = open(dataFileName, 'r')
	fileObj.readline()
	for line in fileObj:
		if line[0].isdigit():
			if name:
				if name[0:2]  == (tax1):
					it = lowest(values, name, tax1, tax2)
					result[name]=it
					Write_name_values('values.txt',name,values)
					values=[]
					name=''
					line=line.rstrip() 
					r = line.split('  ') 
					r=line.split()
					name=r.pop(0) 
					ListOfNames.append(name)
					valuesFragm = [float(i) for i in r] 
					values.extend(valuesFragm)
					valuesFragm=[]	
				elif name[0:2]  == (tax2):
					it = lowest(values, name, tax1, tax2)
					result[name]=it	
					Write_name_values('values.txt',name,values)
					values=[]
					name=''
					line=line.rstrip() 
					r = line.split('  ') 
					r=line.split()
					name=r.pop(0) 
					ListOfNames.append(name)
					valuesFragm = [float(i) for i in r] 
					values.extend(valuesFragm)
					valuesFragm=[]				
				else:
					values=[]
					name=''
					line=line.rstrip() 
					r = line.split('  ') 
					r=line.split()
					name=r.pop(0) 
					ListOfNames.append(name)
					valuesFragm = [float(i) for i in r] 
					values.extend(valuesFragm)
					valuesFragm=[]	
			else:
				line=line.rstrip() 
				r = line.split(' ') 
				r=line.split()
				name=r.pop(0) 
				ListOfNames.append(name)
				valuesFragm = [float(i) for i in r] 
				values.extend(valuesFragm)
				valuesFragm=[]
		else:
			line=line.rstrip() 
			line=line.lstrip() 
			r = line.split(' ') 
			r=line.split()
			valuesFragm = [float(i) for i in r] 
			values.extend(valuesFragm)
			valuesFragm=[]			
	
	if name[0:2]  == (tax1):
		it = lowest(values, name, tax1, tax2)
		result[name]=it
		Write_name_values('values.txt',name,values)
		values=[]
		name=''
	elif name[0:2]  == (tax2):
		it = lowest(values, name, tax1, tax2)
		result[name]=it	
		Write_name_values('values.txt',name,values)
		values=[]
		name=''
	else:
		valuesFragm=[]
		values=[]
		name=''

	fileObj.close()	

	MinimaNames=tax1+tax2+'minima.txt'
	write_report(result,MinimaNames)#generates files that will contain the minimum pairs and corresponding values

	MinimaPairs={}
	fileObj = open(MinimaNames, 'r')
	for line in fileObj:
		r = line.rstrip()
		r = r.strip(']')
		r = r.replace("[", "")
		r = r.replace("'", "")
		r = r.replace(" ", "")
		r = r.split(',')
		seq1, seq2, hodn = r
		MinimaPairs[seq1]=[seq2]
		
	fileObj.close()	
	
	MinimaPairsName=tax1+tax2+'MinimaPairs.txt'
	
	SSresult={}

	for key in MinimaPairs:
		k=key 
		v=MinimaPairs[k]
		v=''.join(v) 
		if v in MinimaPairs:
			j=MinimaPairs[v]
			j=''.join(j)
			if j == k:
				SSresult[k]=[v]
	
	FileNamesPairs=('%s_%s_pairs.txt' %(tax1,tax2))
	
	ScrollSawDupl=[]
	ScrollSawDupl=list(SSresult.keys())
	number=len(ScrollSawDupl)
	totalnumber+=number
	ScrollSawsequence.extend(ScrollSawDupl)
	print('Taxonomic groups %s and %s were compared' %(tax1,tax2))
	print('%d sequences meet the requirements' % number)

ScrollSaw=(set(ScrollSawsequence))
totalnumber2=len(ScrollSaw)
print('Final number of sequences is', totalnumber)
print('After removing duplications, there are %d sequences' % totalnumber2)
print('Their list is in file', outputfile)	
	
fileObj = open(outputfile, 'w')
for i in ScrollSaw:
	fileObj.write(i)
	fileObj.write('\n')	
fileObj.close()	

import os
file_name = "values.txt"
if os.path.exists(file_name):
    os.remove(file_name)