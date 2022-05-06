<template>
  <div class="home">
    <div class="name">首页</div>
    <div class="search">
      <div class="title">选择条件：</div>
      <div>
        <el-select v-model="searchInfo.city_id" placeholder="请选择所在城市">
          <el-option
              v-for="item in cityDic"
              :key="item.value"
              :label="item.label"
              :value="item.value">
          </el-option>
        </el-select>
      </div>
      <div>
        <el-select v-model="searchInfo.job_type" placeholder="请选择职业名称">
          <el-option
              v-for="item in wantJobArr"
              :key="item.value"
              :label="item.label"
              :value="item.value">
          </el-option>
        </el-select>
      </div>
      <div>
        <el-select v-model="searchInfo.education" placeholder="请选择学历要求">
          <el-option
              v-for="item in educationArr"
              :key="item.value"
              :label="item.label"
              :value="item.value">
          </el-option>
        </el-select>
      </div>
      <div class="salarySel">
        <!--        <el-select v-model="searchInfo.salary" placeholder="请选择薪资">-->
        <!--          <el-option-->
        <!--              v-for="item in salaryArr"-->
        <!--              :key="item.value"-->
        <!--              :label="item.label"-->
        <!--              :value="item.value">-->
        <!--          </el-option>-->
        <!--        </el-select>-->
        <div class="salaryTitle">薪资区间：</div>
        <div class="salary">
          <div>
            <el-input v-model="low" placeholder=""></el-input>
          </div>
          <div style="margin-left: 10px">元</div>
          <span> — </span>
          <div>
            <el-input v-model="high"></el-input>
          </div>
          <div style="margin-left: 10px">元</div>
        </div>
      </div>
      <div class="button">
        <el-button type="primary" @click="search" icon="el-icon-search">搜索</el-button>
      </div>
    </div>
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
  name: 'home',
  computed: {
    salary() {
      // let low = this.format(this.low - 0)
      // let high = this.format(this.high - 0)
      return (this.low - 0) + '-' + (this.high - 0)
    }
  },
  data() {
    return {
      low: '',
      high: '',
      searchInfo: {
        job_type: '',
        city_id: '',
        education: '',
        salary: ''
      },
      educationArr: [
        // {label: '初中及以下', value: 9},
        {label: '高中', value: '02'},
        // {label: '中专/中技', value: 12},
        {label: '大专', value: '03'},
        {label: '本科', value: '04'},
        {label: '硕士', value: '05'},
        {label: '博士', value: '06'},
        // {label: 'MBA/EMBA', value: 10}
      ],
      wantJobArr: [
        // {label: '销售/商务拓展', value: 19000000000000},
        // {label: '人事/行政/财务/法务', value: 14000000000000},
        // {label: '互联网/通信及硬件', value: 9000000000000},
        // {label: '运维/测试', value: 20000000000000},
        // {label: '视觉/交互/设计', value: 17000000000000},
        // {label: '运营/专业分析', value: 5000000000000},
        // {label: '产品/项目/高级管理', value: 3000000000000},
        // {label: '市场/品牌/公关', value: 16000000000000},
        // {label: '金融/保险', value: 12000000000000},
        // {label: '房地产/工程/建筑', value: 7000000000000},
        // {label: '物流/采购/供应链', value: 2000000000000},
        // {label: '生产制造/营运管理', value: 15000000000000},
        // {label: '农业/能源/环保', value: 21000000000000},
        // {label: '医疗/医美', value: 18000000000000},
        // {label: '教育/培训/科研', value: 11000000000000},
        // {label: '编辑/记者/翻译', value: 1000000000000},
        // {label: '影视传媒', value: 4000000000000},
        // {label: '商务服务/生活服务', value: 6000000000000},
        // {label: '管培生/非企业从业者', value: 8000000000000}
        {label: 'java', value: 'java'},
        {label: '前端', value: '前端'},
        {label: '测试', value: '测试'},
        {label: '大数据', value: '大数据'},
        {label: '算法', value: '算法'},
        {label: '嵌入式', value: '嵌入式'},
        {label: '运维', value: '运维'},
        {label: '数据分析', value: '数据分析'},
        {label: '产品', value: '产品'}
      ],
      cityDic: [
        {label: '北京', value: '010000'},
        {label: '上海', value: '020000'},
        {label: '广州', value: '030200'},
        {label: '深圳', value: '040000'},
        {label: '长沙', value: '190200'},
        {label: '杭州', value: '080200'},
        {label: '厦门', value: '110300'},
        {label: '成都', value: '090200'},
      ],
      salaryArr: [
        {label: '4K-6K', value: '4千-6千'},
        {label: '6K-8K', value: '6千-8千'},
        {label: '8K-10K', value: '8千-1万'},
        {label: '10K-15K', value: '1万-1.5万'},
        {label: '15K-25K', value: '1.5万-2.5万'},
        {label: '25K-35K', value: '2.5万-3.5万'},
        {label: '35K-50K', value: '3.5万-5万'}
      ],
      tableData: [],
      page: 1,
      total: 20
    }
  },
  mounted() {
    // this.getTableData()
  },
  methods: {
    search() {
      this.page = 1
      this.getTableData()
    },
    handleCurrentChange(page) {
      this.page = page
      this.getTableData()
    },
    getTableData() {
      this.$http.get('api/spider/run', {
        params: {
          job_type: this.searchInfo.job_type,
          city_id: this.searchInfo.city_id,
          education: this.searchInfo.education,
          salary: this.salary,
          page: this.page
        }
      }).then(res => {
        if (res.data.code === 200) {
          this.tableData = res.data.data
          this.total = res.data.msg
        }
      })
    },
    format(num) {
      let str = ''
      if (num >= 1e3 && num < 1e4) {
        str = parseInt(num / 1e3).toFixed(0) + '千'
      } else if(num >= 1e4){
        return parseInt(num / 1e4).toFixed(0) + '万'
      } else {
        str = num
      }
      return str
    }
  }
}
</script>

<style scoped src="./home.less" lang="less"></style>
