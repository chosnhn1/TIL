<template>
  <li class="list-group-item d-flex justify-content-between">
    <span class="flex-grow-1" :class="{'is-completed': todo.isCompleted}"  @click="updateTodoStatus">{{ todo.title }}
    </span>
    <span class="ms-3"><button class="btn btn-warning" @click="deleteTodo">Delete</button></span>
  </li>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {
    updateTodoStatus: function () {
      this.$store.dispatch('updateTodoStatus', this.todo)
    },
    deleteTodo: function () {
      this.$store.dispatch('deleteTodo', this.todo)
    },
  },
}
</script>

<style>
  .is-completed {
    text-decoration: line-through;
  }
</style>