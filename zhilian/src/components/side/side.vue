<template>
  <div class="side">
    <div class="left">
      <baseMenu/>
    </div>
    <div class="right">
      <router-view/>
    </div>
  </div>
</template>

<script>
import baseMenu from '../baseMenu/baseMenu'
export default {
  name: 'side',
  components: {
    baseMenu
  }
}
</script>

<style scoped src="./side.less" lang="less"></style>
