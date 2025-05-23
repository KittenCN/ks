---
description: 数学 基础知识
---

[](...menustart)

- [偏导数,梯度](#eb898d04aa10223d988f53daa7844b8f)
    - [Recap](#8912c5512db9003e5c8ce07b7ff36a88)
    - [相关概念的定义和公式](#430cca5a0998d5986401995af25a41f6)

[](...menuend)


<h2 id="eb898d04aa10223d988f53daa7844b8f"></h2>

# 偏导数,梯度

导数描述的是函数在某一点处的变化快慢的趋势，是一个变化的速率，微分描述的是函数从一点,移动dx,到另一点的变化幅度，是一个变化的量。

在一元函数中，函数从一个点到另一点的变化只有一个方向，就是沿着函数曲线移动就醒了。

然而多元函数就不同了，多元函数往往是一个面。 过A点有无数条曲线，也就必然有无数条切线。**如何将一元函数的导数和微分的概念进行拓展，来适应这些"无数"的问题** ?

- 变化快慢
    - A点存在无数条切线，这些切线的斜率都是导数，就定义一个方向导数来表示他们。
    - 既然有无数条切线，就会有无数个变化的方向，这里面哪个方向变化是最快的呢？  把变化最快的那个方向定义为**梯度**,所以，梯度其实是一个向量, 表示的是在A点变化趋势最大的那个方向。
    - 变化快慢的问题基本解决了

- 变化量
    - 从A到B 变化多少的问题，这就是全微分的定义了。 把从A到B的变化的多少定义为全微分。
- 如果函数降维变化，比如固定x ，让y 单独变化，这种变化怎么描述
    - 降维变化定义为 **偏导数** .


<h2 id="8912c5512db9003e5c8ce07b7ff36a88"></h2>

## Recap 

1. 方向导数
    - 函数在A点无数个切线的斜率的定义。 每一个切线都代表一个变化的方向。
2. 梯度
    - 函数在A点无数个变化方向中，变化最快的那个方向。
3. 全微分
    - 函数从A点到B点变化的量( 其实是取一个无穷小的变化的量 )
4. 偏导数
    - 多元函数降维时候的变化， 比如二元函数固定y，只让x单独变化，从而看成是关于x的一元函数的变化来研究.

<h2 id="430cca5a0998d5986401995af25a41f6"></h2>

## 相关概念的定义和公式

1. 偏导数
    - 举例: 二元函数关于x的偏导公式
    - ![](../../ap/calculus/imgs/partialDerivative_00.svg)
2. 方向导数
    - 二元函数f 在A点 沿一个方向L变化，这条切线L 由点A和切线L上另外一个点B确定。
    - 其中, A(x1,y1), B(x2,y2),  那么f沿L的方向导数:
    - ![](../../ap/calculus/imgs/dirDerivative.svg)
3. 梯度
    - 数学家经过证明，发现函数只要每一个变量都沿着关于这个变量的偏导数所指定的方向来变化，函数整体变化就能达到最快(变化的绝对值最大).
    - 因此函数在A点出的梯度为( 以三元函数为例 ):
    - gradA = ( f<sub>x</sub>(A),f<sub>y</sub>(A),f<sub>z</sub>(A) )

