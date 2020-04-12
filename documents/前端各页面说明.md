# frontend

## 环境配置

### 安装需要的包

```
npm install
```

​		`package.json`是新的，应该用`npm  install`就可以安装好新的包。如果不能运行且出现之前没有install会出现的错误提示的话，试一下单独安装以下几个包（正常来说应该用不到）

```
npm install vue bootstrap-vue bootstrap
npm install sass-loader -D
npm install node-sass -D / cnpm install node-sass -D
npm install vue-perfect-scrollbar
```

## 运行

### 开发前端测试

```
npm run serve //在frontend文件夹下
```

### 打包生成`dist`文件夹
```
npm run build //在frontend文件夹下
```

### 前后端交互测试

```
python manage.py runserver //在项目文件夹下 需要先做上一步打包
```

## 前后端接口

​		利用`axios`实现的前后端交互，基本来说就是利用它从前端往某一个后端的`url`发送一个get或者post的http包，然后再获得后端回复的包。

​		这里的`url`采用的是base+函数自定义部分来实现的，在`frontend/src/main.js`中设置了base。

```javascript
axios.defaults.baseURL='http://127.0.0.1:8000/';
```



### 登录

​		在`frontend/src/views/Login.vue`中设置了点击登录的按钮（就是那个写了冲啊的按钮），会向后端发送一个get的http包。

```javascript
Login: function () {
    //TODO:  登录传参
    this.$ajax({
        method: 'get',
        url: '/', //这里发送到http://127.0.0.1:8000/
        params:{  //传递的参数如下：
            name: this.$parent.name,
            pass: this.$parent.password,
            type: 'log'
       }
    }).then(response => (this.$router.push({path: '/UserHome/' + this.$parent.name}))) 
    	//这个then就是用来处理后端回复的包的
    .catch(function (error) {
    	console.log(error);
    })
}
```

### 注册

​		在`frontend/src/views/Register.vue`中设置了点击注册的按钮（就是那个写了冲啊的按钮），会向后端发送一个get的http包。

```javascript
Register: function () {
    //    TODO: 注册传参数
    this.$ajax({
        method: 'get',
        url: '/', //这里发送到http://127.0.0.1:8000/
        params:{  //传递的参数如下：
            name: this.$parent.name,
            pass: this.$parent.password,
            type: 'reg'
       }
    }).then(response => (this.$router.push({path: '/UserHome/' + this.$parent.name})))
    	//这个then就是用来处理后端回复的包的
    .catch(function (error) {
    	console.log(error);
    })
}
```

---

​		现在设置的是点击按钮之后收到回复就会直接跳转到home界面，对回复的包没有任何处理，之前有测试过包发送到后端之后因为`url`设置的是主页面的`url`所以会直接返回`index.html`的完整代码，但是如果设置成非主页面`url`的话就会404。

​		登录和注册不需要返回什么内容，我这边只需要返回一个确定是否登录或注册成功即可，用户名和密码等参数都保存在`app.vue`定义的一个实例里面，所以我可以直接读取，至于主界面需要的数据可能需要主界面在创建的时候再向后端发送一个get的包，然后返回`json`文件（这里需要ncr来做一下接口）

---

###课程主页

- 添加了 views/lessons.vue 以及 components/Lessonbook.vue

  - 在 lessons.vue中有两个接口：

    1. 加载页面时后端传入json参数 `{curriculums: string 类型; index: integer 类型}`

       ```javascript
     lessons:function() {
                       var params = {
                           name: this.$parent.name,
                           type: 'lesson'
                       };
                       this.$ajax.get('/', params).then(res => {
                           var obj = JSON.parse(JSON.stringify());
                           console.log(JSON.stringify(jsonObj));
                           this.data.number = obj.length;
                           for (var i = 0; i < obj.length; i++) {
                               this.data.items.append({curriculum: jsonobj[i], index: i + 1}); //前端接收json加入list
                           }
                       }).catch(error => {
                           console.log(error.response.data.code)
                       });
       ```
    
    2. 点击课程名称，可以跳转至相关的课程主页。这个url的参数现在传的是课程的名称和用户名，但后续可以改成id。更方便一些。
    
       ```javascript
       go_to_lesson:function(name){
                       var params ={
                           curriculum: name, //未来最好改成传课程id
                           name:this.$parent.name,
                           type:'jplesson'
                       };
                       this.$router.go(''); //重定向到课程子页面
                   },
       ```
    
       

- 之前配置了routers，但听说routers不用了，我就没有改其他文件，目前没有把它和其他页面串连在一起

