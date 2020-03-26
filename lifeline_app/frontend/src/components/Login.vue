<template>
    <div id="login_window">
        <header>
            <h1>LifeLine</h1>
        </header>
        <div v-show="check">
            <p class="sec">
                {{ name_message }}<input v-model="name" placeholder="Your name?" @change="input">
                <CustomButton source="grinningface" size="large" message="来对暗号=3="
                              @click.native="next_page"></CustomButton>
            </p>

            <p>
                <CustomButton source="grinningface" size="large" message="我走错了:("
                              @click.native="back_to_main"></CustomButton>
            </p>
        </div>
        <div v-show="!check">
            <p class="sec">
                {{password_message}}<input v-model="password" placeholder="嘘~" @change="input">
                <CustomButton source="grinningface" size="large" message="冲呀！"
                              @click.native="Login"></CustomButton>
            </p>

            <p>
                <CustomButton source="grinningface" size="large" message="名字写错了" @click.native="back_to_name"></CustomButton>
            </p>

        </div>
    </div>
</template>

<script>
    import CustomButton from "./CustomButton";

    export default {
        name: "Login",
        components: {
            CustomButton
        },
        data() {
            return {
                name_message: 'Welcome back ,    ',
                password_message: '这里想放一个类似哔哩哔哩那个输密码会捂脸的那个',
                name: "",
                password: "",
                check: true
            }
        },
        methods: {
            back_to_main: function () {
                this.$parent.display = 1;
            },
            next_page: function () {
                this.check = false;
            },
            back_to_name: function () {
                this.check = true;
            },
            Login: function () {
                //TODO:  登录传参
            },
            input: function () {
                if (this.check === true) {
                    this.$parent.name = this.name;
                } else this.$parent.password = this.password;
                //TODO: 更新输入框长度
            }
        },
        watch: {
            check: function (newCheck, oldCheck) {
                console.log(newCheck, oldCheck);
            },
            name: function (newName, oldName) {
                console.log(newName, oldName);
            },
            password: function (newPass, oldPass) {
                console.log(newPass, oldPass);
            }
        }
    }
</script>

<style scoped>
    @font-face {
        font-family: 'Montserrat-ExtraBold';
        src: url('../assets/font/Montserrat-ExtraBold.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    #login_window {
        background-color: mistyrose;
        padding: 0 0;
        width: 100%;
        height: 100%;
        font-family: Montserrat-ExtraBold, sans-serif;
    }

    header {
        text-align: left;
        padding: 20px;
    }

    h1 {
        padding: 10px 0;
        width: 200px;
        text-align: center;
        border: dotted 10px rosybrown;
    }

    input {
        padding: 0 20px;
        background: transparent;
        width: 300px;
        height: 100px;
        border: 0px;
        outline: #7B7988;
        font-size: 60px;
        font-family: Montserrat-ExtraBold, sans-serif;
    }

    input::placeholder {
        font-size: 45px;
    }

    .sec {
        margin: auto;
        width: 80%;
        padding: 10% 15%;
        display: flex;
        align-items: center;
        font-size: 60px;
    }

</style>