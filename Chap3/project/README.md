# oh my weather

简单的天气查询Web App

# Feature

- 输入城市名，点击「查询天气」可获取该城市最新天气情况和未来5天天气预报概况

-  点击「帮助」，获取帮助信息
-  点击「历史记录」，获取历史查询信息

## Require

-  Python 3.6
-  requests 2.14.2
-  flask 0.12.2
-  jinja2 2.9.6
-  werkzeug 0.12.2

## Installation

1. 下载 mvp-jinja2目录及下属所有文件

2. 安装所需依赖包，推荐创建一个虚拟环境，在该环境下进入`requirements.txt`所在目录下

   ```
   pip install -r requirements.txt
   ```

# Usage

1. 使用`Python 3.6`启动服务端完成部署

```
python app_jinja2.py
```

2. 默认可通过`127.0.0.1:5000`访问天气查询系统，端口及ip可在在`app_jinja2.py`文件修改内

# Changelog

-  V17.09.08.0230
   -  Feature
      -  添加未来5天天气预报
      -  使用 `Bootstrap` 适配移动端,美化页面

- V17.09.01.1750
  - Feature
    - 使用`flask`+ `Jinja2` 模板引擎实现基本的需求，可查询实时天气，查看帮助和历史记录

    - 访客打开主页时，显示访问地的天气信息

      ​