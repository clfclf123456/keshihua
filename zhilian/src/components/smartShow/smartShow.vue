<template>
  <div class="smartShow">
    <div class="name">智能展示</div>
    <div class="table">
      <el-table :data="tableData" border style="width: 100%">
        <el-table-column prop="公司名称" label="公司名称" width="300"></el-table-column>
        <el-table-column prop="公司类型" label="公司类型" width="120"></el-table-column>
        <el-table-column prop="公司规模" label="公司规模" width="140"></el-table-column>
        <el-table-column prop="学历要求" label="学历要求" width="120"></el-table-column>
        <el-table-column prop="工作城市" label="工作城市" width="80"></el-table-column>
        <el-table-column prop="工作经验" label="工作经验" width="80"></el-table-column>
        <el-table-column prop="福利待遇" label="福利待遇"></el-table-column>
        <el-table-column prop="职位名称" label="职位名称"></el-table-column>
        <el-table-column prop="薪资范围" label="薪资范围" width="120"></el-table-column>
      </el-table>
    </div>
    <div class="page" v-if="tableData.length">
      <el-pagination
          background
          @current-change="handleCurrentChange"
          :current-page.sync="page"
          :page-size="10"
          :total="total"
          layout="total, prev, pager, next">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: 'smartShow',
  mounted() {
    this.id = window.sessionStorage.getItem('id')
    this.getData()
  },
  data () {
    return {
      tableData: [],
      page: 1,
      total: 0,
      id: ''
    }
  },
  methods: {
    handleCurrentChange (page) {
      this.page = page
      this.getData()
    },
    getData() {
      this.$http.get('api/data/recommend', {
        params: {
          id: this.id,
          page: this.page
        }
      }).then(res => {
        if (res.data.code === 200) {
          this.tableData = res.data.data
          this.total = res.data.msg
        }
      })
    }
  }
}
</script>

<style scoped src="./smartShow.less" lang="less"></style>
