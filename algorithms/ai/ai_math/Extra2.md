# 番外-似然函数：一个摸小球的例子
> 似然函数的话题在 [线性回归](/algorithms/ai/ai_math/LinearRegression.md) 一篇中解释过，然后由于实在是太重要了，在其他的markdown中频频出现，这里就再以一个简单的摸小球的例子进一步解释

## 一、问题
1. 一个袋子里有数量若干的两种颜色的小球，黑色和白色
2. 有放回的摸100个小球，有70个是白色
3. 求袋子中的白色小球的占比最有可能是多少

## 二、分析过程

1. 袋子中的白色小球占比，是多少都有可能，有可能总共就两个小球，一黑一白，但是可能性比较低
2. 所以只能求出袋子中白色小球的占比 最有可能是多少
3. 总结：袋子中的白色小球的占比是多少才能使得有放回的摸100个小球，有70个是白色 这种情况概率最大

## 三、求解过程

1. 假设袋子中白色小球占比为 p，则目标情况

   $p^{70} * (1-p)^{30}$\
也就是说，p是多少，发生题目描述的那个事件的概率($p^{70} * (1-p)^{30}$)最大

2. 对上述目标情况求导，令导数等于零

   $70*p^{69}*(1-p)^{30}+p^{70}*30*(1-p)^{29}*(-1)=0$
> 注：复合函数求导 $uv=u'v+v'u$
3. 同除$p^{69}*(1-p)^{29}$

   $70*(1-p)+p*30*(-1)=0$

4. 化简得

   $70=100p$

## 四、重新理解
在[线性回归](/algorithms/ai/ai_math/LinearRegression.md) 一篇中提到<center><font color=62D257>一件事情发生了，一定是可能性最大的那件事发生了才合理</font></center>

1. 这件事情就是题目描述的事情
2. 在机器学习中就是我们采集到的特征是它们个字标签的事情（训练集的特征和标签匹配的事情）
3. 那么就把每个样本能够和标签匹配的概率 连续乘 起来，让这个表达式最大就可以了
> 数据是独立同分布的假设保证我们乘起来的概率就是联合概率

## 五、深入理解
### 5.1 似然与概率
> 似然基本可以等同于概率，但并不完全相同

1. 机器学习的任务，是把参数当成“因”，把训练数据当成“果”，通过训练数据来学习参数
2. 而参数并不是事件，不符合概率的严格定义，因此对于某一参数产生实际数据情况的可能性，只能称之为“似然”
### 5.2 似然函数
> 「似然概率」单独来看没有意义，乘以一个常数得到似然函数的表达
1. 似然函数是一个由“因”到“果”的条件概率和常数相乘
2. 似然函数是一个关于模型参数的函数（衡量了输入有多大可能得到输出）

### 5.3 先验概率、后验概率、似然函数
> 因：瓜熟；果：蒂落
1. P(蒂落): 先验概率
2. P(蒂落｜瓜熟): 后验概率
3. L(瓜熟｜蒂落) = C * P(瓜熟｜蒂落): 似然函数