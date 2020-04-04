<script>
import appConfig from '@src/app.config'
import Layout from '@layouts/main'
export default {
  page: {
    title: 'Dashboard',
    meta: [{ name: 'description', content: appConfig.description }],
  },
  components: { Layout },
}
</script>

<template>
  <Layout>
        <router-view></router-view>
  </Layout>
</template>
