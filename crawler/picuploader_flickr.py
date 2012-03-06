#!/usr/bin/env python
#-*- coding:utf8 -*-
import flickrapi, md5, ClientForm
import urllib2, urllib
from BeautifulSoup import BeautifulSoup
from ClientCookie import build_opener, install_opener
from ClientCookie import CookieJar, HTTPCookieProcessor, \
     HTTPHandler, HTTPRefreshProcessor, HTTPSHandler,\
     HTTPEquivProcessor, HTTPRedirectHandler,\
     HTTPRedirectDebugProcessor

api_key = '08c571c52f656fb78d8c3ad27960dd04'
api_secret = '21904fa87d4a1898'
cj = CookieJar()
fiddler_proxy = urllib2.ProxyHandler({"https":"http://localhost:8888", "http":"http://localhost:8888"})
opener = build_opener(
                    HTTPCookieProcessor(cj),
                    HTTPHandler,
                    HTTPSHandler,
                    HTTPRedirectHandler,
                    HTTPRefreshProcessor,
                    HTTPEquivProcessor,
                    HTTPRedirectDebugProcessor,
#                    fiddler_proxy,
                    )
install_opener(opener)
DEBUG = False

def upload_call(process, done):
    if done:
        print "Done uploading"
    else:
        print "At %s%%" % process

def auth_call(frob, perms):
    print "authorizing... frob:%s  perms: %s" % (frob, perms)

def gen_api_sig(sig_str):
    api_sig = md5.new(sig_str).hexdigest()
    return str(api_sig)

def login(uname, passwd):
    #get the login page
#    print uname, passwd
    opener.addheaders = [('Host', 'login.yahoo.com'),
                         ('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN;\
                                                rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3'),
                         ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                         ('Accept-Language', 'zh-cn,zh;q=0.5'),
                         ('Accept-Encoding', 'deflate'),
                         ('Accept-Charset', 'GB2312,utf-8;q=0.7,*;q=0.7'),
                         ('Keep-Alive', 115),
                         ('Connection', 'keep-alive'),
                         ('Referer', 'http://www.flickr.com')]
    res = opener.open('http://www.flickr.com/signin/')
    if DEBUG:
        #if read out the content from the res(buffer), the res(buffer) will be empty
        #then the ClientForm will get nothing
        html = res.read()
        f = open('login.html', 'w')
        f.write(html)
        f.close()
#    print res.read()
    forms = ClientForm.ParseResponse(res)
    res.close()
    form = forms[0]
    try:
        form['login'] = uname
    except Exception:
        try:
            form['passwd'] = passwd
        except Exception:
            print 'Already Login'
            return
    form['passwd'] = passwd
#    print form
    req = form.click()
    #post it
    res = opener.open(req)
    res_html = res.read()
    if DEBUG:
        f = open('login_res.html', 'w')
        f.write(res_html)
        f.close()
    if DEBUG:
        res = opener.open('http://my.yahoo.com')
        html = res.read()
        f = open('login_home.html', 'w')
        f.write(html)
        f.close()
    return res_html

def uploadit(perms, filename, title='', description='', tags='''''', is_public='1', is_family='0', is_friend='0'):
    flick = flickrapi.FlickrAPI(api_key, api_secret)
    (tok, frob) = flick.get_token_part_one(perms=perms, auth_callback=auth_call)
    if not tok:
        print 'need authorization', frob
        authorize(uname=uname, passwd=passwd, frob=frob)
    flick.get_token_part_two((tok, frob))
#    print tok, frob
    flick.upload(filename=filename, callback=upload_call, title=title, description=description, tags=tags, \
                        is_public=is_public, is_family=is_family, is_friend=is_friend)

def authorize(uname, passwd, frob):
    login(uname, passwd)
    sig_str = api_secret+'api_key'+api_key+'frob'+frob+'perms'+perms
    api_sig = gen_api_sig(sig_str)
#    print 'frob:', frob
    tokreq_url = 'http://api.flickr.com/services/auth/?perms=' + perms + '&api_key='\
                    + api_key + '&frob=' + frob + '&api_sig=' + api_sig
#    print tokreq_url
    opener.addheaders = [('Host', 'www.flickr.com'),
                         ('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN;\
                                                rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3'),
                         ('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                         ('Accept-Language', 'zh-cn,zh;q=0.5'),
                         ('Accept-Encoding', 'deflate'),
                         ('Accept-Charset', 'GB2312,utf-8;q=0.7,*;q=0.7'),
                         ('Keep-Alive', 115),
                         ('Connection', 'keep-alive')]
    res = opener.open(tokreq_url)
    if not res:
        print 'not get response when getting token'
        return 
    html = res.read()
#    confirm_html = decompress(zip_content)
    if DEBUG:
        f = open('confirm.html', 'w')
        f.write(html)
        f.close()
#    return
    soup = BeautifulSoup(html)
    input_eles = soup.findAll(name='input', attrs={'type':'hidden'})
    need_attr = ['magic_cookie', 'api_key', 'api_sig', 'perms', 'frob', 'done_auth']
    paras = {}
    for ele in input_eles:
        if ele['name'] in need_attr:
            paras[ ele['name'] ] = ele['value']
    res = opener.open('http://www.flickr.com/services/auth/', urllib.urlencode(paras))
    confirmed_html = res.read()
    if DEBUG:
        f = open('confirmed.html', 'w')
        f.write(confirmed_html)
        f.close() 
    return

def verify_flickr_account(username, password):
    #return True if succeed
    print 'verifying....'
    ret = login(uname, passwd)
    if ret:
        soup = BeautifulSoup(ret)
        a_eles = soup.findAll(name='a', attrs={'class':'Pale', 'href':'/account'})
        if a_eles:
            print 'exsist: %s' % (uname)
            return True
        else:
            print 'not exist: %s' % (uname)
            return False
    else:
        print 'no return'
        return True

def send_flickr_imgs(username, password, imgs, msg):
    print 'sending...'
    uploadit(perms='write', filename=imgs, title=msg)
    print 'send successfully!'

if __name__ == '__main__':
#    flickApi("", "test.jpg")
    uname = 'crazypic11@yahoo.com'
    passwd = 'linux123'
    perms = 'write'
    filename = 'test.jpg'
    title = '标题'.encode('utf8')
    des = 'Avatar, the last air bender哈哈'.encode('utf8')
    tags = 'catoon avatar'
    
    verify_flickr_account(uname, passwd)
    send_flickr_imgs(uname, passwd, imgs='home.jpg', msg='标题'.encode('utf8'))
