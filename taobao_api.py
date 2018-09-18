# coding=utf-8

import requests
import json

api_search_url = 'https://s.taobao.com/search?q=%s'

# def get_web_page(url):
# 	return requests.get(url)
# 	pass

line_tag = "    g_page_config = "

def get_page_config(word):
	html = requests.get(api_search_url % (word)).text
	g_page_config_str = None
	for line in html.split("\n"):
		# line = line.encode("utf-8")
		if line.startswith(line_tag):
			g_page_config_str = line.replace(line_tag, "").rstrip(";")

			print(line)
			break
	return g_page_config_str
	pass

def get_node(url, tag):
	html = requests.get(url).text
	pass

def main():
	g_page_config_str = get_page_config("电钻")
	g_page_config_obj = json.loads(g_page_config_str)
	auctions = g_page_config_obj["mods"]["itemlist"]["data"]["auctions"]
	for auction_obj in auctions:
		print(auction_obj["title"])
		print(auction_obj["raw_title"])
		print(auction_obj["detail_url"])
		detail_url = "http:" + auction_obj["detail_url"]

	pass

if __name__ == '__main__':
	main()