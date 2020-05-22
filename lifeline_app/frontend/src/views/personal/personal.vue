<template>


  <div class="text-center card-box">

    <div class="circle" @click="showChooseImg">
      <img :src="userImg">
    </div>

    <div class="default-img animated" v-show="showChooseAvatar">
      <ul>
        <li v-for="item in imgList" :key="item.id">
          <img :src="item.imgUrl" alt="" width="100px" @click="chooseImg(item.imgUrl)">
        </li>
      </ul>
    </div>

    <div>
      <p class="text-muted font-13 mb-4">
        {{formValidate.desc}}
      </p>

      <div class="">
        <p class="text-muted font-15"><strong>用户名 :</strong> <span class="ml-2">{{formValidate.name}}</span></p>
        <p><br></p>
        <p class="text-muted font-15"><strong>联系方式 :</strong><span class="ml-2">{{formValidate.phone}}</span></p>
        <p><br></p>
        <p class="text-muted font-15"><strong>Email :</strong> <span class="ml-2">{{formValidate.mail}}</span></p>
        <p><br></p>
        <p class="text-muted font-15"><strong>地址 :</strong> <span class="ml-2">{{formValidate.address}}</span></p>
        <p><br></p>
        <p><br></p>

      </div>
      <button type="button" @click="modal1=true,formValidate2=JSON.parse(JSON.stringify(formValidate))" class="btn btn-primary btn-rounded waves-effect waves-light">修改个人信息</button>
      <button v-if="!elearning_stats" type="button" @click="modal2=true" class="btn btn-primary btn-rounded waves-effect waves-light">登录elearning</button>
      <button v-if="elearning_stats" type="button" @click="del_register" class="btn btn-primary btn-rounded waves-effect waves-light">退出elearning登录</button>

      <Modal v-model="modal1" width="360">
        <p slot="header" style="color:#98a6ad;text-align:center">
          <Icon type="ios-bulb" />
          <span>个人信息修改</span>
        </p>
        <div style="text-align:center">
          <Form ref="formValidate" :model="formValidate2" :rules="ruleValidate" :label-width="80">
            <FormItem label="用户名" prop="name">
              <Input v-model="formValidate2.name" placeholder="请输入您的用户名"></Input>
            </FormItem>
            <FormItem label="个人简介" prop="desc">
              <Input v-model="formValidate2.desc" type="textarea" :autosize="{minRows: 2,maxRows: 5}" placeholder="请输入您的个人简介"></Input>
            </FormItem>

            <FormItem label="联系方式" prop="phone">
              <Input v-model="formValidate2.phone" placeholder="请输入您的联系方式"></Input>
            </FormItem>

            <FormItem label="E-mail" prop="mail">
              <Input v-model="formValidate2.mail" placeholder="请输入您的e-mail"></Input>
            </FormItem>

            <FormItem label="地址" prop="address">
              <Input v-model="formValidate2.address" placeholder="请输入您的地址"></Input>
            </FormItem>

          </Form>

        </div>
        <div slot="footer" style="">
          <Button :loading="modal_loading" @click="change_del">返回</Button>
          <Button type="primary" :loading="modal_loading" @click="handleSubmit('formValidate')">确认修改</Button>
        </div>
      </Modal>

      <Modal v-model="modal2" width="360">
        <p slot="header" style="color:#98a6ad;text-align:center">
          <Icon type="ios-bulb" />
          <span>elearning登录</span>
        </p>
        <div style="text-align:center">
            <Input prefix="ios-contact" v-model="elearning_username" placeholder="请输入elearning账号"  />
          <p><br></p>
            <Input prefix='md-keypad' v-model="elearning_password" type="password" password placeholder="请输入elearning密码" />
        </div>
        <div slot="footer" style="">
          <Button :loading="modal_loading" @click="register_del">返回</Button>
          <Button type="primary" :loading="modal_loading" @click="try_register">登录</Button>
        </div>
      </Modal>

    </div>
  </div>

</template>

<script>
    export default {
        name: "personal",
        data () {
        return {
          userImg:'/static/img/user0.png',
          showChooseAvatar: false,
          imgList:[
            {
              'id':1,
              imgUrl:'/static/img/user0.png'
            },
            {
              'id':2,
              imgUrl:'/static/img/user1.png'
            },
            {
              'id':3,
              imgUrl:'/static/img/user2.png'
            },
            {
              'id':4,
              imgUrl:'/static/img/user3.png'
            },
            {
              'id':5,
              imgUrl:'/static/img/user4.png'
            },
            {
              'id':6,
              imgUrl:'/static/img/user5.png'
            },
            {
              'id':7,
              imgUrl:'/static/img/user6.png'
            },
            {
              'id':8,
              imgUrl:'/static/img/user7.png'
            },
            {
              'id':9,
              imgUrl:'/static/img/user8.png'
            }
          ],
          elearning_username:'',
          elearning_password:'',
          elearning_stats:false,
          modal_loading: false,
          modal1: false,
          modal2:false,
          formValidate: {
            name: '小白',
            mail: '12345678901@fudan.edu.cn',
            phone: '123131312311',
            address: '高科苑1-1',
            desc: '玻璃晴朗，橘子辉煌'
          },
          formValidate2: {
            name: '',
            mail: '',
            phone: '',
            address: '',
            desc: ''
          },
          ruleValidate: {
            name: [
              { required: true, message: 'The name cannot be empty', trigger: 'blur' }
            ],
            mail: [
              { required: false, message: 'Mailbox cannot be empty', trigger: 'blur' },
              { type: 'email', message: 'Incorrect email format', trigger: 'blur' }
            ],
            desc: [
              { required: false, message: 'Please enter a personal introduction', trigger: 'blur' },
              { type: 'string', min: 5, message: 'Introduce no less than 5 words', trigger: 'blur' }
            ],
            address: [
              { required: false, message: 'Please enter a personal introduction', trigger: 'blur' }
            ],
            phone: [
              { required: false, message: 'Please enter a personal introduction', trigger: 'blur' }
            ]


          }
        }

              },
      methods: {
        chooseImg (imgUrl) {
          localStorage.setItem('avatar', imgUrl)
          this.userImg = localStorage.getItem('avatar')
          this.$ajax({
            method: "post",
            url: "/picture/",
            params: {
              pic:this.userImg
            },
          })
            .catch(function(error) {
              console.log(error);
            });

          this.showChooseAvatar = false


        },
        showChooseImg () {
          this.showChooseAvatar = true
        }
        ,
          del_register()
          {
            this.elearning_stats=false;
            this.elearning_password='';
            this.elearning_username='';
            this.$ajax({
              method: "get",
              url: "/elearning_del_register/"
            })
              .then((response) => {
                this.elearning_stats=response.data.flag;
                })
              .catch(function(error) {
                console.log(error);
              });

            this.$Message.success('退出elearning');
          },
          change_del(){
            this.modal_loading = false;
            this.modal1 = false;
            this.$Message.success('结束修改');
          },
        register_del()
        {
          this.modal_loading = false;
          this.modal2 = false;
          this.$Message.success('返回个人信息界面');
        },
        try_register()
        {

          this.$ajax({
            method: "post",
            url: "/elearning_register/",
            params: {
                username:this.elearning_username ,
                password:this.elearning_password
            },
          })
            .then((response) => {
              this.elearning_stats=response.data.flag;
            })
            .catch(function(error) {
              console.log(error);
            });

          if(this.elearning_stats== true){
            this.modal_loading = false;
            this.modal2 = false;
            this.$Message.success('登录成功');
          }
          else {
            console.log('fail')
            this.$Message.success('登录失败，请重新登录');
          }
        },
        handleSubmit (name) {

          this.$refs[name].validate((valid) => {
            if (valid) {
              this.formValidate=this.formValidate2
              this.$Message.success('成功修改!');
            } else {
              this.$Message.error('修改失败!');
            }
          })
          this.$ajax({
            method: "post",
            url: "/information/",
            params: {
              name:this.formValidate.name ,
              addr:this.formValidate.address,
              mail:this.formValidate.mail,
              phone:this.formValidate.phone,
              desc:this.formValidate.desc
            },
          })
            .catch(function(error) {
              console.log(error);
            });


        },
        handleReset (name) {
          this.$refs[name].resetFields();
        },

        }

    }
</script scope>

</style>
