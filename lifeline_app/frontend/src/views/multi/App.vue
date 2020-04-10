<template>
    <router-view></router-view>
</template>

<script>
    import first from "../first/first";
    import Login from "../login/Login";
    import Register from "../register/Register";
    export default {
        name: "App.vue",
        components: {
            first,
            Login,
            Register
        }
    }
</script>

<style scoped>

</style>