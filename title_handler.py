# coding=utf-8

import re
import json
import jieba

city_file = "city.txt"
country_file = "country.txt"
province_file = "province.txt"
# city_file = "city.txt"

pending_titles = set()
key_words = set()

def read_data(filename):
	fd = open(filename, "r")
	data = fd.read()
	fd.close()
	return data

def load_pending_titles(filename):
	data = read_data(filename)
	# data = data.decode("gbk").encode("utf-8")
	for line in data.split("\n"):
		# print(line.decode("utf-8"))	
		pending_titles.add(line.decode("utf-8"))
	pass

def load_brand_name_database():
	pass

def load_sensitive_word_database():
	pass

def load_violation_word_database():
	pass

def load_country_name_database():
	data = read_data(country_file)
	key_words.update(json.loads(data))
	pass

def load_province_name_database():
	data = read_data(province_file)
	key_words.update(json.loads(data))
	pass

def load_city_name_database():
	data = read_data(city_file)
	for line in data.split("\n"):
		data_list = line.split("：")
		word = None
		if len(data_list) == 1:
			word = data_list[0].decode("utf-8")
		elif len(data_list) == 2:
			word = data_list[1].decode("utf-8")
		print(word)
		key_words.add(word)
		if (word.endswith(u"市")):
			word = word.rstrip(u"市")
		elif word.endswith(u"自治州"):
			word = word.rstrip(u"自治州")
		
		print(word)
		key_words.add(word)
	pass

def remove_brand_name():
	pass

# def

def remove_punctuation(title):
	# re.sub('', "", title)
	return re.sub(r'[<>,\.\?;:\'\"\\\|\[\]\{\}_\+=\(\)\*&\^%\$#@!~`，《。》？；：‘“’”、\|【】\{\}）（……￥！~·]+', "", title)
	pass

def main(title_file):
	total = 0
	load_pending_titles(title_file)
	load_country_name_database()
	load_province_name_database()
	load_city_name_database()
	for title in pending_titles:
		print(title)
		title = remove_punctuation(title)
		# word_list = jieba.cut(title, cut_all=False)
		# print(" ".join(word_list))
		for word in key_words:
			if title.count(word) > 0:
				title = title.replace(word, "")
				total += 1
		print(title)

	print("removed %d" % (total))
	# for word in key_words:
	# 	print(word)
	pass

if __name__ == '__main__':
	title_file = "./test.txt"
	main(title_file)