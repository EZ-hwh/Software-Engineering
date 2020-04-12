<template>
    <div id="first">
        <div class="main">
            <div id="header">
                <h1>LIFELINE</h1>
            </div>
            <div id="But">
                <div id="buttons">
                    <CustomButton source="grinningface" size="large" message="login" @click.native="log"></CustomButton>
                    <CustomButton source="grinningface" size="large" message="register"
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
                // TODO: 后端获取login.html
                this.$router.push({name:"Login"});
            },
            reg: function () {
                // TODO：后端获取register.html
                this.$router.push('/Register');
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

    h1 {
        font-family: Montserrat-ExtraBold, monospace;
        font-size: 150px;
    }

    .main {
        font-family: Montserrat-ExtraBold, monospace;
        background-color: antiquewhite;
        background-size: cover;
        padding: 15% 0 12.9%;
        width: 100%;
        height: 100%;
        text-align: center;
    }

    #header {
        text-align: center;
    }

    #But {
        padding: 1% 0 0;
        margin: 0 auto;
        width: 190px;
        text-align: center;
    }

    #buttons {
        display: flex;
    }

</style>

<style lang="scss">
    // Allow element/type selectors, because this is global CSS.
    // stylelint-disable selector-max-type, selector-class-pattern

    // Design variables and utilities from src/design.
    @import '../home/design';
</style>