import api
def xFind (text, first, last):
	list = []
	x = 0
	y = 0
	size = text.count (first)
	for i in range(size):
		x = text.find(first ,y)+ len (first)
		y = text.find(last, x)
		list.append(text[x:y])
	return list

def nvdaPo ():
	x = api.getClipData()
	list1 = xFind(x, '_("', '")')
	list2 = xFind(x, "_('", "')")
	list = list1+list2
	for i in list:
		print ('msgid "%s"\nmsgstr ""\n' %(i))

