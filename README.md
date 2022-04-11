运行需求
===
* **1. 需要Python 3环境。**  
* **如何安装Python 3？**  
* **在没有安装Python 3时，请在确保已安装"应用安装程序(winget)"时，可通过运行软件中提供的bat程序进行安装**  
* **在没有安装"应用安装程序(winget)"时，请单击[此链接来进行下载Python 3](https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe)**  
* **如果是[Mac](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg)，请[单击此链接](https://www.python.org/ftp/python/3.10.4/python-3.10.4-macos11.pkg)进行下载安装**  
* **目前Linux端需要自行apt-get或yum进行安装**  
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

我的Gitee仓库
===

[单击此链接跳转](https://gitee.com/chengzhilin2021/Python-Requests)


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

#### 演示

* __html爬取__

![图片跑到了外太空](https://raw.githubusercontent.com/chengzhilin2021/Python-Requests/main/Pictures/requests%20html.gif "爬取html演示")

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

其他版本下载链接
===
Dev
---
~~[Dev 4.2](https://allall02.baidupcs.com/file/f50ff0e45g86b973eca2f35bbbdadaf2?bkt=en-6766f9da69592c12a24af92c808f286be220f7c7e5a75f8fcc91dd5a20fe43e17b738a5dd97102150042f7b0c91b0c51e3634df01d1ebfb9ed21d10888392317&fid=1211192705-250528-558135348571776&time=1649638271&sign=FDTAXUbGERLQlBHSKfWqiu-DCb740ccc5511e5e8fedcff06b081203-Ua2yLWo4%2FsWyT1wmY7SRvhC4PPo%3D&to=80&size=7710&sta_dx=7710&sta_cs=0&sta_ft=py&sta_ct=0&sta_mt=0&fm2=MH%2CBaoding%2CAnywhere%2C%2Cshandong%2Ccnc&ctime=1649637883&mtime=1649638097&resv0=0&resv1=0&resv2=rlim&resv3=5&resv4=7710&vuk=1211192705&iv=0&htype=&randtype=&tkbind_id=0&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=en-fca699842cbdec2c2b2b85f70a4b4c8bb043d79babacce17fb94f169da78271078c86c4d9a0c342ec6c5469ea4b08f16fa57e032a17f60bb305a5e1275657320&sl=68616270&expires=8h&rt=sh&r=361701101&vbdid=4192235366&fin=Dev+4.2.py&fn=Dev+4.2.py&rtype=1&dp-logid=21994668588559966&dp-callid=0.1&hps=1&tsl=200&csl=200&fsl=0&csign=6GJyjh1K7rzpRtczl%2B88goPk5TU%3D&so=0&ut=6&uter=4&serv=0&uc=4029387593&ti=497b2742088ef3a3bda77b6fc1fe378842fa3bd577debabb&hflag=30&from_type=1&adg=c_c5e85b811725782865682f80153df6b1&reqlabel=250528_f_2cb9b9f080f5e577239bca8dff423f98_-1_61b4f1e054aa1e870102fa9b42174bcb&by=themis&resvsflag=1-0-0-1-1-1)~~  
~~[Dev 4.9](https://yqcu02.baidupcs.com/file/7ac77468ai551525cdb0768a5179e72e?bkt=en-6f7dc9883530f8c903812b52029171e7c414a9da8fbb83247ef18233cdb5633e35633f19a51161aae9d2e6914dcec19d8fe446f200b226cf96ab908e42d44fd2&fid=1211192705-250528-452021462235189&time=1649638293&sign=FDTAXUbGERLQlBHSKfWqiu-DCb740ccc5511e5e8fedcff06b081203-Qsa6F4oWwZeMeghXLym8QznMI70%3D&to=120&size=11818&sta_dx=11818&sta_cs=1&sta_ft=py&sta_ct=0&sta_mt=0&fm2=MH%2CYangquan%2CAnywhere%2C%2Cshandong%2Ccnc&ctime=1649637884&mtime=1649638097&resv0=0&resv1=0&resv2=rlim&resv3=5&resv4=11818&vuk=1211192705&iv=0&htype=&randtype=&tkbind_id=0&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=en-a727d949ec4d89fcbe7d6a9ea2a76bfc401b1d5bcb7ca10596e870b89f3898baeb6a192af9264aa2f87e8447344ab742cdcdffd3616e5234305a5e1275657320&sl=68616270&expires=8h&rt=sh&r=342615612&vbdid=4192235366&fin=Dev+4.9.py&fn=Dev+4.9.py&rtype=1&dp-logid=22000579177964510&dp-callid=0.1&hps=1&tsl=200&csl=200&fsl=0&csign=6GJyjh1K7rzpRtczl%2B88goPk5TU%3D&so=0&ut=6&uter=4&serv=0&uc=4029387593&ti=4744d9fc935001bf5fb00bc6468a521ee74ff757a1dff87c&hflag=30&from_type=1&adg=c_c5e85b811725782865682f80153df6b1&reqlabel=250528_f_2cb9b9f080f5e577239bca8dff423f98_-1_61b4f1e054aa1e870102fa9b42174bcb&by=themis&resvsflag=1-0-0-1-1-1)~~  
[Dev 5.5](https://allall02.baidupcs.com/file/dfb43bcect6aa79679717153775beffa?bkt=en-0f64e6ca9b24f0bcdd4afa9f2508cde942c32a100e437ec00bc214e2538f2afdbe3b93f327792ea116b66f2613c048338fe446f200b226cfb9835ba29cb3f4d4&fid=1211192705-250528-1065752825215909&time=1649638336&sign=FDTAXUbGERLQlBHSKfWqiu-DCb740ccc5511e5e8fedcff06b081203-wrp7X%2BZl7cfIWiIJ29OBjj5c%2FRI%3D&to=80&size=8713&sta_dx=8713&sta_cs=1&sta_ft=py&sta_ct=0&sta_mt=0&fm2=MH%2CBaoding%2CAnywhere%2C%2Cshandong%2Ccnc&ctime=1649637885&mtime=1649638097&resv0=0&resv1=0&resv2=rlim&resv3=5&resv4=8713&vuk=1211192705&iv=0&htype=&randtype=&tkbind_id=0&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=en-171b04810b509f53c1dd5bee02a56ffcc2b45af87113b430ecb7dc5e9887a13f4b752ff2be02806d77295d3f7785c2d80bdb4de6058fc9e2305a5e1275657320&sl=68616270&expires=8h&rt=sh&r=861720946&vbdid=4192235366&fin=Dev+5.5.py&fn=Dev+5.5.py&rtype=1&dp-logid=22012018743397295&dp-callid=0.1&hps=1&tsl=200&csl=200&fsl=0&csign=6GJyjh1K7rzpRtczl%2B88goPk5TU%3D&so=0&ut=6&uter=4&serv=0&uc=4029387593&ti=643d984421895662c498a9c05fc3a9f32990ebd5fe5a08d3305a5e1275657320&hflag=30&from_type=1&adg=c_c5e85b811725782865682f80153df6b1&reqlabel=250528_f_2cb9b9f080f5e577239bca8dff423f98_-1_61b4f1e054aa1e870102fa9b42174bcb&by=themis&resvsflag=1-0-0-1-1-1)  

Beta
---
[Beta 5.1](https://allall02.baidupcs.com/file/0e8b75bc5i731f0a646a8ab5cc967e06?bkt=en-6766f9da69592c128e0667ff72fb5be9807f4335bc5f6f920396adcb5168273815aa1dc4b0e911ff7bb79a0c75eb15bce3634df01d1ebfb95003e92166265d17&fid=1211192705-250528-811368848602&time=1649638355&sign=FDTAXUbGERLQlBHSKfWqiu-DCb740ccc5511e5e8fedcff06b081203-nYCaqLi0Y5enEMGX1Saq43cfG7Y%3D&to=80&size=8057&sta_dx=8057&sta_cs=1&sta_ft=py&sta_ct=0&sta_mt=0&fm2=MH%2CBaoding%2CAnywhere%2C%2Cshandong%2Ccnc&ctime=1649637893&mtime=1649638084&resv0=0&resv1=0&resv2=rlim&resv3=5&resv4=8057&vuk=1211192705&iv=0&htype=&randtype=&tkbind_id=0&newver=1&newfm=1&secfm=1&flow_ver=3&pkey=en-d584ca9085e88665c362ed582b01e387747a848eca4eb5971766139da7000a0bd387fa6957357f5d0c03c3237bb1d6d6dca22cbd5a29ccb8305a5e1275657320&sl=68616270&expires=8h&rt=sh&r=823212624&vbdid=4192235366&fin=Beta+5.1.py&fn=Beta+5.1.py&rtype=1&dp-logid=22017142131259190&dp-callid=0.1&hps=1&tsl=200&csl=200&fsl=0&csign=6GJyjh1K7rzpRtczl%2B88goPk5TU%3D&so=0&ut=6&uter=4&serv=0&uc=4029387593&ti=497b2742088ef3a337d85dbfa1ddfe69f55759dadf2f7569&hflag=30&from_type=1&adg=c_c5e85b811725782865682f80153df6b1&reqlabel=250528_f_2cb9b9f080f5e577239bca8dff423f98_-1_61b4f1e054aa1e870102fa9b42174bcb&by=themis&resvsflag=1-0-0-1-1-1)  

其他版本查看链接
===

Dev
---

* ~~[Dev 4.2](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%204.2.py)~~  
* ~~[Dev 4.9](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%204.9.py)~~  
* [Dev 5.5](https://github.com/chengzhilin2021/Python-Requests/blob/main/Dev/Dev%205.5.py)  

Beta
---

* [Beta 5.1](https://github.com/chengzhilin2021/Python-Requests/blob/main/Beta/Beta%205.1.py)

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
