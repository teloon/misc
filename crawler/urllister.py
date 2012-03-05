from sgmllib import SGMLParser
import sgmllib, re

class PageURLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.urls = []
		self.classflag = 0
		self.urlflag = 0
		self.dateflag = 0	
	def start_a(self, attrs):
		blank_flag = 0
		properurl_flag = 0
		properurl = []
		for k,v in attrs:
			if k=="target" and v=="_blank":
				blank_flag = 1
			elif k=="href" and re.search(r'/yobin/blog/item/.*.html', v):
				properurl_flag = 1
				properurl.append(v)
		if 	blank_flag == 1	and properurl_flag == 1:
			self.urls.extend(properurl)
	def handle_data(self, data):
		if self.classflag == 1:
			self.titles.append(data)
		if self.dateflag == 1:
			self.dates.append(data)	
	def get_urls(self):
		return self.urls

class PageInfo(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.titles = ""
		self.dates = ""
		self.text = ""
		self.titleflag = 0		
		self.dateflag = 0
		self.textflag = 0
	def start_div(self, attrs):
		for k,v in attrs:
			if k=="class" and v=="date":
				self.dateflag = 1
			elif k=="id" and v=="blog_text":
				self.textflag = 1
	def end_div(self):
		self.dateflag = 0
		self.textflag = 0
	def start_title(self, attrs):
		self.titleflag = 1
	def end_title(self):
		self.titleflag = 0
	def handle_data(self, data):
		if self.dateflag==1:
			self.dates = data
		elif self.titleflag==1:
			self.titles = data
		elif self.textflag==1:
			self.text += data
	def get_titles(self):
		return self.titles
	def get_dates(self):
		return self.dates
	def get_text(self):
		return self.text