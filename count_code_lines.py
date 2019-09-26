# coding=utf-8
'''
统计代码脚本
'''
import os,sys
file_suffix = ".py"
def count_code(path):
    count = 0
    flag = True
    # 判断传入值是文件
    if os.path.isfile(path):
        # 判断是否是 py 文件
        if path.endswith(file_suffix):
            # 如果是 py 文件就打开文件循环每一行代码，进行逻辑处理
            with open(path,"r",encoding="utf8") as fr:
                for line in fr:


                    # 不统计注释
                    if (line.startswith('"""') or line.startswith('\'\'\'')) and flag:
                        flag = False
                        continue
                    elif (line.startswith('"""') or line.startswith('\'\'\'')) and not flag:
                        flag = True
                        continue

                    if line == "\n" and flag:
                        continue
                    elif "#" in line and flag:
                        continue
                    elif flag:
                        count += 1
    # 判断传入值是目录
    elif os.path.isdir(path):

        # 将目录下的文件遍历
        f = os.walk(path)
        for file in f:

            # 解压缩取出来
            d_dir, _, file = file
            for f in file:
                # 拼凑文件的绝对路径
                f = os.path.join(d_dir, f)
                # print(f)
                file_path_list = f.split(".")
                # if f.endswith(file_suffix):
                if file_path_list[-1] == "py":
                    # 如果是 py 文件就打开文件循环每一行代码，进行逻辑处理
                    # print(f)
                    with open(f, "r", encoding="utf8") as fr:
                        for line in fr:

                            # 不统计注释
                            if (line.startswith('"""') or line.startswith('\'\'\'')) and flag:
                                flag = False
                                continue
                            elif (line.startswith('"""') or line.startswith('\'\'\'')) and not flag:
                                flag = True
                                continue

                            if line == "\n" and flag:
                                continue
                            elif "#" in line and flag:
                                continue
                            elif flag:
                                count += 1

                # else:
                #     print(f"{f}不是.py文件")

    return count

if __name__ == '__main__':
    path = sys.argv[1]
    #path = r"C:\Users\Administrator\Desktop\老男孩python文档\老男孩Python程序编写\正式班"
    count = count_code(path)
    print(count)

