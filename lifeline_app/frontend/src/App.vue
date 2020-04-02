<template>
    <div id="app">
        <router-view></router-view>
    </div>
</template>

<script>
    import Register from "./views/Register";
    import first from "./views/first";
    import Login from "./views/Login";
    import home from "./views/home";

    export default {
        name: 'App',
        data() {
            return {
                name: "",
                password: ""
            }
        },
        components: {
            first,
            Register,
            Login,
            home
        },
        watch: {
            display: function (newDisplay, oldDisplay) {
                console.log(newDisplay, oldDisplay);
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

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
        padding: 0px;
        margin: 0px;
        top: 0px;
        left: 0px;
        width: 100%;
        height: 100%;
        border: hidden;
    }
</style>

<style lang="scss">
// Allow element/type selectors, because this is global CSS.
// stylelint-disable selector-max-type, selector-class-pattern

// Design variables and utilities from src/design.
@import 'design';
</style>
