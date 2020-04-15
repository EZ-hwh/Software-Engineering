<script>
import appConfig from "../app.config";
import Layout from "../views/SingleCourse/Layout/main";
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
