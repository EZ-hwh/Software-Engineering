<script>
import Layout from '@layouts/auth'
import { authMethods } from '@state/helpers'
import appConfig from '@src/app.config'
export default {
  page: {
    title: 'Register',
    meta: [{ name: 'description', content: `Register to ${appConfig.title}` }],
  },
  components: { Layout },
  data() {
    return {
      fullname: '',
      email: '',
      password: '',
      regError: null,
      tryingToRegister: false,
      isRegisterError: false,
    }
  },
  computed: {},
  methods: {
    ...authMethods,
    // Try to register the user in with the email, fullname
    // and password they provided.
    tryToRegisterIn() {
      this.tryingToRegister = true
      // Reset the regError if it existed.
      this.regError = null
      return this.register({
        fullname: this.fullname,
        email: this.email,
        password: this.password,
      })
        .then((token) => {
          this.tryingToRegister = false
          this.isRegisterError = false
          // Redirect to the originally requested page, or to the confirm-account page
          this.$router.push(
            this.$route.query.redirectFrom || { name: 'confirm-account' }
          )
        })
        .catch((error) => {
          this.tryingToRegister = false
          this.regError = error.response ? error.response.data.message : ''
          this.isRegisterError = true
        })
    },
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
        <div class="card">
          <div class="card-body p-4">

            <div class="text-center mb-4">
              <h4 class="text-uppercase mt-0">Register</h4>
            </div>

            <b-alert
              v-model="isRegisterError"
              variant="danger"
              dismissible
            >
              {{regError}}
            </b-alert>

            <b-form @submit.prevent="tryToRegisterIn">
              <b-form-group
                id="fullname-group"
                label="Full Name"
                label-for="fullname"
              >
                <b-form-input
                  id="fullname"
                  v-model="fullname"
                  type="text"
                  required
                  placeholder="Enter your name"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="email-group"
                label="Email"
                label-for="email"
              >
                <b-form-input
                  id="email"
                  v-model="email"
                  type="email"
                  required
                  placeholder="Enter email"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="password-group"
                label="Password"
                label-for="password"
              >
                <b-form-input
                  id="password"
                  v-model="password"
                  type="password"
                  required
                  placeholder="Enter password"
                ></b-form-input>
              </b-form-group>

              <b-form-group
                id="button-group"
                class="mt-4"
              >
                <b-button
                  type="submit"
                  variant="primary"
                  class="btn-block"
                >Sign Up</b-button>
              </b-form-group>
            </b-form>
          </div>
          <!-- end card-body -->
        </div>
        <!-- end card -->

        <div class="row mt-3">
          <div class="col-12 text-center">
            <p class="text-muted">Already have account?
              <router-link
                tag="a"
                to="/login"
                class="text-dark ml-1"
              ><b>Log In</b></router-link>
            </p>
          </div>
          <!-- end col -->
        </div>
        <!-- end row -->
      </div>
      <!-- end col -->
    </div>
    <!-- end row -->
  </Layout>
</template>

<style lang="scss" module></style>
