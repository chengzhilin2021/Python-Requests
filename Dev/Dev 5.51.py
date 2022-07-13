print("首次使用可能需要较长的时间")
import os  # 导入os库

while 1 == 1:
    #打印类型选择
    print("请选择爬取类型： 1.html      2.图片")
    answer = input("请输入：")
    if answer == "1":
        import platform
        if(platform.system()=='Windows'):
            os.system('pip install requests >nul >nul') #安装requests工具
            import requests  # 导入requests库
        else:
            os.system('pip3 install requests')

        header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2"
        }
        print()
        print()
        print()
        
        print("请选择您要查看源码的网址")
        print("1.百度      2.必应")
        print("3. 哔哩哔哩      4.微软")
        print("5. 自定义")


        answer = input("请输入序号:") #询问选择


        #爬取百度
        if answer == "1":
            url = r"http://www.baidu.com/"
            response = requests.get(url,headers=header) #将爬取的值保存至变量
            response.encoding='utf-8' #将其转化为utf-8格式
            html=response.text #将返回值转化为源码
            print(html) #打印源码
            #打印空行
            print()
            print()
            print()
            print()

            #结束
            print("爬取完成")
            input("按任意键退出")
            exit()


        #爬取必应
        if answer == "2":
            url = r"http://cn.bing.com/"
            response = requests.get(url,headers=header) #将爬取的值保存至变量
            response.encoding='utf-8' #将其转化为utf-8格式
            html=response.text #将返回值转化为源码
            print(html) #打印源码
            print()
            print()
            print()
            print()

            #结束
            print("爬取完成")
            input("按任意键退出")
            exit()

        #爬取B站
        if answer == "3":
            url = r"http://www.bilibili.com/"
            response = requests.get(url,headers=header) #将爬取的值保存至变量
            response.encoding='utf-8' #将其转化为utf-8格式
            html=response.text #将返回值转化为源码
            print(html) #打印源码
            #打印空行
            print()
            print()
            print()
            print()

            #结束
            print("爬取完成")
            input("按任意键退出")
            exit()


        #爬取微软
        if answer == "4":
            url = r"http://www.microsoft.com/"
            response = requests.get(url,headers=header) #将爬取的值保存至变量
            response.encoding='utf-8' #将其转化为utf-8格式
            html=response.text #将返回值转化为源码
            print(html) #打印源码
            #打印空行
            print()
            print()
            print()
            print()

            #结束
            print("爬取完成")
            input("按任意键退出")
            exit()
            #爬取自定义网站
        while 1 == 1:
            if answer == "5":
                url = input(r"请输入您要查看的网址:") #询问查看的网址
                print(r"如果爬取失败，与本软件和作者无关！") #免责声明
                print(r"请输入是否添加http：//或https：//")
                Return = input(r"如果已添加，请输入Y，否则请输入N(注意大小写):")
                if Return == "Y" :
                    print("准备爬取")
                    response = requests.get(url,headers=header) #将爬取的值保存至变量
                    response.encoding='utf-8' #将其转化为utf-8格式
                    html=response.text #将返回值转化为源码
                    print(html) #打印源码
                    #打印空行
                    print()
                    print()
                    print()
                    print()

                    #结束
                    print("爬取完成")
                    input("按任意键退出")
                    exit()
                else:
                    if Return == "N":
                        url = "http://"+url
                        response = requests.get(url,headers=header) #将爬取的值保存至变量
                        response.encoding='utf-8' #将其转化为utf-8格式
                        html=response.text #将返回值转化为源码
                        print(html) #打印源码
                        #打印空行
                        print()
                        print()
                        print()
                        print()

                        #结束
                        print("爬取完成")
                        input("按任意键退出")
                        exit()
                    else:
                        print("您输入错误，请重新输入！！")
                        continue
    
    if answer == "2" :
        print("目前只能爬取百度贴吧！")
        
        # 导入库
        import urllib
        import urllib.request
        import platform
        if(platform.system()=='Windows'):
            os.system("pip install lxml >nul>nul")
        else:
            os.system("pip3 install lxml")
        from lxml import etree

        answer = input("请输入需要爬取的贴吧：")
        begin = input("请输入起始页码：")
        end = input("请输入结束页码：")
        begin = int(begin)
        end = int(end)
        
        
        if begin > end:
            a = input("您可能输入错误，已自动为您调换")
            temporary = begin
            begin = end
            end = temporary
            begin = int(begin)
            end = int(end)
        else:
            pass

        # 创建文件夹
        if(platform.system()=='Windows'):
            mkpath = "C:\\" + answer + "吧图片\\"
            print("将保存至" + mkpath)
            input("按任意键继续")
            if os.path.isdir(mkpath) == False:
                os.mkdir(mkpath)
        else:
            import getpass
            UserName = getpass.getuser()
            mkpath = "/home/" + UserName + "/Desktop/" + answer + "吧图片/"
            print("将保存至" + mkpath)
            input("按任意键继续")
            if os.path.isdir(mkpath) == False:
                os.mkdir(mkpath)

        class Spider(object):
            def __init__(self):
                self.tiebaName = answer
                self.beginPage = begin
                self.endPage = end
                self.url = r"http://tieba.baidu.com/F?"
                self.ua_header = {}
                self.fileName = 1
            def tiebaSpider(self):
                for page in range(int(self.beginPage),int(self.endPage)+1):
                    pn = (page-1)*50
                    wo = {'pn':pn,'kw':self.tiebaName}
                    word = urllib.parse.urlencode(wo)
                    myurl = self.url+word
                    self.loadPage(myurl)


            def loadPage(self,url):
                req = urllib.request.Request(url,headers=self.ua_header)
                data = urllib.request.urlopen(req).read()

                html = etree.HTML(data)
                links = html.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

                for link in links:
                    link = "http://tieba.baidu.com"+link
                    self.loadImages(link)

            def loadImages(self,link):
                req = urllib.request.Request(link,headers=self.ua_header)
                
                data = urllib.request.urlopen(req).read()
                
                html = etree.HTML(data)
                links = html.xpath('//img[@class="BDE_Image" ]/@src')
                for imageslink in links:
                    self.writeImages(imageslink)

            def writeImages(self,imagesLink):

                
                print("正在存储图片：",self.fileName,"……")

                image = urllib.request.urlopen(imagesLink).read()

                file = open(mkpath+str(self.fileName)+".jpg","wb")
                file.write(image)

                file.close()

                self.fileName += 1

        if __name__  ==  '__main__':

            mySpider = Spider()

            mySpider.tiebaSpider()
        
        exit()
