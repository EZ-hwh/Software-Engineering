const IS_PROD = ["production", "prod"].includes(process.env.NODE_ENV);
const webpack = require("webpack");

module.exports = {
  publicPath: IS_PROD ? process.env.VUE_APP_PUBLIC_PATH : "./", // 默认'/'，部署应用包时的基本 URL
  // outputDir: process.env.outputDir || 'dist', // 'dist', 生产环境构建文件的目录
  // assetsDir: "", // 相对于outputDir的静态资源(js、css、img、fonts)目录
  assetsDir: "static",
  lintOnSave: false,
  runtimeCompiler: true, // 是否使用包含运行时编译器的 Vue 构建版本
  productionSourceMap: !IS_PROD, // 生产环境的 source map
  parallel: require("os").cpus().length > 1,
  pwa: {},
  pages: {
    index: {
      entry: "src/views/first/main.js",
      template: "public/index.html",
      filename: "index.html",
      chunks: ["chunk-vendors", "chunk-common", "index"],
    },
    login: {
      entry: "src/views/login/main.js",
      template: "public/login.html",
      filename: "login.html",
      chunks: ["chunk-vendors", "chunk-common", "login"],
    },
    register: {
      entry: "src/views/register/main.js",
      template: "public/register.html",
      filename: "register.html",
      chunks: ["chunk-vendors", "chunk-common", "register"],
    },
    home: {
      entry: "src/views/home/main.js",
      template: "public/home.html",
      filename: "home.html",
      chunks: ["chunk-vendors", "chunk-common", "home"],
    },
    SingleCourse: {
      entry: "src/views/SingleCourse/main.js",
      template: "public/SingleCourse.html",
      filename: "SingleCourse.html",
      chunks: ["chunk-vendors", "chunk-common", "SingleCourse"],
    },
    lessons: {
      entry: "src/views/lessons/main.js",
      template: "public/lessons.html",
      filename: "lessons.html",
      chunks: ["chunk-vendors", "chunk-common", "lessons"],
    },
  },
  configureWebpack: {
    plugins: [
      new webpack.ProvidePlugin({
        $: "jquery",
        jQuery: "jquery",
        "window.jQuery": "jquery",
      }),
    ],
  },
  // devServer: {
  //     index: '/', // 运行时，默认打开application1页面
  //     // 告诉dev-server在服务器启动后打开浏览器，将其设置true为打开默认浏览器
  //     open: true,
  //     host: 'localhost',
  //     port: 8080,
  //     https: false,
  //     hotOnly: false,
  //     // 配置首页 入口链接
  //     before: app => {
  //         app.get('/', (req, res, next) => {
  //             for (let i in pages) {
  //                 res.write(`<a target="_self" href="/${i}">/${i}</a></br>`);
  //             }
  //             res.end()
  //         });
  //     }
  // }
};
