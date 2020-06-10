<template>
  <!-- end col-->
  <div>
    <div class="row">
      <div class="col-lg-11">
        <div class="card-box">
          <div id="calendar"></div>
        </div>
      </div>
    </div>
    <!-- end col -->
  </div>
</template>

<script>
import $ from "jquery";
import "bootstrap";
import "moment";
import "jquery-ui/ui/widgets/draggable";
import "jquery-ui/ui/widgets/droppable";
import "jquery-ui/ui/widgets/resizable";
import "../../../assets/libs/jquery-ui/jquery-ui.min.js";

import "../../../assets/libs/fullcalendar/fullcalendar.min.js";
import {
  calendar1,
  calendar2,
} from "../../../assets/js/pages/fullcalendar.init.js";

export default {
  components: {},
  data() {
    return {
      courseList: null,
    };
  },
  mounted: function() {
    console.log("now working")
    this.get_schedule();
    // this.courseList = ;
    // console.log($);    
  },
  methods: {
    get_schedule: function() {
      this.$ajax({
        method: "get",
        url: "/get_schedule/",
      })
        .then((response) => {
          if (response.data.flag === true) {
            console.log("get schedule");
            this.courseList = response.data.course;
            console.log(this.courseList);
            calendar1($, this.courseList);
            calendar2();
          } else {
            this.$ajax({
              method: "get",
              url: "/personal/",
            });
            console.log(response.data.error_msg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
};
</script>

<style>
@import url("../../../assets/libs/fullcalendar/fullcalendar.min.css");
/* @import url("../../../assets/css/bootstrap.min.css"); */
</style>
