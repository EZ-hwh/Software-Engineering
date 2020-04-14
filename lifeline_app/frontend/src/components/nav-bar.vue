<script>
    // import { authComputed } from '@state/helpers'
    import data from '../datasample.json'

    export default {
        components: {},
        props: {
            user: {
                type: Object,
                required: false,
                default: () => ({}),
            },
            isMenuOpened: {
                type: Boolean,
                required: false,
                default: false,
            },
        },
        data() {
            return {
                courses: data.Curriculum
            }
        },
        // computed: {
        //   ...authComputed,
        // },
        methods: {
            onMenuClick(event) {
                event.preventDefault()
                const nextEl = event.target.nextSibling
                if (nextEl && !nextEl.classList.contains('open')) {
                    const parentEl = event.target.parentNode
                    if (parentEl) {
                        parentEl.classList.remove('open')
                    }

                    nextEl.classList.add('open')
                } else if (nextEl) {
                    nextEl.classList.remove('open')
                }
                //TODO: 这里可以做到homepage的跳转 暂时可以不动 这里response好像要改改...
                window.location.href = "/home"; //转跳到home
                /*console.log("qitadejiubudong")
                this.$ajax({
                    method: 'get',
                    url: '/home',
                }).then(response => (console.log(response)))
                    .catch(function (error) {
                        console.log(error);
                    })
                return false*/
            },

            ToLessons(event) {
                event.preventDefault()
                const nextEl = event.target.nextSibling
                if (nextEl && !nextEl.classList.contains('open')) {
                    const parentEl = event.target.parentNode
                    if (parentEl) {
                        parentEl.classList.remove('open')
                    }

                    nextEl.classList.add('open')
                } else if (nextEl) {
                    nextEl.classList.remove('open')
                }
                //TODO: 这里跳转lessons
                console.log("从这里应该可以跳转")
                window.location.href = "/lesson";  //转跳到lesson
                /*this.$ajax({
                    method: 'get',
                    url: '/lessons',
                }).then(response => (console.log(response)))
                    .catch(function (error) {
                        console.log(error);
                    })
                return false*/
            },
            ToCourse(value) {
              //TODO: 这里跳转singlecourse的界面
                console.log(value)
                window.location.href = "/course"; //还没有加课程的value
                /*this.$ajax({
                    method: 'get',
                    url: '/SingleCourse',
                    params: {
                      name: value
                    }
                }).then(response => (console.log(response)))
                    .catch(function (error) {
                        console.log(error);
                    })*/
            }
        },
    }
</script>

<template>
    <!-- Topbar Start -->
    <div class="topbar-menu">
        <div class="container-fluid">
            <b-collapse id="navigation" v-model="isMenuOpened">
                <!-- Navigation Menu-->
                <ul class="navigation-menu">
                    <li class="has-submenu active">
                        <a href="#" @click="onMenuClick">
                            <i class="mdi mdi-view-dashboard"></i>Main
                        </a>
                    </li>

                    <li class="has-submenu">
                        <a href="#" @click="ToLessons">
                            <i class="mdi mdi-share-variant"></i>Curriculum
                            <div class="arrow-down"></div>
                        </a>

                        <ul class="submenu">
                            <li v-for="value in courses" :key="value">
                              <a href="#" @click="ToCourse(value)">
                                {{value}}
                              </a>
                            </li>
                        </ul>
                    </li>

                    <li class="has-submenu">
                        <a href="#">
                            <i class="mdi mdi-invert-colors"></i>Ispace
                        </a>
                    </li>
                </ul>
                <!-- End navigation menu -->

                <div class="clearfix"></div>
            </b-collapse>
            <!-- end #navigation -->
        </div>
        <!-- end container -->
    </div>
    <!-- end navbar-custom -->
</template>

<style lang="scss">
</style>
