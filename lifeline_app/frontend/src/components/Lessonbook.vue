<template>
    <svg xmlns="http://www.w3.org/2000/svg"
         viewBox= "0 0 800 600" width="100%" height="100%"
         class='lesson_book' id="bookIcon">
        <g id = book>
            <rect :fill="getColor()" :x="getX()" :y="getY()" width="80" :height= "getHeight()" rx="5.0"></rect>
            <text font-family="Montserrat-ExtraBold" :x="getTextX()" :y="getTextY()" :transform ="'rotate(90, ' + getTextX() + ','+ getTextY()+ ')'" style="letter-spacing:10px; font-weight: bold" dominant-baseline="middle" rotate="-90" font-size="25px">{{name}}</text>
        </g>
    </svg>
</template>

<script>
    export default {
        name: "Lessonbook",
        props: {
            name: String,
            xv: Number,
            yv: Number,
            // items:[
            //     {}
            // ]
            number:{type:Number, default:0},
            index:{type:Number, default:0}
        },
        methods: {
            // getStyle:function{
            //     console.log(this.number);
            //     console.log(this.index);
            //     if(this.number % 2 === 0) {
            //         var xx = 400 - 30 * this.number + 60 * this.index;
            //         if (this.index <= this.number / 2) {
            //             var yy= Number(150 + 15 * this.number - 30 * this.index;
            //         }
            //         else{
            //             var yy =  120 - 15 * this.number + 30 * this.index;
            //         }
            //     }
            //     else {
            //         var xx =  370 - 30 * this.number  + 60 * this.index
            //         if (this.index <= (this.number + 1) / 2) {
            //             var yy = 165 + 15 * this.number - 30 * this.index;
            //         }
            //         else{
            //             var yy = 165 - 15 * this.number + 30 * this.index;
            //         }
            //     }
            //     var color = '#68e4aa'
            //     return {
            //         x: xx,
            //         y: xx,
            //         fill: color,
            //     }
            // }
            getX: function(){
                console.log(this.number);
                console.log(this.index);
                if(this.number % 2 === 0) {
                    return Number(360 - 40 * this.number + 80 * this.index);
                }
                else {
                    return Number(360 - 40 * this.number + 80 * this.index);
                }
            },

            getTextX:function(){
                console.log(this.number);
                console.log(this.index);
                if(this.number % 2 === 0) {
                    return Number(360 - 40 * this.number + 80 * this.index + 25)
                }
                else {
                    return Number(360 - 40 * this.number  + 80 * this.index + 25)
                }
            },


            getTextY:function(){
                console.log(this.number);
                console.log(this.index);
                if(this.number % 2 === 0) {
                    if (this.index <= this.number / 2) {
                        return Number(90 + 15 * this.number - 30 * this.index)
                    } else {
                        return Number(60 - 15 * this.number + 30 * this.index)
                    }
                }
                else {
                    if (this.index <= (this.number + 1) / 2) {
                        return Number(105 + 15 * this.number - 30 * this.index)
                    } else {
                        return Number(75 - 15 * this.number + 30 * this.index)
                    }
                }
            },

            getY:function(){
                console.log(this.number);
                console.log(this.index);
                if(this.number % 2 === 0) {
                    if (this.index <= this.number / 2) {
                        return Number(30 + 15 * this.number - 30 * this.index)
                    } else {
                        return Number(0 - 15 * this.number + 30 * this.index)
                    }
                }
                else {
                    if (this.index <= (this.number + 1) / 2) {
                        return Number(45 + 15 * this.number - 30 * this.index)
                    } else {
                        return Number(15 - 15 * this.number + 30 * this.index)
                    }
                }
            },

            getColor:function(){
                if(this.index === 1){
                    return '#68e4aa'
                }
                else if(this.index === 2){
                    return  '#7ec6cc'
                }
                else if(this.index === 3){
                    return '#6d4fd8'
                }
                else if(this.index === 4){
                    return '#d976c2'
                }
                else if(this.index === 5){
                    return  '#f5926e'
                }
                else if(this.index === 6){
                    return '#f7d95c'
                }
                else if(this.index === 7){
                    return '#cef9ad'
                }
                else if(this.index === 8){
                    return '#f4737e'
                }
                else if(this.index === 9){
                    return '#e0cb6e'
                }

            },

            getHeight:function(){
                console.log(this.number);
                console.log(this.index);
                 if(this.number % 2 === 0) {
                    if(this.index <= this.number/2) {
                        return Number(470 - 15 * this.number + 30 * this.index )
                    }
                    else{
                        return Number(500  + 15 * this.number - 30 * this.index)
                    }
                 }
                else{
                    if(this.index <= (this.number + 1)/2){
                        return Number(455 -  15 * this.number + 30 * this.index)
                     }
                    else{
                        return Number(485 + 15 * this.number - 30 *this.index)
                    }
                }
            }

        },

        created:function(){
            console.log(this.name + this.index +this.number);
        },
        mounted:function () {
            console.log(this.name + this.index +this.number);
        }
    }
</script>

<style scoped>
    html {
	  overflow: hidden;
	}

    @font-face {
        font-family: 'Montserrat-ExtraBold';
        src: url('../assets/fonts/Montserrat-ExtraBold.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    #book{
        text-align: center;
        margin: auto;
    }
    .lesson_book {
        font-family: Montserrat-ExtraBold, sans-serif;
        padding: 0 0;
        font-size: 10px;
        width: 100vw;
        height: 75vh;
        text-align: center;
        position:absolute;
    }
    svg {
	    height: 75vh;
	    width: 100vw;
	}
</style>