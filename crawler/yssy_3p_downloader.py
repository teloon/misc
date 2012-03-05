from sgmllib import SGMLParser
import urllib,re,os,sys

class URLLister(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.tbodyflag = 0
		self.num = 0
		self.urls = []
		self.getnumflag = 0
		self.urlflag = 0
		self.targetflag = 0
		self.hrefflag = 0
	def start_table(self, attrs):
		self.tbodyflag = 1
	def end_table(self):
		self.tbodyflag = 0
	def start_a(self, attrs):
		url = ""
		for k,v in attrs:
			if k=="target" and v=="_blank":
				self.targetflag = 1
			elif k=="href" and re.search(r'http://bbs.sjtu.edu.cn/file/PPPerson/\d{15,16}.(jpg|JPG)',v):
				self.hrefflag = 1
				url += v
		if self.targetflag == 1 and self.hrefflag==1:
			print url
			self.urls.append(url)
	def end_a(self):
		self.targetfalg = 0
		self.hrefflag = 0
		self.goodurlflag = 0
	def handle_data(self, data):
		if self.tbodyflag==1 and self.getnumflag==0:
			res = re.search(r'^\d{1,6}$',data)
			if res:
				self.num = (int)(res.group())
				self.getnumflag = 1
				print self.num
def downloadppp(urls, dir):
	if not os.path.exists(dir):
		os.mkdir(dir)
	for url in urls:
		sock = urllib.urlopen(url)
		f = file(dir+url.split(r'/')[-1], 'wb')
		f.write(sock.read())
		sock.close()
		f.close()
		
pppdocurl = r'http://bbs.sjtu.edu.cn/bbsfdoc2?board=PPPerson'
sock = urllib.urlopen(pppdocurl)
urllister = URLLister()
urllister.feed(sock.read())
currentnum = urllister.num
downloadppp(urllister.urls, dir=r'ppp\\')
urllister.close()
sock.close()

picnum = 40
if sys.argv[1]:
	picnum = (int)(sys.argv[1])
pagenum = currentnum-21
while pagenum > currentnum-21-((int)(picnum/20)-1)*20:
	sock = urllib.urlopen(pppdocurl+r'&start='+repr(pagenum))
	urllister = URLLister()
	urllister.feed(sock.read())
	downloadppp(urllister.urls, dir=r'ppp\\')
	urllister.close()
	sock.close()
	pagenum -= 20