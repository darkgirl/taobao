# coding=utf-8

import requests
import json

api_search_url = 'https://s.taobao.com/search?q=%s'

# def get_web_page(url):
# 	return requests.get(url)
# 	pass

line_tag = "    g_page_config = "

def main():
	html = requests.get(api_search_url % ("电钻")).text
	g_page_config_str = None
	for line in html.split("\n"):
		# line = line.encode("utf-8")
		if line.startswith(line_tag):
			g_page_config_str = line.replace(line_tag, "").rstrip(";")

			print(line)
			break
	g_page_config_obj = json.loads(g_page_config_str)
	auctions = g_page_config_obj["mods"]["itemlist"]["data"]["auctions"]
	for auction_obj in auctions:
		print(auction_obj["title"])
		print(auction_obj["raw_title"])
		print(auction_obj["detail_url"])
	pass

if __name__ == '__main__':
	main()