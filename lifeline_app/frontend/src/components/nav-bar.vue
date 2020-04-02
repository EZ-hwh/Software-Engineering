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
      courses:data.Curriculum
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
      return false
    },
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
            <a href="#" @click="onMenuClick">
              <i class="mdi mdi-share-variant"></i>Curriculum
              <div class="arrow-down"></div>
            </a>

            <ul class="submenu">
              <li v-for="value in courses" :key="value">
                <router-link tag="a" to="/l">{{value}}</router-link>
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
