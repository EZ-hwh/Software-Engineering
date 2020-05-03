<template>
    <div>
        <div id="register_window">
            <header>
                <h1>LifeLine</h1>
            </header>
            <div v-show="check">
                <p class="sec">
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

                        <input v-model="name" placeholder="Your name?" type="text" maxlength="11">

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
                        <p><input v-model="password" placeholder="嘘~"></p>
                        <p><input v-model="password_again" placeholder="再嘘~"></p>
                    </div>
                    <CustomButton source="grinningface" size="large" message="!冲呀!"
                                  @click.native="Register"></CustomButton>
                </div>
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
                check: true,
                response: null
            }
        },
        methods: {
            back_to_main: function () {
                window.location.href = "/";
                // this.$router.go(-1);
            },
            next_page: function () {
                this.check = false;
            },
            back_to_name: function () {
                this.check = true;
            },
            Register: function () {
                this.$ajax({
                    method: 'post',
                    url: '/register/',
                    params: {
                        name: this.name,
                        pass: this.password,
                        pass_again: this.password_again,
                        type: 'reg',
                        contentType: 'application/json',
                        dataType: 'json',
                    }
                }).then(response => {
                    if (response.data.flag == true) {
                        window.location.href = "/login";
                    } else {
                        console.log(response.data.error_msg);
                    }
                    //console.log("sbhwh");
                    //console.log(response);
                    //console.log(response.data);
                }/*function(response){
                   console.log("fuck you");
                    window.location.href = "home";
                    var res = JSON.parse(response);
                    console.log(res["flag"]);
                    if (res["flag"] == "true"){
                        window.location.href = "home";
                    }
                })*/)
                    .catch(function (error) {
                            console.log(error);
                        }
                    )
            },
        },
        watch: {
            check: function (newCheck, oldCheck) {
                console.log(newCheck, oldCheck);
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
        width: 55%;
        height: 100px;
        border: 0px;
        outline: #7B7988;
        font-size: 55px;
        font-family: Montserrat-ExtraBold, sans-serif;
    }

    input::placeholder {
        font-size: 45px;
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
        padding: 5% 10% 6.4% 20%;
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
