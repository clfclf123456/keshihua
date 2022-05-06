<template>
  <div class="baseMenu">
    <div></div>
    <ul>
      <li v-for="(item, i) in menuArr" :class="{active: active === item.value}"
          :key="i" @click="goLink(item.value)">
        {{item.name}}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'baseMenu',
  data () {
    return {
      menuArr: [
        {name: '首页', value: 'home'},
        {name: '可视化展示', value: 'chart'},
        {name: '智能展示', value: 'smartShow'},
        {name: '就业分析报告', value: 'employment'},
        {name: '职位课程推荐', value: 'recommend'},
        {name: '个人中心', value: 'user'}
      ],
      active: this.$route.name || 'home'
    }
  },
  mounted() {

  },
  methods: {
    goLink (value) {
      this.active = value
      this.$router.push({name: value})
    }
  }
}
</script>

<style scoped src="./baseMenu.less" lang="less"></style>
