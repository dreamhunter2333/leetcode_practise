# -*- coding: utf-8 -*-

import random


def gene_height(pram):
    """"
    生成不存在于pram中的身高
    """
    flag = True
    line = random.randint(150, 300)
    for people_line in pram:
        if line in people_line:
            flag = False
    if flag:
        return line
    else:
        return gene_height(pram)


if __name__ == '__main__':
    # 百人数组
    people = [[] for c in range(10)]
    # 生成100个身高
    for i in range(10):
        for j in range(10):
            people[i].append(gene_height(people))
        print(people[i])
    high_list = []
    short_list = []
    # 获得高子和矮子
    for col in range(10):
        high_list.append(max(people[col]))
        short_list.append(min([people[col][row] for row in range(10)]))
    print("高子： " + str(high_list))
    print("矮子： " + str(short_list))
    print("「高子里的矮子」: " + str(min(high_list)) + "\n「矮子里的高子」: " + str(max(short_list)))
    # 为什么「高子里的矮子」>「矮子里的高子」
    high_position = []
    short_position = []
    for p in range(10):
        for q in range(10):
            if min(high_list) == people[p][q]:
                high_position = [p, q]
            if max(short_list) == people[p][q]:
                short_position = [p, q]
    print(high_position)
    print(short_position)
    # 高子里的矮子 > 所在行除了自己的所有人
    # for person in people[high_position[0]]:
    #     print(people[high_position[0]][high_position[1]] >= person)

    # 高子里的矮子 >= 高子里的矮子 所在行 和 矮子里的高子所在列 的人
    print(str(people[high_position[0]][high_position[1]]) + '>=' + str(people[high_position[0]][short_position[1]]))
    # 交叉处的人 >= 矮子里的高子
    print(str(people[high_position[0]][short_position[1]]) + '>=' + str(people[short_position[0]][short_position[1]]))
