<script>
    import TopBar from '../top-bar'
    import NavBar from '../nav-bar'
    import RightBar from '../right-bar'
    import Footer from '../footer'

    export default {
        components: {TopBar, NavBar, RightBar, Footer},
        data() {
            return {
                isMenuOpened: false,
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
            <TopBar/>
            <!-- 这里有一个 :user="user" 先注释掉了-->
            <NavBar :is-menu-opened="isMenuOpened"/>
        </header>


        <div class="wrapper" style="padding-bottom: 60px">
            <div class="container-fluid">
                <slot/>
            </div>
        </div>
        <Footer/>
        <RightBar/>
    </div>
</template>
