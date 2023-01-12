#Dominant genes are written in uppercase letters and recessive genes are written in lowercase letters.

#This is one example of gene combination you can set for task:
#genes of mother:
# colour of eyes: blue-blue
# size of eyes: LARGE-LARGE
# nose: narrow-narrow
# colour of hair: BROWN-blonde
# hair: CURLY-straight
# freckles: YES-no

#genes of father:
# colour of eyes: BROWN-blue
# size of eyes: LARGE-small
# nose: BROAD-narrow
# colour of hair: BROWN-blonde
# hair: CURLY-straight
# freckles: YES-no

import random #importing this library so we can choose random number later (in this case, 0 or 1)

#genes of each parent in 2D array:
mother = [['blue','blue'],['LARGE','LARGE'],['narrow','narrow'],['BROWN','blonde'],['CURLY','straight'],['YES','no']]
father = [['BROWN','blue'],['LARGE','small'],['BROAD','narrow'],['BROWN','blonde'],['CURLY','straight'],['YES','no']]

#defining blank arrays we'll use below:
DNA_mother = [] #for one gene of each mother's trait
DNA_father = [] #for one gene of each father's trait
baby = [] #for baby's genome, e.g. combination of DNA_mother and DNA_father
face = [] #array for traits baby will have

#choosing one of genes for every mother's and father's trait:
for i in range(len(mother)):
	k = round(random.random()) #k = random number (0 or 1)
	DNA_mother.append(mother[i][k]) #making 1D array for one gene for each trait of mother
for i in range(len(father)):
	k = round(random.random())
	DNA_father.append(father[i][k]) #making 1D array for one gene for each trait of father
	
#merging two 1D arrays of mother's and father's genes
for i in range(len(mother)):
	a = [];
	a.append(DNA_mother[i])
	a.append(DNA_father[i])
	baby.append(a)

#DNA of baby:	
print(f'DNA of baby: {baby}\n')

#looking what gene is dominant and appending it to baby (which represents baby's traits)
#if both are dominant or neither of them is, then we choose on random
for i in range(len(baby)):
	if baby[i][0].isupper == True and baby[i][1].isupper == False: #if mother's gene is dominant and father's gene is recessive
		face.append(baby[i][0])
	elif baby[i][0].isupper == False and baby[i][1].isupper == True: #if mother's gene is recessive and father's gene is dominant
		face.append(baby[i][1])
	else: #if both genes are dominant or both genes are recessive
		k = round(random.random())
		face.append(baby[i][k])

#look of baby's face
print(f'Colour of eyes: {face[0]}\nsize of eyes: {face[1]} \nnose: {face[2]} \ncolour of hair: {face[3]} \nhair: {face[4]} \nfreckles: {face[5]}')
