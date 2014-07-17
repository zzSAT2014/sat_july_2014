import word_bank
a = word_bank.dictionary()
lisnums = ['Dl5','Dl6', 'Dl8', 'Dl9']
coors = [['B5', 'A1', 'A4', 'C6', 'C3', 'D1', 'B6', 'A6', 'D9', 'B9'],['B13', 'A12', 'B11', 'B10', 'A3', 'C1', 'D10', 'D11', 'A11', 'B5'],['B11', 'A8', 'A9', 'A12', 'D10', 'C12', 'B4', 'C9', 'C11', 'C4'],['B4', 'B9', 'B2', 'C9', 'D7', 'C3', 'B6', 'B12', 'A8', 'D10']]
coordinates = []
for index,lisnum in enumerate(lisnums):
	for coor in coors[index]:
		coordinates.append((lisnum,coor))
print coordinates
trans = lambda index: a.get_w(index)
words = map(trans,coordinates)
count = 0
to_print =''
for coor,word in zip(coordinates,words):
	#print str(coor) +'\t'+word

	if count < 3:
		to_print += ' '*(20-len(word)) + word
		count +=1
	else:
		to_print += ' '*(20-len(word)) + word
		print to_print; to_print=''; count = 0