<template>
    <div class="but">
        <img :src="getImage" :style="getStyle()">
        <p id="button_tag">{{message}}</p>
    </div>
</template>

<script>
    export default {
        name: "CustomButton",
        props: {
            source: String,
            size: String,
            message: String
        },
        methods: {
            getStyle: function () {
                if (this.size === 'small') {
                    return {
                        width: "15px"
                    }
                } else if (this.size === 'median') {
                    return {
                        width: "30px"
                    }
                } else return {
                    width: "45px"
                }
            }
        },
        computed: {
            getImage: function () {
                console.log('../assets/images/button/' + this.source + '.png');
                return require('../assets/images/button/' + this.source + '.png');
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

    #button_tag{
        text-align: center;
        margin: auto;
    }
    .but {
        font-family: Montserrat-ExtraBold, sans-serif;
        margin: 20px auto 0;
        font-size: 15px;
        width: 100px;
        height: 70px;
        text-align: center;
    }
</style>