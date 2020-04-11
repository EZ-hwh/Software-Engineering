<template>
    <div id="homework">
        <h3>未完成作业</h3>
        <p></p>
        <List item-layout="vertical" border="true">
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

    <List item-layout="vertical" border="true">
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
                course:{
                    name: 'COMP130011.01 算法设计与分析 Algorithm Design and Analysis',
                    not_done:[
                        {
                            title: '算法设计与分析作业3',
                            description: '<a class="instructure_file_link" title="算法设计与分析习题 3.pdf" href="https://elearning.fudan.edu.cn/files/519713/download?wrap=1">算法设计与分析习题 3.pdf</a>',
                            content: '第三次算法与设计分析作业，具体内容见文档',
                            ddl:'4.14日 13：30前',
                            score:'10'
                        }
                    ],
                    done:[
                        {
                            title: '算法设计与分析作业2',
                            description: '<a class="instructure_file_link" title="算法设计与分析习题 2.pdf" href="https://elearning.fudan.edu.cn/files/519713/download?wrap=1">算法设计与分析习题 2.pdf</a>',
                            content: '第二次算法与设计分析作业，具体内容见文档',
                            ddl:'4.6日 13：30前',
                            score:'10',
                            grade:'A',
                            comment:'nice!',
                            finish:true,
                            submission:'<a href="/courses/22322/assignments/8981/submissions/14325?download=480636">\n' + '            下载 17307130254-2.pdf\n' + '          </a>'
                        },
                        {
                            title: '算法设计与分析作业1',
                            description: '<a class="instructure_file_link" title="算法设计与分析习题 1.pdf" href="https://elearning.fudan.edu.cn/files/519713/download?wrap=1">算法设计与分析习题 1.pdf</a>',
                            content: '第一次算法与设计分析作业，具体内容见文档',
                            ddl:'4.1日 13：30前',
                            score:'10',
                            grade:'D',
                            comment:'where is your homework??',
                            finish:false,
                            submission: ''
                        }
                    ]
                }
            }
        }
    }
</script>