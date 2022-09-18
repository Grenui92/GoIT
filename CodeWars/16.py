def domain_name(url: str):
	print(url)
	if url.startswith('http'):
		url = url.split('//')[1]
	if url.startswith('www'):
		url = url.split('.')[1]
	else:
		url = url.split('.')[0]
	return url
print(domain_name("http://google.co.jp"))