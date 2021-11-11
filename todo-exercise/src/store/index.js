import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

import createPersistedState from 'vuex-persistedstate'
export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    todos: [
      // {
      //   title: 'Sample Todo #1',
      //   isCompleted: false,
      //   date: new Date().getTime(),
      // },
      // {
      //   title: 'Sample Todo #2',
      //   isCompleted: false,
      //   date: new Date().getTime(),
      // },
      // {
      //   title: 'Sample Todo #3',
      //   isCompleted: false,
      //   date: new Date().getTime(),
      // },
    ],
  },
  mutations: {
    // 여기에 todos를 직접 조작할 mutations를 작성합니다.
    CREATE_TODO: function (state, payload) {
      // 가령 todos에 push하는 것은 mutations만 해야 합니다.
      state.todos.push(payload)
    },

    UPDATE_TODO_STATUS: function (state, payload) {
      state.todos = state.todos.map(todo => {
        if (todo === payload) {
          return {
            ...todo,
            isCompleted: !todo.isCompleted
          }
        } else {
          return todo
        }
      })
    },

    DELETE_TODO: function (state, payload) {
      const idx = state.todos.indexOf(payload)
      state.todos.splice(idx, 1)
    },

    // DELETE_TODO: function (state, payload) {
    // },
  },
  actions: {
    // 여기에 실제 Vue components들이 호출할 actions를 작성합니다.
    // state 조작은 이들 actions이 mutations을 호출하는 형태로 구현합니다.
    // payload에는 조작의 대상이 될 todo Object가 담깁니다.
    createTodo: function ({commit}, payload) {
      commit('CREATE_TODO', payload)
    },
    updateTodoStatus: function ({commit}, payload) {
      commit('UPDATE_TODO_STATUS', payload)
    },
    deleteTodo: function ({commit}, payload) {
      commit('DELETE_TODO', payload)
    },
  },
  getters: {
    // 여기에는 Todo App이 필요로 할 Computed가 작성됩니다.
    // 가령 할 일의 갯수 등을 count할 수 있습니다.
    todosCount: function (state) {
      return state.todos.length
    },
    completedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted
      }).length
    },
    uncompletedTodosCount: function (state) {
      return state.todos.filter(todo => {
        return todo.isCompleted === false
      }).length
    },
  },
  modules: {
  },
})
