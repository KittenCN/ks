# AdaBoost计算示例
> 付尧 PKU 机器学习AdaBoost示例
## 目录
[AdaBoost计算示例](#AdaBoost计算示例)

&emsp;&emsp;[目录](#目录)

&emsp;&emsp;[一、数据集](#一数据集)

&emsp;&emsp;[二、AdaBoost过程](#二AdaBoost过程)

&emsp;&emsp;&emsp;&emsp;[2.1&nbsp;初始化权重](#21-初始化权重)

&emsp;&emsp;&emsp;&emsp;[2.2&nbsp;训练第一个分类器](#22-训练第一个分类器)

&emsp;&emsp;&emsp;&emsp;[2.3&nbsp;训练第二个分类器](#23-训练第二个分类器)

&emsp;&emsp;&emsp;&emsp;[2.4&nbsp;训练第三个分类器](#24-训练第三个分类器)

&emsp;&emsp;[三、代码附录](#三代码附录)

---
## 一、数据集
Index     | X1   |  X2 | Y  
----     | ----     | ----     | ----     
1      |  3 | 2050 | D
2      |  1 | 2200 | A 
3      |  2 | 2090 | A 
4      |  4 | 2230 | D
5      |  5 | 2330 | A
6      |  6 | 2220 | D 
7      |  6 | 2390 | A 
8      |  7 | 2320 | A 
9      |  8 | 2330 | D 
10      |  8 | 2090 | D 

## 二、AdaBoost过程
> 指导思想：每一轮调整样本的权重（分类错误时对不同的样本区别计算错误率），得到多个分类器，根据分类器的不同权重加权得到预测结果
> 说明：为了方便，弱分类器只采用 某一个特征进行二分
### 2.1 初始化权重
$$D_1 = (w_{11}, w_{12}....,w_{110})$$
$$w_{1i}=\frac{1}{10}, i=1,2,3,4...,10$$

### 2.2 训练第一个分类器
经过代码查找得到最佳分类为 特征x1
1. 当x1 < 2.5 预测A
2. 当x1 > 2.5 预测D
3. 误分率 $G_1(x)= 0.1 + 0.1 + 0.1 = 0.3$
4. 模型权重：$\alpha_1 = \frac{1}{2}log\frac{1-e_1}{e_1}=0.4236$
5. 更新样本权重：$w_{wi} = \frac{w_{1i}}{Z_1}exp(-\alpha_2y_iG_1(x_i))$
6. 更新后：除了样本578是0.16667，其他样本是0.07143
### 2.3 训练第二个分类器
经过代码查找得到最佳分类为 特征x1
1. 当x1 < 7.5 预测A
2. 当x1 > 7.5 预测D
4. 误分率 $G_2(x)= 0.214$
5. 模型权重：$\alpha_2 = \frac{1}{2}log\frac{1-e_2}{e_2}=0.6496$
6. 更新样本权重
### 2.4 训练第三个分类器
经过代码查找得到最佳分类为 特征x2
1. 当x2 < 2230.5 预测D
2. 当x2 > 2230.5 预测A
4. 误分率 $G_3(x)= 0.136$
5. 模型权重：$\alpha_3 = \frac{1}{2}log\frac{1-e_2}{e_2}=0.9229$
6. 此时，加权模型发现全部预测正确
## 三、代码附录

~~~python
# author: fuyao.cookie
# company: PKU
# date: 2022-03-27

# 该项目是AdaBoost算法的一个例题
# 可以修改load_data方法中的数据集，以进行其他数据集的训练
# 算法核心：
#   1. 每个样本都有一个权重（衡量分类错误时的误分率）
#   2. 每一轮需要得到一个误分率最小的算法（会受到之前预测正确还是错误的影响）
#       为了演示方便，这里采用了类似CART的思想进行每一个决策树的划分（二分类）
#   3. 根据每一轮的误分率也会得到这次算法的最终权重
#       math.log((1-err_rate) / err_rate) * 0.5
#   4. 每一轮算完还需要重新分配样本的权重
#       temp = data["weight"] * np.exp(-1 * data["rightOrWrong"] * weight_of_model)   # rightOrWrong=1 or -1
#       data["weight"] = temp / temp.sum()
#   5. 全部分类正确或者触发终止条件会停止迭代（代码中是10次）
#   6. 加权最终的算法得到最终的结果
#       for ...
#           res += temp_perdict * weight_of_model
#       data["final_predict"] = np.sign(res)


import pandas as pd
import math
import numpy as np


# load_data : 加载数据（数据配置）
def load_data():
    # A -> 1    D -> -1
    features = ["x1", "x2"] # 特征列
    x1 = [3, 1, 2, 4, 5, 6, 6, 7, 8, 8]
    x2 = [2050, 2200, 2090, 2230, 2330, 2220, 2390, 2320, 2330, 2090]
    y = [-1, 1, 1, -1, 1, -1, 1, 1, -1, -1]

    weight = np.array([1/len(y)] * len(y))
    index = range(1, len(y)+1)

    data = pd.DataFrame({"x1": x1, "x2": x2, "y": y, "weight": weight, "index": index})
    return data, features


# cal_error : 计算当前模型的错误率
def cal_error(data, feature, n, rule):
    # rule: -1: 前n个就是 “D”   1  前n个就是就是“A”
    temp = data.sort_values(by=feature)
    temp = temp.reset_index(drop=True)
    temp["predict"] = np.zeros(len(temp))
    temp["rightOrWrong"] = -1
    temp["predict"][:n] = -1 if rule == -1 else 1
    temp["predict"][n:] = 1 if rule == -1 else -1
    temp["predict"][:n] = 1 if rule == 1 else -1
    temp["predict"][n:] = -1 if rule == 1 else 1
    temp["rightOrWrong"][temp["predict"] == temp["y"]] = 1
    div = temp[feature][0]-0.5 if n==0 else temp[feature][n-1]+0.5
    return temp, temp[temp["predict"] != temp["y"]]["weight"].sum(), n, rule, div


# cal_weight_of_model : 计算当前模型的权重
def cal_weight_of_model(err_rate):
    return math.log((1-err_rate) / err_rate) * 0.5


# cal_weight_of_sample : 计算每次预测后的样本权重分布
def cal_weight_of_sample(data, weight_of_model):
    # 预测一致（相同）相乘为1，取反为-1
    # 预测不一致（相反）相乘为-1，取反为1
    temp = data["weight"] * np.exp(-1 * data["rightOrWrong"] * weight_of_model) 
    data["weight"] = temp / temp.sum()
    return data


# per_round : 每一轮的训练
def per_round(data, features):
    lowest_err = 1
    best_feature = None
    best_top = None
    best_rule = None
    best_div = None
    for t in features:  # 遍历所有特征
        for i in range(len(data)+1):  # 遍历所有可能的划分方式
            for rule in [-1, 1]:  # 遍历两种分类方法，小于阈值是分类1 或者 小于阈值是分类2
                temp, err, n ,rule, div = cal_error(data, t, i, rule)
                if err < lowest_err:
                    lowest_err = err
                    data = temp
                    best_feature = t
                    best_rule = rule
                    best_top = n
                    best_div = div
    
    # 计算当前模型权重
    weight_of_model = cal_weight_of_model(lowest_err)
    # 更新数据权重
    data = cal_weight_of_sample(data, weight_of_model)
    # 返回所有信息
    return data, lowest_err, weight_of_model, (best_feature, best_top, best_rule, best_div)


# cal_final_err : 计算最终模型效果（如果全对提前终止）
def cal_final_err(data, weight_of_model_list, model_list):
    # 每一个弱分类器结果为1或者-1（代表两个类）
    # 加权平均后，大于0取1，小于0取-1
    # rule: -1: 前n个就是 “D”   1  前n个就是就是“A”
    res = np.zeros(len(data))
    for i in range(len(model_list)):
        temp_perdict = np.zeros(len(data))
        weight_of_model = weight_of_model_list[i]
        f, top, rule, div = model_list[i]
        print(div, rule)
        temp_perdict[data[f]<div] = -1 if rule == -1 else 1
        temp_perdict[data[f]>div] = 1 if rule == -1 else -1
        temp_perdict[data[f]<div] = 1 if rule == 1 else -1
        temp_perdict[data[f]>div] = -1 if rule == 1 else 1
        
        res += temp_perdict * weight_of_model
        print(temp_perdict, weight_of_model)
    data["final_predict"] = np.sign(res)
    data["final_right_or_wrong"] = data["final_predict"]==data["y"]
    return data

# 核心函数
def run():
    # 1. 加载数据
    data, features = load_data()

    # 2. 初始化全局结果
    err_list = []
    weight_of_model_list = []
    model_list = []  # (x1, 3, 1)  x1升序后，小于3是A

    # 3. 构建树
    for i in range(10):  # 最多10轮
        data, lowest_err, weight_of_model, model = per_round(data, features)
        err_list.append(lowest_err)
        weight_of_model_list.append(weight_of_model)
        model_list.append(model)
        data = cal_final_err(data, weight_of_model_list, model_list)
        # 如果全对直接退出
        if data["final_right_or_wrong"].sum() == len(data["final_right_or_wrong"]):
            break
    
    # 4. 输出结果
    print(" ============= 计算已完成 =============")
    print("误分率变化列表：", err_list)
    print("模型权重列表：", weight_of_model_list)
    print("模型列表：", model_list)
    print(data)


if __name__ == "__main__":
    run()
~~~