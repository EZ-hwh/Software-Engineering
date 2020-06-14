<template>
    <svg xmlns="http://www.w3.org/2000/svg"
         viewBox="0 0 1600 600"
         class='lesson_book' id="bookIcon">
        <g v-for="lesson in lessons">
            <g id=book @click="go_to_lesson(lesson.id)">
                <g id=cover>
                    <rect id=cover :fill="getColor(lesson.index)" :x="getX(lesson.index)" :y="getY(lesson.index)"
                          width="80" :height="getHeight(lesson.index)" rx="5.0"
                          @click="go_to_lesson(lesson.id)"></rect>
                </g>
                <g id=title>
                    <text class="text text-1" font-family="Montserrat-ExtraBold" :x="getTextX(lesson.index) + 10"
                          :y="getTextY(lesson.index)- 10"
                          :transform="'rotate(90, ' + getTextX(lesson.index) + ','+ getTextY(lesson.index)+ ')'"
                          style="letter-spacing:10px;" dominant-baseline="middle" rotate="-90" font-size="30px"
                          @click="go_to_lesson(lesson.id)">{{lesson.name}}
                    </text>
                </g>
                <!--                <rect fill="#fefffe" fill-opacity="0.8" :x="getTextX(lesson.index) - 10" width="10" :y="getY(lesson.index) + 10" rx="3.0" :height="getHeight(lesson.index) - 20" onclick="window.top.location.href='/course'"></rect>-->
            </g>
        </g>
        <g id=shelve>
            <rect id="desk" x=0 y=540 width=1400 height=60 fill="#a09890"></rect>
            <!--            540 -> 480-->
        </g>
    </svg>

</template>

<script>
    export default {
        name: "Lessonbook",
        book: '#book',
        props: {
            lessons: {type: Array},
            number: {type: Number, default: 0},
        },
        data() {
            return {
                get_id: 0,
                get_hover: false
            }
        },
        methods: {
            go_to_lesson: function (id) {
                this.$ajax({
                    method: 'post',
                    url: '/course/',
                    params: {
                        course_id :id,
                    }
                }).then(response => {
                    if(response.data.flag === true)
                        window.location.href = "2Course";
                }).catch(function (error) {
                    console.log(error);
                });
            },
            getX: function (index) {
                // console.log(this.number);
                // console.log(this.index);
                if (this.number % 2 === 0) {
                    return Number(600 - 40 * this.number + 80 * index);
                } else {
                    return Number(600 - 40 * this.number + 80 * index);
                }
            },
            getTextX: function (index) {
                // console.log(this.number);
                // console.log(this.index);
                if (this.number % 2 === 0) {
                    return Number(600 - 40 * this.number + 80 * index + 25)
                } else {
                    return Number(600 - 40 * this.number + 80 * index + 25)
                }
            },


            getTextY: function (index) {
                // console.log(this.number);
                // console.log(this.index);
                if (this.number % 2 === 0) {
                    if (index <= this.number / 2) {
                        return Number(130 + 15 * this.number - 30 * index)
                    } else {
                        return Number(100 - 15 * this.number + 30 * index)
                    }
                } else {
                    if (index <= (this.number + 1) / 2) {
                        return Number(145 + 15 * this.number - 30 * index)
                    } else {
                        return Number(115 - 15 * this.number + 30 * index)
                    }
                }
            },

            getY: function (index) {
                // console.log(this.number);
                // console.log(this.index);
                var y = 0;
                if (this.number % 2 === 0) {
                    if (index <= this.number / 2) {
                        y = Number(70 + 15 * this.number - 30 * index)
                    } else {
                        y = Number(40 - 15 * this.number + 30 * index)
                    }
                } else {
                    if (index <= (this.number + 1) / 2) {
                        y = Number(85 + 15 * this.number - 30 * index)
                    } else {
                        y = Number(55 - 15 * this.number + 30 * index)
                    }
                }

                if (index === this.get_id && this.get_hover === true) {
                    y = y + 40
                }

                return y
            },

            getColor: function (index) {
                if (index % 10 === 1) {
                    return '#8ae9bd'
                } else if (index % 10 === 2) {
                    return '#9cdadf'
                } else if (index % 10 === 3) {
                    return '#947ce8'
                } else if (index % 10 === 4) {
                    return '#ee92d9'
                } else if (index % 10 === 5) {
                    return '#fba383'
                } else if (index % 10 === 6) {
                    return '#f7dd73'
                } else if (index % 10 === 7) {
                    return '#cef9ad'
                } else if (index % 10 === 8) {
                    return '#dd87e6'
                } else if (index % 10 === 9) {
                    return '#e0cb6e'
                } else {
                    return '#b3d3ec'
                }

            },
            getHeight: function (index) {
                // console.log(this.number);
                // console.log(this.index);
                if (this.number % 2 === 0) {
                    if (index <= this.number / 2) {
                        return Number(470 - 15 * this.number + 30 * index)
                    } else {
                        return Number(500 + 15 * this.number - 30 * index)
                    }
                } else {
                    if (this.index <= (this.number + 1) / 2) {
                        return Number(455 - 15 * this.number + 30 * index)
                    } else {
                        return Number(485 + 15 * this.number - 30 * index)
                    }
                }
            },

        },

        created: function () {
            console.log(this.lessons);
            console.log(this.number);
        },
        mounted: function () {
            console.log(this.lessons + this.number);
        }
    }
</script>

<style scoped>
    /*html {*/
    /*  overflow: hidden;*/
    /*}*/

    @font-face {
        font-family: 'Montserrat-ExtraBold';
        src: url('../../../assets/fonts/Montserrat-ExtraBold.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

    #book {
        text-align: center;
        margin: auto;
    }

    #cover :hover {
        transform: translate(0px, -50px);
    }

    #cover :hover:after {
        transform: translateY(-50px);
        transition: all 2s ease-in-out;
    }

    #title :hover {
        transform: translate(0px, 50px) rotate(90deg);
    }

    #title :hover:after {
        transform: translateY(-50px) rotate(90deg);
        transition: all 2s ease-in-out;
    }

    .lesson_book {
        font-family: Montserrat-ExtraBold, sans-serif;
        padding: 0 0;
        font-size: 10px;
        text-align: center;
        /*position:absolute;*/
    }

    .text {
        /*font-size: 64px;*/
        font-weight: bold;
        text-transform: uppercase;
        fill: #ffffff;
        /*fill: none;*/
        stroke: #a09890;
        stroke-width: 1px;
        /*stroke-dasharray: 90 310;*/
        /*animation: stroke 12s infinite linear;*/
    }

    .text:hover {
        fill: #a09890;
        stroke-dasharray: 90 310;
    }


    .text-1 {
        stroke: #a09890;
        text-shadow: 0 0 1px #a09890;
        /*animation-delay: -3s;*/
    }

</style>