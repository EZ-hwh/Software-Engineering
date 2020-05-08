<script>
export default {
  components: {},
  props: {
    title: {
      type: String,
      default: '',
    },
    items: {
      type: Array,
      default: () => {
        return []
      },
    },
  },
}
</script>

<template>
  <!-- start page title -->
  <div class="row">
    <div class="col-12">
      <div class="page-title-box">
        <div class="page-title-right">
          <b-breadcrumb
            :items="items"
            class="m-0"
          ></b-breadcrumb>
        </div>
        <h4 class="page-title">{{ title }}</h4>
      </div>
    </div>
  </div>
  <!-- end page title -->
</template>
