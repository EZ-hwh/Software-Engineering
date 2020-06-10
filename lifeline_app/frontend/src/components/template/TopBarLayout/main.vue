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
            document.body.classList.remove('authentication-bg');
        },
        methods: {
            toggleMenu() {
                this.isMenuOpened = !this.isMenuOpened
            },
            toggleRightSidebar() {
                document.body.classList.toggle('right-bar-enabled')
            },
        },
        computed: {
            checkFooter: function () {
                console.log(this.showFooter);
                return this.showFooter !== "false";
            }
        }
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
        <Footer/>
        <RightBar/>
    </div>
</template>
