#/usr/bin/env python
#-*- coding:utf8 -*-

#transform file's line terminator 
#from Windows-style(CR-LF) to UNIX-style(LF)

import re, os, shutil

#fn_with_path: filename with path
def win_style_file(fn_with_path):
    bak_fn = fn_with_path+".bak"
    shutil.copy2(fn_with_path, bak_fn)
    des_f = open(fn_with_path,  'wb')
    src_f = open(bak_fn,  'r')
    lines_gen = (l for l in src_f.readlines())
    for ln in lines_gen:
        ln = ln.strip()+'\n'
        des_f.write(ln)
    des_f.close()
    src_f.close()
    os.remove(bak_fn)

#dn_with_path: directory name with path
#ext_rule: .vim .txt .....
def win_style_dir(dn_with_path, ext_rule=""):
    for root, dirs, files in os.walk(dn_with_path):
        for fn in files:
            if ext_rule!="" and os.path.splitext(fn)[1]==ext_rule:
                win_style_file(os.path.join(root, fn))
    
if __name__ == "__main__":
#    win_style_file("D:/work/test/torte.vim")
    win_style_dir("D:/work/.vim/", '.vim')
