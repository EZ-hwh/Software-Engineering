<template>
    <div id = 'lesson_window'>
        <Layout>
            <header>
                <svg width="100%" height="100%">
                        <text text-anchor="middle" x="15%" y="20%" class="text text-1">
                            LIFELINE
                        </text>
                        <text text-anchor="middle" x="15%" y="20%" class="text text-2">
                            LIFELINE
                        </text>
                        <text text-anchor="middle" x="15%" y="20%" class="text text-3">
                            LIFELINE
                        </text>
                        <text text-anchor="middle" x="15%" y="20%" class="text text-4">
                            LIFELINE
                        </text>
                </svg>
<!--                <h1>LifeLine  Lesson</h1>-->
            </header>
            <div class ='lessons'>
<!--                <div class="semester" v-if="item.term === page">-->
                    <Lessonbook :lessons="items[number-page].lesson" :number="items[number-page].lesson.length"></Lessonbook>
<!--                </div>-->
                <div class="prev_button" v-if="page > 1">
                     <CustomButton  source="grinningface" size="large" message="prev" @click.native="go_to_prev"></CustomButton>
                </div>
                <div class="next_button" v-if="page < number">
                    <CustomButton  source="grinningface" size="large" message="next" @click.native="go_to_next"></CustomButton>
                </div>
            </div>

        </Layout>
    </div>

</template>

<script>
    import Layout from "../../components/template/TopBarLayout/main"
    import Lessonbook from "./component/Lessonbook"
    import CustomButton from "../../../../frontend/src/components/CustomButton";
    export default {
        name: "Lessons",
        components: {
            Lessonbook,
            CustomButton,
            Layout
        },
        data() {
            return {
                number: 2,
                page:2,
                items:[
                    {term : 2, lesson:[{name:'人工智能', index:1},
                    {name:'模式识别与机器学习', index:2},
                    {name:'数字信号处理', index:3},
                    {name:'软件工程', index:4},
                    {name:'数据挖掘', index:5},
                    {name:'算法设计',index:6}]
                    },
                    {term: 1, lesson:[{name:'数据库', index: 1},
                        {name: '代数结构', index: 2}]
                    }
                ]
            }
        },
        methods:{
            go_to_prev: function(){
                console.log('prev');
                this.page = this.page - 1;
                // window.reload();
            },
            go_to_next:function(){
                console.log('next');
                this.page = this.page + 1;
                // window.reload();
            },
            back_to_main: function () {
                window.location.href = "/home";
                // 回到课程主页
            },
            go_to_lesson:function(){
                window.location.href = "/course";
                // var params ={
                //     curriculum: name, //未来最好改成传课程id
                //     name:this.$parent.name,
                //     type:'jplesson'
                // };
                // this.$router.go(''); //重定向到课程子页面
            },
            //
            lessons:function() {
                var params = {
                    name: this.$parent.name,
                    type: 'lessons'
                };
                this.$ajax.get('/get_semester/', params).then(response => {
                    console.log(response.data.course_table);
                    console.log(response.data.course_table.length);
                    // var obj = JSON.parse(JSON.stringify(response));
                    // console.log(JSON.stringify(obj));
                    this.data.number = response.data.course_table.length;
                    this.data.page = response.data.course_table.length;
                    //TODO：这个部分还有bug 这里console打不出来 但我还不知道咋回事...
                    for (let i = 0; i < this.number; i++) {
                        console.log(response.data.course_table[i]);
                        this.data.items.append(response.data.course_table[i]); //前端接收json加入list
                    }
                }).catch(error => {
                    console.log("something wrong");
                });
            }
        },
        created: function(){
            this.lessons()
            console.log(this.page, this.items)
        },
        mounted:function () {
            console.log(this.page)
        }
    }
</script>


<style scoped>
    @font-face {
        font-family: 'Montserrat-ExtraBold';
        src: url('../../../../frontend/src/assets/fonts/Montserrat-ExtraBold.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }
    #lesson_window {
        background-color: #e7f7a9;
        background-size: 100% 100%;
        padding: 0 0;
        font-family: Montserrat-ExtraBold, sans-serif;
        bottom:0
    }
    header {
        font-size: 80px;
        text-align: left;
        padding: 20px;
        height: 10vh;
    }

    input {
        padding: 0 20px;
        background: transparent;
        width: 300px;
        height: 100px;
        border: 0px;
        outline: #c8e17b;
        font-size: 60px;
        font-family: Montserrat-ExtraBold, sans-serif;
    }
    input::placeholder {
        font-size: 45px;
    }

    button{
        margin: auto;
        padding: 10% 10% 10% 18%;
        display: flex;
        align-items: center;
        font-size: 60px;
        position:absolute;
    }
    .lessons{
        /*background-size: 100% 100%;*/
        /*top: 20vh;*/
        padding: 0% 0% 0% 0%;
        height:60vh;
        width:100%;
        /*position: absolute;*/
        background-color:transparent;
    }
    svg{
        height: 60vh;
        width: 100vw;
    }
    .prev_button{
        padding: 0 0 0 0;
        bottom: 20%;
        left: 15%;
        position: absolute;
        font-size: 60px;
    }
    .next_button{
        padding: 0 0 0 0;
        bottom: 20%;
        right: 15%;
        position: absolute;
        font-size: 60px;
    }
    p{
        background-size: 100% 100%;
        height: 100vh;
        width: 100vw;
    }
    .text {
        /*font-size: 64px;*/
        font-weight: bold;
        text-transform: uppercase;
        fill: none;
        stroke: #3498db;
        stroke-width: 2px;
        stroke-dasharray: 90 310;
        animation: stroke 6s infinite linear;
    }

    .text-1 {
        stroke: #3498db;
        text-shadow: 0 0 5px #3498db;
        animation-delay: -1.5s;
    }

    .text-2 {
        stroke: #f39c12;
        text-shadow: 0 0 5px #f39c12;
        animation-delay: -3s;
    }

    .text-3 {
        stroke: #e74c3c;
        text-shadow: 0 0 5px #e74c3c;
        animation-delay: -4.5s;
    }

    .text-4 {
        stroke: #9b59b6;
        text-shadow: 0 0 5px #9b59b6;
        animation-delay: -6s;
    }

    @keyframes stroke {
        100% {
            stroke-dashoffset: -400;
        }
    }

</style>

<style lang="scss">
    // Allow element/type selectors, because this is global CSS.
    // stylelint-disable selector-max-type, selector-class-pattern

    // Design variables and utilities from src/TopBarDesign.
    @import '../../assets/css/TopBarDesign';
</style>