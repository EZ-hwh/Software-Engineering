<template>
    <div>
        <div id="coursesTable"></div>
    </div>

</template>

<script>
    import {Timetables} from "../../../assets/js/pages/Timetables.min.js";

    var courseList = [
        [
            '',
            '软件工程',
            '软件工程',
            '软件工程',
            '',
            '程序设计语言原理',
            '程序设计语言原理',
            '算法设计与分析',
            '算法设计与分析',
            '',
            '',
            '',
            '',
        ],
        [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
        ],
        [
            '',
            '游戏设计基础',
            '游戏设计基础',
            '游戏设计基础',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
        ],
        [
            '',
            '计算机体系结构实验',
            '计算机体系结构实验',
            '计算机体系结构实验',
            '',
            '算法设计与分析',
            '算法设计与分析',
            '算法设计与分析',
            '',
            '',
            '',
            '',
            '',
        ],
        [
            '',
            '计算机体系结构',
            '计算机体系结构',
            '计算机体系结构',
            '',
            'Java语言',
            'Java语言',
            'Java语言',
            '',
            '',
            '',
            '',
            '',
        ],
        [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
        ],
        [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
        ]
    ]
    var week =
        window.innerWidth > 360
            ? ['周一', '周二', '周三', '周四', '周五','周六','周日']
            : ['一', '二', '三', '四', '五','六','日']
    var day = new Date().getDay()
    var courseType = [
        [{index: '1', name: '8:00'}, 1],
        [{index: '2', name: '8:55'}, 1],
        [{index: '3', name: '9:55'}, 1],
        [{index: '4', name: '10:50'}, 1],
        [{index: '5', name: '11:45'}, 1],
        [{index: '6', name: '13:30'}, 1],
        [{index: '7', name: '14:25'}, 1],
        [{index: '8', name: '15:25'}, 1],
        [{index: '9', name: '16:20'}, 1],
        [{index: '10', name: '17:15'}, 1],
        [{index: '11', name: '18:30'}, 1],
        [{index: '12', name: '19:25'}, 1],
        [{index: '13', name: '20:20'}, 1],
    ]

    export default {
        components: {},
        data() {
            return {
                courseList: courseList,
                week: week,
                day: day,
                courseType: courseType,
                Timetable: null,
            }
        },
        mounted: function () {
            this.Timetable = new Timetables({
                el: '#coursesTable',
                timetables: courseList,
                week: week,
                timetableType: courseType,
                highlightWeek: day,
                gridOnClick: function (e) {
                    alert(
                        e.name +
                        '  ' +
                        e.week +
                        ', 第' +
                        e.index +
                        '节课, 课长' +
                        e.length +
                        '节'
                    )
                    console.log(e)
                },
                styles: {
                    Gheight: 50,
                },
            })
        },
        methods: {
        }
    }
</script>

<style>
    .Courses-head {
        background-color: #edffff;
    }

    .Courses-head > div {
        text-align: center;
        font-size: 14px;
        line-height: 28px;
    }

    .left-hand-TextDom,
    .Courses-head {
        background-color: #f2f6f7;
    }

    .Courses-leftHand {
        background-color: #f2f6f7;
        font-size: 12px;
    }

    .Courses-leftHand .left-hand-index {
        color: #9c9c9c;
        margin-bottom: 4px !important;
    }

    .Courses-leftHand .left-hand-name {
        color: #666;
    }

    .Courses-leftHand p {
        text-align: center;
        font-weight: 900;
    }

    .Courses-head > div {
        border-left: none !important;
    }

    .Courses-leftHand > div {
        padding-top: 5px;
        border-bottom: 1px dashed rgb(219, 219, 219);
    }

    .Courses-leftHand > div:last-child {
        border-bottom: none !important;
    }

    .left-hand-TextDom,
    .Courses-head {
        border-bottom: 1px solid rgba(0, 0, 0, 0.1) !important;
    }

    .Courses-content > ul {
        border-bottom: 1px dashed rgb(219, 219, 219);
        box-sizing: border-box;
    }

    .Courses-content > ul:last-child {
        border-bottom: none !important;
    }

    .highlight-week {
        color: #02a9f5 !important;
    }

    .Courses-content li {
        text-align: center;
        color: #666666;
        font-size: 14px;
        line-height: 50px;
    }

    .Courses-content li span {
        padding: 6px 2px;
        box-sizing: border-box;
        line-height: 18px;
        border-radius: 4px;
        white-space: normal;
        word-break: break-all;
        cursor: pointer;
    }

    .grid-active {
        z-index: 9999;
    }

    .grid-active span {
        box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.2);
    }
</style>
