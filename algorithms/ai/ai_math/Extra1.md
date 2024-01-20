# 决策树计算示例
> 付尧 PKU 机器学习决策树示例
## 目录
[决策树计算示例](#决策树计算示例)

&emsp;&emsp;[一、数据集](#一数据集)

&emsp;&emsp;[二、ID3过程](#二ID3过程)

&emsp;&emsp;&emsp;&emsp;[2.1&nbsp;第一轮计算](#21-第一轮计算)

&emsp;&emsp;&emsp;&emsp;[2.2&nbsp;第一轮计算后的结果](#22-第一轮计算后的结果)

&emsp;&emsp;&emsp;&emsp;[2.3&nbsp;第二轮计算](#23-第二轮计算)

&emsp;&emsp;&emsp;&emsp;[2.4&nbsp;构建树](#24-构建树)

&emsp;&emsp;[三、CART过程](#三CART过程)

&emsp;&emsp;&emsp;&emsp;[3.1&nbsp;第一轮计算](#31-第一轮计算)

&emsp;&emsp;&emsp;&emsp;[3.2&nbsp;第一轮计算后的结果](#32-第一轮计算后的结果)

&emsp;&emsp;&emsp;&emsp;[3.3&nbsp;第二轮计算](#33-第二轮计算)

&emsp;&emsp;&emsp;&emsp;[3.4&nbsp;第三轮计算](#34-第三轮计算)

&emsp;&emsp;&emsp;&emsp;[3.5&nbsp;构建树](#35-构建树)
## 一、数据集
Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
1      |  Sunny | Hot | High | Weak | No
2      |  Cloudy | Hot | High | Weak | Yes
3      |  Sunny | Mild | Normal | Strong | Yes
4      |  Cloudy | Mild | High | Strong | Yes
5      |  Rainy | Mild | High | Strong | No
6      |  Rainy | Cool | Normal | Strong | No
7      |  Rainy | Mild | High | Weak | Yes
8      |  Sunny | Hot | High | Strong | No
9      |  Cloudy | Hot | Normal | Weak | Yes
10      |  Rainy | Mild | High | Strong | No

## 二、ID3过程
> 指导思想：通过「信息增益进行维度排序」（找最大的），并「保留维度的所有项」构建多叉树，直到不可再分或信息增益低于阈值
### 2.1 第一轮计算
1. 经验熵：，带入公式得$$H(D)=-\frac{5}{10}log_2\frac{5}{10}-\frac{5}{10}log_2\frac{5}{10} = 2$$
2. Weather维度条件熵【示例】 \
2.1 Sunny：$$ H(D|Weather=Sunny)=-\frac{2}{3}log_2\frac{2}{3}-\frac{1}{3}log_2\frac{1}{3} = 0.918$$
2.2 Cloudy：$$ H(D|Weather=Cloudy)=-\frac{3}{3}log_2\frac{3}{3}-\frac{0}{3}log_2\frac{0}{3} = 0$$
2.3 Rainy：$$ H(D|Weather=Rainy)=-\frac{3}{4}log_2\frac{3}{4}-\frac{1}{4}log_2\frac{1}{4} = 0.811$$
2.4 加权求和：$$ H(D|Weather)=\frac{3}{10}*H(D|Weather=Sunny) + \frac{3}{10}*H(D|Weather=Cloudy) + \frac{4}{10}*H(D|Weather=Rainy)= 0.6$$
2.5 信息增益：$$g(D, Weather) = H(D) - H(D|Weather) = 0.4$$
3. 同理可得
$$g(D, Temperature)=0.115$$
$$g(D, Humidity)=0.035$$
$$g(D, Wind)=0.125$$
$$g(D, Weather) > g(D, Wind) > g(D, Temperature) > (D, Humidity)$$
> 总结：第一轮，选择Weather作为最优特征
### 2.2 第一轮计算后的结果
此时按照Weather划分得到：
1. Weather==Sunny：

Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
1      |  Sunny | Hot | High | Weak | No
3      |  Sunny | Mild | Normal | Strong | Yes
8      |  Sunny | Hot | High | Strong | No

2. Weather==Cloudy：

Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
2      |  Cloudy | Hot | High | Weak | Yes
4      |  Cloudy | Mild | High | Strong | Yes
9      |  Cloudy | Hot | Normal | Weak | Yes

3. Weather==Rainy：

Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
5      |  Rainy | Mild | High | Strong | No
6      |  Rainy | Cool | Normal | Strong | No
7      |  Rainy | Mild | High | Weak | Yes
10      |  Rainy | Mild | High | Strong | No
> 综上：按分类可知，Weather=Cloudy无须再分，标签为Yes，Weather=Sunny和Rainy继续讨论
### 2.3 第二轮计算
1. Weather==Sunny：按照第一轮计算的思路得到
$$g(D, Temperature)=0.918$$
$$g(D, Humidity)=0.918$$
$$g(D, Wind)=0.252$$
$$g(D, Temperature) = g(D, Humidity) > g(D, Wind)$$
> 总结1：此时，选择Temperature作为最优特征\
> 总结2：Weather=Sunny，选择Temperature切分后，无需再分，Hot -> No，Mild->Yes

2. Weather==Rainy：按照第一轮计算的思路得到
$$g(D, Temperature)=0.123$$
$$g(D, Humidity)=0.123$$
$$g(D, Wind)=0.811$$
$$g(D, Wind) = g(D, Humidity) = g(D, Temperature)$$
> 总结1：此时，选择Wind作为最优特征\
> 总结2：Weather=Rainy，选择Wind切分后，无需再分，Strong -> No，Weak->Yes

### 2.4 构建树
经过两轮划分后，得到最终树，逻辑如下：
1. Weather==Cloudy -> Yes
2. (Weather==Sunny && Temperature==Hot) -> No
3. (Weather==Sunny && Temperature==Mild) -> Yes
4. (Weather==Rainy && Wind==Strong) -> No
5. (Weather==Rainy && Wind==Weak) -> Yes

## 三、CART过程
> 指导思想：通过「GINI系数进行维度排序」(找最小的)，需要「对维度项寻找合适切分点」构建二叉树（离散值用OVR思想，连续值排序后用均值思想），直到不可再分或GINI系数低于阈值
### 3.1 第一轮计算
1. Weather维度GINI系数
$$GINI(D,Weather=Sunny)=\frac{3}{10} * [2*\frac{1}{3}(1-\frac{1}{3})] + \frac{7}{10} * [2*\frac{4}{7}(1-\frac{4}{7})]=0.476$$

$$GINI(D,Weather=Cloudy)=\frac{3}{10} * [2*\frac{3}{3}(1-\frac{3}{3})] + \frac{7}{10} * [2*\frac{2}{7}(1-\frac{2}{7})]=0.286$$

$$GINI(D,Weather=Rainy)=\frac{4}{10} * [2*\frac{1}{4}(1-\frac{1}{4})] + \frac{6}{10} * [2*\frac{4}{6}(1-\frac{4}{6})]=0.417$$
> 总结：比较后以Cloudy（0.286）作为 Weather的GINI系数

2. 其他维度基尼系数同理（Humidity和Wind不用考虑切分点）：
$$GINI(D,Temperature)=(D,Temperature=Cool)=0.444（其他两项为0.5和0.48）$$
$$GINI(D,Humidity)=0.476$$
$$GINI(D,Wind)=0.417$$
> 总结：选择Weather作为最优特征，且以Cloudy作为最优划分点
### 3.2 第一轮计算后的结果
1. Weather==Cloudy：

Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
2      |  Cloudy | Hot | High | Weak | Yes
4      |  Cloudy | Mild | High | Strong | Yes
9      |  Cloudy | Hot | Normal | Weak | Yes

2. Weather!=Cloudy：

Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
1      |  Sunny | Hot | High | Weak | No
3      |  Sunny | Mild | Normal | Strong | Yes
5      |  Rainy | Mild | High | Strong | No
6      |  Rainy | Cool | Normal | Strong | No
7      |  Rainy | Mild | High | Weak | Yes
8      |  Sunny | Hot | High | Strong | No
10      |  Rainy | Mild | High | Strong | No
> 综上：按分类可知，Weather=Cloudy无须再分，标签为Yes，Weather!=Cloudy继续讨论
### 3.3 第二轮计算
在Weather!=Cloudy的情况下，重新按照3.1的计算可得
$$GINI(D,Temperature)=(D,Temperature=Mild)=0.286（其他两项为0.343和0.381）$$
$$GINI(D,Humidity)=0.371$$
$$GINI(D,Wind)=0.371$$
> 总结：此时，选择Temperature作为最优特征，Temperature=Mild最优切分点，数据如下
1. Temperature==Mild：

Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
3      |  Sunny | Mild | Normal | Strong | Yes
5      |  Rainy | Mild | High | Strong | No
7      |  Rainy | Mild | High | Weak | Yes
10      |  Rainy | Mild | High | Strong | No

2. Temperature!=Mild：

Day     | Weather   |  Temperature | Humidity  |  Wind | Play?
----     | ----     | ----     | ----     | --- | ---
1      |  Sunny | Hot | High | Weak | No
6      |  Rainy | Cool | Normal | Strong | No
8      |  Sunny | Hot | High | Strong | No

> 总结：此时，Temperature!=Mild 无须再分，标签为No，Temperature==Mild 继续讨论
### 3.4 第三轮计算
重新按照3.1的计算可得

$$GINI(D,Humidity)=0.333$$
$$GINI(D,Wind)=0.333$$

> 总结1：此时，选择Humidity 或 Wind均可，无须再讨论最优切分点\
> 总结2：本例中选择 Humidity 作为最优特征
> 总结3：Humidity==Normal 标签为yes，Humidity!=Normal  Wind==Strong 标签为yes，Wind!=Strong 标签为No

### 3.5 构建树
经过三轮划分后，得到最终树，逻辑如下：
1. Weather=Cloudy -> Yes，否则走第二步
2. Temperature!=Mild -> No，否则走第三步
3. Humidity==Normal -> Yes，否则走第四步
4. Wind==Strong -> Yes，否则No