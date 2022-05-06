import json

def clear(job):
    _list = list()
    with open(f"{job}.txt", "r", encoding="utf-8") as f:
        content = f.readlines()
    for line in content:
        line = json.loads(line.strip("\n"))

        # 处理薪资
        line_salary = line["薪资范围"].split("-")
        if line_salary[0][-1] == "万":
            if float(line_salary[0][:-1])<=5:
                # 处理工作经验
                with open(f"new_job/{job}.txt", "a", encoding="utf-8") as f:
                    f.write(json.dumps(line, ensure_ascii=False))
                    f.write("\n")

clear("运维")

