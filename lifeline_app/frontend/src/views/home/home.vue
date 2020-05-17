<script>
    import appConfig from '../../app.config'
    import Layout from '../../components/template/TopBarLayout/main'
    import Calendar from './component/calendar.vue'
    import ToDoList from './component/toDoList.vue'
    import ToDoListWeek from './component/toDoListWeek.vue'
    import $ from "jquery"

    export default {
        page: {
            title: 'LifeLine',
            meta: [{name: 'description', content: appConfig.description}],
        },
        components: {Layout, Calendar, ToDoList, ToDoListWeek},
    }
</script>

<template>
    <div id="home">
        <Layout>
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box">
                        <div class="page-title-right">
                            <ol class="breadcrumb m-0">
                                <li class="breadcrumb-item">
                                    <a href="javascript: void(0);">LifeLine</a>
                                </li>
                                <li class="breadcrumb-item active">Curriculum</li>
                            </ol>
                        </div>
                        <h4 class="page-title">Keep studying.</h4>
                    </div>
                </div>
            </div>
            <!-- end page title -->
            <!-- <Calendar></Calendar> -->

            <div class="row">
                <div class="col-lg-12">
                    <div class="row">

                        <div class="col-lg-3">
                            <ToDoList/>
                        </div>
                        
                        

                        <!-- end col-->
                        <div class="col-lg-9">
                            <Calendar/>
                        </div>
                        <!-- end col -->
                    </div>
                    <!-- end row -->

                    <!-- BEGIN MODAL -->
                    <div class="modal fade none-border" id="event-modal">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h4 class="modal-title mt-0">
                                        <strong>Add New Event</strong>
                                    </h4>
                                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                                        &times;
                                    </button>
                                </div>
                                <div class="modal-body"></div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-light waves-effect" data-dismiss="modal">
                                        Close
                                    </button>
                                    <button
                                            type="button"
                                            class="btn btn-success save-event waves-effect waves-light"
                                    >Create event
                                    </button>
                                    <button
                                            type="button"
                                            class="btn btn-danger delete-event waves-effect waves-light"
                                            data-dismiss="modal"
                                    >Delete
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Modal Add Category -->
                    <div class="modal fade none-border" id="add-category">
                        <div class="modal-dialog">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h4 class="modal-title mt-0">
                                        <strong>Add a category</strong>
                                    </h4>
                                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                                        &times;
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <form role="form">
                                        <div class="row">
                                            <div class="col-md-6">
                                                <label class="control-label">Category Name</label>
                                                <input
                                                        class="form-control form-white"
                                                        placeholder="Enter name"
                                                        type="text"
                                                        name="category-name"
                                                />
                                            </div>
                                            <div class="col-md-6">
                                                <label class="control-label">Choose Category Color</label>
                                                <select
                                                        class="form-control form-white"
                                                        data-placeholder="Choose a color..."
                                                        name="category-color"
                                                >
                                                    <option value="success">Success</option>
                                                    <option value="danger">Danger</option>
                                                    <option value="info">Info</option>
                                                    <option value="pink">Pink</option>
                                                    <option value="primary">Primary</option>
                                                    <option value="warning">Warning</option>
                                                    <option value="inverse">Inverse</option>
                                                </select>
                                            </div>
                                        </div>
                                    </form>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-light waves-effect" data-dismiss="modal">
                                        Close
                                    </button>
                                    <button
                                            type="button"
                                            class="btn btn-danger waves-effect waves-light save-category"
                                            data-dismiss="modal"
                                    >Save
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- END MODAL -->
                </div>
                <!-- end col-12 -->
            </div>
            <!-- end row -->
        </Layout>
    </div>
</template>

<style lang="scss">
    // Allow element/type selectors, because this is global CSS.
    // stylelint-disable selector-max-type, selector-class-pattern

    // Design variables and utilities from src/TopBarDesign.
    @import '../../assets/css/TopBarDesign';
</style>