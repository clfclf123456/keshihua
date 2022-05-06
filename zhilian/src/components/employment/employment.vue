<template>
  <div class="employment">
    <div class="name">就业分析报告</div>
<!--    <div>-->
<!--      <el-select v-model="city" @change="selectType" placeholder="请选择职业名称">-->
<!--        <el-option-->
<!--            v-for="item in cityDic"-->
<!--            :key="item.value"-->
<!--            :label="item.label"-->
<!--            :value="item.value">-->
<!--        </el-option>-->
<!--      </el-select>-->
<!--    </div>-->
    <div class="charts">
      <div>
        <div ref="city"></div>
      </div>
      <div>
        <div ref="education"></div>
      </div>
    </div>
    <div class="charts">
      <div>
        <div class="cityDic">
          <el-select v-model="city" @change="selectType" placeholder="请选择职业名称">
            <el-option
                v-for="item in cityDic"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </div>
        <div ref="educationCity"></div>
      </div>
      <div>
        <div ref="cityNum"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'employment',
  data () {
    return {
      wantJob: '',
      city: '010000',
      id: '',
      education: ['高中', '大专', '本科', '硕士', '博士'],
      cityDic: [
        {label: '北京', value: '010000'},
        {label: '上海', value: '020000'},
        {label: '广州', value: '030200'},
        {label: '深圳', value: '040000'},
        {label: '长沙', value: '190200'},
        {label: '杭州', value: '080200'},
        {label: '厦门', value: '110300'},
        {label: '成都', value: '090200'},
      ]
    }
  },
  mounted() {
    this.id = window.sessionStorage.getItem('id')
    this.getUser()
  },
  methods: {
    selectType () {
      this.getEducationCity()
    },
    getUser() {
      this.$http.get('api/user/info', {
        params: {
          id: this.id
        }
      }).then(res => {
        if (res.data.code === 200) {
          this.wantJob = res.data.data.want_job
          this.charts()
        }
      })
    },
    charts() {
      this.getEducation()
      this.getCity()
      this.getEducationCity()
      this.getCityChart()
    },
    getEducation () {
      let education = this.$refs.education
      let bar = this.$echarts.init(education)
      this.$http.get('api/data/job/education', {
        params: {
          job: this.wantJob
        }
      }).then(res => {
        let [x, y] = [[], []]
        if (res.data.code === 200) {
          let obj = res.data.data
          // for (let i in obj) {
          //   x.push(i)
          //   y.push(obj[i])
          // }
          delete obj['初中及以下']
          let b = []
          for (let i in obj) {
            this.education.forEach((a, j) => {
              if (a === i) {
                let c = {i: j, name: i, value: obj[i]}
                b.push(c)
              }
            })
          }
          b.sort((q, e) => {
            return q.i - e.i
          })
          b.forEach(a => {
            x.push(a.name)
            y.push(a.value)
          })
          let series = []
          for (let i = 0; i < x.length; i++) {
            let obj = {
              label: {
                align: 'center'
              },
              name: x[i],
              type: 'bar',
              data: [y[i]]
            }
            series.push(obj)
          }
          let option = {
            grid: {
              bottom: '10%',
              right: '36px',
              left: '56px'
            },
            // color: ['#5470c6'],
            color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
            title: {
              text: '不同学历的平均薪资',
              left: 'center',
              top: '8%'
            },
            legend: {
              top: '1%'
            },
            // tooltip: {
            //   formatter: function (params) {
            //     let str = '<span style="display:inline-block;width:10px;height:10px;background:' + params.color + ';border-radius: 50%;margin-right:5px;"></span>' + params.name + '：' + params.value + 'K'
            //     return str
            //   },
            //   transitionDuration: 0
            // },
            tooltip: {
              formatter: function (params) {
                // let str = '<span style="display:inline-block;width:10px;height:10px;background:' + params.color + ';border-radius: 50%;margin-right:5px;"></span>' + params.name + '：' + params.value + '万'
                // return str
                let xValue = params[0].axisValue
                let levelValues = ''
                for (let i = 0; i < params.length; i++) {
                  if (params[i].value !== 0) {
                    levelValues += '<span style="display:inline-block;width:10px;height:10px;background:' + params[i].color + ';border-radius: 50%;margin-right:5px;"></span>' + params[i].seriesName + '：' + params[i].value + '万<br>'
                  }
                }
                return xValue + '<br>' + levelValues
              },
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              },
              transitionDuration: 0
            },
            xAxis: {
              // data: x
              data: ['不同学历的平均薪资']
            },
            yAxis: {
              type: 'value',
              name: '万'
            },
            series: series
            // series: [
            //   {
            //     label: {
            //       align: 'center'
            //     },
            //     type: 'bar',
            //     data: y,
            //     backgroundStyle: {
            //       color: 'rgba(180, 180, 180, 0.2)'
            //     }
            //   }
            // ]
          }
          bar.setOption(option)
        }
      })
    },
    getCity () {
      let city = this.$refs.city
      let bar = this.$echarts.init(city)
      // 不同城市平均薪资
      this.$http.get('api/data/job/city', {
        params: {
          job: this.wantJob
        }
      }).then(res => {
        let [x, y] = [[], []]
        if (res.data.code === 200) {
          let obj = res.data.data
          // for (let i in obj) {
          //   x.push(i)
          //   y.push(obj[i])
          // }
          let b = []
          for (let i in obj) {
            let c = {name: i, value: obj[i]}
            b.push(c)
          }
          b.forEach(a => {
            x.push(a.name)
            y.push(a.value)
          })
          let series = []
          for (let i = 0; i < x.length; i++) {
            let obj = {
              label: {
                align: 'center'
              },
              name: x[i],
              type: 'bar',
              data: [y[i]]
            }
            series.push(obj)
          }
          let option = {
            grid: {
              bottom: '10%',
              right: '36px',
              left: '56px'
            },
            // color: ['#5470c6'],
            color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
            legend: {
              top: '1%'
            },
            title: {
              text: '不同城市平均薪资',
              left: 'center',
              top: '8%'
            },
            tooltip: {
              formatter: function (params) {
                // let str = '<span style="display:inline-block;width:10px;height:10px;background:' + params.color + ';border-radius: 50%;margin-right:5px;"></span>' + params.name + '：' + params.value + 'K'
                // return str
                // console.log(params)
                let xValue = params[0].axisValue
                // console.log(xValue)
                let levelValues = ''
                for (let i = 0; i < params.length; i++) {
                  if (params[i].value !== 0) {
                    levelValues += '<span style="display:inline-block;width:10px;height:10px;background:' + params[i].color + ';border-radius: 50%;margin-right:5px;"></span>' + params[i].seriesName + '：' + params[i].value + '万<br>'
                  }
                }
                return xValue + '<br>' + levelValues
              },
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              },
              transitionDuration: 0
            },
            xAxis: {
              // data: x
              data: ['不同城市平均薪资']
            },
            yAxis: {
              type: 'value',
              name: '万'
            },
            // series: [
            //   {
            //     label: {
            //       align: 'center'
            //     },
            //     type: 'bar',
            //     data: y,
            //     backgroundStyle: {
            //       color: 'rgba(180, 180, 180, 0.2)'
            //     }
            //   }
            // ],
            series: series
          }
          bar.setOption(option)
        }
      })
      // 不同城市薪资
    },
    getEducationCity () {
      // 不同城市学历要求
      let educationCity = this.$refs.educationCity
      let bar = this.$echarts.init(educationCity)
      this.$http.get('api/data/city/worktime', {
        params: {
          job: this.wantJob,
          city: this.city
        }
      }).then(res => {
        let [x, y] = [[], []]
        if (res.data.code === 200) {
          let obj = res.data.data
          // for (let i in obj) {
          //   x.push(i)
          //   y.push(obj[i])
          // }
          delete obj['空']
          let b = []
          for (let i in obj) {
            let c = {name: i, value: obj[i]}
            b.push(c)
          }
          b.forEach(a => {
            x.push(a.name)
            y.push(a.value)
          })
          let series = []
          for (let i = 0; i < x.length; i++) {
            let obj = {
              label: {
                align: 'center'
              },
              name: x[i],
              type: 'bar',
              data: [y[i]]
            }
            series.push(obj)
          }
          let option = {
            grid: {
              bottom: '10%',
              right: '36px',
              left: '56px',
              top: '20%'
            },
            legend: {
              top: '1%',
              left: '5%'
            },
            // color: ['#5470c6'],
            color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
            title: {
              text: '指定城市不同工作经验的平均薪资',
              left: 'center',
              top: '8%'
            },
            // tooltip: {
            //   formatter: function (params) {
            //     let str = '<span style="display:inline-block;width:10px;height:10px;background:' + params.color + ';border-radius: 50%;margin-right:5px;"></span>' + params.name + '：' + params.value + 'K'
            //     return str
            //   },
            //   transitionDuration: 0
            // },
            tooltip: {
              formatter: function (params) {
                // let str = '<span style="display:inline-block;width:10px;height:10px;background:' + params.color + ';border-radius: 50%;margin-right:5px;"></span>' + params.name + '：' + params.value + '万'
                // return str
                let xValue = params[0].axisValue
                let levelValues = ''
                for (let i = 0; i < params.length; i++) {
                  if (params[i].value !== 0) {
                    levelValues += '<span style="display:inline-block;width:10px;height:10px;background:' + params[i].color + ';border-radius: 50%;margin-right:5px;"></span>' + params[i].seriesName + '：' + params[i].value + '万<br>'
                  }
                }
                return xValue + '<br>' + levelValues
              },
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              },
              transitionDuration: 0
            },
            xAxis: {
              data: ['指定城市不同工作经验的平均薪资']
            },
            yAxis: {
              type: 'value',
              name: '万'
            },
            // series: [
            //   {
            //     label: {
            //       align: 'center'
            //     },
            //     type: 'bar',
            //     data: y,
            //     backgroundStyle: {
            //       color: 'rgba(180, 180, 180, 0.2)'
            //     }
            //   }
            // ]
            series: series
          }
          bar.setOption(option)
        }
      })
    },
    getCityChart () {
      let cityNum = this.$refs.cityNum
      let bar = this.$echarts.init(cityNum)
      this.$http.get('api/data/nums/city', {
        params: {
          id: this.id
        }
      }).then(res => {
        let [x, y] = [[], []]
        if (res.data.code === 200) {
          let obj = res.data.data
          // for (let i in obj) {
          //   x.push(i)
          //   y.push(obj[i])
          // }
          let b = []
          for (let i in obj) {
            let c = {name: i, value: obj[i]}
            b.push(c)
          }
          b.forEach(a => {
            x.push(a.name)
            y.push(a.value)
          })
          let series = []
          for (let i = 0; i < x.length; i++) {
            let obj = {
              label: {
                align: 'center'
              },
              name: x[i],
              type: 'bar',
              data: [y[i]]
            }
            series.push(obj)
          }
          let option = {
            grid: {
              bottom: '10%',
              right: '36px',
              left: '56px'
            },
            legend: {
              top: '1%'
            },
            color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de', '#3ba272', '#fc8452', '#9a60b4', '#ea7ccc'],
            title: {
              text: '不同城市的需求量',
              left: 'center',
              top: '8%'
            },
            tooltip: {
              formatter: function (params) {
                // let str = '<span style="display:inline-block;width:10px;height:10px;background:' + params.color + ';border-radius: 50%;margin-right:5px;"></span>' + params.name + '：' + params.value + 'K'
                // return str
                // console.log(params)
                let xValue = params[0].axisValue
                // console.log(xValue)
                let levelValues = ''
                for (let i = 0; i < params.length; i++) {
                  if (params[i].value !== 0) {
                    levelValues += '<span style="display:inline-block;width:10px;height:10px;background:' + params[i].color + ';border-radius: 50%;margin-right:5px;"></span>' + params[i].seriesName + '：' + params[i].value + '<br>'
                  }
                }
                return xValue + '<br>' + levelValues
              },
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              },
              transitionDuration: 0
            },
            xAxis: {
              data: ['不同城市的需求量']
            },
            yAxis: {},
            series: series
            // series: [
            //   {
            //     label: {
            //       align: 'center'
            //     },
            //     type: 'bar',
            //     data: y,
            //     backgroundStyle: {
            //       color: 'rgba(180, 180, 180, 0.2)'
            //     }
            //   }
            // ]
          }
          bar.setOption(option)
        }
      })
    }
    // /data/nums/city
  }
}
</script>

<style scoped src="./employment.less" lang="less"></style>
