# 170828 3wd1
## 探索 `1.5h`
### 0.1 晚上

- 学习 VWan 从 json 中去数据的思路，解决 bug `1h`
  - 自己实现一遍 .attr 方式访问 dict 数据（非`__geiattr__`方法）
  - 因无法解决数组问题，Vwan 从网上其他人的思路中得到灵感，进行改进，但 Vwan 最后调试时出现bug
    - 看懂 其他人的思路
    - 看到 Vwab 改进的方法
    - 调试 bug

- 根据 Scott 教练发布的 issue，再次探索闭包，学习装饰器 `0.5h`
  - 闭包代码实例
  - 引入装饰器，与闭包对比学习


# 170829 3wd2

## 探索 `2.5h`
### 0.1 下午

- 16:40-18:00 优化 ch2 程序代码 1.5h`
  - 取消使用`now`和`future`命令转换天气查询模式，统一两种模式的输入入口，用户输入`北京`时查询实时天气，`北京 3`查询北京未来3天的天气
  - 新建 `User` 类，把指令功能封装为实例方法，使用类似路由的思路，将指令对应的函数和实例方法封装进`dict`,通过`dict.get`方法调用，代替`if/elif/../else`，减少`main()`条件复杂度。

```python
    def print_help():
        print(program_help_doc)


    def quit_():
        pass


    def command_response(user):
        """
        根据用户输入的指令调用对应函数或实例方法
        :param user: User 实例
        :return:
        """

        command_func_dt = {
            'h': print_help,
            'help': print_help,
            'q': quit_,
            'quit': quit_,
            'history': user.print_history,
            'c': user.temperature_unit_switch,
            'f': user.temperature_unit_switch,
        }
        command_not_found_msg = "抱歉，您输入的指令未能识别"
        func = command_func_dt.get(user.input, lambda: print(command_not_found_msg))
        func()
```

### 0.2 晚上
- 22:40-23:10 删去重构后不需要的函数等，更新脚本文件的`__all__`属性 `0.5h`
- 23:10-23:40 新增城市拼音名数据，完成拼音自动补全功能 `0.5h`


### 复盘之收获
- 在优化代码时，尝试改变以前想得多，动手少的习惯，试着在纸上写下简单的逻辑后开始写代码，以伪代码形式把逻辑写完，然后补充代码。

### 复盘至改进
- 最近 3 天娱乐过多，学习时间继续下降，考虑是因为没有计划性导致，故对本周任务有一个初步规划
    - 3wd3 虚拟机Linux，了解 Flask 部署的 Demo
    - 3wd4 ch3 初版成果及优化
    - 3wd5 ch3 个人教程+个人博客搭建(Pelican Github-Pages)

# 170830 3wd3

## 探索 `1.5h`
### 0.1 晚上
- 使用 vagrant + VirtualBox搭建虚拟开发环境 `1.5h`
  - 搜索教程
  - 搭建
  - 出 bug

# 170831 3wd4

## 探索 `5.5h`
### 0.1 上午下午 `2h`
- 继续 vagrant + VirtualBox搭建虚拟开发环境 `2h`
  - 安装 pyenv
  - 出bug，无法添加至path
    - 问题是以 `$~`, `~`代替`/root`，发现无法代替
  - 各种解决
  - zsh PATH也出问题，解决
  - 安装 virtualenv
    - `git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv `
    - `echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc`
    - `source ~/.zshrc `
    - 安装 Python 3.6.2
      - `pyenv install 3.6.2` 速度太慢
      - 搜索发现执行上述命令时需要下载文件`Python-3.6.2.tar.xz`，可从官网使用下载工具下载它，把这个文件放在`~/.pyenv/cache/`目录之下，然后在执行上述命令
      - 又遇到一个坑，如何在主机和虚拟机传输文件。按官方介绍说，虚拟机安完后，`Vagrantfile`所在文件夹`d:/vagrant`默认就成为了一个共享文件夹，在虚拟机内通过`cd /vagrant`可访问，但是在虚拟机内访问后发现文件夹是存在，可以`ls /vagrant`发现没有任何文件
        - 最终搜索也没发现好用的解决方案，在`Vagrantfile`文件内自己重新配置一个共享文件夹，把`c:/py/py104`共享给虚拟机内的`/py`
      ```
      Vagrant.configure("2") do |config|
            # 虚拟机名字，不能改
            config.vm.box = "ubuntu64"
            # 端口映射，用 localhost:8080 去访问虚拟机内的 80 端口
            config.vm.network "forwarded_port", guest: 3000, host: 8000
            # 共享文件夹
            config.vm.synced_folder "C:/py/Py104", "/py"
      ```
      - 接下来输入以下命令
        ```
        ➜  /vagrant mv Python-3.6.2.tar.xz ~/.pyenv/cache
        ➜  /vagrant pyenv install 3.6.2
        Installing Python-3.6.2...
        WARNING: The Python bz2 extension was not compiled. Missing the bzip2 lib?
        WARNING: The Python readline extension was not compiled. Missing the GNU readline lib?
        WARNING: The Python sqlite3 extension was not compiled. Missing the SQLite3 lib?
        Installed Python-3.6.2 to /root/.pyenv/versions/3.6.2
        ```
  - 创建一个 创建一个基于 Python 3.6.2 版本的virtualenv 环境，环境名字为py362
    - `pyenv virtualenv 3.6.2 py362`

### 0.2 晚上 `3.5h`

- 18:40-19:00 看Flask教程
- 19:00-19:35 构架好部分基本框架
  - 获取输入，并且在页面输出

- 20：20-20：50 复用 ch2 函数，完成用户输入判断，通过城市名判断时查询天气并返回结果
- 21：40-22：35 实现未来天气查询，并且输出天气情况时每天的天气单独一行
- 22:55-24:00 实现历史查询，帮助，但帮助显示有问题，未分行

## 复盘之收获
- vagrant 虚拟机 + pyenv 初步探坑，对于Linux中的 `$PATH`有一个朦胧的认识
- 听了 Hugo ch3 的编程直播分享，知道 jinja2 的模版继承功能，感受到其探索的路径，学习的热情

## 复盘至改进
- 下次探索时候，如果来不及系统整理探坑过程，那么就把有用的网址记一下，防止下次重复搜索浪费时间。


# 170901 3wd5

## 探索 `4h`
### 0.1 上午
- 12:00-12:50 阅读flash quiuk start

### 0.1 下午
- 13:22-13:48 验证了带query参数的 url 不能作为flask路由里的 path
- 14:40-16:23 解决帮助信息的多行显示问题，统一天气查询结果以list类型保存，便于使用jinja2渲染页面
- 16:23-16:44 历史查询记录为0时，提示语`prompt=无记录`；大于0时，提示语`prompt=您的查询记录为：`，然后逐条显示记录

### 0.3 晚上
- 22:30-23:00 访客打开主页时，显示访问地的天气信息

## 复盘之收获
- 使用 Github 能方便的完成本地与服务器之间的代码同步。基本流程为本地开发完成 push--> Github --> pull 至服务器 -->部署

# 170902 3wd6
无进行作业方面探索,学习链表,哈希表实现

# Todo
- 优化
  - 返回城市，天气，温度等变量，html组装，css美化
  - 去掉温度转换
  - 卡包学习
    - Flask WTK 制作表单

# Timelog
- 3wd1 `1.5h`
- 3wd2 `2.5h`
- 3wd3 `1.5h`
- 3wd4 `5.5h`
- 3wd5 `4h`
- 3wd6
- 3wd7