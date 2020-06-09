<script>
    import appConfig from "../../app.config";

    export default {
        page: {
            title: 'LifeLine',
            meta: [{name: 'description', content: appConfig.description}],
        },
    }

</script>

<template>
    <div id="course">
        <!--
        Even when routes use the same component, treat them
        as distinct and create the component again.
        -->
        <RouterView :key="$route.fullPath" />
    </div>
</template>

<!-- This should generally be the only global CSS in the app. -->
<style lang="scss">
    // Allow element/type selectors, because this is global CSS.
    // stylelint-disable selector-max-type, selector-class-pattern

    // Design variables and utilities from src/TopBarDesign.
    @import '../../assets/css/SideBarDesign';
</style>
