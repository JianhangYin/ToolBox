import Vue from 'vue'
import Router from 'vue-router'
import Questionnaire from '../components/mealplanning/Questionnaire'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/meal-planning',
      name: 'Questionnaire',
      component: Questionnaire
    }
  ]
})
