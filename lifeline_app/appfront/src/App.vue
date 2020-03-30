<template>
    <div id="app">
        <first v-if="display===1"></first>
        <Login v-else-if="display===2"></Login>
        <Register v-else-if="display===3"></Register>
    </div>
</template>

<script>
    import Register from "./components/Register";
    import first from "./components/first";
    import Login from "./components/Login";

    export default {
        name: 'App',
        data() {
            return {
                display: 1,
                name: "",
                password: ""
            }
        },
        components: {
            first,
            Register,
            Login
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
        text-align: center;
        color: #2c3e50;
        padding: 0px;
        margin: 0px;
        position: absolute;
        top: 0px;
        left: 0px;
        width: 100%;
        height: 100%;
        border: hidden;
    }
</style>
