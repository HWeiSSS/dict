“#dict”
这是一个电子词典

功能说明：
1. 用户可以登录和注册
   登录凭借用户名密码即可
   注册要求用户必须填写用户名和密码其他内容自定
   用户名要求不能够重复

2. 用户数据要求使用数据库长期保存
   数据报自定

3. 能够满足多个用户同时登陆操作的需求

4. 功能分为客户单和服务端，客户单主要发起请求，服务    端处理请求，用户启动客户端即进入一级界面
     登陆   注册   退出
5. 用户登录后即进入二级界面
     查单词   查看历史记录   退出
         单词本 ： 每行一个单词
               单词和解释之间一定有空格
           后面的单词一定比前面的大

     查单词 ： 输入单词，显示单词意思，可以循环查询。输入 ## 表示退出查词

     查看历史记录： 查看当前用户的历史查词记录
        name     word    time
      
     退出 ： 退出到一级界面，相当于注销
     
项目分析
服务器 ： 登录  注册   查词   历史记录
客户端 ： 打印界面   发出请求    接收反馈   打印结果
技术点 :  并发   sys.fork
        套接字  tcp 套接字
        数据库  mysql
        查词    文本