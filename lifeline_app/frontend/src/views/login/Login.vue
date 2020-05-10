<template>
    <div id="login">
        <div id="login_window">
            <header>
                <h1>LifeLine</h1>
            </header>
            <div v-show="check">
                <p class="sec">
                    <svg width="100%" height="100%">
                        <symbol id="s-text">
                            <text text-anchor="middle"
                                  x="50%" y="70%">
                                Welcome back
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
                    <input v-model="name" placeholder="报上名来" style="overflow: visible">
                    <CustomButton v-show="!NameCheck" source="face-screaming-in-fear" size="large" message="输入不正确哦"
                                  type="alert"></CustomButton>
                    <CustomButton v-show="NameCheck" source="zipper-mouth-face" size="large" message="来对暗号=3="
                                  @click.native="next_page"></CustomButton>
                </p>

                <p>
                    <CustomButton source="waving-hand-sign" size="large" message="我要注册:("
                                  @click.native="back_to_main"></CustomButton>
                </p>
            </div>
            <div v-show="!check">
                <p class="sec">
                    {{password_message}}<input v-model="password" type="password" placeholder="交出密码"
                                               style="overflow: visible">
                    <CustomButton v-show="!PassCheck" source="face-screaming-in-fear" size="large" message="输入不正确哦"
                                  type="alert"></CustomButton>
                    <CustomButton v-show="PassCheck" source="heavy-black-heart" size="large" message="!冲呀!"
                                  @click.native="Login"></CustomButton>
                </p>

                <p>
                    <CustomButton source="white-left-pointing-backhand-index" size="large" message="呀名字错了"
                                  @click.native="back_to_name"></CustomButton>
                </p>
            </div>
        </div>
    </div>
</template>

<script>
    import CustomButton from "../../components/CustomButton";

    export default {
        name: "Login",
        components: {
            CustomButton
        },
        data() {
            return {
                //todo: 做动画
                password_message: '不看不看~',
                name: "",
                password: "",
                check: true,
            }
        },
        methods: {
            back_to_main: function () {
                window.location.href = "/";
            },
            next_page: function () {
                this.check = false;
            },
            back_to_name: function () {
                this.check = true;
            },
            submit: function () {
                window.location.href = "/login";
            },
            Login: function () {
                this.$ajax({
                    method: 'post',
                    url: '/login/',
                    params: {
                        name: this.name,
                        pass: this.password,
                        type: 'log'
                    }
                }).then(response => {
                    if (response.data.flag === true) {
                        this.$Notice.success({
                            title: 'Login Successfully!',
                            duration: 2,
                        });
                        setTimeout(() => {
                            window.location.href = "/home"
                        }, 2000);
                    } else {
                        this.$Notice.error({
                            title: 'Error!Try again',
                            duration: 2,
                        });
                        setTimeout(() => {
                            window.location.href = "/home"
                        }, 2000)
                    }
                })
                    .catch(function (error) {
                        console.log(error);
                    })
            }
        },
        watch: {
            check: function (newCheck, oldCheck) {
                console.log(newCheck, oldCheck);
            }
            ,
            name: function (newName, oldName) {
                console.log(newName, oldName);
            }
            ,
            password: function (newPass, oldPass) {
                console.log(newPass, oldPass);
            }
        },
        computed: {
            /**
             * @return {boolean}
             */
            NameCheck: function () {
                return (this.name.length > 3);
            },
            /**
             * @return {boolean}
             */
            PassCheck: function () {
                return (this.password.length > 6);
            }
        }
    }
</script>

<style scoped>
    #login_window {
        background-color: mistyrose;
        background-size: cover;
        padding: 0;
        font-family: Montserrat-ExtraBold;
        align-items: center;
    }

    header {
        font-family: Montserrat-ExtraBold;
        text-align: left;
        padding: 1% 2.5%;
    }

    h1 {
        font-family: Montserrat-ExtraBold;
        padding: 0.8% 0;
        width: 12%;
        text-align: center;
        border: dotted 10px rosybrown;
    }

    input {
        padding: 0 0 0 2%;
        background: transparent;
        width: 55%;
        height: 100px;
        border: 0px;
        outline: #7B7988;
        font-size: 55px;
        font-family: Montserrat-ExtraBold;
        /*TODO: 字体待更换*/
    }

    input::placeholder {
        font-size: 45px;
        font-family: Montserrat-ExtraBold;
    }

    .sec {
        margin: auto;
        padding: 9% 10%;
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
        animation: stroke 6s ease-in-out forwards;
    }

    .text:nth-child(4n+2) {
        stroke: #f39c12;
        text-shadow: 0 0 5px #f39c12;
        animation: stroke1 6s ease-in-out forwards;
    }

    .text:nth-child(4n+3) {
        stroke: #e74c3c;
        text-shadow: 0 0 5px #e74c3c;
        animation: stroke2 6s ease-in-out forwards;
    }

    .text:nth-child(4n+4) {
        stroke: #9b59b6;
        text-shadow: 0 0 5px #9b59b6;
        animation: stroke3 6s ease-in-out forwards;
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
