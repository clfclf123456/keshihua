<template>
  <div class="recommend">
    <div class="name">职位课程推荐</div>
    <div class="tabs">
      <ul>
        <li v-for="(item, i) in tabArr" :key="i" @click="changeTab(i)" :class="{active: activeName === i}">
          {{item}}
        </li>
      </ul>
    </div>
    <div class="tabContent">
      <div v-if="activeName === 0" class="result flex">
        <div class="font">
          <div>
            通过大数据分析后<br>
            我们为您准备了学习路线<br>
            要掌握的技能和推荐书籍
          </div>
        </div>
        <div class="img">
          <img src="./../../assets/2.png" alt="">
        </div>
      </div>
      <div v-if="activeName === 1" class="route">
        <img :src="`${publicPath + '/' + job + '.png'}`" alt="">
      </div>
      <div v-if="activeName === 2">
        <div class="table">
          <el-table
              :data="list"
              border
              style="width: 100%;">
            <el-table-column
                prop="course"
                width="400"
                label="课程">
            </el-table-column>
            <el-table-column
                label="链接">
              <div slot-scope="scope" @click="goLink(scope.row.link)" class="url">
                {{scope.row.link}}
              </div>
            </el-table-column>
          </el-table>
        </div>
      </div>
      <div v-if="activeName === 3">
        <div class="table">
          <el-table
              :data="bookList"
              border
              style="width: 100%;">
            <el-table-column
                prop="name"
                width="400"
                label="书名">
            </el-table-column>
            <el-table-column
                label="链接">
              <div slot-scope="scope" @click="goLink(scope.row.link)" class="url">
                {{scope.row.link}}
              </div>
            </el-table-column>
          </el-table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'recommend',
  data () {
    return {
      tableData: [
        {type: 'java', professional: 'Java 开发工程师', course: 'Java 基础编程', link: 'https://www.icourse163.org/course/ZJU-1001541001?from=searchPage'},
        {type: 'java', professional: 'Java 开发工程师', course: '数据结构', link: 'https://www.icourse163.org/course/ZJU-93001?from=searchPage'},
        {type: 'java', professional: 'Java 开发工程师', course: '数据库基础', link: 'https://www.icourse163.org/course/RUC-488001?from=searchPage'},
        {type: 'java', professional: 'Java 开发工程师', course: 'JavaWeb 开发', link: 'https://www.bilibili.com/video/BV1Y7411K7zz?spm_id_from=333.337.search-card.all.click'},
        {type: 'java', professional: 'Java 开发工程师', course: 'Java 主流框架', link: 'https://www.bilibili.com/video/BV1Fe411x77G?spm_id_from=333.337.search-card.all.click'},
        {type: 'java', professional: 'Java 开发工程师', course: 'Java 设计模式', link: 'https://www.bilibili.com/video/BV1Np4y1z7BU?spm_id_from=333.337.search-card.all.click'},
        {type: 'java', professional: 'Java 开发工程师', course: 'Java 微服务+分布式实', link: 'https://www.bilibili.com/video/BV1V5411K7rT?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '前端', professional: '前端开发工程师', course: 'Web 前端基础&进阶', link: 'https://www.bilibili.com/video/BV1XJ411X7Ud?spm_id_from=333.337.search-card.all.click'},
        {type: '前端', professional: '前端开发工程师', course: 'JavaScript 语法进阶', link: 'https://www.bilibili.com/video/BV1YW411T7GX?spm_id_from=333.337.search-card.all.click'},
        {type: '前端', professional: '前端开发工程师', course: 'jQuery&Ajax', link: 'https://www.bilibili.com/video/BV1ts411E7ag?spm_id_from=333.337.search-card.all.click'},
        {type: '前端', professional: '前端开发工程师', course: 'ES6 语法新增', link: 'https://www.bilibili.com/video/BV1uK411H7on?spm_id_from=333.337.search-card.all.click'},
        {type: '前端', professional: '前端开发工程师', course: '移动 Web 开发', link: 'https://www.bilibili.com/video/BV1b54y1h7br?spm_id_from=333.337.search-card.all.click'},
        {type: '前端', professional: '前端开发工程师', course: 'Node.js 教程', link: 'https://www.bilibili.com/video/BV1bs411E7pD?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '大数据', professional: '大数据分析工程师', course: '统计学基础', link: 'https://www.bilibili.com/video/BV1M4411p77A?spm_id_from=333.337.search-card.all.click'},
        {type: '大数据', professional: '大数据分析工程师', course: 'Excel 从入门到精通', link: 'https://www.bilibili.com/video/BV1Gq4y1M716?spm_id_from=333.337.search-card.all.click'},
        {type: '大数据', professional: '大数据分析工程师', course: '数据库基础', link: 'https://www.icourse163.org/course/RUC-488001?from=searchPage'},
        {type: '大数据', professional: '大数据分析工程师', course: 'Python 从入门到精通', link: 'https://www.bilibili.com/video/BV1wD4y1o7AS?spm_id_from=333.337.search-card.all.click'},
        {type: '大数据', professional: '大数据分析工程师', course: 'Tableau 教程', link: 'https://www.bilibili.com/video/BV1E4411B7ef?spm_id_from=333.337.search-card.all.click'},
        {type: '大数据', professional: '大数据分析工程师', course: '计算机算法导论', link: 'https://www.bilibili.com/video/BV1Tb411M7FA?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '测试', professional: '软件测试工程师', course: 'Java 基础编程', link: 'https://www.icourse163.org/course/ZJU-1001541001?from=searchPage'},
        {type: '测试', professional: '软件测试工程师', course: '测试理论基础', link: 'https://www.bilibili.com/video/BV1bg411V7pp?spm_id_from=333.337.search-card.all.click'},
        {type: '测试', professional: '软件测试工程师', course: '功能测试', link: 'https://www.bilibili.com/video/BV1QM4y137xX?spm_id_from=333.337.search-card.all.click'},
        {type: '测试', professional: '软件测试工程师', course: '数据库基础', link: 'https://www.icourse163.org/course/RUC-488001?from=searchPage'},
        {type: '测试', professional: '软件测试工程师', course: 'Linux 基础教程', link: 'https://www.bilibili.com/video/BV1mW411i7Qf?spm_id_from=333.337.search-card.all.click'},
        {type: '测试', professional: '软件测试工程师', course: '计算机网络协议', link: 'https://www.bilibili.com/video/BV1Fy4y1Y7n6?spm_id_from=333.337.search-card.all.click'},
        {type: '测试', professional: '软件测试工程师', course: '版本控制工具', link: 'https://www.bilibili.com/video/BV1mW411M7yR?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '算法', professional: '算法工程师', course: 'Python 编程基础', link: 'https://www.icourse163.org/course/BIT-268001?from=searchPage'},
        {type: '算法', professional: '算法工程师', course: '数据库基础', link: 'https://www.icourse163.org/course/RUC-488001?from=searchPage'},
        {type: '算法', professional: '算法工程师', course: 'Linux 基础教程', link: 'https://www.bilibili.com/video/BV1mW411i7Qf?spm_id_from=333.337.search-card.all.click'},
        {type: '算法', professional: '算法工程师', course: '计算机算法导论', link: 'https://www.bilibili.com/video/BV1Tb411M7FA?spm_id_from=333.337.search-card.all.click'},
        {type: '算法', professional: '算法工程师', course: '机器学习', link: 'https://www.icourse163.org/course/BIT-1001872001?from=searchPage'},
        {type: '算法', professional: '算法工程师', course: '深度学习', link: 'https://www.icourse163.org/course/HIT-1206320802?from=searchPage'},
        {type: '算法', professional: '算法工程师', course: 'NLP 自然语言', link: 'https://www.bilibili.com/video/BV1hM4y157xX?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '嵌入式', professional: '嵌入式开发工程师', course: 'C语言编程', link: 'https://www.bilibili.com/video/BV1q54y1q79w?spm_id_from=333.337.search-card.all.click'},
        {type: '嵌入式', professional: '嵌入式开发工程师', course: '数据结构与算法', link: 'https://www.bilibili.com/video/BV1E4411H73v?spm_id_from=333.337.search-card.all.click'},
        {type: '嵌入式', professional: '嵌入式开发工程师', course: 'ARM 嵌入式', link: 'https://www.bilibili.com/video/BV16K4y1b7AB?spm_id_from=333.337.search-card.all.click'},
        {type: '嵌入式', professional: '嵌入式开发工程师', course: '应用编程与网络编程', link: 'https://www.bilibili.com/video/BV1zQ4y1q7Vj?spm_id_from=333.337.search-card.all.click'},
        {type: '嵌入式', professional: '嵌入式开发工程师', course: 'Linux 驱动开发', link: 'https://www.bilibili.com/video/BV1zQ4y1q7Vj?spm_id_from=333.337.search-card.all.click'},
        {type: '嵌入式', professional: '嵌入式开发工程师', course: '操作系统', link: 'https://www.bilibili.com/video/BV1wq4y1M7qf?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '产品', professional: '嵌入式开发工程师', course: '产品入门', link: 'https://www.bilibili.com/video/BV13z4y1m7UQ?spm_id_from=333.337.search-card.all.click'},
        {type: '产品', professional: '嵌入式开发工程师', course: '产品前台', link: 'https://www.bilibili.com/video/BV1Lp4y1D7iN?spm_id_from=333.337.search-card.all.click'},
        {type: '产品', professional: '嵌入式开发工程师', course: '产品后台', link: 'https://www.bilibili.com/video/BV1kg411A7Xi?spm_id_from=333.337.search-card.all.click'},
        {type: '产品', professional: '嵌入式开发工程师', course: '产品运营', link: 'https://www.bilibili.com/video/BV1o7411h7xp?spm_id_from=333.337.search-card.all.click'},
        {type: '产品', professional: '嵌入式开发工程师', course: '产品思维', link: 'https://www.bilibili.com/video/BV1GA411B7Tp?spm_id_from=333.337.search-card.all.click'},
        {type: '产品', professional: '嵌入式开发工程师', course: '项目实战', link: 'https://www.bilibili.com/video/BV1Hp4y1r7YY?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '数据分析', professional: '嵌入式开发工程师', course: 'Python编程基础', link: 'https://www.icourse163.org/course/BIT-268001?from=searchPage'},
        {type: '数据分析', professional: '嵌入式开发工程师', course: '数据库基础', link: 'https://www.icourse163.org/course/RUC-488001?from=searchPage'},
        {type: '数据分析', professional: '嵌入式开发工程师', course: '统计学基础', link: 'https://www.bilibili.com/video/BV1M4411p77A?spm_id_from=333.337.search-card.all.click'},
        {type: '数据分析', professional: '嵌入式开发工程师', course: 'Excel从入门到精通', link: 'https://www.bilibili.com/video/BV1Gq4y1M716?spm_id_from=333.337.search-card.all.click'},
        {type: '数据分析', professional: '嵌入式开发工程师', course: 'Tableau 教程', link: 'https://www.bilibili.com/video/BV1E4411B7ef?spm_id_from=333.337.search-card.all.click'},
          //
        {type: '运维', professional: '嵌入式开发工程师', course: 'C语言编程', link: 'https://www.bilibili.com/video/BV1q54y1q79w?spm_id_from=333.337.search-card.all.click'},
        {type: '运维', professional: '嵌入式开发工程师', course: '数据结构与算法', link: 'https://www.bilibili.com/video/BV1E4411H73v?spm_id_from=333.337.search-card.all.click'},
        {type: '运维', professional: '嵌入式开发工程师', course: 'Python编程基础', link: 'https://www.icourse163.org/course/BIT-268001?from=searchPage'},
        {type: '运维', professional: '嵌入式开发工程师', course: '数据库基础', link: 'https://www.icourse163.org/course/RUC-488001?from=searchPage'},
        {type: '运维', professional: '嵌入式开发工程师', course: 'Linux基础教程', link: 'https://www.bilibili.com/video/BV1mW411i7Qf?spm_id_from=333.337.search-card.all.click'},
        {type: '运维', professional: '嵌入式开发工程师', course: 'Java基础编程', link: 'https://www.icourse163.org/course/ZJU-1001541001?from=searchPage'},
        {type: '运维', professional: '嵌入式开发工程师', course: '计算机网络协议', link: 'https://www.bilibili.com/video/BV1Fy4y1Y7n6?spm_id_from=333.337.search-card.all.click'}
      ],
      spanArr: [],
      tabArr: ['分析结果', '学习路线', '推荐课程', '推荐书籍'],
      activeName: 0,
      id: '',
      job: '',
      bookArr: [
        {type: 'java', name: '《Java编程思想 》（第4版）', link: 'https://book.douban.com/subject/2130190/'},
        {type: 'java', name: '《数据结构与算法分析 C语言描述》（原书第2版）', link: 'https://book.douban.com/subject/33419792/'},
        {type: 'java', name: '《数据库系统概念》（原书第7版）', link: 'https://book.douban.com/subject/35501216/'},
        {type: 'java', name: '《Java设计模式》', link: 'https://book.douban.com/subject/30173863/'},
        {type: 'java', name: '《微服务架构设计模式》', link: 'https://book.douban.com/subject/33425123/'},
          //
        {type: '前端', name: '《Web界面设计》', link: 'https://book.douban.com/subject/3821157/'},
        {type: '前端', name: '《JavaScript高级程序设计》（第3版）', link: 'https://book.douban.com/subject/10546125/'},
        {type: '前端', name: '《jQuery基础教程》', link: 'https://book.douban.com/subject/3082293/'},
        {type: '前端', name: '《ES6标准入门》', link: 'https://book.douban.com/subject/27127030/'},
        {type: '前端', name: '《深入浅出Node.js》', link: 'https://book.douban.com/subject/25768396/'},
          //
        {type: '大数据', name: '《统计学习方法》（第2版）', link: 'https://book.douban.com/subject/33437381/'},
        {type: '大数据', name: '《和秋叶一起学Excel》（第2版）', link: 'https://book.douban.com/subject/35006472/'},
        {type: '大数据', name: '《Python编程》', link: 'https://book.douban.com/subject/35196328/'},
        {type: '大数据', name: '《Tableau 8权威指南》', link: 'https://book.douban.com/subject/26384640/'},
        {type: '大数据', name: '《算法导论》（原书第3版）', link: 'https://book.douban.com/subject/20432061/'},
          //
        {type: '测试', name: '《Java编程思想 》（第4版）', link: 'https://book.douban.com/subject/2130190/'},
        {type: '测试', name: '《数据库系统概念》（原书第7版）', link: 'https://book.douban.com/subject/35501216/'},
        {type: '测试', name: '《鸟哥的Linux私房菜》', link: 'https://book.douban.com/subject/4889838/'},
        {type: '测试', name: '《软件测试的艺术》', link: 'https://book.douban.com/subject/1445661/'},
        {type: '测试', name: '《计算机网络》（原书第7版）', link: 'https://book.douban.com/subject/30280001/'},
        {type: '测试', name: '《Git版本控制管理》', link: 'https://book.douban.com/subject/5311565/'},
          //
        {type: '嵌入式', name: '《C程序设计语言》（第2版·新版）', link: 'https://book.douban.com/subject/1139336/'},
        {type: '嵌入式', name: '《数据结构与算法分析》', link: 'https://book.douban.com/subject/1139426/'},
        {type: '嵌入式', name: '《ARM嵌入式系统开发》', link: 'https://book.douban.com/subject/1435663/'},
        {type: '嵌入式', name: '《Linux驱动开发入门与实战》', link: 'https://book.douban.com/subject/5415952/'},
        {type: '嵌入式', name: '《操作系统原理、实现与实践》', link: 'https://book.douban.com/subject/30391722/'},
          //
        {type: '产品', name: '《产品设计与开发》（原书第6版）', link: 'https://book.douban.com/subject/30236735/'},
        {type: '产品', name: '《微信背后的产品观》', link: 'https://book.douban.com/subject/35339729/'},
        {type: '产品', name: '《策略产品经理：模型与方法论》', link: 'https://book.douban.com/subject/35218721/'},
        {type: '产品', name: '《ViP产品设计法则》', link: 'https://book.douban.com/subject/35038867/'},
        {type: '产品', name: '《数据产品经理：实战进阶》', link: 'https://book.douban.com/subject/35184865/'},
          //
        {type: '数据分析', name: '《Python编程》', link: 'https://book.douban.com/subject/35196328/'},
        {type: '数据分析', name: '《统计学习方法》（第2版）', link: 'https://book.douban.com/subject/33437381/'},
        {type: '数据分析', name: '《和秋叶一起学Excel》（第2版）', link: 'https://book.douban.com/subject/35006472/'},
        {type: '数据分析', name: '《精益数据分析》', link: 'https://book.douban.com/subject/26278639/'},
        {type: '数据分析', name: '《利用Python进行数据分析》', link: 'https://book.douban.com/subject/25779298/'},
          //
        {type: '运维', name: '《C程序设计语言》（第2版·新版）', link: 'https://book.douban.com/subject/1139336/'},
        {type: '运维', name: '《Python编程》', link: 'https://book.douban.com/subject/35196328/'},
        {type: '运维', name: '《Java编程思想 》（第4版）', link: 'https://book.douban.com/subject/2130190/'},
        {type: '运维', name: '《数据结构与算法分析 C语言描述》（原书第2版）', link: 'https://book.douban.com/subject/33419792/'},
        {type: '运维', name: '《数据库系统概念》（原书第7版）', link: 'https://book.douban.com/subject/35501216/'},
        {type: '运维', name: '《鸟哥的Linux私房菜》', link: 'https://book.douban.com/subject/4889838/'},
        {type: '运维', name: '《算法导论》（原书第3版）', link: 'https://book.douban.com/subject/20432061/'},
          //
        {type: '算法', name: '《Python编程》', link: 'https://book.douban.com/subject/35196328/'},
        {type: '算法', name: '《鸟哥的Linux私房菜》', link: 'https://book.douban.com/subject/4889838/'},
        {type: '算法', name: '《算法导论》（原书第3版）', link: 'https://book.douban.com/subject/20432061/'},
        {type: '算法', name: '《数据库系统概念》（原书第7版）', link: 'https://book.douban.com/subject/35501216/'},
        {type: '算法', name: '《机器学习实战》（原书第2版）', link: 'https://book.douban.com/subject/35218199/'},
        {type: '算法', name: '《Python深度学习》', link: 'https://book.douban.com/subject/30293801/'}
      ],
      publicPath: process.env.BASE_URL
    }
  },
  mounted() {
    this.id = window.sessionStorage.getItem('id')
    this.getData()
    this.getIndex()
  },
  computed: {
    list () {
      return this.tableData.filter(item => item.type === this.job)
    },
    bookList () {
      return this.bookArr.filter(item => item.type === this.job)
    }
  },
  methods: {
    goLink (url) {
      window.open(url)
    },
    // objectSpanMethod ({ row, column, rowIndex, columnIndex }) {
    //   if (columnIndex === 0) {                     //合并第一列
    //     const _row = this.spanArr[rowIndex]
    //     const _col = _row > 0 ? 1 : 0
    //     return {
    //       rowspan: _row,
    //       colspan: _col
    //     }
    //   }
    // },
    getIndex () {
      let contactDot = 0;
      this.tableData.forEach((item, index) => {
        item.index = index
        if (index === 0) {
          this.spanArr.push(1)
        } else {
          if (item.professional === this.tableData[index - 1].professional) {
            this.spanArr[contactDot] += 1
            this.spanArr.push(0)
          } else {
            this.spanArr.push(1)
            contactDot = index
          }
        }
      })
    },
    changeTab (i) {
      this.activeName = i
    },
    getData() {
      this.$http.get('api/user/info', {
        params: {
          id: this.id
        }
      }).then(res => {
        if (res.data.code === 200) {
          this.userInfo = res.data.data
          this.job = res.data.data.want_job
          this.registerInfo = JSON.parse(JSON.stringify(res.data.data))
        }
      })
    }
  }
}
</script>

<style scoped src="./recommend.less" lang="less"></style>
