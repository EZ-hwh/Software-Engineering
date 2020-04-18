<template>
  <div class="card-box">
    <div class="dropdown float-right">
      <a
        href="#"
        class="dropdown-toggle arrow-none card-drop"
        data-toggle="dropdown"
        aria-expanded="false"
      >
        <i class="mdi mdi-dots-vertical"></i>
      </a>
      <div class="dropdown-menu dropdown-menu-right">
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">Action</a>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">Another action</a>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">Something else</a>
        <!-- item-->
        <a href="javascript:void(0);" class="dropdown-item">Separated link</a>
      </div>
    </div>

    <h4 class="header-title mt-0">Today</h4>

    <p class="text-muted font-13">
      PLEASE DO THEM TODAY!
    </p>
    <div v-for="(value,index) in TodayList" :key="value">
      <div class="checkbox checkbox-success">
        <input :id="'checkbox'+index" type="checkbox" aria-label="Single checkbox One"/>
        <label :for="'checkbox'+index">
          {{ value }}
        </label>
      </div>
    </div>
  </div>
</template>

<script>
import data from '../../../datasample.json'

export default {
  components: {},
  data() {
    return {
      TodayList:data.TodayList,
    }
  },
  methods: {},
}
</script>
