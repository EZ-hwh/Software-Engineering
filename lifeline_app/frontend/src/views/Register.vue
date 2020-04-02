<template>
    <div id="register_window">
        <header>
            <h1>LifeLine</h1>
        </header>
        <div v-show="check">
            <p class="sec">
                {{ name_message }}<input v-model="name" placeholder="Your name?" @change="input">
                <CustomButton source="grinningface" size="large" message="设置暗号=3="
                              @click.native="next_page"></CustomButton>
            </p>
            <p>
                <CustomButton source="grinningface" size="large" message="我走错了:("
                              @click.native="back_to_main"></CustomButton>
            </p>
        </div>
        <div v-show="!check">
            <div class="sec2">
                {{password_message}}
                <div id="pass_input">
                    <p><input v-model="password" placeholder="嘘~" @change="input"></p>
                    <p><input v-model="password_again" placeholder="再嘘~" @change="input"></p>
                </div>
                <CustomButton source="grinningface" size="large" message="!冲呀!"
                              @click.native="Register"></CustomButton>
            </div>
            <p>
                <CustomButton source="grinningface" size="large" message="名字写错了" @click.native="back_to_name"></CustomButton>
            </p>
        </div>
    </div>
</template>

<script>
    import CustomButton from "../components/CustomButton";

    export default {
        name: "Register",
        components: {
            CustomButton
        },
        data() {
            return {
                name_message: 'Nice to meet you, ',
                password_message: '不看不看',
                name: "",
                password: "",
                password_again: "",
                check: true
            }
        },
        methods: {
            back_to_main: function () {
                this.$router.go(-1);
            },
            next_page: function () {
                this.check = false;
            },
            back_to_name: function () {
                this.check = true;
            },
            Register: function () {
                //    TODO: 注册传参数
                this.$ajax({
                    method: 'get',
                    url: '/',
                    params:{
                        name: this.$parent.name,
                        pass: this.$parent.password,
                        type: 'reg'
                    }
                }).then(response => (this.$router.push({path: '/UserHome/' + this.$parent.name})))
                .catch(function (error) {
                    console.log(error);
                })
            },
            input: function () {
                if (this.check === true) {
                    this.$parent.name = this.name;
                } else this.$parent.password = this.password;
                //    TODO: 更新输入框长度
            }
        },
        watch: {
            check: function (newCheck, oldCheck) {
                console.log(newCheck, oldCheck);
            }
        }
    }
</script>

<style scoped>
    @font-face {
        font-family: 'Montserrat-ExtraBold';
        src: url('../assets/fonts/Montserrat-ExtraBold.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    #register_window {
        background-color: aliceblue;
        background-size: cover;
        padding:0 1% 4.7%;
        font-family: Montserrat-ExtraBold, sans-serif;
        align-items: center;
    }

    header {
        font-family: Montserrat-ExtraBold,monospace;
        text-align: left;
        padding: 20px;
    }

    h1 {
        font-family: Montserrat-ExtraBold, sans-serif;
        padding: 10px 0;
        width: 200px;
        text-align: center;
        border: dotted 10px lightskyblue;
    }

    input {
        padding: 0 0 0 100px;
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
        padding: 10% 10% 10% 18%;
        display: flex;
        align-items: center;
        font-size: 60px;
    }

    .sec2 {
        margin: auto;
        padding: 5% 10% 6.4% 20%;
        display: flex;
        align-items: center;
        font-size: 60px;
    }

</style>