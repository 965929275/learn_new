#encoding:utf8

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.CurrentData = ''
		self.type = ''
		self.format = ''
		self.year = ''
		self.rating = ''
		self.stars = ''
		self.description = ''

	# 元素开始事件处理
	def startElement(self,tag,attributes):
		self.CurrentData = tag
		if tag == "movie":
			print('*****Movie*****')
			title = attributes['title']
			print('Title:', title)

	# 元素结束事件处理
	def endElement(self,tag):
		if self.CurrentData == 'type':
			print('type:', self.type)
		elif self.CurrentData == 'format':
			print('format:', self.format)
		elif self.CurrentData == 'year':
			print('year:', self.year)
		elif self.CurrentData == 'rating':
			print('rating:', self.rating)
		elif self.CurrentData == 'stars':
			print('stars:', self.stars)
		elif self.CurrentData == 'description':
			print('description:', self.description)
	
	# 内容事件处理
	def characters(self, content):
		if self.CurrentData == 'type':
			self.type = content
		elif self.CurrentData == 'format':
			self.format = content
		elif self.CurrentData == 'year':
			self.year = content
		elif self.CurrentData == 'rating':
			self.rating = content
		elif self.CurrentData == 'stars':
			self.rating = content
		elif self.CurrentData == 'description':
			self.description = content


if __name__ == '__main__':
	# 创建并返回一个sax解析器
	parser = xml.sax.make_parser()
	# turn off namepsaces 关闭命名空间
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)


	#重写 ContextHandler
	Handler = MovieHandler()
	# 返回当前ContentHandler
	parser.setContentHandler(Handler)

	# 创建一个sax解析器并解析xml文档
	parser.parse('movies.xml')