<script>
import Layout from '@layouts/auth'
import { authMethods } from '@state/helpers'
import appConfig from '@src/app.config'
export default {
  page: {
    title: 'Forget Password',
    meta: [
      { name: 'description', content: `Forget Password to ${appConfig.title}` },
    ],
  },
  components: { Layout },
  data() {
    return {
      email: '',
      error: null,
      tryingToReset: false,
      isResetError: false,
      isSuccess: false,
      successMessage: null,
    }
  },
  computed: {},
  methods: {
    ...authMethods,
    // Try to register the user in with the email, fullname
    // and password they provided.
    tryToReset() {
      this.tryingToReset = true
      // Reset the authError if it existed.
      this.error = null
      return this.resetPassword({
        email: this.email,
      })
        .then((data) => {
          this.tryingToReset = false
          this.isResetError = false
          this.isSuccess = true
          this.successMessage = data.message
        })
        .catch((error) => {
          this.tryingToReset = false
          this.error = error ? error.response.data.message : ''
          this.isResetError = true
          this.isSuccess = false
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
              <h4 class="text-uppercase mt-0 mb-3">Reset Password</h4>
              <p class="text-muted mb-0 font-13">Enter your email address and we'll send you an email with instructions to reset your password. </p>
            </div>

            <b-alert
              v-model="isResetError"
              variant="danger"
              dismissible
            >
              {{error}}
            </b-alert>

            <b-alert
              v-model="isSuccess"
              variant="success"
              dismissible
            >
              {{successMessage}}
            </b-alert>

            <b-form @submit.prevent="tryToReset">
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
                id="button-group"
                class="mt-4"
              >
                <b-button
                  type="submit"
                  variant="primary"
                  class="btn-block"
                > Reset Password </b-button>
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
