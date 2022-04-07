import requests
import json
import urllib.request
import os

new_prefix = "https://ecfsapi.fcc.gov/filings/file"

api_url = "https://publicapi.fcc.gov/ecfs/filings?api_key=t7IfiKsQgvRs0RSkhGyEKwvo2nHOFVclg9xHY5xa&q=(submissiontype.description:(%22COMPLIANCE%20FILING%22)+AND+proceedings.name:(%2218-142*%22))&limit=100"

get_data = requests.get(api_url).text
data = json.loads(get_data)["filing"]

url_file = open("document_urls", "w")

for filing in data:
	file_url = filing["documents"][0]["src"]
	doc_id = file_url[file_url.rindex('/'):]
	doc_url = new_prefix + doc_id
	filer_id = filing["filers"][0]["name"]
	filer_id = filer_id.replace(" ", "_").replace(',', '').replace('/', '')
	
	new_url = json.loads(requests.get(doc_url).text)["temporary_url"]
	
	try:
		file_ext = doc_id[doc_id.rindex('.'):]
	except:
		file_ext = ""
	
	os.system('curl "{}" --output {}'.format(new_url, filer_id+file_ext))
	



