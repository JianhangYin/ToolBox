<template>
  <div id="app">
    <router-link to="/">
      <div style="text-align:center">
        <img src="./assets/black-hole.svg" width="50px">
        <h3>ToolBox</h3>
      </div>
    </router-link>
    <Menu mode="horizontal" active-name="1">
      <MenuItem name="1">
        <Icon type="md-restaurant" />
        <router-link to="/meal-planning">Meal Planning</router-link>
      </MenuItem>
      <MenuItem name="2">
        <Icon type="md-add" />
        TBD
      </MenuItem>
      <MenuItem name="4">
        <Icon type="md-add" />
        TBD
      </MenuItem>
      <MenuItem name="4">
        <Icon type="md-add" />
        TBD
      </MenuItem>
    </Menu>
    <br>
    <router-view/>
    <!--
    <div class="footer">
      Icons made by <a href="https://www.flaticon.com/authors/nhor-phai" title="Nhor Phai">Nhor Phai</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
    </div>
    -->
  </div>
</template>

<script>
export default {
  name: 'App',
  methods: {
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    margin: 30px 50px 0;
  }
</style>
