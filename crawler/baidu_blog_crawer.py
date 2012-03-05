from httplib import HTTPConnection
from urllister import PageURLLister
from urllister import PageInfo
import urllib, tools, os

print "Crawler begins working..."
catg_base_url = "/yobin/blog/category/python%20%26%2338%3B%20django%20%26%2338%3B%20gae/index/"
urls = []
titles = []
dates = []
header = {
"Host"	:	"hi.baidu.com",
"User-Agent"	:	'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh-CN; rv:1.9.1.4) Gecko/20091016 Firefox/3.5.4',
"Accept"	:	"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language"	:	"zh-cn,zh;q=0.5",
"Accept-Encoding"	:	"gzip,deflate",
"Accept-Charset"	:	"GB2312,utf-8;q=0.7,*;q=0.7",
"Keep-Alive"	:	"300",
"Proxy-Connection"	:	"keep-alive",
"Referer"	:	"http://hi.baidu.com/yobin/blog/category/python%20%26%2338%3B%20django%20%26%2338%3B%20gae",
#"Cookie"	:	"BAIDUID=4E327A5919F7E2D1D5D82E6F44F97A69:FG=1; BDSTAT=00d5681e80d41c55e032edbf3f70922214e1ed6135a85edf99b1cb134b54b3eb; BDSP_REFERFLAG=1257143683792; BDSP=009e8f93f3d2572cdba7abf2559d6820ca0046024e01abeba02ae03caced5ace3d6d55fbb2fb43166d224f4a20a4462309f790529822720e0cf3d7ca7bcb0a46f21fbe096b63f6246b600c338744ebf81a4c510fd9f9d72a6059252dd52a2834309bc2d0; BDUSS=c3Y1N4dFc2ZWNWUS1RTWdkeFpsaU0tcTBKTWk0TnNCSWwtfmM3ZWI5bW8yQlJMQVFBQUFBJCQAAAAAAAAAAApBESLfjgsHdGVsb29uMTk4OAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAu8NmAAAAAAAAAAAAAAAAIRRCAAAAAAAxMC42NS4yNKhL7UqoS-1KQ2; USERID=470b0bb6522cdc2d11dcf0de10bc; BDSPINFO=9c986625e79a91a54723e80c|teloon1988|teloon1988|d50606360b3efd36ce19f9b2e09862c0; BDOPINFO=9c986625e79a91a54723e80c|teloon1988|teloon1988|d50606360b3efd36ce19f9b2e09862c0; OPENPLATFORM_SP=df8e74656c6f6f6e313938380b07_1257065393; IM_old=0|g1hnedpr; IM_=1",
"Proxy-Authorization"	:	"Basic dGlhbmxvbmcxOTg4OjUzMjUzMjY5"
}

for pagenum in range(0,12):
	print "###########",pagenum,"#############"
	url = "http://hi.baidu.com"+catg_base_url+repr(pagenum)
#	url = "http://list.mp3.baidu.com/list/newhits.html?id=1#top1"
#	print url
	sock = urllib.urlopen(url)
#	if sock.status == 200:
#	print "get it in"
	pageLister = PageURLLister()
	pageLister.feed(sock.read())
	urls.extend(pageLister.get_urls())
	pageLister.close()
	sock.close()
urls = tools.uniq(urls)
pageSep = "\n\n=====================================================================================\n\n"
output = "output.txt"
os.remove(output)
for extendurl in urls:
	url = "http://hi.baidu.com"+extendurl
	sock = urllib.urlopen(url)
	pageInfo = PageInfo()
	pageInfo.feed(sock.read())
	try:
		f = file(output, 'a')
		f.write(pageInfo.get_titles()[0:-17]+'\n')
		f.write(pageInfo.get_dates()+"\n")
		f.write(pageInfo.get_text()+"\n")
		f.write(pageSep)
	except:
		print "write file error"
		pass
	f.close
#	print pageInfo.get_titles()
#	print pageInfo.get_dates()
#	print pageInfo.get_text()
	
#print urls
#print titles
#print dates
		
