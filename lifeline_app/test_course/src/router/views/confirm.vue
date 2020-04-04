<script>
import Layout from '@layouts/auth'
import { authMethods } from '@state/helpers'
import appConfig from '@src/app.config'
export default {
  page: {
    title: 'Confirm',
    meta: [
      { name: 'description', content: `Confirm account to ${appConfig.title}` },
    ],
  },
  components: { Layout },
  data() {
    return {}
  },
  computed: {},
  methods: {
    ...authMethods,
  },
}
</script>

<template>
  <Layout>
    <div class="row justify-content-center">
      <div class="col-md-8 col-lg-6 col-xl-5">
        <div class="text-center">
          <a href="/">
            <span><img
                src="@assets/images/logo-dark.png"
                alt=""
                height="22"
              ></span>
          </a>
          <p class="text-muted mt-2 mb-4">Responsive Admin Dashboard</p>
        </div>

        <div class="card text-center">

          <div class="card-body p-4">

            <div class="mb-4">
              <h4 class="text-uppercase mt-0">Confirm Email</h4>
            </div>
            <img
              src="@assets/images/mail_confirm.png"
              alt="img"
              width="86"
              class="mx-auto d-block"
            />

            <p class="text-muted font-14 mt-2"> A email has been send to <b>youremail@domain.com</b>.
              Please check for an email from company and click on the included link to
              reset your password. </p>

            <router-link
              tag="a"
              to="/login"
              class="btn btn-block btn-pink waves-effect waves-light mt-3"
            >Back to Home</router-link>

          </div> <!-- end card-body -->
        </div>
        <!-- end card -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>

<style lang="scss" module></style>
