<template>
    <div id="login">
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
                    {{password_message}}<input v-model="password" placeholder="嘘~  " @change="input">
                    <CustomButton source="grinningface" size="large" message="!冲呀!"
                                  @click.native="Login"></CustomButton>
                </p>

                <p>
                    <CustomButton source="grinningface" size="large" message="名字写错了"
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
                name_message: 'Welcome back ,    ',
                password_message: '不看不看~',
                name: "",
                password: "",
                check: true
            }
        },
        methods: {
            back_to_main: function () {
                // TODO：获取index.html
                // this.$router.go(-1);
            },
            next_page: function () {
                this.check = false;
            },
            back_to_name: function () {
                this.check = true;
            },
            Login: function () {
                // TODO: 登录传参数+获取home.html
                this.$ajax({
                    method: 'post',
                    url: '/login/',
                    data: {
                        name: this.$parent.name,
                        pass: this.$parent.password,
                        type: 'log'
                    }
                }).then(response => (console.log(response)))
                    .catch(function (error) {
                        console.log(error);
                    })
            },
            input: function () {
                //TODO: 更新输入框长度+store数据存储
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
        src: url('../../assets/fonts/Montserrat-ExtraBold.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    #login_window {
        background-color: mistyrose;
        background-size: cover;
        padding: 0 1% 4.7%;
        font-family: Montserrat-ExtraBold, sans-serif;
        align-items: center;
    }

    header {
        font-family: Montserrat-ExtraBold, monospace;
        text-align: left;
        padding: 20px;
    }

    h1 {
        font-family: Montserrat-ExtraBold, sans-serif;
        padding: 10px 0;
        width: 200px;
        text-align: center;
        border: dotted 10px rosybrown;
    }

    input {
        padding: 0 0 0 30px;
        background: transparent;
        width: 350px;
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
        padding: 10% 10% 10% 18%;
        display: flex;
        align-items: center;
        font-size: 60px;
    }

</style>

<style lang="scss">
    // Allow element/type selectors, because this is global CSS.
    // stylelint-disable selector-max-type, selector-class-pattern

    // Design variables and utilities from src/design.
    @import '../home/design';
</style>