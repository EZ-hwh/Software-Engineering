<template>
    <div class="main">
        <div id="header">
            <h1>LIFELINE</h1>
        </div>
        <div id="But">
            <div id="buttons">
                <CustomButton source="grinningface" size="large" message="login" @click.native="log"></CustomButton>
                <CustomButton source="grinningface" size="large" message="register" @click.native="reg"></CustomButton>
            </div>
        </div>
    </div>
</template>

<script>
    import CustomButton from "./CustomButton";

    export default {
        name: "first",
        components: {
            CustomButton
        },
        methods: {
            log: function () {
                this.$parent.display = 2;
            },
            reg: function () {
                this.$parent.display = 3;
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

    .main {
        background-color: antiquewhite;
        padding: 15% 0;
        width: 100%;
        height: 100%;
        font-family: Montserrat-ExtraBold,sans-serif;
        align-items: center;
    }

    #header {
        font-size: 80px;
        text-align: center;
        height: auto;
    }

    #But {
        margin: auto;
        width: 186px;
        padding: 2% 0;
    }

    #buttons {
        display: flex;
    }

</style>