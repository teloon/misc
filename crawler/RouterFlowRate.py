from sgmllib import SGMLParser
from httplib import HTTPConnection
import urllib, re, time, winsound

class RouterFlowRate(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.tr_flag = 0
		self.script_flag = 0
		self.ip_list = []
		self.amount_list = []
	
	def start_tr(self, attrs):
		for k, v in attrs:
			if k=="align" and v=="center":
				self.tr_flag = 1
	
	def start_script(self, attrs):
		for k,v in attrs:
			if k == "language" and v == "JavaScript":
				self.script_flag = 1
	
	def handle_data(self, data):
		ip_patt = r'192\.168\.1\.\d{0,3}'
		info_patt = r'\(\s*([^,]+,){0,68}[\d\D]{0,3}\)'
		if(self.script_flag == 1):
			self.ip_list.extend(re.findall(ip_patt, data))
			info = re.search(info_patt, data)
			if info:
				info_list = re.split(',', info.group())
				for num in [6, 19, 32, 45, 58]:

					self.amount_list.append(info_list[num])
			self.script_flag = 0
			return
	def get_iplist(self):
		return self.ip_list
	def get_amountlist(self):
		return self.amount_list

header = {
"Host"			:	"192.168.1.1",
"User-Agent"	:	"Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.4) Gecko/20091016 Firefox/3.5.4",
"Accept"		:	"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language":	"zh-cn,zh;q=0.5",
"Accept-Encoding":	"gzip,deflate",
"Accept-Charset":	"GB2312,utf-8;q=0.7,*;q=0.7",
"Keep-Alive"	:	"300",
"Connection"	:	"keep-alive",
"Authorization"	:	"Basic cm9vdDoxMjM0NTY=",
"Cache-Control"	:	"max-age=0"
}
print "start...."			
ip_list = []
amount_list = []
#for count in range(0,2):
conn = HTTPConnection("192.168.1.1")
conn.request("GET", "/userRpm/SystemStatisticRpm.htm", "", header)
res = conn.getresponse()
if res.status == 200:
	data = res.read()
#		print data
	fr = RouterFlowRate()
	fr.feed(data)
	ip_list = fr.get_iplist()
	amount_list.extend(fr.get_amountlist())
	fr.close()
for i in range(0, len(ip_list)):
	avg = (int)(amount_list[i])/1000
	print ip_list[i],'\t\t', avg,'KB/s'
#print ip_list
#print amount_list
conn.close
#winsound.Beep(783,200)
#winsound.Beep(783,200)
#winsound.Beep(783,200)
#time.sleep(5)
print "end..."	
	
