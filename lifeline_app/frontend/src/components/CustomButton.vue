<template>
    <div class="but">
        <img :src="getImage" :style="getStyle()">
        <p>{{message}}</p>
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
                console.log('../assets/image/' + this.source + '.png');
                return require('../assets/image/' + this.source + '.png');
            }
        }
    }
</script>

<style scoped>
    .but {
        margin: 20px 20px 0 20px;
        font-size: 15px;
    }
</style>