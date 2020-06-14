<template>
    <div id="homework">
        <h3>未完成作业</h3>
        <p></p>
        <List item-layout="vertical" :border="true">
        <ListItem v-for="item in course.not_done" :key="item.title">
            <ListItemMeta  :title="item.title"  />
            <div v-html="item.description"></div>
            {{ item.content }}
            <template slot="action">
                <li>
                    <Icon type="logo-freebsd-devil" /> DDL: {{item.ddl}}
                </li>
                <li>
                    <Icon type="ios-star" /> score: {{item.score}}
                </li>
            </template>
            <template>
                <Upload action="//jsonplaceholder.typicode.com/posts/">
                    <Button icon="ios-cloud-upload-outline">上传文件</Button>
                </Upload>
                    <Button>提交</Button>

            </template>

        </ListItem>
    </List>
        <p></p>
        <p></p>
        <h3>已完成作业</h3>
        <p></p>

    <List item-layout="vertical" :border="true">
        <ListItem v-for="item in course.done" :key="item.title">
            <ListItemMeta  :title="item.title"  />
            <div v-html="item.description"></div>
            {{ item.content }}
            <p></p>
            <p></p>
            评分:{{item.grade}}
            <p></p>
            <p></p>
            评价:{{item.comment}}
            <p></p>
            <p></p>
            已上传的文件:<div v-html="item.submission"></div>
            <template slot="action">
                <li v-show="item.finish">
                    <Icon type="md-checkmark-circle" /> 已完成作业

                </li>
                <li v-show="!item.finish">
                    <Icon type="ios-close-circle" /> 超时未完成作业
                </li>
            </template>
        </ListItem>
    </List>

    </div>
</template>
<script>
    export default {
        name:'homework',
        data () {
            return {
                course:{}
            }
        },
        Created() {
            this.$ajax.get('get_course_homework')
                .then(response => {
                    console.log(response.data)
                    this.course = response.data
                })
        }
    }
</script>