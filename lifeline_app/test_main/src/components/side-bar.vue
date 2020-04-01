<script>
import VuePerfectScrollbar from 'vue-perfect-scrollbar'
import { authComputed } from '@state/helpers'
import SideNav from './side-nav'

export default {
  components: { VuePerfectScrollbar, SideNav },
  props: {
    isCondensed: {
      type: Boolean,
      default: false,
    },
    user: {
      type: Object,
      required: false,
      default: () => ({}),
    },
  },
  data() {
    return {
      settings: {
        minScrollbarLength: 60,
      },
    }
  },
  computed: {
    ...authComputed,
  },
  methods: {},
}
</script>

<template>
  <!-- ========== Left Sidebar Start ========== -->
  <div class="left-side-menu">
    <VuePerfectScrollbar
      v-if="!isCondensed"
      v-once
      class="slimscroll-menu"
      :settings="settings"
    >
      <SideNav :user="user" />
    </VuePerfectScrollbar>
    <SideNav
      v-else
      :user="user"
    />

    <!-- Sidebar -left -->
  </div>
  <!-- Left Sidebar End -->
</template>

<style lang="scss">
.slimscroll-menu {
  height: 100%;
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
</style>
