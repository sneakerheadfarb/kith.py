import requests
import feedparser
import json

url = "https://kith.com/"
keyword = "Nike"
size_input = "7"
found = "false"

while found == "false":
	print("LOOKING FOR PRODUCT!")
	d = feedparser.parse('https://kith.com/collections/footwear.atom')
	count = 0
	products = len(d['entries'])
	print("Number of products found:" + products)
	while count < products:
		title = d['entries'][count]['title']
		if keyword in title:
			prod_title = d['entries'][count]['title']  
			prod_link = d['entries'][count]['link'] 
			found = "true"
			entry_num = count
			count = 100
		else:
			count = count + 1
print(prod_title)
print(prod_link)
count = 0
r2 = requests.get(prod_link + ".json")
variants = json.loads(r2.text)
found_size = "false"
for variant in variants:
    while found_size == "false":
        variant_id = str(variants[u'product'][u'variants'][count][u'id'])
        size = str(variants[u'product'][u'variants'][count]['title']).replace("u", "")
        size = size.replace("'", "")
        if size.find(size_input) == -1:
            count = count + 1
            found_size = "false"
        else:
            checkout_link = url + "cart/" + variant_id + ":1"
            found_size = "true"
            count = 0
print(checkout_link)


