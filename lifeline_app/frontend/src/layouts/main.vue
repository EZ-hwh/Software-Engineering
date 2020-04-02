<script>
import TopBar from '../components/top-bar'
import NavBar from '../components/nav-bar'
import RightBar from '../components/right-bar'
import Footer from '../components/footer'
import Calendar from '../components/calendar'

export default {
  components: { TopBar, NavBar, RightBar, Footer, Calendar},
  data() {
    return {
      isMenuOpened: false,
      // user: this.$store ? this.$store.state.auth.currentUser : {} || {},
      //TODO:估计是一个储存登录信息的
    }
  },
  created: () => {
    document.body.classList.remove('authentication-bg')
  },
  methods: {
    toggleMenu() {
      this.isMenuOpened = !this.isMenuOpened
    },
    toggleRightSidebar() {
      document.body.classList.toggle('right-bar-enabled')
    },
  },
}
</script>

<template>
  <div>
    <header id="topnav">
      <TopBar />
<!-- 这里有一个 :user="user" 先注释掉了-->
      <NavBar :is-menu-opened="isMenuOpened" />
    </header>
    

    <div class="wrapper" style="padding-bottom: 60px">
      <div class="container-fluid">
        <slot />
      </div>
    </div>
    <Footer />
    <RightBar />
  </div>
</template>
