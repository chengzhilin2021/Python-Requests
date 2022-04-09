运行需求
===
* **1. 需要Python 3环境。**  
* **如何安装Python 3？**  
* **在没有安装Python 3时，请在确保已安装"应用安装程序(winget)"时，可以通过运行软件中提供的bat程序进行安装**  
* **在没有没有安装"应用安装程序(winget)"时，请单击[此链接来进行下载Python 3](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)**  
* **如果是[Mac](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg)，请单击Mac或[单击此链接](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg)进行下载进行下载安装**  
* **目前Linux端需要自行apt-get或yum进行安装**  
* **2. 目前需要使用Windows环境，否则将无法运行。**  
* **3. 不允许使用Python 2环境，请进行升级！！！**  
* **4. 目前查看未安装库使用为pip命令，在Mac端或Linux端中，pip命令只能安装Python 2扩展包。**  

如何在非Windows端运行？
===
### 目前可在Dev 5.5版本中可用，稳定性待测试

* **1. 使用终端安装Requests和lxml库**  
* **2. 只能使用爬取源码，无法使用爬取图片**  
* **3. 将在以后的更新中进行解决:blush:**  

更新日志  
===

* 1.0 开始运行  
* 2.0 加入自定义功能  
* 3.0 修复了整体软件的稳定性  
* 3.9 __(内部测试版)__ 加入了header，可以进行爬取真正的源码；并增加了对图片的支持（只能爬取百度贴吧）  
* 4.0 修复了一些已知问题  
* 4.1 修复需要删除C:\img文件夹的Bug，会自动创建文件夹  
* 4.2 __(内部测试版)__ 增加了自动命名功能，稳定性待测试  
* 4.9 __(内部测试版)__ 增加了用户输入错误自动改正的功能  
* 5.0 修复了一些已知问题  
* 5.1 __(公测版)__ 增加了使用者某些库未安装无法运行的问题，以及用户不知道保存路径的问题  
* 5.5 __(内部测试版)__ 增加了支持Mac和Linux等系统

#### 演示

* __html爬取__

![图片跑到了外太空](https://github.com/chengzhilin2021/Python-Requests/blob/main/Pictures/requests%20html.gif "爬取html演示")

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

内测版本链接
===
Dev
---
~~[Dev 4.2](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%204.2.py)~~  
~~[Dev 4.9](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%204.9.py)~~  
[Dev 5.5](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%205.5.py)  

Beta
---
[Beta 5.1](https://github.com/chengzhilin2021/Python-Requests/blob/main/Beta/Beta%205.1.py)  

