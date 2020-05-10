<script>
// import { authComputed } from '@state/helpers'
import VuePerfectScrollbar from "vue-perfect-scrollbar";
import data from '../../datasample.json';

export default {
  components: { VuePerfectScrollbar },
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
    };
  },
  // computed: {
  //   ...authComputed,
  // },
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
      //TODO: 这里跳转lessons
      console.log("从这里应该可以跳转");
      window.location.href = "/lesson"; //转跳到lesson
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
      console.log(value);
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
    },
  },
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

        <!-- 这里是通知栏 -->
        <b-nav-item-dropdown right class="notification-list">
          <template
            slot="button-content"
            class="nav-link dropdown-toggle  waves-effect waves-light"
          >
            <i class="fe-bell noti-icon"></i>
            <!-- <span class="badge badge-danger rounded-circle noti-icon-badge"
              >9</span
            > -->
          </template>

          <b-dropdown-text href="#" class="dropdown-item noti-title">
            <h5 class="m-0">
              <span class="float-right">
                <a href="" class="text-dark">
                  <small>Clear All</small>
                </a> </span
              >Notification
            </h5>
          </b-dropdown-text>

          <b-dropdown-text href="#" class="p-0">
            <VuePerfectScrollbar v-once class="noti-scroll">
              <a
                href="javascript:void(0);"
                class="dropdown-item notify-item active"
              >
                <div class="notify-icon">
                  <img
                    src="../../assets/images/user/user-1.jpg"
                    class="img-fluid rounded-circle"
                    alt=""
                  />
                </div>
                <p class="notify-details">Cristina Pride</p>
                <p class="text-muted mb-0 user-msg">
                  <small>Hi, How are you? What about our next meeting</small>
                </p>
              </a>


              <a href="javascript:void(0);" class="dropdown-item notify-item">
                <div class="notify-icon bg-primary">
                  <i class="mdi mdi-comment-account-outline"></i>
                </div>
                <p class="notify-details">
                  Caleb Flakelar commented on Admin
                  <small class="text-muted">1 min ago</small>
                </p>
              </a>

              <a href="javascript:void(0);" class="dropdown-item notify-item">
                <div class="notify-icon">
                  <img
                    src="../../assets/images/user/user-1.jpg"
                    class="img-fluid rounded-circle"
                    alt=""
                  />
                </div>
                <p class="notify-details">Karen Robinson</p>
                <p class="text-muted mb-0 user-msg">
                  <small>Wow ! this admin looks good and awesome design</small>
                </p>
              </a>


              <a href="javascript:void(0);" class="dropdown-item notify-item">
                <div class="notify-icon bg-warning">
                  <i class="mdi mdi-account-plus"></i>
                </div>
                <p class="notify-details">
                  New user registered.
                  <small class="text-muted">5 hours ago</small>
                </p>
              </a>


              <a href="javascript:void(0);" class="dropdown-item notify-item">
                <div class="notify-icon bg-info">
                  <i class="mdi mdi-comment-account-outline"></i>
                </div>
                <p class="notify-details">
                  Caleb Flakelar commented on Admin
                  <small class="text-muted">4 days ago</small>
                </p>
              </a>


              <a href="javascript:void(0);" class="dropdown-item notify-item">
                <div class="notify-icon bg-secondary">
                  <i class="mdi mdi-heart"></i>
                </div>
                <p class="notify-details">
                  Carlos Crouch liked
                  <b>Admin</b>
                  <small class="text-muted">13 days ago</small>
                </p>
              </a>
            </VuePerfectScrollbar>

            <a
              href="javascript:void(0);"
              class="dropdown-item text-center text-primary notify-item notify-all"
            >
              View all
              <i class="fi-arrow-right"></i>
            </a>
          </b-dropdown-text>
        </b-nav-item-dropdown>

        <!-- 这里是头像和下拉菜单 -->
        <b-nav-item-dropdown
          right
          class="notification-list"
          menu-class="profile-dropdown"
        >
          <template slot="button-content">
            <div class="nav-user mr-0 waves-effect waves-light">
              <img
                src="../../assets/images/user/user-1.jpg"
                alt="user-image"
                class="rounded-circle"
              />
              <span class="pro-user-name ml-1">
                {{ user ? user.name : "" }} <i class="mdi mdi-chevron-down"></i>
              </span>
            </div>
          </template>

          <b-dropdown-item href="#">
            <i class="fe-user mr-1"></i>
            <span>My Account</span>
          </b-dropdown-item>

          <b-dropdown-item href="#">
            <i class="fe-settings mr-1"></i>
            <span>Settings</span>
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
        <a href="index.html" class="logo text-center">
          <!-- 这个图片不知道哪里出错了 -->
          <span class="logo-lg">
            <img
              src="../../assets/images/logo/logo-dark.png"
              alt=""
              height="16"
            />
          </span>
          <span class="logo-sm">
            <img
              src="../../assets/images/logo/logo-sm.png"
              alt=""
              height="24"
            />
          </span>
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
</style>
