<template>
    <div id="mainpage">

        <h2> {{course.name}}</h2>
        <u></u>>
        <div v-html="course.description"></div>
        >

    </div>
</template>

<script>
    export default {
        name: "mainpage",
        data() {
            return {
                course: {}
            }
        },

        beforeCreate() {
            this.$ajax.get('get_courseinfo')
                .then(response => {
                    console.log(response.data)
                    this.course = response.data
                })
        }
    }
</script>

<style scoped>

</style>

<!--{-->
<!--          name:'COMP130011.01 算法设计与分析 Algorithm Design and Analysis',-->
<!--          description:'<div class="show-content user_content clearfix enhanced">\n' +-->
<!--                  '  <h1 class="page-title">COMP30011.01 算法设计与分析   （2020春）</h1>\n' +-->
<!--                  '  \n' +-->
<!--                  '    \n' +-->
<!--                  '  \n' +-->
<!--                  '  \n' +-->
<!--                  '    <p><strong>教师</strong>：朱山风&nbsp; （zhusf@fudan.edu.cn)</p>\n' +-->
<!--                  '<p><strong>助教</strong>：游榕晖(<a href="mailto:19210240010@fudan.edu.cn">18110240018@fudan.edu.cn)</a>、马金辰 (<a href="mailto:19210240085@fudan.edu.cn"></a>16307130043<a href="mailto:19210240085@fudan.edu.cn">@fudan.edu.cn</a>&nbsp;主要负责PJ相关事宜)&nbsp;</p>\n' +-->
<!--                  '<p><strong>时间</strong>：</p>\n' +-->
<!--                  '<p class="p1">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 每周四 下午1点30分-4点10分<span class="Apple-converted-space">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </span></p>\n' +-->
<!--                  '<p class="p1">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;周一（双周）下午3点25分-5点05分</p>\n' +-->
<!--                  '<p class="p1">&nbsp;</p>\n' +-->
<!--                  '<p><strong>在线课程</strong>：学堂在线&nbsp; 算法设计与分析</p>\n' +-->
<!--                  '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<a class="external" href="https://next.xuetangx.com/course/THU08091001409/1515822" target="_blank">https://next.xuetangx.com/course/THU08091001409/1515822</a></p>\n' +-->
<!--                  '<p>&nbsp; <strong>教材</strong></p>\n' +-->
<!--                  '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; J. Kleinberg, E. Tardos. Algorithm Design.&nbsp; &nbsp;算法设计 清华大学出版社 2007</p>\n' +-->
<!--                  '<p>&nbsp;</p>\n' +-->
<!--                  '<p><strong>参考书目</strong></p>\n' +-->
<!--                  '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;算法导论 （殷建平等编译，机械工业出版社2013年出版）</p>\n' +-->
<!--                  '<p>&nbsp; <strong style="font-family: sans-serif; font-size: 1rem;">参考课程&nbsp; &nbsp;</strong></p>\n' +-->
<!--                  '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 网易公开课&nbsp; &nbsp; 算法导论</p>\n' +-->
<!--                  '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="http://open.163.com/newview/movie/courseintro?newurl=%2Fspecial%2Fopencourse%2Falgorithms.html" class="external" target="_blank" rel="noreferrer noopener"><span>http://open.163.com/newview/movie/courseintro?newurl=%2Fspecial%2Fopencourse%2Falgorithms.html</span><span aria-hidden="true" class="ui-icon ui-icon-extlink ui-icon-inline" title="链接到外部网站。"></span><span class="screenreader-only">&nbsp;(链接到外部网站。)</span></a></p>\n' +-->
<!--                  '<p>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</p>\n' +-->
<!--                  '  \n' +-->
<!--                  '</div>'-->

<!--        }-->