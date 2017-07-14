# coding:utf-8
#!/usr/bin/python  
import re   
import urllib  
# def getHtml(url):  
#     page=urllib.urlopen(url)  
#     html=page.read()  
#     return html  
# def getMp4(html):  
#     r=r"href='(http.*\.mp4)'"  
#     re_mp4=re.compile(r)  
#     mp4List=re.findall(re_mp4,html)  
#     filename=1  
#     for mp4url in mp4List:  
#         urllib.urlretrieve(mp4url,"%s.mp4" %filename)  
#         print  'file "%s.mp4" done' %filename  
#         filename+=1  
# url=raw_input("please input the source url:")  
# html=getHtml(url)  
# getMp4('http://v1.365yg.com/d11dd8733d015085ae1110d675d652db/5966e28c/video/m/220eebb4a7cdaf647e5a952b5c6c31a8773114951400004fe603afd290/')
urllib.urlretrieve('http://v1.365yg.com/d11dd8733d015085ae1110d675d652db/5966e28c/video/m/220eebb4a7cdaf647e5a952b5c6c31a8773114951400004fe603afd290/',"1.mp4")  
# print  'file "1.mp4" done'   