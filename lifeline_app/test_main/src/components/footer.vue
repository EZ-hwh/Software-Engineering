<script>
import { authComputed } from '@state/helpers'

export default {
  components: {},
  computed: {
    ...authComputed,
  },
  methods: {},
}
</script>

<template>
  <footer class="footer">
    <div class="container-fluid">
      <div class="row">
        <div class="col-md-6">
          2019 - 2020 &copy; LifeLine by <a href="https://github.com/EZ-hwh/Software-Engineering">Software Engineer Group 2</a>
        </div>
        <div class="col-md-6">
          <div class="text-md-right footer-links d-none d-sm-block">
            <a href="https://github.com/EZ-hwh/Software-Engineering">About Us</a>
            <a href="https://github.com/EZ-hwh/Software-Engineering">Help</a>
            <a href="https://github.com/EZ-hwh/Software-Engineering">Contact Us</a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<style lang="scss"></style>
