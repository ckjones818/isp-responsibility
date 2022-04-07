import requests
import json
import urllib.request
import os

download_prefix = "https://www.fcc.gov/ecfs/file/download"

api_url = "https://publicapi.fcc.gov/ecfs/filings?api_key=t7IfiKsQgvRs0RSkhGyEKwvo2nHOFVclg9xHY5xa&q=(submissiontype.description:(%22COMPLIANCE%20FILING%22)+AND+proceedings.name:(%2218-142*%22))&limit=100"

get_data = requests.get(api_url).text
data = json.loads(get_data)["filing"]

url_file = open("document_urls", "w")

for filing in data:
	file_url = filing["documents"][0]["src"]
	doc_id = file_url[file_url.rindex('/'):]
	doc_url = download_prefix + doc_id
	filer_id = filing["filers"][0]["name"]
	filer_id = filer_id.replace(" ", "_").replace(',', '').replace('/', '')
	url_file.write(doc_url+'\n')



