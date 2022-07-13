运行需求
===
* **1. 需要Python 3环境。**  
* **如何安装Python 3？**  
* **在没有安装Python 3时，请在确保已安装"应用安装程序(winget)"时，可通过运行软件中提供的bat文件进行安装**  
* **在没有安装"应用安装程序(winget)"时，请单击[此链接来进行下载Python 3](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)**  
* **如果是[Mac](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg)，请[单击此链接](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg)进行下载安装**  
* **目前Linux端可通过提供的sh文件进行安装**  
* **2. 目前需要使用Windows环境，否则将无法运行。**  
* **3. 不允许使用Python 2环境，请进行升级！！！**  
* **4. 目前查看未安装库使用为pip命令，在Mac端或Linux端中，pip命令只能安装Python 2扩展包。**  

如何在非Windows端运行？
===
### 目前可在Dev 5.5版本中可用，稳定性待测试  
[单击此链接进行跳转](#Dev)

* **1. 使用终端安装Requests和lxml库**  
* **2. 只能使用爬取源码，无法使用爬取图片**  
* **3. 将在以后的更新中进行解决:blush:**  


更新日志  
===

* 1.0 开始运行  
* 2.0 加入自定义功能  
* 3.0 修复了软件的整体稳定性  
* 3.9 __(内部测试版)__ 加入了header，可以进行爬取真正的源码；并增加了对图片的支持（只能爬取百度贴吧）  
* 4.0 修复了一些已知问题  
* 4.1 修复需要删除C:\img文件夹的Bug，会自动创建文件夹  
* 4.2 __(内部测试版)__ 增加了自动命名功能，稳定性待测试  
* 4.9 __(内部测试版)__ 增加了用户输入错误自动改正的功能  
* 5.0 修复了一些已知问题（目前还存在某些问题，请使用Dev 5.5版本解决）  
* 5.1 __(公测版)__ 增加了使用中某些库未安装无法运行的问题，以及用户不知道保存路径的问题  
* 5.5 __(内部测试版)__ 增加了支持Mac和Linux等系统
* 5.51 __(内部测试版)__ 修复了部分已知问题

#### 演示

* __html爬取__

![图片跑到了外太空]([./Image/requests%20html.gif](https://raw.githubusercontent.com/chengzhilin2021/Python-Requests/main/Image/requests%20html.gif) "爬取html演示")

User-Agent提供
===

__1.__
``` "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2" ```  

__2.__
``` "User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;" ```  

为何会有两个User-Agent？
===

* **在使用爬取源码时，将会使用第一个(也就是其他浏览器的User-Agent)。**  
* **在使用爬取图片时，由于只能爬取百度贴吧，所以使用"Internet Explorer"的User-Agent。**  



其他版本查看链接
===

Dev
---

* [Dev 5.5](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%205.5.py)  



出现问题怎么办？
===
Dev版本出现了问题
---
#### 模板
```
本人在chengzhilin2021/Python-Requests的项目的Dev[填写版本]+版本中发现了问题，  
[描述问题]  
```
* 然后发送至邮箱```chengzhilin2021@outlook.com```，本人一定会第一时间进行回复  

----------------------------

Beta版本出现了问题  
---
#### 模板  
```
本人在chengzhilin2021/Python-Requests的项目的Beta[填写版本]+版本中发现了问题，  
[描述问题]  
```
* 然后发送至邮箱```chengzhilin2021@outlook.com```，本人一定会第一时间进行回复  

-----------------------------

正式版出现了问题  
---
#### 出现问题的解决方案
* 如您急需使用此软件，请使用[Dev 5.5](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%205.5.py)  

如何反馈
===
* 1.请向邮箱```chengzhilin2021@outlook.com```反馈  
* 2.请切换至Dev或Beta版本正常使用  
* 3.正式版目前还存在某些问题，已在Dev 5.5版本中解决，为您带来的不便深感抱歉。  
