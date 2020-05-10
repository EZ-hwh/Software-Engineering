<template>
    <div>
        <div id="register_window">
            <header>
                <h1>LifeLine</h1>
            </header>
            <div v-show="check===1">
                <div class="sec">
                    <svg width="100%" height="100%">
                        <symbol id="s-text">
                            <text text-anchor="middle"
                                  x="50%" y="70%">
                                Nice to meet you
                            </text>
                        </symbol>
                        <use xlink:href="#s-text" class="text"
                        ></use>
                        <use xlink:href="#s-text" class="text"
                        ></use>
                        <use xlink:href="#s-text" class="text"
                        ></use>
                        <use xlink:href="#s-text" class="text"
                        ></use>
                    </svg>
                    <div>
                        <Poptip trigger="focus">
                            <input v-model="name" placeholder="Your name?" type="text" maxlength="11"
                                   style="padding-top: 4%">
                            <div slot="content">{{ name }}</div>
                        </Poptip>
                        <p class="tip" v-bind:style="NameLengthStyle">不可以少于4个字符，也不能超过11个字符哦！</p>
                        <p class="tip" v-bind:style="NameCheckStyle">只能由汉字、字母、数字、下划线组成哦！</p>
                    </div>
                    <CustomButton v-show="!(NameCheck&&NameLength)" source="face-screaming-in-fear" size="large"
                                  type="alert" message="输入不正确哦"
                    ></CustomButton>
                    <CustomButton v-show="NameCheck&&NameLength" source="face-throwing-a-kiss" size="large"
                                  message="验证邮箱"
                                  @click.native="next_page"></CustomButton>
                </div>

                <p>
                    <CustomButton source="waving-hand-sign" size="large" message="我走错了:("
                                  @click.native="back_to_main"></CustomButton>
                </p>
            </div>
            <div v-show="check===2">
                <div class="sec2">
                    <img src="../../assets/images/button/closed-mailbox-with-raised-flag.png" class="pic">
                    <div>
                        <input v-model="email" placeholder="Your email?" type="text" style="padding-left: 5%">
                        <p class="tip" v-show="!EmailCheck" style="color: salmon">邮箱格式不对哦！</p>
                    </div>
                    <CustomButton v-show="!EmailCheck" source="face-screaming-in-fear" size="large"
                                  type="alert" message="输入不正确哦"
                    ></CustomButton>
                    <CustomButton v-show="EmailCheck" source="winking-face" size="large" message="给我码"
                                  @click.native="next_page"></CustomButton>
                </div>
                <CustomButton source="white-left-pointing-backhand-index" size="large" message="想换名字QAQ"
                              @click.native="back"></CustomButton>
            </div>
            <div v-show="check===3">
                <div class="sec2">
                    <img src="../../assets/images/button/open-mailbox-with-raised-flag.png" class="pic">
                    <input id="codeInput" v-model="code" placeholder="code?" type="text" style="padding-left: 5%">
                    <CustomButton source="zipper-mouth-face" size="large" message="设置暗号"
                                  @click.native="next_page"></CustomButton>
                </div>
                <CustomButton source="white-left-pointing-backhand-index" size="large" message="邮箱搞错liao"
                              @click.native="back"></CustomButton>
            </div>
            <div v-show="check===4">
                <div class="sec2" style="padding-bottom: 4%">
                    <img v-show="!InputFocus" src="../../assets/images/button/hear-no-evil-monkey.png" class="pic" style="padding-right: 6%">
                    <img v-show="InputFocus" src="../../assets/images/button/see-no-evil-monkey.png" class="pic" style="padding-right: 6%">
                    <div id="pass_input">
                        <p><input v-model="password" type="password" placeholder="嘘~" @blur="Nfocus" @focus="Yfocus"></p>
                        <p class="tip" v-bind:style="PassNumberStyle">要超过6个字符哦</p>
                        <p class="tip" v-bind:style="PassCheckStyle">由大小写字母、下划线和数字组成哦，而且至少要有一个大写字母哦！</p>
                        <p><input v-model="password_again" type="password" placeholder="再嘘~" @blur="Nfocus" @focus="Yfocus"></p>
                        <p class="tip" v-bind:style="PassAgainStyle">要跟第一遍一模一样哦</p>
                    </div>
                    <CustomButton v-show="!(PassNumber&&PassCheck&&PassAgain)" source="face-screaming-in-fear" size="large"
                                  type="alert" message="输入不正确哦"
                    ></CustomButton>
                    <CustomButton v-show="PassNumber&&PassCheck&&PassAgain" source="heavy-black-heart" size="large" message="!冲呀!"
                                  @click.native="Register"></CustomButton>
                </div>
                <p>
                    <CustomButton source="face-with-rolling-eyes" size="large" message="唔返回主页"
                                  @click.native="back_to_main"></CustomButton>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
    import CustomButton from "../../components/CustomButton";

    export default {
        name: "Register",
        components: {
            CustomButton
        },
        data() {
            return {
                password_message: '不看不看',
                name: "",
                password: "",
                email: "",
                code: "",
                password_again: "",
                check: 1,
                response: null,
                InputFocus: false,
            }
        },
        methods: {
            back_to_main: function () {
                window.location.href = "/";
                // this.$router.go(-1);
            },
            next_page: function () {
                this.check += 1;
            },
            get_email: function () {
                this.$ajax({
                    method: 'post',
                    url: '/getcode/',
                    params: {
                        email: this.email,
                        type: 'code',
                        contentType: 'application/json',
                        dataType: 'json',
                    }
                }).then(response => {
                    if (response.data.flag === true) {
                        this.$Notice.success({
                            title: 'Send Successfully!',
                            duration: 2,
                        });
                        console.log(response.data.ret);
                        setTimeout(this.next_page, 2000);
                    } else {
                        this.$Notice.error({
                            title: 'Error!Try again!',
                            duration: 2,
                        });
                        console.log(response.data.error_msg);
                    }
                })
            },
            check_code: function () {
                this.$ajax({
                    method: 'post',
                    url: '/checkcode/',
                    params: {
                        email: this.email,
                        code: this.code,
                        type: 'code',
                        contentType: 'application/json',
                        dataType: 'json',
                    }
                }).then(response => {
                    if (response.data.flag === true) {
                        this.$Notice.success({
                            title: 'Right Code!',
                            duration: 2,
                        });
                        setTimeout(this.next_page, 2000);
                    } else {
                        this.$Notice.error({
                            title: 'Wrong!Try again!',
                            duration: 2,
                        });
                        console.log(response.data.error_msg);
                    }
                })
            },
            back: function () {
                this.check -= 1;
            },
            Register: function () {
                this.$ajax({
                    // TODO:
                    method: 'post',
                    url: '/register/',
                    params: {
                        name: this.name,
                        pass: this.password,
                        email: this.email,
                        type: 'reg',
                        contentType: 'application/json',
                        dataType: 'json',
                    }
                }).then(response => {
                    if (response.data.flag === true) {
                        this.$Notice.success({
                            title: 'Register Successfully!',
                            duration: 2,
                        });
                        setTimeout(() => {
                            window.location.href = "/login"
                        }, 2000);
                    } else {
                        this.$Notice.error({
                            title: 'Error!Try again!',
                            duration: 2,
                        });
                        setTimeout(() => {
                            window.location.href = "/register"
                        }, 2000)
                        console.log(response.data.error_msg);
                    }
                })
                    .catch(function (error) {
                            console.log(error);
                        }
                    )
            },
            Yfocus: function(){
                console.log("YES");
                this.InputFocus=true;
            },
            Nfocus: function(){
                console.log("NO");
                this.InputFocus=false;
            },
        }
        ,
        watch: {
            check: function (newCheck, oldCheck) {
                console.log(newCheck, oldCheck);
            }
        },
        computed: {
            /**
             * @return {boolean}
             */
            NameCheck: function () {
                const regu = "^[_0-9a-zA-Z\u4e00-\u9fa5]+$";
                const re = new RegExp(regu);
                return re.test(this.name) && this.name.length > 3;
            },
            NameCheckStyle: function () {
                if (this.NameCheck) return {color: "grey"};
                else return {color: "salmon"};
            },
            /**
             * @return {boolean}
             */
            NameLength: function(){
                return this.name.length >3;
            },
            NameLengthStyle: function(){
                if(this.NameLength) return {color: "grey"};
                else return {color: "salmon"};
            },
            /**
             * @return {boolean}
             */
            EmailCheck: function () {
                const regu = "^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\\.[a-zA-Z0-9_-]+)+$";
                const re = new RegExp(regu);
                return re.test(this.email);
            },
            /**
             * @return {boolean}
             */
            PassNumber: function() {
                return this.password.length > 6;
            },
            PassNumberStyle: function(){
                if(this.PassNumber) return {color:"grey"};
                else return {color:"salmon"};
            },
            /**
             * @return {boolean}
             */
            PassCheck: function () {
                const regu1 = "^[_0-9a-zA-Z]+$";
                const regu2 = "[A-Z]";
                const re1 = new RegExp(regu1);
                const re2 = new RegExp(regu2);
                return re1.test(this.password) && re2.test(this.password);
            },
            PassCheckStyle: function(){
                if(this.PassCheck) return {color:"grey"};
                else return {color:"salmon"};
            },
            /**
             * @return {boolean}
             */
            PassAgain: function () {
                return this.password===this.password_again;
            },
            PassAgainStyle: function () {
                if(this.PassAgain) return {color:"grey"};
                else return {color:"salmon"};
            }
        }
    }
</script>

<style scoped>
    #register_window {
        background-color: aliceblue;
        background-size: cover;
        padding: 0 1% 4.7%;
        font-family: Montserrat-ExtraBold, sans-serif;
        align-items: center;
    }

    header {
        font-family: Montserrat-ExtraBold, monospace;
        text-align: left;
        padding: 1% 2.5%;
    }

    h1 {
        font-family: Montserrat-ExtraBold;
        padding: 0.8% 0;
        width: 12%;
        text-align: center;
        border: dotted 10px lightskyblue;
    }

    input {
        padding: 0 0 0 2%;
        background: transparent;
        width: 100%;
        height: 100px;
        border: 0px;
        outline: #7B7988;
        font-size: 55px;
        font-family: Montserrat-ExtraBold, sans-serif;
    }

    input::placeholder {
        font-size: 45px;
    }

    .tip {
        padding: 0 4%;
        font-size: 20%;
        color: grey;
    }

    .pic {
        zoom: 75%;
    }

    .sec {
        margin: auto;
        padding: 9% 5%;
        display: flex;
        align-items: center;
        font-size: 4.5em;
    }

    .sec2 {
        margin: auto;
        padding: 7% 10%;
        display: flex;
        align-items: center;
        font-size: 4.5em;
    }

    .text {
        font-weight: bold;
        text-transform: uppercase;
        fill: none;
        stroke: #3498db;
        stroke-width: 2px;
        stroke-dasharray: 0 350;
        stroke-dashoffset: 0;
    }

    .text:nth-child(4n+1) {
        stroke: #3498db;
        text-shadow: 0 0 5px #3498db;
        animation: stroke 4s ease-in-out forwards;
    }

    .text:nth-child(4n+2) {
        stroke: #f39c12;
        text-shadow: 0 0 5px #f39c12;
        animation: stroke1 4s ease-in-out forwards;
    }

    .text:nth-child(4n+3) {
        stroke: #e74c3c;
        text-shadow: 0 0 5px #e74c3c;
        animation: stroke2 4s ease-in-out forwards;
    }

    .text:nth-child(4n+4) {
        stroke: #9b59b6;
        text-shadow: 0 0 5px #9b59b6;
        animation: stroke3 4s ease-in-out forwards;
    }

    @keyframes stroke {
        100% {
            stroke-dashoffset: 0;
            stroke-dasharray: 80 240;
        }
    }

    @keyframes stroke1 {
        100% {
            stroke-dashoffset: 90;
            stroke-dasharray: 80 240;
        }
    }

    @keyframes stroke2 {
        100% {
            stroke-dashoffset: 180;
            stroke-dasharray: 80 240;
        }
    }

    @keyframes stroke3 {
        100% {
            stroke-dashoffset: 270;
            stroke-dasharray: 80 240;
        }
    }


</style>
