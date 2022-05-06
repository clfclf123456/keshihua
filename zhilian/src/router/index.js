import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)

import login from '../components/login/login'
import side from '../components/side/side'
import home from '../components/home/home'
import chart from '../components/chart/chart'
import smartShow from '../components/smartShow/smartShow'
import employment from '../components/employment/employment'
import user from '../components/user/user'
import recommend from '../components/recommend/recommend'

const originalPush = VueRouter.prototype.push

VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

const routes = [
    {path: '/', redirect: '/login'},
    {path: '/login', component: login, name: 'login'},
    {
        path: '/side',
        component: side,
        name: 'side',
        children: [
            {
                path: '/home',
                component: home,
                name: 'home',
            },
            {
                path: '/chart',
                component: chart,
                name: 'chart',
            },
            {
                path: '/smartShow',
                component: smartShow,
                name: 'smartShow',
            },
            {
                path: '/employment',
                component: employment,
                name: 'employment',
            },
            {
                path: '/user',
                component: user,
                name: 'user',
            },
            {
                path: '/recommend',
                component: recommend,
                name: 'recommend',
            }
        ]
    },
    {path: '*', redirect: '/login'},
]

//实例化VueRouter并将routes添加进去
const router = new VueRouter({
//ES6简写，等于routes：routes
//     mode: 'history',
//     base: process.env.BASE_URL,
    routes
})

export default router
