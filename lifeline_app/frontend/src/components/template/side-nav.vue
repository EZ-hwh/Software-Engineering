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
        mounted: function () {
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
                    src="../../assets/images/button/sun-with-face.png"
                    alt="user-img"
                    class="rounded-circle img-thumbnail avatar-lg"
            >
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
                            to="/mainpage"
                            class="active"
                    >
                        <i class="mdi mdi-view-dashboard"></i>
                        <span> 主页 </span>

                    </router-link>
                </li>

                <li class="active">
                    <router-link
                            tag="a"
                            to="/homework"
                            class="active"
                    >
                        <i class="mdi mdi-view-dashboard"></i>
                        <span> 作业 </span>

                    </router-link>
                </li>

                <li class="active">
                    <router-link
                            tag="a"
                            to="/document"
                            class="active"
                    >
                        <i class="mdi mdi-view-dashboard"></i>
                        <span> 文件 </span>

                    </router-link>
                </li>


            </ul>
            <div class="clearfix"></div>
        </div>
        <!-- End Sidebar -->
    </div>

</template>

<style lang="scss">
    @import "../../../node_modules/metismenujs/scss/metismenujs";
</style>
