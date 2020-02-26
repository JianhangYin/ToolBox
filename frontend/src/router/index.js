import Vue from 'vue'
import Router from 'vue-router'
import Questionnaire from '../components/mealplanning/Questionnaire'
import MealPlan from '../components/mealplanning/MealPlan'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/meal-planning',
      name: 'Questionnaire',
      component: Questionnaire
    },
    {
      path: '/meal-planning/meal-plan',
      name: 'MealPlan',
      component: MealPlan
    }
  ]
})
