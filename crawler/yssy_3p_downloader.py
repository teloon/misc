#!/usr/bin/env python
#-*- coding:utf8 -*-

# wy@2012.3

from pyquery import PyQuery as pq
import urllib, re, os, sys, getopt

HOMEPAGE_URL = r'http://bbs.sjtu.edu.cn/bbsfdoc2?board=PPPerson'
DOWNLOAD_DIR = r'ppp'

class Record():
    def __init__(self):
        """
            all attributes are in string format
        """
        self.url = ""
        self.pic_name = ""
        self.date = ""
        self.num = ""
    def print_it(self):
        print "url:\t%s" % self.url
        print "picname:\t%s" % self.pic_name
        print "date:\t%s" % self.date
        print "num:\t%s" % self.num

class PageParser():
    def  __init__(self):
       self.records = []
       self.page_start = ""
       self.page_url = ""
    def parse(self, url):
        self.page_url = url
        html = urllib.urlopen(url).read()
        pq_obj = pq(html)
        self.page_start = pq_obj("tr :eq(1)")("td :eq(0)").text()
        print "## Parsing page %s, first record num:%s" % (self.page_url, self.page_start)
        for tr_obj in pq_obj("tr :gt(0)"):
            rec = Record()
            tr_obj = pq(tr_obj)
            rec.num = tr_obj("td :eq(0)").text()
            rec.pic_name = tr_obj("td :eq(1)").text()
            rec.url = tr_obj("td :eq(1)")("a").attr("href")
            rec.date = tr_obj("td :eq(3)").text()
            self.records.append(rec)
        print "## Finish parsing"
    def print_it(self):
        for i,rec in enumerate(self.records):
            print "## Record%d" % (i+1)
            rec.print_it()

def do_download(urls, dst_sub_dir):
    if not os.path.exists(DOWNLOAD_DIR):
        os.mkdir(DOWNLOAD_DIR)
    dst_path = os.path.join(DOWNLOAD_DIR, dst_sub_dir)
    if not os.path.exists(dst_path):
        os.mkdir(dst_path)
    for url in urls:
        sock = urllib.urlopen(url)
        f = open(os.path.join(dst_path, url.split(r"/")[-1]), 'wb')
        f.write(sock.read())
        sock.close()
        f.close()

month_name_map = {  1:"Jan", 2:"Feb", 3:"Mar", 4:"Apr", 5:"May", 6:"Jun",
                        7:"Jul", 8:"Aug", 9:"Sep", 10:"Oct", 11:"Nov", 12:"Dec" }
def get_today():
    import datetime
    today = datetime.date.today()
    mon_str = month_name_map[today.month] 
    day_str = str(today.day)
    date_str = mon_str+day_str
    parser = PageParser()
    parser.parse(HOMEPAGE_URL)
    get_all, is_first = False, True
    while not get_all:
        urls = []
        is_first = True
        for rec in parser.records:
            if is_first and not get_all:
                if re.sub("\s", "", rec.date)!=date_str:
                    get_all = True
                is_first = False
            if re.sub("\s", "", rec.date) == date_str:
                urls.append(rec.url)
        print "## Get %d today's new pictures!" % len(urls)
        do_download(urls, date_str)
        curr_start = int(parser.page_start)
        if not get_all:
            parser.__init__()
            parser.parse((HOMEPAGE_URL+"&start=%d") % (curr_start-21))

def get_recent(num):
    urls = []
    parser = PageParser()
    parser.parse(HOMEPAGE_URL)
    while num>0:
        for rec in parser.records:
            urls.append(rec.url)
            num -= 1
            if num<=0:
                break
        curr_start = int(parser.page_start)
        if num>0:
            parser.__init__()
            parser.parse( (HOMEPAGE_URL+"&start=%d")%(curr_start-21) )
    do_download(urls, ("recent%d"%len(urls)))
    print "## Get %d recent pictures!" % len(urls)

def naive_test():
    parser = PageParser()
    parser.parse(HOMEPAGE_URL)
    parser.print_it()

def help():
    print \
    """
    usage: python yssy_3p_downloader.py [-h|--help] [-t|--today] [-n|--number num]
        -h      : show help message
        -t      : get today's new pictures
        -n num  : get recent num pictures
    """

if __name__ == "__main__":
    if len(sys.argv)<2:
        help()
    else:
        try:
            options, remained = getopt.getopt(sys.argv[1:], "htn:", ["help", "today", "number="])
            for opt, arg in options:
                if opt in ("-h", "-help"):
                    help()
                elif opt in ("-t", "--today"):
                   get_today()
                elif opt in ("-n", "--number"):
                    get_recent(int(arg))
        except Exception, e:
            print "#### Error! %s ####" % e

