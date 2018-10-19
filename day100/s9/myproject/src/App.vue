<template>
   <!-- 页面结构 -->
  <div class="app">
    <h1>{{msg}}</h1>
    <h3>可爱的VUE</h3>
    <Vheader></Vheader>
    <Vcontent></Vcontent>
    <Vfooter></Vfooter>
  </div>

</template>

<script>
// 先引入子组件
import Vheader from './components/Vheader.vue';
import Vfooter from './components/Vfooter.vue';
import Vcontent from './components/Vcontent.vue';
  export default{
    name:'App',
    data(){
      return {
        msg:'hello 组件!'

      }
    },
    methods:{

    },
    computed:{

    },
    // 挂载子组件
    components:{
      Vheader,
      Vfooter,
      Vcontent
    }
  }
</script>
<style>

</style>
