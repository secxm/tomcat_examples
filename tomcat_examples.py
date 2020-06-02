# coding:utf-8
import os
import sys
import requests

def get_tomcat(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate',
    'Connection':'keep-alive'}
    url=url.replace('\\','/')
    r1=requests.get(url,headers=headers)
    r2=r1.status_code
    return r2


def get_dict(filename):
   
    f1=open(filename,'r+')
    s2=f1.readlines()
    f1.close()
    s3=list()
    for i in s2:
        i=i.replace('\n','')
        i=i.strip()
        s3.append(i)
    
    return s3


def sum(filename,url):
    try:
        d1=get_dict(filename)
    except IOError:
        print "Error: file erro"
    
    s1=list()

    for u1 in range(0,len(d1)):
        u2=""
        s2=list()
        u2=url+"\\"+d1[u1]  # 拼接请求URL
        u2=u2.replace('\\','/')
        try:
            re1=get_tomcat(u2)
            re1=str(re1)
        except:
            re1="000"
        s2.append(u2)
        s2.append(re1)
        s1.append(s2)
    
    return s1      

if __name__=='__main__':
    print "tomcat 默认文件存在路径"
    try:
        filename=sys.argv[2]  #字典文件
        url=sys.argv[1]       #请求url
        m1=sum_get(filename,url)
        for i in range(0,len(m1)):
            if(m1[i][1]=="200"):
                print m1[i][0]+" "+m1[i][1]
    except Exception:       
        print "程序运行错误"
