<template>
  <div class="row g-3 justify-content-center align-items-center">
    <div class="col-3">
    <input class="form-control" v-model.trim="todoTitle" @keyup.enter="createTodo" type="text">
    </div>
    <div class="col-auto">
    <button class="btn btn-primary" @click="createTodo" >Add</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: null,
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        isCompleted: false,
        date: new Date().getTime(),
      }
      if (todoItem.title) {
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = null
    },
  },
}
</script>

<style>

</style>