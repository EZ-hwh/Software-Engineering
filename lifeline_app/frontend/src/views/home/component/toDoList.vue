<template>
  <div class="card-box taskboard-box">
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

    <h4 class="header-title mt-0 mb-3 text-primary">DDL Today</h4>

    <ul class="sortable-list list-unstyled taskList" id="upcoming">
      <li v-for="ddl in TodayList" :key="ddl">
        <div class="kanban-box">
          <div class="checkbox-wrapper float-left">
            <div class="checkbox checkbox-success checkbox-single">
              <input
                @click="check_todolist(ddl['id'], ddl['status'])"
                type="checkbox"
                :id="'singleCheckbox' + ddl['id']"
                value="option2"
                :checked="ddl['status'] == 1 ? 'checked' : ''"
                :disabled="ddl['status'] == 2 ? 'disabled' : ''"
                aria-label="Single checkbox Two"
              />
              <label></label>
            </div>
          </div>

          <div class="kanban-detail">
            <span class="badge badge-danger float-right">{{
              ddl["time"]
            }}</span>
            <h5 class="mt-0">
              <a href="" class="text-dark">{{ ddl["name"] }}</a>
            </h5>

            <ul class="list-inline">
              <!-- <button type="button" class="btn btn-info btn-xs" id="sa-success">Click me</button> -->

              <li class="list-inline-item">
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="5 Tasks"
                >
                  <i class="mdi mdi-format-align-left"></i>
                </a>
              </li>
              <li class="list-inline-item">
                {{ ddl["description"] }}
              </li>
            </ul>
          </div>
        </div>
      </li>
    </ul>

    <div class="text-center pt-2">
      <a
        href="#custom-modal"
        class="btn btn-primary waves-effect waves-light"
        data-animation="fadein"
        data-plugin="custommodal"
        data-overlaySpeed="200"
        data-overlayColor="#36404a"
      >
        <i class="mdi mdi-plus"></i> Add New
      </a>
    </div>
  </div>
</template>

<script>
// import data from "../../../datasample.json";

export default {
  components: {},
  data() {
    return {
      TodayList: null,
    };
  },
  methods: {
    update_todaylist: function() {
      this.$ajax({
        method: "get",
        url: "/get_Todaylist/",
        params: {
          // 后端应该保存了现在登陆的人？
          type: "log",
        },
      })
        .then((response) => {
          if (response.data.flag === true) {
            console.log("get info");
            this.TodayList = response.data.TodayList;
            console.log(response.data.TodayList[1]);
          } else {
            console.log(response.data.error_msg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    checkbox: function(id, std) {
      this.$ajax({
        method: "get",
        url: "/check_todolist/",
        params: {
          data_check: id,
          data_status: !std,
          type: "log",
        },
      })
        .then((response) => {
          if (response.data.flag === true) {
            console.log("check");
            update_todaylist();
          } else {
            console.log(response.data.error_msg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
  },
  created: function() {
      this.$ajax({
        method: "get",
        url: "/get_Todaylist/",
        params: {
          // 后端应该保存了现在登陆的人？
          type: "log",
        },
      })
        .then((response) => {
          if (response.data.flag === true) {
            console.log("get info");
            this.TodayList = response.data.TodayList;
            console.log(response.data.TodayList[1]);
          } else {
            console.log(response.data.error_msg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
};
</script>
