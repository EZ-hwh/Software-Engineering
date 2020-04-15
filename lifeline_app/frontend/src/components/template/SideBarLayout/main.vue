<script>
    import NavBarC from "../nav-bar-c";
    import SideBar from "../side-bar";
    import RightBar from "../right-bar";
    import Footer from "../footer";

    export default {
        components: {NavBarC, SideBar, RightBar, Footer},
        data() {
            return {
                isMenuCondensed: false,
                // user: this.$store ? this.$store.state.auth.currentUser : {} || {},
                title: this.$route ? this.$route.meta.title || "" : ""
            };
        },
        created: () => {
            document.body.classList.remove("authentication-bg");
        },
        methods: {
            toggleMenu() {
                this.isMenuCondensed = !this.isMenuCondensed;
                document.body.classList.toggle("sidebar-enable");
                if (
                    !/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini|Mobile|mobile|CriOS/i.test(
                        navigator.userAgent
                    )
                )
                    document.body.classList.toggle("enlarged");
            },
            toggleRightSidebar() {
                document.body.classList.toggle("right-bar-enabled");
            }
        }
    };
</script>

<template>
    <div id="wrapper">
        <NavBarC :title="title"/>
        <SideBar :is-condensed="isMenuCondensed"/>
        <!-- ============================================================== -->
        <!-- Start Page Content here -->
        <!-- ============================================================== -->

        <div class="content-page">
            <div class="content">
                <!-- Start Content-->
                <div class="container-fluid">
                    <slot/>
                </div>
            </div>
            <Footer/>
        </div>
        <RightBar/>
    </div>
</template>


