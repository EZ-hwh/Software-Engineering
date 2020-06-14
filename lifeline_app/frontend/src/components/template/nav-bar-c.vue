<script>
    // import { authComputed } from '@state/helpers'
    import VuePerfectScrollbar from 'vue-perfect-scrollbar'

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
                default: () => '',
            },
        },
        data() {
            return {
                UserImg: null,
                HomeImg: require("../../assets/images/button/house-building.png"),
                LessonsImg: require("../../assets/images/button/books.png")
            }
        },
        computed: {
            getImage: function () {
                console.log(this.UserImg);
                return this.UserImg;
            },
        },
        methods: {
            toggleMenu() {
                this.$parent.toggleMenu()
            },
            toggleRightSidebar() {
                this.$parent.toggleRightSidebar()
            },
            ToLessons: function () {
                window.location.href = "/lessons"
            },
            ToPersonal: function () {
                window.location.href = "/personal"
            },
            ToHome: function () {
                window.location.href = "/home"
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
    }
</script>

<template>
    <!-- Topbar Start -->
    <div class="navbar-custom">
        <ul class="list-unstyled topnav-menu float-right mb-0">

            <b-nav-item-dropdown
                    right
                    class="notification-list"
                    menu-class="profile-dropdown"
            >
                <template slot="button-content">
                    <div class="nav-user mr-0 waves-effect waves-light">
                        <img :src="getImage" class="circle"/>
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

            <li class="dropdown notification-list" @click="ToLessons">
                <template>
                    <div class="nav-user mr-0 btn btn-link nav-link right-bar-toggle waves-effect waves-light">
                        <img :src="LessonsImg" class="circle"/>
                    </div>
                </template>
            </li>

            <li class="dropdown notification-list" @click="ToHome" style="margin: 0px 18px">
                <template>
                    <div class="nav-user mr-0 btn btn-link nav-link right-bar-toggle waves-effect waves-light">
                        <img :src="HomeImg" class="circle"/>
                    </div>
                </template>
            </li>

            <!--      <li class="dropdown notification-list">-->
            <!--        <button-->
            <!--          class="btn btn-link nav-link right-bar-toggle waves-effect waves-light"-->
            <!--          @click="ToHome"-->
            <!--        >-->
            <!--          <img :src="HomeImg" class="circle"/>-->
            <!--        </button>-->
            <!--      </li>-->
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
                  src="../../assets/images/button/black-heart-suit.png"
                  alt=""
                  height="32"
          />
        </span>
                <span class="logo-sm">
          <img
                  src="../../assets/images/button/black-heart-suit.png"
                  alt=""
                  height="32"
          />
        </span>
                <p class="TitleFont">LIFELINE</p>
            </a>
        </div>

        <ul class="list-unstyled topnav-menu topnav-menu-left m-0">
            <li>
                <button
                        class="button-menu-mobile disable-btn waves-effect"
                        @click="toggleMenu"
                >
                    <i class="fe-menu"></i>
                </button>
            </li>

            <li>
                <h4 class="page-title-main">{{title || ''}}</h4>
            </li>

        </ul>
    </div>
    <!-- end Topbar -->
</template>

<style lang="scss">
    @font-face {
        font-family: 'Montserrat-ExtraBold';
        src: url('../../../../frontend/src/assets/fonts/Montserrat-ExtraBold.ttf') format('truetype');
        font-weight: normal;
        font-style: normal;
    }

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
        color: coral;
    }
</style>
