import requests





for i in range(1, 73):
	url = "http://www.dearclimate.net/img/jpgs/" + str(i) + ".jpg"
	f = "poster-" + str(i) + ".jpg"

	r = requests.get(url, allow_redirects=True)
	open(f, 'wb').write(r.content)
	print(f, "done")

	# urllib.request.urlretrieve(url, f)

	# testfile = urllib.URLopener()
	# testfile.retrieve(url, f)
	
	# file_url = "http://www.dearclimate.net/img/pdfs/" + str(i) + ".pdf"
	# file_name = wget.download(file_url)