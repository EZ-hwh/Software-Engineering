## personal information界面

### 后端数据
具体详情可以见personal.vue
1. 个人信息
name：用户名 string类型
mail：用户邮箱 string类型
phone：用户电话
address：用户地址
desc：用户个人信息描述
这些信息应该在用户刚注册的时候都为空，或者用户名为初始注册时用户名，展示需要从后端传数据。
用户可以修改这些信息，每一次修改都应该将修改结果传给后端。用户修改完成的函数在personal.vue里面methods里的handleSubmit函数
```
        handleSubmit (name) {
          this.$refs[name].validate((valid) => {
            if (valid) {
              this.formValidate=this.formValidate2
              #####应该把传回后端数据的一步添加在这个地方#####
              this.$Message.success('成功修改!');
            } else {
              this.$Message.error('修改失败!');
            }
          })
        }
```
2. elearning登录
elearning_username:用户elearning 用户名
elearning_password:用户elearning 密码
elearning_stats: 用户是否处于登录状态 bool类 登录状态为True，否则为False，初始为False
用户通过methods里面的try_register进行登录，调用这个函数时this.elearning_username和elearning_password应该传输给后端，后端传输回elearning_stats。(这部分逻辑我就不太确定了，此处@yst)
如果用户并非第一次登录，之前曾经登录过elearning账号的话，可以通过同样的del_register函数进行退出登录。可以通过将this.elearning_username和elearning_password都设为’‘，进行退出登录？此时也需要向后端传数据。
3. 不知道怎么在vue的methods里加注释，我把应该需要填传输的地方多打了几个空格。

### 具体实现过程
1. 显示个人信息
这部分比较好做，为了统一格式，采用的是素材库里的用户信息界面，通过简单的删除和调整界面得到现在的展示页面，用到了src/assets/css/里面的css

2. 修改个人信息
使用了iview组件，创建了一个Modal(personal.vue 里面的 Modal1)，通过 ‘修改个人信息’ button 展现这个Modal，在click这个按钮的时候，会展示这个Modal并且将此时的用户信息复制一份，用于修改，避免产生用户最后放弃修改却污染了原数据的情况。
在Modal1中通过 header和footer定义Modal的一些信息，在footer中定义了两个button，一个用于不保存修改直接返回，click这个button会调用change_del这个函数，直接关闭Modal1。一个用于保存用户修改并关闭Modal1，调用的是handleSubmit这个函数，这个函数将之前复制的已修改过的表单复制回用于展示的数据，并且将修改提交给后端（提交后端目前未实现）
在Modal1的主题部分是一个表单 formValidate，展现的是data里面formValidate2的数据，可以通过定义data里面的ruleValidate对表单的修改进行限定，目前的限定是描述的话至少5个单词，邮箱必须符合规范。

3. elearning登录
和修改个人信息同理，通过‘elearning’登录的button，click可以显示Modal2，Modal2的结构和Modal1大致相同，在主体部分由一个表单变成了两个input，用于用户输入账户和密码。
footer中有两个按钮，一个用于登录，一个用于返回。返回按钮调用register_del直接关闭Modal，登录按钮通过调用try_register按钮试图登录。向后端传输数据，接受登录情况，进行不同的反馈。
如果用户已经登录的话即elearning_stats=True，会出现‘退出’按钮，通过点击这个按钮将数据库内的elearning相关数据删除，将elearning_stats变为False，可以重新登录。

### 实现结果
可以展示用户的个人信息
可以修改用户的个人信息
可以进行elearning的登录和退出

