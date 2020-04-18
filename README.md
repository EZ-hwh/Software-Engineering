# Software-Engineering

 Project for *Software Engineering* 2020 Spring @ Fudan University, by [**Chenran Ning**](< https://github.com/chty627 >) , [**Rui Tian**](<https://github.com/Stephyuka>), [**Shutian Yu**](<https://github.com/ystttttt>) , [**Yushan Liu**](<https://github.com/613lys>) , [**Yixian Du**](<https://github.com/Riki-Du>) and [**Wenhao Huang**](<https://github.com/EZ-hwh>)

## Prerequisites
e.g.

`npm x.x.x`

`node.js x.x.x`

## Build
e.g.

```
cd xx
npm install
...
```

## Feature
e.g.

UPDATE: 新添加了xxx页面，可以实现xxx

## In-progress

e.g.

### [完善文档](https://github.com/EZ-hwh/Software-Engineering/issues/35)

从主页的readme.md维护一个树状的文档，希望有如下功能：

1. 用户可以下载本项目后成功运行
2. 介绍Feature，项目完成情况
3. 公布正在进行的工作
4. 一个良好的开发文档，具有引导新加入开发组的成员快速融入团队进行开发的功能，同时帮助现有members梳理整个开发过程。

问题状态：添加了前后端交互以及后端的部分内容。

...

## 开发文档

如果你想加入本项目的开发组，请阅读以下文档。

### 项目管理
e.g.

使用zenhub的规范，何时添加issue（跳转）

### 前后端交互

前端和后端通过HTTP协议沟通，因此一般会话开始自前端，其请求一个url，同时通过`get`或`post`方式发送一些数据，然后等待后端返回数据或者页面。**[详细文档点击这里](documents/前后端数据交互格式&界面转跳说明.md)。**

前端每个请求均会占用一个不能重复的url，**详细的url使用约定看[这里](documents/url接口.md)。**

当前端返回数据时，一般以json格式储存，因此前后端对于每一个数据请求均要约定一个数据格式。同时后端为了知道哪个前端（哪个用户）在于其对话，会在前端利用`session`储存一些用户个人信息，如登陆状态，购物网站的购物车等。**详细的数据及`session`格式看[这里](documents/数据接口.md)。**


### 前端

### 后端

**[这篇文档](documents/数据库模型.md)拥有数据库模型的ER图以及对其的详细解释。**

### Tools
e.g.

pycharm小技巧（跳转）

vscode好插件（跳转）
