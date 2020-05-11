# Software-Engineering

 Project for *Software Engineering* 2020 Spring @ Fudan University, by [**Chenran Ning**](< https://github.com/chty627 >) , [**Rui Tian**](<https://github.com/Stephyuka>), [**Shutian Yu**](<https://github.com/ystttttt>) , [**Yushan Liu**](<https://github.com/613lys>) , [**Yixian Du**](<https://github.com/Riki-Du>) and [**Wenhao Huang**](<https://github.com/EZ-hwh>)



## Prerequisites

### 本地

- 我们的项目使用 `Vue.js` 和 `django`作为开发框架。因此，在使用/开发我们的网页前，需要确保它们已经安装成功（同时应确保 `npm` 安装完成)。

- 我们使用的脚手架版本号为`vue-cli:4.2.3`，django 版本号为`3.0.4`（我们的建议是：你的脚手架和django的版本号不要低于低于我们的版本）

- 获取我们项目的代码

  ```shell
  git clone
  cd lifeline_app
  ```

### 服务器

- 项目暂时还未部署，现阶段仅支持本地运行



## Build

- 确保满足prerequisites后，在命令行输入以下命令，随后可以运行项目：

  ```shell
  cd frontend
  npm install
  npm run-script build
  python manage.py migrate
  python manage.py runserver
  ```

- 若正常运行，则终端返回默认本机地址：`127.0.0.1:8080`，在浏览器中输入后即可访问我们的网页



## Feature

*此前的开发工作中缺乏规范的issue记录，有一些数据可能不够准确，在之后的工作中请及时更新自己的issue*

- **3.23 Update** 搭建vue.js + django 框架，见[框架说明](documents/项目框架.md)
- **3.26 Update** 添加登陆注册页面
- **3.30 Update** 创建数据库模型，支持前端渲染，设计Spring1所需的数据库模型，包括表，表之间的联系等。
- **4.01 Update** 添加主页页面，支持前端默认参数渲染
- **4.02 Update** 添加课程主页，支持前端默认渲染
- **4.02 Update** 添加课程子页面，支持首页/作业/文件三个板块渲染
- **4.03 Update** 后端支持登陆注册逻辑，可支持登陆注册基于数据库验证。
- **4.04 Update** 前端框架完成整合，所有页面可以在同一个框架下渲染
- **4.06 Update** 创建数据接口文档，实现后端链接并支持前端页面跳转
- **4.18 Update** 完成第一阶段前后端框架整理



## In-progress

*本板块有待完善，在新建立 issue 后，请及时将其内容更新到 in-progress板块并保持对问题状态的更新，对于已经 close 的 issue，请及时移除并将完成的功能更新至 feature 板块*


### 完善文档

【[**issue**](https://github.com/EZ-hwh/Software-Engineering/issues/35)】从主页的readme.md维护一个树状的文档，希望有如下功能：

1. 用户可以下载本项目后成功运行
2. 介绍Feature，项目完成情况
3. 公布正在进行的工作
4. 一个良好的开发文档，具有引导新加入开发组的成员快速融入团队进行开发的功能，同时帮助现有members梳理整个开发过程。

**问题状态**：需要帮助，完成urls信息。


### 前端总体设计美化

【[**issue**](https://github.com/EZ-hwh/Software-Engineering/issues/36)】解决前端不同网页设计风格不同的问题，改进的目标是：

1. 保留主页和课程子页面的`css`风格
2. 调整登陆注册/课程主页组件的颜色

**问题状态**：进行中


### 课程页面数据接口

【[**issue**](https://github.com/EZ-hwh/Software-Engineering/issues/42)】课程页面传参接口，包括：

1. mainpage页面，显示课程名称和描述
2. document页面，显示课程的文件
3. homework页面，显示课程作业

**问题状态**：起草了接口，需要讨论。


## Development Documents

*如果你想加入本项目的开发组，请阅读以下文档。*



### 项目管理

- 加入我们的[项目仓库](https://github.com/EZ-hwh/Software-Engineering)
- 按照[合作开发流程指南](documents/开发流程.md)更新自己的开发工作
  - 在将自己分支的代码 merge 到 master branch 时，需要提交 `pull request`，其它小组成员可以添加`review`，在确认提交代码正确性后，可以 `merge pull request`
- 学习使用zenhub，**按照[zenhub使用指南](documents/zenhub指南.md)添加/处理issue**。
  - 确保及时更新自己的issue
- **文档维护**
  - 记录自己开发过程中的技术细节和问题解决方案。将文档更新在master branch的`/documents/`文件夹下。文档更新无需 `pull request`。
  - 新建文档时，文档命名需简略、清晰概括文档主要内容。如有必要，请及时更新主页的 `readme.md`， 文档的组织结构为树状结构。



### 前后端交互

- 前端和后端通过HTTP协议沟通，因此一般会话开始自前端，其请求一个url，同时通过`get`或`post`方式发送一些数据，然后等待后端返回数据或者页面。**详见[交互的格式/界面跳转说明](documents/前后端数据交互格式&界面转跳说明.md)。**

- 前端每个请求均会占用一个不能重复的url，**详见[url使用约定](documents/url接口.md)。**

- 当前端返回数据时，一般以json格式储存，因此前后端对于每一个数据请求均要约定一个数据格式。同时后端为了知道哪个前端（哪个用户）在于其对话，会在前端利用`session`储存一些用户个人信息，如登陆状态，购物网站的购物车等。**详见[数据接口说明文档](documents/数据接口.md)。**



### 前端

#### 前端框架

- 在设计自己的网页时，**请保证你的前端组织结构符合团队框架规范，以便于合并前端所有文件，详见[前端框架说明](documents/前端结构文档.md)**。



#### 登陆/注册页面

- 加载网页后的第一个页面vue文件在`frontend/src/views/first`下，该网页可以跳转至登陆/注册界面。
- 登陆页面的vue文件在`frontend/src/views/login`下。
- 注册页面的vue文件在`frontend/src/views/register`下。
- **登陆注册页面的传参说明详见[前端页面说明](documents/前端各页面说明.md)中的登陆/注册部分。**
- 页面功能说明
  - 目前支持的功能有
    - 输入用户名/密码注册账户
    - 输入用户名/密码登陆账户
  - 有待添加的功能有：
    - 使用验证码验证登陆
    - 密码加密处理



#### 主页

- 主页的vue文件在`frontend/src/views/home`下。

- 前端主页设计部分，使用了模版`Adminto`，`Adminto`是一个后台管理模版主题的前端框架UI，内有vue框架和各种html小组件，基于此可以开发发有特定主题的前端。
- **在开发过程中请注意**：**尽量使用模版，以便于设计的统一**。
- `Adminto`的使用方法跟本此项目略有不同，需要区分Adminto和本项目的文件管理：
  - 在adminto中有html的各个板块和vue/react等不同框架，只需要关注文件夹html和vue。html文件夹内使用了light vertical的设计，可以直接在dist文件夹中index.html中进入主页查看。需要某个部件时，直接将html的代码复制进入.vue文件中的<template>板块中，或者建立新的部件（如果有传参建议新建部件）。
  - component/home.vue是主页的显示部分。查看其中的html template可以看到<layout>部分，这个是页面的顶部和底部的两栏，需要时可以按同样方法接进去。
    component/calendar.vue和todolist.vue是主页的小部件，传参时需要通过这些文件进行。
  - **如何安装`Adminto`详见[前端模版说明](documents/前端模版.md)。**



#### 课程主页

- 课程主页的vue文件在`frontend/src/views/lessons`下。
- 网页设计主要使用`svg`，在后端传入数据之后可以相应地加载全部课程，**详见[前端页面说明](documents/前端各页面说明.md)中的课程主页部分。**
- 页面功能说明
  - 目前支持的功能有：
    - 可根据传入参数显示最多10门课程
  - 有待添加的功能有：
    - 课程预览时的动态效果
    - 根据学期分类对课程进行展示



#### 课程页面

- 课程页面的vue文件在`frontend/src/views/SingleCourse`下。
- **课程页面的技术细节详见[前端页面说明](documents/前端各页面说明.md)中的课程页面部分。**
- 页面功能说明
  - 主页：介绍课程内容和教师组织结构
  - 文件：发放PPT/作业
  - 作业：同学提交作业



### 后端

- **数据库模型**：我们现阶段的模型可由**ER图**描述如下，详见[数据库模型文档](documents/数据库模型.md)

  <img src="./documents/png/ER.jpg" style="zoom:60%;" />



### Reference & Tips
*以下是开发过程中参考的blog和开发成员自己写的tips*

- [pycharm小技巧](https://www.zhihu.com/question/37787004)

- [svg动画效果实例教程](https://www.html5tricks.com/18-svg-animations.html)



### 会议记录

- **Sprint1会议**：[会议记录](documents/Sprint1会议.md)



### 开发感想

 [Yixian Du](documents/工作记录-Du.md) 





