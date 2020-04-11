<template>
    <div id = 'lesson_window'>
        <Layout>
            <header>
                <h1>LifeLine  Lesson</h1>
            </header>
<!--            <div class='books'>-->
            <div class="bg">
                <div class="'button">
                    <CustomButton source="grinningface" size="large" message="back" @click.native="back_to_main"></CustomButton>
                </div>
            </div>
            <div class ='lessons' v-for="item in items">
                <Lessonbook :index="item.index" :number="items.length" :name = "item.curriculum" v-on:click= 'go_to_lesson("item.curriculum")'></Lessonbook>
            </div>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox= "0 0 800 600" width="100%" height="100%">
                <rect id="desk" x = -400 y = 540 width= 1600 height= 100 fill="#a09890"></rect>
            </svg>
<!--            </div>-->
        </Layout>
    </div>
    
</template>

<script>
    import Layout from "../../views/lessons/layouts/main"
    import Lessonbook from "../../components/Lessonbook"
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
                number: 3,
                items:[
                    {curriculum:'算法设计', index:1},
                    {curriculum:'模式识别与机器学习', index:2},
                    {curriculum:'数字信号处理', index:3},
                    {curriculum:'软件工程', index:4},
                    {curriculum:'数据挖掘', index:5},
                    {curriculum:'人工智能',index:6}

                ]
            }
        },
        methods:{
            back_to_main: function () {
                // 回到课程主页
            },
            go_to_lesson:function(name){
                var params ={
                    curriculum: name, //未来最好改成传课程id
                    name:this.$parent.name,
                    type:'jplesson'
                };
                this.$router.go(''); //重定向到课程子页面
            },
            //
            lessons:function() {
                var params = {
                    name: this.$parent.name,
                    type: 'lessons'
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
            }
        },

        created: function(){
            // this.lessons()
            // console.log(this.items)
        },

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
        background-color: #c8e17b;
        background-size: 100% 100%;
        padding: 0 0;
        font-family: Montserrat-ExtraBold, sans-serif;
        bottom:0
    }

    header {
        text-align: left;
        padding: 20px;
        height: 25vh;
    }

    h1 {
        padding: 10px 0;
        width: 200px;
        left: 50px;
        text-align: center;
        font-family: Montserrat-ExtraBold, sans-serif;
        border: dotted 10px yellow;
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

    .bg{
        position:absolute;
        top: 15%;
        right:10%;
    }
    button{
        margin: auto;
        padding: 10% 10% 10% 18%;
        display: flex;
        align-items: center;
        font-size: 60px;

    }

    .lessons{
        background-size: 100% 100%;
        top: 20vh;
        padding: 10% 0% 0% 0%;
        height:50vh;
        width:100vw;
        padding:0 0;
        position: absolute;
        background-color:transparent;
    }

    svg{
        height: 60vh;
        width: 100vw;

    }

    .books{
        background-size: 100% 100%;
        height: 75vh;
        width: 100vw;
        /*position: absolute;*/
        top: 25vh;
        padding: 0 0;
        background-color: #c8e17b;
    }
    p{
        background-size: 100% 100%;
        height: 100vh;
        width: 100vw;

    }

</style>

<style lang="scss">
    // Allow element/type selectors, because this is global CSS.
    // stylelint-disable selector-max-type, selector-class-pattern

    // Design variables and utilities from src/design.
    @import '../../design';
</style>