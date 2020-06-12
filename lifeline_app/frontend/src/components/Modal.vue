<template>
        <div>
            <div>
                {{ title }}
            </div>
            <div>
                <slot></slot>
            </div>
            <div class="modal-footer">
                <button @click="submit">OH I Understand...</button>
            </div>
        </div>
</template>

<script>
    export default {
        name: "Modal",
        props: {
            title: {
                type: String,
                default: ""
            }
        },
        methods: {
            submit(){
                this.$emit('submit')
            }
        }
    }
</script>

<style scoped>

</style>