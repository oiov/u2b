# 投稿姬

把YouTube视频自动搬运到B站的机器人，通过一行命令调用。

# 快速开始

```shell
# 1.本地安装
git clone https://github.com/yesmore/U-To-B.git
cd U-To-B
sudo bash setup.sh

# 2.使用biliup登录账号 
#  biliup是一个B站命令行投稿工具, 官网 https://biliup.github.io/biliup-rs
#  在不同平台需要下载对应二进制文件，下载教程：https://biliup.github.io/biliup-rs/Installation.html，本项目默认使用mac包
./biliup login

# 3.启动项目
#  在运行下面这行命令之前请先参照下文中 `参数修改` 中的 1、2 步对 task_manager.py 和 new_downloader.py 做出修改
sudo bash start.sh 
```

## 参数修改

- 1.将task_manager.py中的`OWNER`变量改为自己的uid.  
- 2.将new_downloader.py中的`OWNER_NAME`变量改为自己的用户名.  
- 3.运行:

```shell
sudo bash setup.sh && sudo bash start.sh 
```

# 调用命令

```shell
python3 new_downloader.py <url> <tid>
```
如:
```shell
python3 new_downloader.py https://www.youtube.com/watch?v=xxxxxxxxx 21
```

> tid参考：https://biliup.github.io/tid-ref.html

# 示例demo

[盛佳冉](https://space.bilibili.com/486914885/video)
