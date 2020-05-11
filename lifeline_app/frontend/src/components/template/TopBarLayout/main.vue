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
                showFooter: true,
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
        </header>


        <div class="wrapper" style="padding-bottom: 60px">
            <div class="container-fluid">
                <slot/>
            </div>
        </div>
        <Footer v-show="showFooter"></Footer>
        <RightBar/>
    </div>
</template>
