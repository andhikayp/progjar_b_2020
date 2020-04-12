class HttpServer:
	def __init__(self):
		self.sessions={}
		self.types={}

	def response(self,messagebody='',headers={}):
		resp=[]; response_str=''
		resp.append(messagebody)
		for i in resp:
			response_str="{}{}" . format(response_str,i)
		return response_str

	def proses(self,data):
		requests = data.split("\r\n")
		baris = requests[0]
		# print(baris)
		j = baris.split(" / ")
		try:
			method=j[0].upper().strip()
			if (method=='GET'):
				object_address = j[1].strip()
				return self.http_get(object_address)
			else:
				return self.response(400,'Bad Request')
		except IndexError:
			return self.response(400,'Bad Request')

	def http_get(self,object_address):
		# print(object_address)
		if object_address:
			return self.response('<h1>SERVER HTTP</h1>')
		else:
			return self.response('<h1>Bad Request</h1>')

if __name__=="__main__":
	httpserver = HttpServer()
	d = httpserver.proses('GET / HTTP/1.0')
	# d = httpserver.proses('POST / HTTP/1.0')
	print(d)