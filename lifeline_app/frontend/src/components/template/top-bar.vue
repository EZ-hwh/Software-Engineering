<script>
    // import { authComputed } from '@state/helpers'
    import VuePerfectScrollbar from "vue-perfect-scrollbar";
    import data from '../../datasample.json';

    export default {
        components: {VuePerfectScrollbar},
        props: {
            user: {
                type: Object,
                required: false,
                default: () => ({}),
            },
            title: {
                type: String,
                required: false,
                default: () => "",
            },
        },
        data() {
            return {
                courses: data.Curriculum,
                isMenuOpened: false,
                UserImg: null
            };
        },
        computed: {
            getImage: function () {
                console.log(this.UserImg);
                return this.UserImg;
            },
        },
        methods: {
            toggleMenu() {
                this.isMenuOpened = !this.isMenuOpened;
                this.$parent.toggleMenu();
            },
            toggleRightSidebar() {
                this.$parent.toggleRightSidebar();
            },
            onMenuClick(event) {
                event.preventDefault();
                const nextEl = event.target.nextSibling;
                if (nextEl && !nextEl.classList.contains("open")) {
                    const parentEl = event.target.parentNode;
                    if (parentEl) {
                        parentEl.classList.remove("open");
                    }

                    nextEl.classList.add("open");
                } else if (nextEl) {
                    nextEl.classList.remove("open");
                }
                window.location.href = "/home"; //转跳到home
            },

            ToLessons(event) {
                event.preventDefault();
                const nextEl = event.target.nextSibling;
                if (nextEl && !nextEl.classList.contains("open")) {
                    const parentEl = event.target.parentNode;
                    if (parentEl) {
                        parentEl.classList.remove("open");
                    }

                    nextEl.classList.add("open");
                } else if (nextEl) {
                    nextEl.classList.remove("open");
                }
                window.location.href = "/lesson"; //转跳到lesson
            },
            ToCourse(value) {
                //TODO: 这里跳转singlecourse的界面
                console.log(value);
                window.location.href = "/course"; //还没有加课程的value
            },
            ToPersonal: function () {
                window.location.href = "/personal" //TODO：修改成带value的get
            }
        },
        beforeCreate: function () {
            this.$ajax.get('/get_IDpic').then(
                response => {
                    console.log(response.data.ImgUrl);
                    this.UserImg = response.data.ImgUrl;
                }).catch(function (error) {
                console.log(error);
            });
        }

    };
</script>

<template>
    <!-- Topbar Start -->
    <div class="navbar-custom">
        <div class="container-fluid">
            <ul class="list-unstyled topnav-menu float-right mb-0">
                <li class="dropdown notification-list">
                    <!-- Mobile menu toggle-->
                    <a
                            class="navbar-toggle nav-link"
                            :class="{ open: isMenuOpened }"
                            @click="toggleMenu"
                    >
                        <div class="lines">
                            <span></span>
                            <span></span>
                            <span></span>
                        </div>
                    </a>
                    <!-- End mobile menu toggle-->
                </li>

                <!-- 这里是search框 视情况添加 -->
                <!-- <li class="d-none d-sm-block">
                  <form class="app-search">
                    <div class="app-search-box">
                      <div class="input-group">
                        <input
                          type="text"
                          class="form-control"
                          placeholder="Search..."
                        />
                        <div class="input-group-append">
                          <button class="btn" type="submit">
                            <i class="fe-search"></i>
                          </button>
                        </div>
                      </div>
                    </div>
                  </form>
                </li> -->

                <!-- 这里是头像和下拉菜单 -->
                <b-nav-item-dropdown
                        right
                        class="notification-list"
                        menu-class="profile-dropdown"
                >
                    <template slot="button-content">
                        <div class="nav-user mr-0 waves-effect waves-light">
                            <img
                                    :src="getImage"
                                    alt="user-image"
                                    class="rounded-circle"
                            />
                            <span class="pro-user-name ml-1">
                {{ user ? user.name : "" }} <i class="mdi mdi-chevron-down"></i>
              </span>
                        </div>
                    </template>

                    <b-dropdown-item @click="ToPersonal">
                        <i class="fe-user mr-1"></i>
                        <span>My Account</span>
                    </b-dropdown-item>

                    <b-dropdown-divider></b-dropdown-divider>
                    <b-dropdown-item href="/logout">
                        <i class="fe-log-out mr-1"></i>
                        <span>Logout</span>
                    </b-dropdown-item>
                </b-nav-item-dropdown>

                <!-- 这里是侧栏 按需求添加吧 -->
                <!-- <li class="dropdown notification-list">
                  <button
                    class="btn btn-link nav-link right-bar-toggle waves-effect waves-light"
                    @click="toggleRightSidebar"
                  >
                    <i class="fe-settings noti-icon"></i>
                  </button>
                </li> -->
            </ul>

            <!-- LOGO -->
            <div class="logo-box">
                <a
                        href="index.html"
                        class="logo"
                        style="display: flex;margin:auto"
                >
        <span class="logo-lg" style="margin:auto">
          <img
                  src="../../assets/images/button/timer-clock.png"
                  alt=""
                  height="32"
          />
        </span>
                    <span class="logo-sm">
          <img
                  src="../../assets/images/button/timer-clock.png"
                  alt=""
                  height="32"
          />
        </span>
                    <p class="TitleFont">LIFELINE</p>
                </a>
            </div>

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
                            <i class="mdi mdi-book-open-variant"></i>Curriculum
                        </a>
                    </li>

                    <li class="has-submenu">
                        <a href="#"> <i class="mdi mdi-account-badge-outline"></i>Ispace </a>
                    </li>
                </ul>
                <!-- End navigation menu -->

                <div class="clearfix"></div>
            </b-collapse>
            <!-- end #navigation -->
        </div>
    </div>
    <!-- end Topbar -->
</template>

<style lang="scss">
    .noti-scroll {
        height: 220px;
    }

    .ps > .ps__scrollbar-y-rail {
        width: 8px !important;
        background-color: transparent !important;
    }

    .ps > .ps__scrollbar-y-rail > .ps__scrollbar-y,
    .ps.ps--in-scrolling.ps--y > .ps__scrollbar-y-rail > .ps__scrollbar-y,
    .ps > .ps__scrollbar-y-rail:active > .ps__scrollbar-y,
    .ps > .ps__scrollbar-y-rail:hover > .ps__scrollbar-y {
        width: 6px !important;
    }

    .button-menu-mobile {
        outline: none !important;
    }

    .TitleFont {
        font-family: Montserrat-ExtraBold, serif;
        font-size: 200%;
        margin: 0 25px 0 10px;
        color: aliceblue;
    }
</style>
