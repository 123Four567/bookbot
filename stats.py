def count_words(filepath):
	with open(filepath) as f:
		file_content = f.read()
		words = file_content.split()
		num_words = 0
		for word in words:
			num_words += 1
		return f'Found {num_words} total words'

def count_char_to_str(filepath):
	with open(filepath) as f:
		file_content = f.read()
		words = file_content.split()
		dic = {}
		for sentence in words:
			for char in sentence:
				c = char.lower()
				if c in dic:
					dic[c] += 1
				else:
					dic[c] = 1
		return dic

def sort_by(num):
	return num['num']

def sort_dict(dic):
	list_of_dic = []
	for key in dic:
		new_dic = {'char':key, 'num':dic[key]}
		list_of_dic.append(new_dic)
	list_of_dic.sort(reverse=True, key=sort_by)
	for dic in list_of_dic:
		if dic["char"].isalpha():
			print(f'{dic["char"]}: {dic["num"]}')