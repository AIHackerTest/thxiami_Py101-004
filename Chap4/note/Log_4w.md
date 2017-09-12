# 170904 4wd1

## 探索 `10.5h`

### 0.1 下午

-  1300-1320 重构parse函数,返回含数据的`dict`供前端渲染,而非直接返回文本信息

-  1440-1453 修改前端HTML内jinja2模板, 从`dict`中获取数据渲染

-  1453-1534 用户输入城市,返回实时天气和未来5天天气预报情况

-  1534-1618  修改了`fetch_weather() `,传入参数由` api_url`,`api_params_dict`改为`user`, `query_mode`. 函数内部逻辑为,在调用API时根据`query_mode`选择对应的url和默认的参数字典, 保存在`user.input`内的用户输入的城市 作为调用API时需要的参数  `location` 的`value`

-  1700-1757 学习使用Echarts显示天气信息,学会实例,中间在使用`js` 时出现bug, 

   ```javascript
   var myChart = echarts.init(document.getElementById("main"))；
   ```

   找了半天,最终发现是末尾的";"写成了中文的"；"

   下次找bug,应该在 chrome 里, 按F12 打开调试工具栏后, 刷新页面,在`console`区域 看报错情况,上面这种可以在这里面直接找到,不用自己肉眼去寻找了.

## 0.2 晚上

-  1834- 1928 前端使用`js`生成 `echarts `需要一个包含显示格式和数据的字典, 需要将天气数据放进去, 如何从后端生成这个字典并传给前端.思路是后端生成字典,然后序列化为`json`数据保存本地文件, 前端的 `jquery` 库打开本地的`json`文件

-  2050- 23:00学习 `ajax` 异步,目的是代替之前的`json`文件方案,完成前端与后端数据的传递, 可以从后端获得生成`echarts` 所需要的数据(日期, 高温,低温等)

   -  [W3school AJAX](https://www.w3schools.com/xml/ajax_intro.asp)

      -  什么是 AJAX? 跟 XML 什么关系? 

         -  >  AJAX is a misleading name. AJAX applications might use XML to transport data, but it is equally common to transport data as plain text or JSON text.

      -  什么是` XMLHttpRequest`对象?js语言的吗,就像python的内置对象一样?与浏览器的关系是?浏览器是一个js解释器吗

      -  AJAX 不能跨域发出请求, 所以在本地测试W3schools代码时没有啥响应. 何为域? 目前知道服务器就是一个域,但不知域的定义是大于服务器还是小于服务器?

      -  debug:

         -  ```javascript
            xmlhttp = new XMLHttpRequest()
            // 定义 XMLHttpRequest 状态发生变化时调用的函数
            xmlhttp.onreadystateChange = function() {...}
            // 异步回传回来时,始终不能执行 function 内代码
            // 找了半天bug,发现是...用了 ATOM的自动补全,导致大小写不对
            // 错误: onreadystateChange 
            // 正确: onreadystatechange
            ```

         ​

-  23:30 - 3:20 调试ajax,后端根据api返回的数据,生成echarts需要的option数据

   -  遇到一个bug, js文件修改后,重载页面,`F12`-`Source` 发现浏览器加载的还是原来的js文件,猜测可能是浏览器缓存了, 百度了一下,在路径后加一个query参数, 比如修改日期. 可以解决该问题

   -  ```javascript
      <script src="{{ url_for('static', filename='options.js') }}?t=2"></script>
      ```

   -  在知乎上看到有系统的解决方案, 有专一工具会校验文件的HASH, 把HASH作为js文件名. 但本次作业规模比较小, 没必要学习这套工具.


# 170905 4wd2

## 探索 

-  激发
   -  希望美化显示效果,达到 ![example](https://raw.githubusercontent.com/thxiami/Py101-004/master/Chap3/resource/example.PNG?token=AZTlP1W2QIJjoJZGTb-8UCGE6fvpRK2Mks5ZuQW2wA%3D%3D)的效果.


   -  思路1 `1h`
      -   在`Echarts `的基础上加入新的非line类型的数据(阴晴),以icon的形式显示.  
   -  搜索
      -  查看官方手册
      -  查找可用icon,找到一个css样式实现的 [weather-icons](http://www.bootcdn.cn/weather-icons/)
   -  方案: 暂未找到合适数据类型添加在Echarts中


   -  思路2 `2h`
      -  找前端的天气预报 css 模板，看懂后修改使用
   -  搜索
      -  有漂亮的,但没找到简单可实际操作的,纯抄袭又无提高
      -  待研究:
         -  <https://dribbble.com/shots/1663525-Weather-Widget-freebie-HTML-CSS>
         -  https://w3layouts.com/simple-weather-widget-responsive-template/
   -  思路3 `未进行`
      -  学习 bootstrap, 使用表格+icon, 简单美化 且能适应移动端

   ## 复盘之改进

   -  后端代码未优化的情况下，过度追求前端效果且急于求成，时间分配不合理
   -  改进：前端应先做出粗糙框架，其目的是配合测试后端的代码功能是否正常。因此若优化前端，应该先想象后端时候仍有未优化之处。

   ​

   # 170906 4wd3

   ## 探索`1.5h`

   -  继续修改前后端交互方式 `1.5h`

   -  激发

      -   天气查询时, 前端使用 AJAX 异步请求,当正常时, 后端返回JSON格式结果,;当不正常时,后端还是原来的jinja2套路, 返回一个提示语字符串替换掉模板页面对应内容。需要统一一下，都是用 AJAX，减少重复刷新页面

   -  方案：

      -  统一后端返回：

      ```python
      data2json = dict(
                      type='option',
                      value=option_dict,  # Echarts生成时所需的参数字典
                  )
      return json.dumps(data2json, ensure_ascii=False)
      ```

      ```python
      prompt = '您输入的城市名不符合要求，请重新输入'
      data2json = dict(
      	type='prompt',
          value=prompt,
      )
      return json.dumps(data2json, ensure_ascii=False)
      ```

      -  前端

         ```javascript
         xmlhttp.onreadystatechange = function() {
                         if (this.readyState == 4 && this.status == 200) {
                             var data = JSON.parse(this.responseText);
                             if (data.type == 'option') {
                                 creatEcharts(data.value);
                             }
                             else {
                                 creatPrompt(data.value);
                             }
                         }
                     }
         ```

      -  参考:

         -  [HTML DOM display 属性](www.w3school.com.cn/jsref/prop_style_display.asp)



​      

## 复盘之收获

-  使用浏览器调试JS的经验
   -  浏览器,比如chrome,打开开发者工具
   -  进入`Console` 工具栏内, 这时可以直接输入js代码并执行
   -  进入`Element` 工具栏内, 可以直接修改页面的HTML
   -  以上过程中进行的操作，并不会对保存在文件内的HTML或JS代码产生改变， 仅对于当前情况有效，就好像是生成一个虚拟环境，所有的修改都是在该虚拟环境内进行。在刷新页面后(即向服务器重请求资源后)，一切修改均不复存在
   -  配合以上2个工具,可以快速调试JS代码, 比如使用JS获取输入栏的内容。调试成功后，修改本地文件中对应的JS代码即可。不用每次改HTML和JS代码，然后刷新页面确认JS代码是否生效。



# 170907 4wd4

## 探索 `4.5h`

-  优化前端显示效果 22:00-2:30

   -  bootstrap 兼容移动设备

      -  `Bootstrap3` 一开始就是移动设备友好,使用时需要注意:

         ```html
         <!DOCTYPE html>
         <html lang="zh-CN">
           <head>
             <meta charset="utf-8">
             <meta http-equiv="X-UA-Compatible" content="IE=edge">
             <meta name="viewport" content="width=device-width, initial-scale=1">
             <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
         ```

      -  [Bootstrap-基本模板](http://v3.bootcss.com/getting-started/#template)

      -  [Bootstrap3-移动设备优先](http://v3.bootcss.com/css/#overview-mobile)

      -  关于`meta`标签,找到一篇博客总结得还不错: [html meta标签使用总结](http://blog.csdn.net/h330531987/article/details/70042511)

   -  使用 bootstrap 模板美化 button,input

   -  未来天气预报和历史记录的结果以表格形式显示, 以天气对应的效果图片代替文字,图片采集自心知天气

# 170910 4wd6

## 探索`4.5h`

-  查阅资料完成个人教程中两个坑的入坑出坑记录 4:00-5:30, 22:40-2:20
   -   JS大小写敏感及Atom自动补全
   -   浏览器缓存静态文件


-  css 生效的坑

   ```html
   <style media="screen">
           .top {
               margin-bottom: 10px;
           };
           .prompt {
               width:10%;
               margin-top: 15px;
           };
           .form-margin {
               margin-bottom: 10px !important;
           };
       </style>
   ```

   上面这样是不会生效的, 摸索发现`.top {margin-bottom: 10px; };`最后的`";"`不能加,去掉后就生效

   ```html
   <style media="screen">
           . top {
               margin-bottom: 10px;
           }
   </style>
   ```

   这样也不会生效, `. top` 中的`.` 和`top`之间不能留空格

-  div 居中

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
   <style media="screen">
           . div1 {
               margin:0 auto;
               width:100px; /*需要设置宽高*/
               height:100px;
           }
   </style>
   </head>
   <body>
     <div class="div1">
         <p>段落</p>
     </div>
       <div align="center">
         <p>段落</p>
     </div>
   </body>
   ```

   css控制`margin`和标签内添加`align="center"`两种方式都可以使div居中

   -  第1种效果:

   ![image](https://user-images.githubusercontent.com/26535231/30242849-d77674b6-95d0-11e7-8408-3dd5de54bc6c.png)

   -  第2种效果:

   ![image](https://user-images.githubusercontent.com/26535231/30242853-f1300192-95d0-11e7-876f-e78674141ada.png)

   ​

   ​

## TODO

-  录屏

-  写README

   -  如何安装
   -  学习下jeetchan推荐的生成requirements.txt
   -  如何使用

-  交自己作业(jinja2版和ajax半成品), 个人教程

-  评价5个同学作业

   -  Vwan 使用蓝图,使用装饰器

-  评价楼上同学作业

   ​