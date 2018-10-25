<template>
  <div>
    <h1>课程详细页面</h1>
    <div>
      <p>{{detail.course}}</p>
      <p>{{detail.img}}</p>
      <p>{{detail.level}}</p>
      <p>{{detail.slogon}}</p>
      <p>{{detail.title}}</p>
      <p>{{detail.why}}</p>
      <div>
        <ul v-for="item in detail.chapter">
          <li>{{item.name}}</li>
        </ul>
      </div>

      <div>
        <ul v-for="item in detail.recommends">
          <li>{{item.title}}</li>
        </ul>
      </div>

    </div>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        detail:{
          course:null,
          img:null,
          level:null,
          slogon:null,
          title:null,
          why:null,
          chapter:[],
          recommends:[],
        }
      }
    },
    mounted(){
      this.initDetail()
    },
    methods:{
      initDetail(){
        var nid = this.$route.params.id
        var that = this
        this.$axios.request({
          url:'http://127.0.0.1:8000/api/v1/course/'+ nid +'/',
          method:'GET'
        }).then(function (arg) {
          if(arg.data.code === 1000){
            that.detail = arg.data.data
          }else{
            alert(arg.data.error)
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
