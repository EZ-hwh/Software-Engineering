# Life Line 首页

使用vue搭建的前端：

## 环境配置

- 需要安装node.js/npm/yarn
- 前两个之前tr已经放上去了的；主要是yarn需要安装
- https://yarnpkg.com/lang/en/docs/install
- 网址点进去之后会叫你先安装Chocolatey，再安装yarn，配置环境不难

## 运行

```bash

# 1. Open command line and go to this folder

# 2. Install dependencies. Make sure yarn is installed: https://yarnpkg.com/lang/en/docs/install
yarn install

# 3. Run following command to start the development server
yarn dev
```

- yarn install 会安装npm的所有依赖包在文件"node_modules"里
- 注意install过程中在link dependency之后的一个步骤中出现很多waiting项的话可以手动"ctrl+c"多次把它结束掉，我也不知道为啥等了很久就是没装完，事实证明后面的也不太重要。
- 如果之后yarn dev报错再重新回来装yarn install.
- 用yarn dev运行编译需要一会儿，再打开local地址即可
- <img src="C:\Users\61082\AppData\Roaming\Typora\typora-user-images\image-20200401123058952.png" alt="image-20200401123058952" style="zoom:67%;" />

## 结构

```
-public
	index.html
-src
	assets
	components
	design
	router
	state
	utils
-tests
```

其中public存放了网址html的模板，不太重要（可以先看看），tests完全不用管，编译用的

src里重点看components

这个里面就是组件库了，包括很多头、尾部、日历、待办事宜等组件

- 如果编写网页就在这里面写组件，最后组装起来。
- index.html的结构就是用了一个大组件app.vue，app.vue又是用了src/router/views/home.vue
- （这个路由我还没搞懂为什么这么做）
- home.vue又将几个小组件组装起来了，这个得看看！
- 注意后面使用的时候上栏和尾部的组件，只需要<layout>就行，在home.vue里面有；你可以注释掉它看看效果是哪里就行，vue是实时渲染
- 这里面有很多文件我不知道是干啥用的，也没有删除特别干净

### vue文件的结构

```js
<script>
    import 组件 from 'xxxx'
export default{
    \\导出子组件
    components{xxx,xxx}\\包括要用的子组件
    \\操作
}
</script>
<template>
    html+组件
</template>
```

推荐看看`src/components`中的各个组件，比如`footer`最简单；`toDoList.vue`是我自己模仿写了，可以把你们需要用的js和json放进去，import一下就行。

