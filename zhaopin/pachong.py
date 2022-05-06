
import re
import execjs
import time
import requests,json,datetime



class PaChong:

    def __init__(self):
        self.urls_list = []
        self.cookie_v2_list = []

    def js_cookie(self, arg1):
        with open('51jod 动态cookie.js', 'r', encoding='utf-8') as f:
            js_code = f.read()
            ctx = execjs.compile(js_code)
            result = ctx.call('get_app', arg1)
        return result

    def get_cookie(self):
        url = 'https://search.51job.com/list/00000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
            # 设置请求头部 防止网站有反爬虫程序
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            # 添加发送请求的浏览器语言
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 添加返回格式
        }
        while True:
            try:
                html = requests.get(url, headers=head, timeout=5).text
                print('开始获取cookie')
                arg1 = re.findall("var arg1='(.*?)';", str(html))
                arg1 = arg1[0]
                cookie_v2 = self.js_cookie(arg1)
                print(cookie_v2)
                self.cookie_v2_list.append(cookie_v2)
                return ''
            except Exception as e:
                if e == 'list index out of range':
                    return ''
                continue

    def q1(self, url):  # 获取网页json 用
        if len(self.cookie_v2_list) == 0:
            self.get_cookie()
        cooki = self.cookie_v2_list[-1]
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
            # 设置请求头部 防止网站有反爬虫程序
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            # 添加发送请求的浏览器语言
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            # 添加返回格式
            'Cookie': 'acw_sc__v2=%s' % cooki
            # 51job采用的是动态cookie验证  由于有效期较长 大概1小时左右  所以选择手动输入cookis
        }
        req = requests.get(url, headers=head, timeout=5)  # 发送请求
        # req.encoding = req.apparent_encoding
        # req.encoding = "utf-8"
        return req.text

    def q2(self, city_id, salary, job, education, page):
        # 开始获取页数 并且储存在txt文件里面
        # for mun in range(1, max_page + 1):  # 在这里设定页数
        url_list_new = f'https://search.51job.com/list/{city_id},000000,0000,00,9,{salary},{job},2,{page}.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom={education}&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare='
        self.urls_list.append(url_list_new)

    def q3(self):  # 下载用
        res = []
        count = 1  # 计数器 用于计算行数
        for urls in self.urls_list:
            print(urls)
            if urls == '':
                continue

            time.sleep(0.5)  # 设置休息间隔  防止速度太快被封禁ip
            data_json = self.q1(urls)  # 发送请求
            print(data_json)
            data_json = json.loads(data_json)  # 转换为json格式
            data = data_json['engine_jds']  # 取值
            for data_for in data:
                _dic = dict()
                count += 1

                # 筛选出岗位名字
                name = data_for['job_name']
                _dic["职位名称"] = name
                # print(name)

                # 公司名
                workname = data_for['company_name']
                _dic["公司名称"] = workname
                # print(workname)

                # 薪资
                money = data_for['providesalary_text']
                _dic["薪资范围"] = money
                # print(money)

                # 工作城市
                workarea = data_for['workarea_text']
                _dic["工作城市"] = workarea

                # print(workarea)

                # 发布时间 待定

                # 公司类型
                worktype = data_for['companytype_text']
                # print(worktype)
                _dic["公司类型"] = worktype

                # 日常待遇
                welf = data_for['jobwelf']
                _dic["福利待遇"]  =welf
                # print(welf)

                # 要求
                bute_text = data_for['attribute_text']
                # 要求里面有很多项 内容 分割一下

                # 要求 --工作经验
                try:  # 异常处理
                    workexp = re.findall(' \'(.*?经验)\'', str(bute_text))
                    _dic["工作经验"] = workexp[0]
                    # print('工作经验', workexp)
                except Exception as ef:
                    pass
                # 学历
                try:  # 异常处理
                    shool = re.findall('博士|硕士|研究生|本科|大专', str(bute_text))
                    _dic["学历要求"] = shool[0]
                    # print('学历', shool)
                except Exception as ef:
                    pass
                # 公司规模
                try:
                    size = data_for['companysize_text']
                    _dic["公司规模"] = size
                except Exception as e:
                    size = '空'
                print(size)
                res.append(_dic)
        print(len(res))
        return res

    def run(self, city_id, salary, job, education, page):
        self.q2(city_id, salary, job, education, page)
        return self.q3()


# pc = PaChong()

if __name__ == '__main__':

    pc = PaChong()
    res = pc.run(city_id=530, salary="3000-100000",job="java", education="04",page=1)
    print(res)



