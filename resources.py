def load_urls(path='images.txt'):
	"""
	Function to load urls using given path
	: urls : String
	:return: List
	"""

	urls = []
	path = path
	with open(path) as freader:
		lines = freader.readlines()
		for url in lines:
			urls.append(url)
	return urls
