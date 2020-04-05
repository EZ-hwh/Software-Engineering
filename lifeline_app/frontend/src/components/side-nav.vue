<script>
// import { authComputed } from '@state/helpers'

import MetisMenu from 'metismenujs/dist/metismenujs'

export default {
  components: {},
  props: {
    user: {
      type: Object,
      required: false,
      default: () => ({}),
    },
  },
  // computed: {
  //   ...authComputed,
  // },
  mounted: function() {
    // eslint-disable-next-line no-unused-vars
    var menuRef = new MetisMenu('#side-menu')
  },
  methods: {},
}
</script>

<template>
  <div>
    <div class="user-box text-center">
      <img
        src="../assets/images/users/user-1.jpg"
        alt="user-img"
        class="rounded-circle img-thumbnail avatar-lg"
      >
      <div class="">
        <a
          href="#"
          class="text-dark dropdown-toggle h5 mt-2 mb-1 d-block"
        >{{user ? user.name : ''}}</a>
      </div>
      <p class="text-muted">Admin Head</p>
      <ul class="list-inline">
        <li class="list-inline-item">
          <a
            href="#"
            class="text-muted"
          >
            <i class="mdi mdi-settings"></i>
          </a>
        </li>

        <li class="list-inline-item">
          <a
            href="#"
            class="text-custom"
          >
            <i class="mdi mdi-power"></i>
          </a>
        </li>
      </ul>
    </div>

    <!--- Sidemenu -->
    <div id="sidebar-menu">
      <ul
        id="side-menu"
        class="metismenu"
      >
        <li class="menu-title">Navigation</li>

        <li class="active">
          <router-link
            tag="a"
            to="/"
            class="active"
          >
            <i class="mdi mdi-view-dashboard"></i>
            <span> Dashboard </span>
          </router-link>
        </li>

        <li>
          <a
            href="javascript: void(0);"
            class="waves-effect"
          >
            <i class="mdi mdi-share-variant"></i>
            <span> Multi Level </span>
            <span class="menu-arrow"></span>
          </a>
          <ul
            class="nav-second-level nav"
            aria-expanded="false"
          >
            <li>
              <a href="javascript: void(0);">Level 1.1</a>
            </li>
            <li>
              <a
                href="javascript: void(0);"
                aria-expanded="false"
              >Level 1.2
                <span class="menu-arrow"></span>
              </a>
              <ul
                class="nav-third-level nav"
                aria-expanded="false"
              >
                <li>
                  <a href="javascript: void(0);">Level 2.1</a>
                </li>
                <li>
                  <a href="javascript: void(0);">Level 2.2</a>
                </li>
              </ul>
            </li>
          </ul>
        </li>
      </ul>
      <div class="clearfix"></div>
    </div>
    <!-- End Sidebar -->
  </div>
</template>

<style lang="scss">
@import '~metismenujs/scss/metismenujs';
</style>
