# 数据库(MYSQL)相关-学习笔记

标签： python mysql 数据库

---
##　MySQL
开源的关系型数据库

## [Ubuntu安装MySQL和Python库MySQLdb步骤](http://blog.csdn.net/zhaobryant/article/details/45501241#)
### 一、安装MySQL服务器和客户端

执行以下命令：

```
sudo apt-get install MySQL-server-5.6 mysql-client-5.6 
sudo apt-get install libmysqlclient-dev libmysqld-dev
```

可能用到的命令：

```
mysql -u root -p #登陆mysql:
sudo apt-get install mysql-workbench #安装workbench
sudo aptitude install mysql-server-5.6
sudo apt-get remove mysql-server #卸载
sudo apt-get autoremove mysql-server
sudo apt-get update
sudo netstat -tap | grep mysql
sudo apt-get -f install
sudo service mysql start #开启服务
```

### 二、Python安装MySQLdb库

执行以下命令：
```
sudo apt-get install Python-pip 
sudo apt-get install python-dev 
sudo pip install mysql-python
```

验证方法：

进入Python命令行界面： 
import MySQLdb 
未报错即表示安装成功

# 数据库操作命令

```
show databases;
# 创建数据库
create database userlogin;
# 进入数据库
use userlogin;
show tables;
# 创建数据表
create table user(id int(11) unsigned auto_increment primary key not null,username varchar(25) not null,passwd varchar(25) not null,email varchar(40) not null);
# 显示数据表
show tables;
# 显示某个表详细信息
describe user;
# 选择
select * from user;
select * from user1 order by id DESC;
# 更新
update user1 set username='meimei' where id=10;
update user1 set passwd = '76543';
update user1 set passwd = 'there' where username = 'mama';
# 删除
delete from user1 where username = 'meimei';
alter table user1 drop column id;
drop database scraping;
# 退出
quit
```

## 解决中文？？？乱码
以下示例给出创建数据库时指定编码的两种方式：
```
1）CREATE  DATABASE  mydbname  CHARACTER SET  utf8  COLLATE utf8_general_ci；
2）CREATE  DATABASE  IF NOT  EXISTS  mydbname  DEFAULT CHARACTER SET utf8;
```
这样就是设置好了我们数据库的编码格式
当然，表的编码格式也要设置一下：
```
CREATETABLEIF NOTEXISTS test (
 namevarchar(64)NOTNULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
[视频教程链接](http://www.imooc.com/learn/475)
[查看图片-python和数据库连接图](http://f.hiphotos.baidu.com/image/pic/item/0824ab18972bd407007242db73899e510fb3095a.jpg)
[查看图片-访问数据库流程](http://b.hiphotos.baidu.com/image/pic/item/63d9f2d3572c11dfd0fd2d056b2762d0f703c2ec.jpg)
[图片-MySQLdb.connect（参数）](http://a.hiphotos.baidu.com/image/pic/item/b812c8fcc3cec3fd0cee4165de88d43f869427ca.jpg)
[图片-connection支持的方法](http://h.hiphotos.baidu.com/image/pic/item/cefc1e178a82b9016d4722237b8da9773912ef3c.jpg)