import requests as r
from lxml import etree
import os
import time
import zipfile

# 进度条模块
def progressbar(url,name):

    start = time.time() #下载开始时间
    response = r.get(url, stream=True) #stream=True必须写上
    size = 0 #初始化已下载大小
    chunk_size = 1024 # 每次下载的数据大小
    content_size = int(response.headers['content-length']) # 下载文件总大小

    if response.status_code == 200: #判断是否响应成功
        print('Start download,[File size]:{size:.2f} MB'.format(size = content_size / chunk_size /1024)) #开始下载，显示下载文件大小
        filepath = name
        with open(filepath,'wb') as file: #显示进度条
            for data in response.iter_content(chunk_size = chunk_size):
                file.write(data)
                size +=len(data)
                print('\r'+'[下载进度]:%s%.2f%%' % ('>'*int(size*50/ content_size), float(size / content_size * 100)) ,end=' ')
    end = time.time() #下载结束时间
    print('Download completed!,times: %.2f秒' % (end - start)) #输出下载用时时间

def unzip(path,folder):
    zip_file = zipfile.ZipFile(path)
    zip_list = zip_file.namelist() # 得到压缩包里所有文件

    for f in zip_list:
        zip_file.extract(f, folder) # 循环解压文件到指定目录
    
    zip_file.close() # 关闭文件，必须有，释放内存

def judge(s):
    try:
        return 'chromedriver' in s.split('/')[1] and 'win32' in s.split('/')[1]
    except:
        return 0


input("make sure vpn connected")
v = input("input your chrome version: ")
url = 'http://chromedriver.storage.googleapis.com/'

resp = r.get(url).text.encode('utf-8')
# print(resp)
root = etree.fromstring(resp)
print(root.nsmap)
data = root.findall('Contents/Key',namespaces=root.nsmap)
res = [i.text for i in data if judge(i.text)]
for i in res:
    if v == i.split('.')[0]:
        url2 = url+i
        break
filename = 'chromedriver.zip'

progressbar(url2,filename)
unzip(filename,'.')
os.remove(filename)