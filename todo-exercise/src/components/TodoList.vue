<template>
  <div>
    <div class="col-10 offset-1">
      <div class="row text-center">
        <h1>Todo List</h1>
        <hr>
        <div class="col-4 text-center">
          <h3>All Todos<br> {{todosCount}}</h3>
        </div>
        <div class="col-4 text-center">
          <h3>Completed Todo<br> {{completedTodosCount}}</h3>
        </div>
        <div class="col-4 text-center">
          <h3>Uncompleted Todo<br> {{uncompletedTodosCount}}</h3>
        </div>
      </div>
      <hr>
    </div>


    <div class="col-10 offset-1">
      <ul class="list-group">
          <TodoListItem v-for="(todo, idx) in todos" :todo="todo" :key="idx" />
      </ul>
    </div>
    <br>

  </div>
</template>

<script>
import TodoListItem from '@/components/TodoListItem'
import { mapGetters } from 'vuex'
export default {
  name: 'TodoList',
  components: {
    TodoListItem,
  },
  computed: {
    todos: function () {
      return this.$store.state.todos
    },
    
    ...mapGetters(['todosCount', 'completedTodosCount', 'uncompletedTodosCount'])
  },
}
</script>

<style>

</style>