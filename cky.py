#! /usr/bin/python2.6
import sys
import string, re
from random import choice
from x2helper import *


'''
	Creates the CKY-recognizer, fills every production in the 
	table and finally returns True, if the sentence is in the 
	grammar, otherwise it returns False.
'''
def parse(string, phrase, grammar):
	'''
		Create the table; index j for rows, i for columns
	'''
	sentence = string.split()
	length = len(sentence)
	table = [None] * (length + 1)

	for j in range(length + 1):
		table[j] = [None] * (length+1)
		for i in range(length+1):
			table[j][i] = []
	'''
		Fill the diagonal of the table with the parts-of-speech of the words.
	'''
	for j in range(1,length + 1):
		table[j - 1][j].extend(producers(sentence[j - 1]))

	for j in range(2, length + 1):
		for i in range( j-2, -1, -1):
			for k in range(i+1, j):
				for keys in grammar:
					for values in grammar[keys]:
						if isinstance(values, list):
							'''
								They are in CNF, so we take the first and 
								the second, since CNF wants exactly two non 
								terminals in the RHS
							'''
							first = values[0] + ''
							second = values[1] + ''
							label = False
							if isinstance(table[i][k], list):
								for in_table in table[i][k]:
									if first == in_table:
										label = True
							if label:
								if isinstance(table[k][j], list):
									for in_table in table[k][j]:
										if second == in_table:
											table[i][j].append(keys)
	'''
		In the last row, we put in each column each word of the sentence
	'''
	for j in range(1, length + 1):
		table[length][j].append(sentence[j-1])

	'''
		Print the table
	'''
	#printtable(table, sentence)

	'''
		Checks if the sentence is valid, the upper left cell of 
		the matrix should be 'S'
	'''
	statement = table[0][length]
	recognized = False
	if statement:
		if phrase in statement:
			recognized =  True
	else:
		recognized = False

	return table, recognized


'''
	Take the CKY-recognizer that was created earlier and fills it 
	with the back-pointers information.
	So the dictionary will have this format (i,j,A):(k, B, C)
	Where A is in position (i,j) of the back_poitner table, 
	B is in position (i, k) and C is in position (k,j).
	So that A -> B C in CNF form
'''
def parse2(table):
	length = len(table) - 1
	back_pointer = dict()
	for j in range(2, length + 1):
		for i in range( j-2, -1, -1):
			for k in range(i+1, j):
				if (table[i][j]) and (table[i][k]) and (table[k][j]):
					if i == 0 and j == length:
						key_list = ( i, j, 'S' )
					else:
						key_list = ( i, j, table[i][j][0] )
					back_pointer.setdefault(key_list, []).append((k, table[i][k], table[k][j]))
	return back_pointer


'''
	Iterates through the dictionary of back pointers and tries to find the 
	key that has the 'S' phrase and it is in the first row and last column.
	It returns the i row, j column, and the k
'''
def back_tree(phrase, str):
	sentence = str.split()
	length = len(sentence)
	back_pointer
	for pointers in back_pointer:
		if phrase in pointers[2] and pointers[1] == length and pointers[0] == 0:
			return pointers[0], pointers[1], back_pointer[pointers][0][0]
			break


'''
	It builds the tree using recursion.
'''
def build_tree(phrase, i, j, k, grammar):
	"""
		Generate a proper sentence or phrase,
		with a complete parse tree.
	"""
	recognizer
	back_pointer
	li = []
	li.append(phrase)

	'''
		If the phrase is a list we go to all its elements and 
		we call the recursion function.
	'''
	if isinstance(phrase, list):
		for ph in phrase:
			build_tree(ph, i, j, k, grammar)
		return
	elif phrase in grammar:
		'''
			We take the value of they key from back_pointer
			and we change the i, j so as to use them in the recu['S'rsion
		'''
		elements = back_pointer[(i, j, phrase)][0]
		one_j = k
		two_i = k
		if (elements[1]) and isinstance(grammar[elements[1][0]][0], list):
			value =  back_pointer[(i, one_j, elements[1][0])]
			k = value[0][0]
			li.append(build_tree(elements[1][0], i, one_j, k, grammar))
		else:
			li.append([elements[1][0]] + recognizer[len(recognizer) - 1][k])
		if (elements[2]) and isinstance(grammar[elements[2][0]][0], list):
			value1 =  back_pointer[(two_i, j, elements[2][0])]
			k = value1[0][0]
			li.append(build_tree(elements[2][0], two_i, j, k, grammar))	
		else:
			li.append([elements[2][0]] + recognizer[len(recognizer) - 1][j])
	return li


'''
	checks if the user input consists of 2 elements
'''
def sub_process(q):
	phrase = 'S'
	#q = "from Athens to Edinburgh in december"
	q = q.lower()
	QUERY = re.split('[\\s]+', q)
	recognized = False

	global recognizer
	global back_pointer
	global tree
	grammar = cnf_grammar('1')

	if not (QUERY[0] == "to" or QUERY[0] == "from") and len(QUERY) < 3:
		for keys in grammar:
			if keys == "N":
				if len(QUERY) == 2:
					if (QUERY[0] in grammar[keys]) and (QUERY[1] in grammar[keys]):
						recognized = True
				if len(QUERY) == 1:
					if (QUERY[0] in grammar[keys]):
						recognized = True
	else:

		'''
			Call the cky_parse that works only as arecognizer.
		'''
		cky_recogn = parse(q, phrase, grammar)

		'''
			Recognizer is a table, and recognized is a boolean 
			if the sentence could be recognized
		'''
		recognizer, recognized = cky_recogn[0], cky_recogn[1]

	return recognized

