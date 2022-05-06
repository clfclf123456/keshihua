<template>
  <div class="user">
    <div class="name">个人信息</div>
    <div class="userInfo">
      <div>用户名：{{userInfo.username}}</div>
      <div>手机：{{userInfo.phone}}</div>
      <div>学校：{{setFilter(userInfo.school, 'school')}}</div>
      <div>学历：{{setFilter(userInfo.education, 'education')}}</div>
      <div>职位：{{setFilter(userInfo.want_job, 'wantJob')}}</div>
      <div>工作年限：{{userInfo.worktime}}年</div>
      <div>
        <el-button type="primary" @click="dialogVisible = true">修改</el-button>
      </div>
    </div>
    <el-dialog
        title="提示"
        :visible.sync="dialogVisible"
        width="30%"
        :before-close="handleClose">
      <div>
        <div class="userPassword">
          <div>用户名：</div>
          <div class="input">
            <el-input v-model="registerInfo.username" placeholder="请输入手机"></el-input>
          </div>
        </div>
        <div class="userPassword">
          <div>手机：</div>
          <div class="input">
            <el-input v-model="registerInfo.phone" placeholder="请输入手机"></el-input>
          </div>
        </div>
        <div class="userPassword">
          <div>学校：</div>
          <div class="input">
            <el-select v-model="registerInfo.school" placeholder="请选择学校">
              <el-option
                  v-for="item in schoolArr"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
        <div class="userPassword">
          <div>学历：</div>
          <div class="input">
            <el-select v-model="registerInfo.education" placeholder="请选择学历">
              <el-option
                  v-for="item in educationArr"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
        <div class="userPassword">
          <div>工作年限：</div>
          <div class="input">
            <el-input v-model.number="registerInfo.worktime" placeholder="请输入工作年限"></el-input>
          </div>
        </div>
        <div class="userPassword">
          <div>职业：</div>
          <div class="input">
            <el-select v-model="registerInfo.want_job" placeholder="请选择职业">
              <el-option
                  v-for="item in wantJobArr"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
              </el-option>
            </el-select>
          </div>
        </div>
      </div>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editUser">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'user',
  data() {
    return {
      id: '',
      userInfo: {},
      registerInfo: {
        phone: '',
        username: '',
        school: '',
        education: '',
        worktime: '',
        want_job: ''
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
      schoolArr: [
        {label: '无', value: 0},
        {label: '双非', value: 1},
        {label: '985/211', value: 2}
      ],
      dialogVisible: false
    }
  },
  mounted() {
    this.id = window.sessionStorage.getItem('id')
    this.getData()
  },
  methods: {
    setFilter (value, name) {
      let a = ''
      this[name + 'Arr'].forEach(item => {
        if (item.value === value) {
          a = item.label
        }
      })
      return a
    },
    editUser () {
      this.registerInfo.id = this.registerInfo.id - 0
      this.$http.post('api/user/info', this.registerInfo).then(res => {
        if (res.data.code === 200) {
          this.dialogVisible = false
          this.getData()
          this.$message({
            message: '修改成功',
            type: 'success'
          })
        } else {
          this.$message.error(res.data.msg)
        }
      })
    },
    handleClose () {
      this.dialogVisible = false
    },
    getData() {
      this.$http.get('api/user/info', {
        params: {
          id: this.id
        }
      }).then(res => {
        if (res.data.code === 200) {
          this.userInfo = res.data.data
          this.registerInfo = JSON.parse(JSON.stringify(res.data.data))
        }
      })
    }
  }
}
</script>

<style scoped src="./user.less" lang="less"></style>
