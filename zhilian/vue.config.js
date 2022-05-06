const { defineConfig } = require('@vue/cli-service')
module.exports = {
  publicPath: './',
  devServer: {
    port: '9088',
    open: true,
    proxy: {
      '/': {
        target: 'http://29c17650j9.zicp.vip',
        changeOrigin: true,
        ws: false,
        // pathRewrite: {
        //     "^/Views": ""
        // }
      }
    }
  },
  lintOnSave:false  //关闭语法检查
}
