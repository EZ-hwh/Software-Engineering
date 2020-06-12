<template>
    <div id="document">
        <h3>{{course.name}}</h3>
        <Tree :data="course.docs" ref="tree" show-checkbox @on-select-change="click_download($event)"
              @on-check-change="select_box($event)">
        </Tree>
        <Button icon="ios-download-outline" @click="getalldownload">下载</Button>
    </div>
</template>

<script>
    export default {
        name: "document",
        methods:
            {

                click_download(data) {
                    console.log('downloading...')

                    console.log(data[0].title)
                    if (!data[0].urls) {
                        return
                    }

                    let urls = data[0].urls
                    let link = document.createElement('a')
                    link.style.display = 'none'
                    link.href = urls
                    link.setAttribute('download', data[0].title)

                    document.body.appendChild(link)
                    link.click()
                },
                select_box(data) {
                    console.log("tree.data", this.$refs.tree.data);
                    console.log('selecting...')
                    this.select = this.$refs.tree.getCheckedNodes();
                    console.log(this.select)

                },
                downloadall(url) {
                    console.log(url)
                    const iframe = document.createElement("iframe");
                    iframe.style.display = "none"; // 防止影响页面
                    iframe.style.height = 0; // 防止影响页面
                    iframe.src = url;
                    document.body.appendChild(iframe); // 这一行必须，iframe挂在到dom树上才会发请求
                    // 5分钟之后删除（onload方法对于下载链接不起作用，就先抠脚一下吧）
                    setTimeout(() => {
                        iframe.remove();
                    }, 5 * 60 * 1000);
                },
                getalldownload(data) {
                    console.log('downloading many in one time')
                    console.log(this.select)
                    this.select.forEach(item => {
                        console.log(item)
                        if (item.urls) {
                            let urls = item.urls
                            this.downloadall(urls)

//                                       let link = document.createElement('a')
//                                       link.style.display = 'none'
//                                       link.href = urls
//                                       link.setAttribute('download',item.title)
//                                       document.body.appendChild(link)
//                                       link.click()
//                                       console.log(link)
                        }
                    })


                }
            },

        data() {
            return {
                select: [],
                course: {},
            }
        },
        created() {
            this.$ajax.get('/get_course_detail')
                .then(response => {
                    console.log(response.data.course)
                    this.course = response.data
                })
        }
    }
</script>

<style scoped>

</style>
