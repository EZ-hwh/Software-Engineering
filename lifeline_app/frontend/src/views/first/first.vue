<template>
    <div id="first">
        <div class="main">
            <div id="header">
                <h1>
                    <svg width="100%" height="100%">
                        <text text-anchor="middle" x="50%" y="95%" class="text text-1">
                            LIFELINE
                        </text>
                        <text text-anchor="middle" x="50%" y="95%" class="text text-2">
                            LIFELINE
                        </text>
                        <text text-anchor="middle" x="50%" y="95%" class="text text-3">
                            LIFELINE
                        </text>
                        <text text-anchor="middle" x="50%" y="95%" class="text text-4">
                            LIFELINE
                        </text>
                    </svg>
                </h1>
            </div>
            <div id="But">
                <div id="buttons">
                    <CustomButton source="face-throwing-a-kiss" size="large" message="login" @click.native="log"></CustomButton>
                    <CustomButton source="smiling-face-with-open-mouth" size="large" message="register"
                                  @click.native="reg"></CustomButton>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import CustomButton from "../../components/CustomButton";

    export default {
        name: "first",
        components: {
            CustomButton,
        },
        methods: {
            log: function () {
                window.location.href = "login";
            },
            reg: function () {
                window.location.href = "register";
            }
        }
    }
</script>

<style scoped>

    h1 {
        font-family: Montserrat-ExtraBold, monospace;
        font-size: 12em;
        margin-top: 4%;
        margin-bottom: 4%;
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

    .main {
        font-family: Montserrat-ExtraBold, monospace;
        background-color: rgba(230, 235, 224, 1);
        color: #2E1C22;
        background-size: cover;
        padding: 0;
        width: 100%;
        height: 100%;
        text-align: center;
    }

    #header {
        padding-top: 8%;
        text-align: center;
    }

    #But {
        padding: 0;
        margin: 0 auto;
        width: 20%;
        text-align: center;
    }

    #buttons {
        display: flex;
    }

</style>
