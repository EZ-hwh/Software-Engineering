<script>
import appConfig from "../../../app.config";
import Layout from "../../../components/template/SideBarLayout/main";
export default {
  page: {
    title: "Dashboard",
    meta: [{ name: "description", content: appConfig.description }]
  },
  components: { Layout }
};
</script>

<template>
  <Layout>
    <router-view></router-view>
  </Layout>
</template>
