#coding=utf-8
import os #导入os库
os.system('pip install requests >nul >nul') #安装requests工具
import requests #导入requests库


#打印内容
print("python爬虫3.0.0") #打印此软件版本

#打印空行
print()
print()
print()

while 1 == 1:
    #打印选择类型
    print("请选择您要查看源码的网址")
    print("1.百度      2.必应")
    print("3. 哔哩哔哩      4.微软")
    print("5. 自定义")


    answer = input("请输入序号:") #询问选择


    #爬取百度
    if answer == "1":
        url = r"http://www.baidu.com/"
        response = requests.get(url) #将爬取的值保存至变量
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
        exit()


    #爬取必应
    if answer == "2":
        url = r"http://cn.bing.com/"
        response = requests.get(url) #将爬取的值保存至变量
        response.encoding='utf-8' #将其转化为utf-8格式
        html=response.text #将返回值转化为源码
        print(html) #打印源码
        print()
        print()
        print()
        print()

        #结束
        print("爬取完成")
        exit()

    #爬取B站
    if answer == "3":
        url = r"http://www.bilibili.com/"
        response = requests.get(url) #将爬取的值保存至变量
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
        exit()


    #爬取微软
    if answer == "4":
        url = r"http://www.microsoft.com/"
        response = requests.get(url) #将爬取的值保存至变量
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
                response = requests.get(url) #将爬取的值保存至变量
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
                exit()
            else:
                if Return == "N":
                    url = "http://"+url
                    response = requests.get(url) #将爬取的值保存至变量
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
                    exit()
                else:
                    print("您输入错误，请重新输入！！")
                    continue
