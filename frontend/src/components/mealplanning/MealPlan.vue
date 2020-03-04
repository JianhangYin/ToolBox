<template>
  <div>
    <Table :columns="columns" :data="content" no-data-text="No Data"></Table>
  </div>
</template>

<script>
export default {
  name: 'MealPlan',
  data () {
    return {
      columns: [
        {
          title: 'Date',
          key: 'date'
        },
        {
          title: 'Name',
          key: 'name'
        },
        {
          title: 'Recipe',
          key: 'recipe'
        }
      ],
      content: [
        {
          date: 'Monday',
          name: this.$route.params.data['Monday'][0],
          recipe: this.$route.params.data['Monday'][1]
        },
        {
          date: 'Tuesday',
          name: this.$route.params.data['Tuesday'][0],
          recipe: this.$route.params.data['Tuesday'][1]
        },
        {
          date: 'Wednesday',
          name: this.$route.params.data['Wednesday'][0],
          recipe: this.$route.params.data['Wednesday'][1]
        },
        {
          date: 'Thursday',
          name: this.$route.params.data['Thursday'][0],
          recipe: this.$route.params.data['Thursday'][1]
        },
        {
          date: 'Friday',
          name: this.$route.params.data['Friday'][0],
          recipe: this.$route.params.data['Friday'][1]
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
