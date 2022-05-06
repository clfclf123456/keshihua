# 单位统一成万

import json

# 获取薪资均值  格式化薪资
def format_money(s: str):
    # 返回0.25
    try:
        low, high = s.split("-")[0], s.split("-")[1]
        if low[-1] == "千":
            flow = float(low[:-1])*0.1
        else:
            flow = float(low[:-1])

        if high[-1] == "千":
            fhigh = float(high[:-1])*.1
        else:
            fhigh = float(high[:-1])

        return round(float(flow+fhigh)/2, 2)
    except Exception:
        return None

def compact(s: str, salary: str):
    """判断salary是否在s的区间内"""
    try:
        s1, s2 = s.split("-")[0], s.split("-")[1]
        if s1[-1] == "千":
            s1 = float(s1[:-1])*0.1
        else:
            s1 = float(s1[:-1])
        if s2[-1] == "千":
            s2 = float(s2[:-1])*0.1
        else:
            s2 = float(s2[:-1])
        salary1, salary2 = salary.split("-")[0], salary.split("-")[1]
        if salary1[-1] == "千":
            salary1 = float(salary1[:-1]) * 0.1
        else:
            salary1 = float(salary1[:-1])
        if salary2[-1] == "千":
            salary2 = float(salary2[:-1])*0.1
        else:
            salary2 = float(salary2[:-1])
        # print((salary1, salary2), (s1, s2))
        if float(salary1)<=float(s2)<=float(salary2) or float(salary1)<=float(s1)<=float(salary2):
            return True
        return False
    except Exception:
        return False

# 返回最低工作经验
def format_worktime(s: str):
    try:
        low = s.split("-")[0]
        return float(low)
    except:
        if s =="无需经验":
            return 0
        else:
            return float(s[0])


# 计算薪资平均值
def get_avg(salary_list: list):
    sum, count =0, 0
    for salary in salary_list:
        _f = format_money(salary)
        if _f is not None:
            count += 1
            sum += format_money(salary)
    try:
        return round(sum/count, 2)
    except:
        return 0

# 处理文件 返回json
def get_json(job: str):
    _list = list()
    with open(f"helper/job/new_job/{job}.txt", "r", encoding="utf-8") as f:
        content = f.readlines()
    for line in content:
        line = line.strip("\n")
        _list.append(json.loads(line))
    return _list

# 根据学历获取薪资均值
def get_avg_by_education(job: str):
    _dic = {
        "初中及以下": list(),
        "高中": list(),
        "大专": list(),
        "本科": list(),
        "硕士": list(),
        "博士": list()
    }
    data = get_json(job)
    for line in data:
        if line["学历要求"] in _dic:
            _dic[line["学历要求"]].append(line["薪资范围"])
    for k, v in _dic.items():
        _dic[k] = get_avg(v)
    return _dic


# 获取不同城市的薪资的均值
def get_avg_by_city(job: str):
    _dic = {
        "北京": list(),
        "上海": list(),
        "广州": list(),
        "深圳": list(),
        "长沙": list(),
        "杭州": list(),
        "厦门": list(),
        "成都": list()
    }
    data = get_json(job)
    for line in data:
        if line["工作城市"] in _dic:
            _dic[line["工作城市"]].append(line["薪资范围"])
    for k, v in _dic.items():
        _dic[k] = get_avg(v)
    return _dic

# 获取不同城市不同学历的均值
def get_education_by_city(job):

    _dic = {
        "北京": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    },
        "上海": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    },
        "广州": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    },
        "深圳": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    },
        "长沙": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    },
        "杭州": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    },
        "厦门": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    },
        "成都": {
        "初中及以下": 0,
        "高中": 0,
        "大专": 0,
        "本科": 0,
        "硕士": 0,
        "博士": 0
    }
    }

    data = get_json(job)
    for line in data:
        _dic[line["工作城市"]][line["学历要求"]] += 1
    for k, v in _dic.items():
        _sum = sum(list(v.values()))
        if _sum:
            for i, j in v.items():
                v[i] =  round(j/_sum, 2)
            _dic[k] = v
    return _dic


def auto_recommend(user):
    # education_dic = {"初中及以下": "01", "高中": "02", "大专": "03", "本科": "04", "硕士": "05", "博士": "06"}
    education_dic = {"01": "初中及以下", "02": "高中", "03": "大专", "04": "本科", "05": "硕士", "06": "博士"}

    want_job = user.want_job
    education = user.education
    worktime = user.worktime

    result = []
    data = get_json(want_job)
    for line in data:
        if line["学历要求"] == education_dic[education]:
            if int(format_worktime(line["工作经验"])) <= int(worktime):
                if "100" in line["公司规模"]:
                    if all([i in line["福利待遇"] for i in ["五险一金"]]):
                        result.append(line)
    return result

def get_avg_worktime_by_city(job: str, city: int):
    city_dic = {"010000": "北京", "020000": "上海", "030200": "广州", "040000": "深圳", "190200": "长沙", "080200": "杭州", "110300": "厦门", "090200": "成都"}
    data = get_json(job)
    _dic = dict()

    for line in data:
        if line["工作城市"] == city_dic[city]:
            if line["工作经验"]:
                if line["工作经验"] not in _dic:
                    _dic[line["工作经验"]] = [line["薪资范围"]]
                else:
                    _dic[line["工作经验"]].append(line["薪资范围"])
    for k, v in _dic.items():
        _dic[k] = get_avg(v)
    return _dic


def get_nums_city(job):
    city_dic = {"010000": "北京", "020000": "上海", "030200": "广州", "040000": "深圳", "190200": "长沙", "080200": "杭州",
                "110300": "厦门", "090200": "成都"}
    data = get_json(job)

    _dic = dict()

    for line in data:
        if line["工作城市"] in list(city_dic.values()):
            if line["工作城市"] not in _dic:
                _dic[line["工作城市"]] = 1
            else:
                _dic[line["工作城市"]] += 1
    return _dic

def get_ciyun_(job):

    wel = {}
    data = get_json(job)
    for line in data:
        for i in line["福利待遇"].split(" "):
            if i not in wel:
                wel[i] = 1
            else:
                wel[i] += 1
    return wel




