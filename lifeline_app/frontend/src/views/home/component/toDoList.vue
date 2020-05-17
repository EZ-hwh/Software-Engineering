<template>
  <div>
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
          <a href="javascript:void(0);" @click="complete(0)" class="dropdown-item">Complete All</a>
          <!-- item-->
          <a href="javascript:void(0);" @click="undo(0)" class="dropdown-item">Undo All</a>
        </div>
      </div>

      <h4 class="header-title mt-0 mb-3 text-primary">DDL Today</h4>

      <ul class="sortable-list list-unstyled taskList" id="upcoming">
        <li v-for="ddl in TodayList" :key="ddl">
          <div class="kanban-box">
            <div class="checkbox-wrapper float-left">
              <div v-if="ddl['status'] == 2">
                <div class="checkbox checkbox-custom">
                  <input type="checkbox" id="checkbox10" checked disabled />
                  <label></label>
                </div>
              </div>
              <div v-else>
                <div class="checkbox checkbox-success checkbox-single">
                  <input
                    @click="checkbox(ddl['id'], ddl['status'])"
                    type="checkbox"
                    :id="'singleCheckbox' + ddl['id']"
                    value="option2"
                    :checked="ddl['status'] == 1 ? 'checked' : ''"
                    aria-label="Single checkbox Two"
                  />
                  <label></label>
                </div>
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
          href="#"
          class="btn btn-primary waves-effect waves-light"
          data-toggle="modal"
          data-target="#addnew"
        >
          <i class="mdi mdi-plus"></i> Add New
        </a>
        <!-- Modal -->
        <div class="modal fade none-border" id="addnew">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h4 class="modal-title mt-0"><strong>Add new DDL </strong></h4>
                <button
                  type="button"
                  class="close"
                  data-dismiss="modal"
                  aria-hidden="true"
                >
                  &times;
                </button>
              </div>
              <div class="modal-body">
                <form role="form">
                  <div class="row">
                    <div class="col-md-6">
                      <label class="control-label">DDL name</label>
                      <input
                        class="form-control form-white"
                        placeholder="Enter name"
                        type="text"
                        v-model="ddlname"
                      />
                    </div>
                    <div class="col-md-6">
                      <label class="control-label">DDL time</label>
                      <input
                        class="form-control form-white"
                        placeholder="Enter time"
                        type="text"
                        v-model="ddltime"
                      />
                    </div>
                    <div class="col-md-12">
                      <label class="control-label">Description</label>
                      <input
                        class="form-control form-white"
                        placeholder="Enter description"
                        type="text"
                        v-model="ddldescription"
                      />
                    </div>
                  </div>
                </form>
              </div>
              <div class="modal-footer">
                <button
                  type="button"
                  class="btn btn-light waves-effect"
                  data-dismiss="modal"
                >
                  Close
                </button>
                <button
                  @click="add_ddl"
                  type="button"
                  class="btn btn-danger waves-effect waves-light save-category"
                  data-dismiss="modal"
                >
                  Save
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
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
          <a href="javascript:void(0);" @click="complete(1)" class="dropdown-item">Complete All</a>
          <!-- item-->
          <a href="javascript:void(0);" @click="undo(1)" class="dropdown-item">Undo All</a>
        </div>
      </div>

      <h4 class="header-title mt-0 mb-3 text-primary">DDL Aheads</h4>

      <ul class="sortable-list list-unstyled taskList" id="upcoming">
        <li v-for="ddl in WeekList" :key="ddl">
          <div class="kanban-box">
            <div class="checkbox-wrapper float-left">
              <div v-if="ddl['status'] == 2">
                <div class="checkbox checkbox-custom">
                  <input type="checkbox" id="checkbox10" checked disabled />
                  <label></label>
                </div>
              </div>
              <div v-else>
                <div class="checkbox checkbox-success checkbox-single">
                  <input
                    @click="checkbox(ddl['id'], ddl['status'])"
                    type="checkbox"
                    :id="'singleCheckbox' + ddl['id']"
                    value="option2"
                    :checked="ddl['status'] == 1 ? 'checked' : ''"
                    aria-label="Single checkbox Two"
                  />
                  <label></label>
                </div>
              </div>
            </div>

            <div class="kanban-detail">
              <span class="badge badge-warning float-right">{{
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
          href="#"
          class="btn btn-primary waves-effect waves-light"
          data-toggle="modal"
          data-target="#addnew"
        >
          <i class="mdi mdi-plus"></i> Add New
        </a>
      </div>
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
      WeekList: null,
      ddlname: null,
      ddltime: null,
      ddldesciption: null,
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
    update_weeklist: function() {
      this.$ajax({
        method: "get",
        url: "/get_Weeklist/",
        params: {
          type: "log",
        },
      })
        .then((response) => {
          if (response.data.flag === true) {
            console.log("get info week");
            this.WeekList = response.data.WeekList;
            // console.log(response.data.WeekList[1]);
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
            this.update_todaylist();
            this.update_weeklist();
          } else {
            console.log(response.data.error_msg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    add_ddl: function() {
      this.$ajax({
        method: "get",
        url: "/add_ddl/",
        params: {
          name: ddlname,
          time: ddltime,
          description: ddldesciption,
          type: "log",
        },
      })
        .then((response) => {
          if (response.data.flag === true) {
            console.log("add ddl");
            update_todaylist();
          } else {
            console.log(response.data.error_msg);
          }
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    complete: function(todo){
      var temp;
      if(todo==0)
        temp = this.TodayList;
      else 
        temp = this.WeekList;
      for(ddl in temp)
        if(ddl["status"]==0)
          this.checkbox(ddl["id"], ddl["status"]);
    },
    undo: function(undo){
      var temp;
      if(undo==0)
        temp = this.TodayList;
      else 
        temp = this.WeekList;
      for(ddl in temp)
        if(ddl["status"]==1)
          this.checkbox(ddl["id"], ddl["status"]);
    }
  },
  created: function() {
    this.update_todaylist();
    this.update_weeklist();
  },
};
</script>
