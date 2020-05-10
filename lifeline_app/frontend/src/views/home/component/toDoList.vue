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
                type="checkbox"
                id="singleCheckbox2"
                value="option2"
                aria-label="Single checkbox Two"
              />
              <label></label>
            </div>
          </div>

          <div class="kanban-detail">
            <span class="badge badge-danger float-right">{{ ddl[1] }}</span>
            <h5 class="mt-0">
              <a href="" class="text-dark">{{ ddl[0] }}</a>
            </h5>

            <ul class="list-inline">
              <!-- <button type="button" class="btn btn-info btn-xs" id="sa-success">Click me</button> -->
              <li class="list-inline-item">
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="Username"
                >
                  <img
                    src="../../../assets/images/user/user-1.jpg"
                    alt="img"
                    class="avatar-sm rounded-circle"
                  />
                </a>
              </li>
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
                {{ ddl[2] }}
              </li>
            </ul>
          </div>
        </div>
      </li>

      <!-- <li>
        <div class="kanban-box">
          <div class="checkbox-wrapper float-left">
            <div class="checkbox checkbox-success checkbox-single">
              <input
                type="checkbox"
                id="singleCheckbox3"
                value="option3"
                aria-label="Single checkbox Two"
              />
              <label></label>
            </div>
          </div>

          <div class="kanban-detail">
            <span class="badge badge-warning float-right">High</span>
            <h5 class="mt-0">
              <a href="" class="text-dark"
                >Write a release note for Admin v1.5</a
              >
            </h5>
            <ul class="list-inline">
              <li class="list-inline-item">
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="Username"
                >
                  <img
                    src="assets/images/users/user-3.jpg"
                    alt="img"
                    class="avatar-sm rounded-circle"
                  />
                </a>
              </li>
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
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="3 Comments"
                >
                  <i class="mdi mdi-comment-outline"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </li>

      <li>
        <div class="kanban-box">
          <div class="checkbox-wrapper float-left">
            <div class="checkbox checkbox-success checkbox-single">
              <input
                type="checkbox"
                id="singleCheckbox4"
                value="option4"
                aria-label="Single checkbox Two"
              />
              <label></label>
            </div>
          </div>

          <div class="kanban-detail">
            <h5 class="mt-0">
              <a href="" class="text-dark">Invite user to a project</a>
            </h5>
            <ul class="list-inline">
              <li class="list-inline-item">
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="Username"
                >
                  <img
                    src="assets/images/users/user-4.jpg"
                    alt="img"
                    class="avatar-sm rounded-circle"
                  />
                </a>
              </li>
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
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="3 Comments"
                >
                  <i class="mdi mdi-comment-outline"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </li>

      <li>
        <div class="kanban-box">
          <div class="checkbox-wrapper float-left">
            <div class="checkbox checkbox-success checkbox-single">
              <input
                type="checkbox"
                id="singleCheckbox5"
                value="option2"
                aria-label="Single checkbox Two"
              />
              <label></label>
            </div>
          </div>

          <div class="kanban-detail">
            <span class="badge badge-danger float-right">Urgent</span>
            <h5 class="mt-0">
              <a href="" class="text-dark"
                >Code HTML email template for welcome email</a
              >
            </h5>
            <ul class="list-inline">
              <li class="list-inline-item">
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="Username"
                >
                  <img
                    src="assets/images/users/user-5.jpg"
                    alt="img"
                    class="avatar-sm rounded-circle"
                  />
                </a>
              </li>
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
                <a
                  href=""
                  data-toggle="tooltip"
                  data-placement="top"
                  title=""
                  data-original-title="3 Comments"
                >
                  <i class="mdi mdi-comment-outline"></i>
                </a>
              </li>
            </ul>
          </div>
        </div>
      </li> -->
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
  methods: {},
  created: function() {
    this.$ajax({
      method: "post",
      url: "/home/todaylist/",
      params: {
        // 后端应该保存了现在登陆的人？
        type: "log",
      },
    })
      .then((response) => {
        if (response.data.flag == true) {
          this.TodayList = response.data.TodayList;
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
