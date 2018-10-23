<template>
  <div>
    <Vheader></Vheader>
    
    <h1>{{msg}}</h1>
  </div>
</template>

<script>
import Vheader from './components/Vheader'
  export default {
    name:'app',
    data() {
      return {
        msg: 'hello yc'
      }
    },
    components:{
      Vheader

    }
  }
</script>

<style scoped>

</style>