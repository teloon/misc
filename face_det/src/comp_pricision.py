# -*- coding: cp936 -*-
f = open('E:\\study\\courses\\ģʽʶ��μ�\\��ϰ2\\exercise\\��ϰ��������˵��\\fisher_effi_res.txt', "r")
ln = f.readline()
classes = ln.strip().split()
err_num = 0
for i,c in enumerate(classes):
    if int(c)<(i-i%5) or int(c)>(i-i%5+5):
        err_num += 1
        print i/5+1,(int(c)-1)/5+1
#    print (int(c)-1)/5+1

print "err num: ", err_num
    
