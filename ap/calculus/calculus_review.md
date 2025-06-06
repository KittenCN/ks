---
description: CoderFAN 资料库 calculus
---

[](...menustart)

- [微积分总览](#cb7b69587d37b4d0d6623ec0b7e15e8f)
    - [differential calculus  微分学](#ed8d58aa5d09e3b6ae85504d2b50fdc2)
    - [integral calculus  积分学  integral(from whole)](#5f310f9e2e62d1ba91b27c396331a47b)
    - [函数1 和 函数2 的关系](#f4fd7794a95a913d0604b6a980f2038c)
- [导数总览](#7b2109108288b88fa80ba74730b04212)
    - [几个重要的函数导数](#b73a32da207260c8c5df891313bd2b8f)
- [极值和二阶导数](#1f1fa83ad7ddf7d7abdfe107fd46cf12)
    - [一阶导数 求 极值点 ，导数=0](#f032e96900ac9530a6f4ffa8ffc71cce)
    - [二阶导数 确定 极值点性质](#095c70e4ae714fca1eabc94bdc766ee4)
    - [距离／速度 / 加速度 的例子](#20aaf0154f6499efa187fd95a73aed9e)
    - [Convex ,bending up, 凸 , 极小值 , ex: x²](#2b7d4dfa847aec16509a257e42a39fe5)
    - [Concave, bending down ,凹, 极大值](#284c4ee74be0c0d60c4df4bd3debf94d)
    - [二阶导数性质](#b86d19c5489576bef0c5d5bf04de7c00)
    - [导数应用例子](#0b43f7c8e73f59c9d943180af743bb58)
- [指数函数 y=eˣ](#6595e47721a328f1a5bb516f8fa0813a)
    - [重要性质:](#c235979153ce388fa10fdc2c52332bcc)
    - [eˣ 构建:](#f2737fb06fa1bdff68a619d1df455e4a)
    - [银行存款和e的联系](#2fd7cf83daee9c8035f0bc838e579211)
    - [`y' = dy/dx = ay` 的情况, `y = eªˣ`](#13b313e41f18896d8340296932e9cb46)
- [积分总览](#908dab53380191dbf2ba5d54eed208eb)
- [sin / cos 的导数](#af4815e6482f933efa0b9289e2658753)
    - [sin/cos 勾股定理](#9573a7fe6010225a11dee60f6fe19330)
    - [弧度 等于半径为1圆周上对应的弧长 ( 圆周长2π )](#713e42f0a226d44520baeb7eb138f3e5)
    - [弧度θ 对应的扇形面积，等于 θ/2](#79c7b4dbddc59b1310ccf03bbd18e10c)
    - [sinθ < θ ( θ>0 , 弧度制)](#894c2a8c512ceb699dd705d26f9d0757)
    - [tanθ > θ  ( 0< θ <π/2 , 弧度制 )](#03dc1c298369e7f0ac48a7996a21ed92)
    - [dsinx/dx = cosx 的证明](#480e9fee6f2514006053e0d466b67b55)
        - [sin(ɑ+β)=sinɑ·cosβ + cosɑ·sinβ](#b0278a380f515a4a19dfab753a1fe183)
        - [cos(ɑ+β)=cosɑ·cosβ - sinɑ·sinβ](#13a15019d339ac81aadba8c97b316e99)
- [乘法法则 Product Rule](#5d61ef648f90fe1da932d6270d61dc14)
- [除法法则 Quotient Rule](#99a35f95c0c8be51c24a89b46014eefd)
- [the Chain Rule for f(g(x))](#e65ee591e72f510c002a5a8613537f59)
- [Limits](#b7a95c6586d57b909e3a9973bf21cccf)
    - [洛必塔法则: 0/0型不定式极限](#2a661f05599573e961f425696d15c0d2)
- [Continuous Function](#fd02bcb971f8c4f9300bbf76c79ce089)
    - [函数不连续的例子:](#2e41522248346e3354b8ffc8acdf7177)
- [Inverse function 逆函数](#0334fb389d4a02b6a2a9200647b8fd31)
- [derivatives of lny and sin⁻¹(y)  (f⁻¹型导数)](#c04bd14033c1317823875289d3318f7b)
- [Growth Rate and Log Graphs](#86a6ce761a1f90300e181889c34a46a5)
- [线性近似 Linear Approximation](#8275f5b0a3123a2083b65b8a636b4d54)
- [Newton's Method 牛顿法](#f89321e8d84448f6094e032b83d84087)
- [泰勒级数 Taylor series](#de311932adf59eb9581579fc96d781d2)
- [幂级数 Power Series](#f827f2d518f96fb22d0eb7c8ff40c0cf)
    - [eˣ 的幂级数](#51b0719fd2c6dde89d85cbf4b01dc52a)
    - [sin, cos的级数](#2e56a9e615ddb27bcc2a5b0196ded3df)
    - [欧拉公式 Euler's Great Formular](#2a1ea84dc72c240923cd72cc1d2b743e)
    - [几何级数 geometric series](#67108d246d52df1f8ac79ca2d1a87255)

[](...menuend)


<h2 id="cb7b69587d37b4d0d6623ec0b7e15e8f"></h2>

# 微积分总览

<h2 id="ed8d58aa5d09e3b6ae85504d2b50fdc2"></h2>

#### differential calculus  微分学    

从距离函数 f->速度函数s

<h2 id="5f310f9e2e62d1ba91b27c396331a47b"></h2>

#### integral calculus  积分学  integral(from whole)   

从 速度函数s->距离函数f 

<h2 id="f4fd7794a95a913d0604b6a980f2038c"></h2>

#### 函数1 和 函数2 的关系

- 函数f 在某个t的函数值，描述的，是函数s的图像面积
- 函数s 在某个t的函数值， 是 函数f 在t 时刻的斜率
- f= ∫s(t)   (f1是f2的积分)
- df/dt = s  (f2是f1的导数)

![](./imgs/calcus01.png)

<h2 id="7b2109108288b88fa80ba74730b04212"></h2>

# 导数总览

<h2 id="b73a32da207260c8c5df891313bd2b8f"></h2>

#### 几个重要的函数导数

![](./imgs/common_func_derivation.png)

`sinx` 
![](./imgs/sinx.png)

`eˣ`
![](./imgs/ex.png)


<h2 id="1f1fa83ad7ddf7d7abdfe107fd46cf12"></h2>

# 极值和二阶导数  

<h2 id="f032e96900ac9530a6f4ffa8ffc71cce"></h2>

#### 一阶导数 求 极值点 ，导数=0

<h2 id="095c70e4ae714fca1eabc94bdc766ee4"></h2>

#### 二阶导数 确定 极值点性质

<h2 id="20aaf0154f6499efa187fd95a73aed9e"></h2>

#### 距离／速度 / 加速度 的例子

距离函数f 的一阶导数 dy/dx 是 速度函数, 是f图像的斜率slope

二阶导数是 d²y/dx² 加速度函数, 是f图像的弯曲度 bending

<h2 id="2b7d4dfa847aec16509a257e42a39fe5"></h2>

#### Convex ,bending up, 凸 , 极小值 , ex: x²

<h2 id="284c4ee74be0c0d60c4df4bd3debf94d"></h2>

#### Concave, bending down ,凹, 极大值

<h2 id="b86d19c5489576bef0c5d5bf04de7c00"></h2>

#### 二阶导数性质

极值点，二阶导数为负值，局部最大值（极大值）

极值点，二阶导数为正值，局部最小值（极小值）

inflection point 拐点: 二阶导数为0的点，也是二阶导数开始改变符号的地方

<h2 id="0b43f7c8e73f59c9d943180af743bb58"></h2>

#### 导数应用例子

![](./imgs/ToMIT.png)

开车到MIT， 从家开车到麻省高速的车速是30,的垂直距离是a, 麻省高速的车速为60，
求最省时间的开车路线（红色)

![](./imgs/ToMIT2.png)

`注意点:`

 1. 如果MIT距离不够远，即MIT 位于x段，需要特殊处理一下
 2. 理论上，需要再求一下2阶导数，来确定是极小值，但是这里f''的符号，可以通过f'的单调性来求出，简单说：x>0时f'(x)>0,斜率变化为正，f''>0 (why?)

<h2 id="6595e47721a328f1a5bb516f8fa0813a"></h2>

# 指数函数 y=eˣ

<h2 id="c235979153ce388fa10fdc2c52332bcc"></h2>

#### 重要性质:

 1. 导数是其自身: `dy/dx = y`
 2. `eˣ·eʸ= eˣ⁺ʸ` , 推论: eˣ·e⁻ˣ =1 ,  e⁻ˣ=1/eˣ, 互为倒数

<h2 id="f2737fb06fa1bdff68a619d1df455e4a"></h2>

#### eˣ 构建:

从x=0, eˣ=1 开始, 根据性质: `(eˣ)'=eˣ` , 无限展开

![][1]

当x=1时，指数级数的值就是e，近似2.7

> 1+x <= eˣ

![](./imgs/1+x<ex.png)

<h2 id="2fd7cf83daee9c8035f0bc838e579211"></h2>

#### 银行存款和e的联系

假设年利率是 100%,

按年结算，第2年的总存款变为 (1+1)¹=2

按月结算，第12个月的总存款变为 (1+1/12)¹²= 2.613035290224676

按天结算，第365天的总存款变为 (1+1/365)³⁶⁵ = 2.7145674820219727

按N 结算，(1+1/N)ᴺ -> e

<h2 id="13b313e41f18896d8340296932e9cb46"></h2>

#### `y' = dy/dx = ay` 的情况, `y = eªˣ`


<h2 id="908dab53380191dbf2ba5d54eed208eb"></h2>

# 积分总览

 1. 函数2是函数1的导数
 2. 函数1是函数2的积分
 3. 积分=函数1=函数2图像下的面积


<h2 id="af4815e6482f933efa0b9289e2658753"></h2>

# sin / cos 的导数

<h2 id="9573a7fe6010225a11dee60f6fe19330"></h2>

#### sin/cos 勾股定理

`(cosθ)²+(sinθ)²=1`

<h2 id="713e42f0a226d44520baeb7eb138f3e5"></h2>

#### 弧度 等于半径为1圆周上对应的弧长 ( 圆周长2π )

<h2 id="79c7b4dbddc59b1310ccf03bbd18e10c"></h2>

#### 弧度θ 对应的扇形面积，等于 θ/2

S = πr²/(2π) * θ = θ/2

<h2 id="894c2a8c512ceb699dd705d26f9d0757"></h2>

#### sinθ < θ ( θ>0 , 弧度制) 

作图证明:

![](./imgs/sin_lessthan_theta.png)

<h2 id="03dc1c298369e7f0ac48a7996a21ed92"></h2>

#### tanθ > θ  ( 0< θ <π/2 , 弧度制 )

作图证明:

![](./imgs/tan_largethan_theta.png)

 1. tanθ = sinθ/cosθ, 如果直角三角形的邻边=1, 则对边就=tanθ
 2. 三角形面积 tanθ/2 > 扇形面积 θ/2 => tanθ > θ

由此可以推出, sinθ/θ > cosθ ,

所以， 当 θ->0 时，sinθ/θ = 1

<h2 id="480e9fee6f2514006053e0d466b67b55"></h2>

#### dsinx/dx = cosx 的证明

<h2 id="b0278a380f515a4a19dfab753a1fe183"></h2>

##### sin(ɑ+β)=sinɑ·cosβ + cosɑ·sinβ

<h2 id="13a15019d339ac81aadba8c97b316e99"></h2>

##### cos(ɑ+β)=cosɑ·cosβ - sinɑ·sinβ

`证明:`

![](./imgs/proof_sinx_derivative.png)

第一项后半部分的比值，其实就是0点处cosx 的斜率=0

<h2 id="5d61ef648f90fe1da932d6270d61dc14"></h2>

# 乘法法则 Product Rule

![](./imgs/ProductRule.png)

`图解:`

![](./imgs/multiply_rule.png)



如图所示:

![](./imgs/multiply_rule_pic_show.png)

`eg:`

x³ = x²·x

d/dx(x³) = x²·1 + x·2x = 3x²

d/dx(f(x)³)= 3f(x)²·df/dx


<h2 id="99a35f95c0c8be51c24a89b46014eefd"></h2>

# 除法法则 Quotient Rule

![](./imgs/quotient_rule.png)

下乘上导，减上乘下导，除以 下下

`利用乘法法则推演:`

![](./imgs/quotient_rule_2.png)


<h2 id="e65ee591e72f510c002a5a8613537f59"></h2>

# the Chain Rule for f(g(x))

![](./imgs/ChainRule.png)

![](./imgs/ChainRule_example.png)



<h2 id="b7a95c6586d57b909e3a9973bf21cccf"></h2>

# Limits 

函数运算| DANGER!
-------|----------
an - bn -> A-B | ∞-∞
an・bn -> AB | 0・∞
an / bn | 0/0 or ∞/∞
(an)ᵇⁿ | shows below

`(an)ᵇⁿ dangerous case:`

![](./imgs/Limits_1.png)

<h2 id="2a661f05599573e961f425696d15c0d2"></h2>

#### 洛必塔法则: 0/0型不定式极限

使用导数求解 0/0 型

     1. 当x趋于a时，函数f(x)及g(x)都趋于零
     2. 在点a的某去心邻域内，f'(x)及g'(x)都存在且g'(x)不为零
     3. 若f'(x)/g'(x)极限存在，则有 f(x)/g(x)的极限 等于 f'(x)/F'(x)的极限 (lim x->a) 。

if f(x)→0, as x→0 ; g(x)→0, as x→0 ;

![](./imgs/L_Hospital.png)

![](./imgs/LHospital_pic.png)

---

极限不存在的例子:

    √x 在 x→0时极限不存在。
    
函数连续是较弱的性质，较强的性质的可导：可导必然连续，连续不一定可导。


<h2 id="fd02bcb971f8c4f9300bbf76c79ce089"></h2>

# Continuous Function

    Continuous f(x) at x→a,
    means f(x)→f(a) as x→a.
    
    also means , for any ϵ choosen by Socrates, Plato can find a δ so that:
    if |x-a|<δ then |f(x)-f(a)|<ϵ 

![](./imgs/ContinuousFunction_delta_epsilon.png)


<h2 id="2e41522248346e3354b8ffc8acdf7177"></h2>

#### 函数不连续的例子:

x→0 时函数不连续:

![](./imgs/sin_1_div_x.png)

修改一下，使其在 x→0 时连续:

![](./imgs/xsin_1_div_x.png)

<h2 id="0334fb389d4a02b6a2a9200647b8fd31"></h2>

# Inverse function 逆函数

`y=f(x) ,  x=f⁻¹(y)`

指数函数eˣ的逆函数是 **lny**

```
y=eˣ , x= lny
ln(y·Y) = lny + lnY   (1)
ln(yⁿ) = n·lny  (2)
```

证明(1):

```
y=eˣ 
Y=e^X 
y·Y = eˣ·e^X = e^(x+X)
ln(y·Y) = x+X = lny + lnY
```

证明(2):

```
ln(y²)=ln(yy)=lny+lny=x+x =2x = 2lny
可以推出:
ln(yⁿ)=nlny
```

所有 逆函数图像和原函数图像，沿y=x 的直线对称

![](./imgs/f_inverse_f.png)



对数函数，即指数函数的逆函数的导数:

![](./imgs/ex_inverse_derivative.png)

<h2 id="c04bd14033c1317823875289d3318f7b"></h2>

# derivatives of lny and sin⁻¹(y)  (f⁻¹型导数)

```
f⁻¹(f(x))=x   (1)
f(f⁻¹(y))=y   (2)
```

上面的式子告诉我们，如果知道怎么求 f(x)的倒数，用链式法则就可以求出f⁻¹(y)的倒数。


lny example 1:

```
ln(eˣ)=x (对数函数的定义)
令y=eˣ , 两边求导:
d(lny)/dy · d(eˣ)/dx = 1
d(lny)/dy · eˣ = 1
d(lny)/dy · y = 1
由此得出:
d(lny)/dy = 1/y
```

在我们求导 xⁿ的时候，如果n=0 , 则 (xⁿ)'＝0, 我们并不能获得 x的⁻¹次幂，事实上，不存在幂函数的导数能得到⁻¹次幂。

这就像一个遗漏，现在 lny 填补了这个遗漏。

lny example 2:

```
eˡⁿʸ=y
(eˡⁿʸ) · d(lny)/dy = 1
d(lny)/dy = 1/y
```

---

x = sin⁻¹y  `(arcsin)`

```
y = sin( sin⁻¹y )
两边求导:
1 = cos( sin⁻¹y ) · d(sin⁻¹y)/dy 
因为 sin²x + sin²y =1, 得出
1 = √(1-y²)· d(sin⁻¹y)/dy 
d(sin⁻¹y)/dy = 1 /( √(1-y²) )

同理可得:
d(cos⁻¹y)/dy = -1 /( √(1-y²) ) 

```

我们发现：

`d(sin⁻¹y)/dy + d(cos⁻¹y)/dy =0 `

常数项的导数为0，由此可知, arcsin + arccos 的和是一个常数，事实上，arcsin + arccos = 直角三角形的两个锐角的和 = π/2

<h2 id="86a6ce761a1f90300e181889c34a46a5"></h2>

# Growth Rate and Log Graphs

函数 | x=1000时近似结果
---|---
cx | 10³
x² | 10⁶
x³ | 10⁹
2ˣ | 10³⁰⁰
eˣ | 10⁴³⁴
10ˣ | 10¹⁰⁰⁰
x! | 10²⁵⁶⁶
xˣ | 10³⁰⁰⁰

TODO

<h2 id="8275f5b0a3123a2083b65b8a636b4d54"></h2>

# 线性近似 Linear Approximation

x 在 a点的导数，近似等于:

![](./imgs/LinearApproximation.png)

由此得出:

- f(x) ≈ f(a)+(x-a)·f'(a)      (1)
- x-a ≈ `-` F(a)/F'(a)         (2，用于解F(x)=0方程)
 
example 1: 求√9.06

```
f(x) = √x = x⁰ᐧ⁵
f'(x) = 1/2 · x⁻⁰ᐧ⁵
choose a=9
f(a)=3
f'(a) = 1/6
√9.06 ≈ 3 + (9.06-9)*1/6 = 3.01
```

example 2: 解方程:  F(x) = x²-9.06 =0

```
choose a=3
F(a)= 9-9.06 = -0.06
F'(a) = 2a = 6
x-3 = -(-0.06/6)
x = 3.01
```

example 3: 求 e⁰ᐧ⁰¹

```
f(x) = eˣ
choose a=0
f(0) =1
f'(0) =1
e⁰ᐧ⁰¹≈ f(a)+(0.01-a)f'(a) = 1+0.01
```

我们可以看到  `eˣ = 1+x`   

**1+x 其实就是 `eˣ` 幂级数 从常数项和线性项之后的拦腰截断。**  当 x 很小的时候，x < 0.1 , eˣ 近似等于 1+x>


<h2 id="f89321e8d84448f6094e032b83d84087"></h2>

# Newton's Method 牛顿法

使用线性近似求的近似值 x₁后,  利用 x₁和公式2进行下一轮迭代，以获得更小的误差。

解方程:  F(x) = x²-9.06 =0

```
a=3.01 
F(a) = 0.0001
F'(a) = 2a = 6.02
x-a ≈ -(F(a)/F'(a))
x ≈ 3.01 - ( 0.0001/6.02  )       // (x*x = 9.0600000002759)
```

<h2 id="de311932adf59eb9581579fc96d781d2"></h2>

# 泰勒级数 Taylor series

在数学中，泰勒级数 用无限项连加式级数来表示一个函数，这些相加的项由函数在某一点的导数求得。

定义：如果  在点x=x0具有任意阶导数，则幂级数

![](http://g.hiphotos.baidu.com/baike/s%3D581/sign=5eee3e47023b5bb5bad720f607d1d523/b90e7bec54e736d159f4b3e49a504fc2d4626972.jpg)

称为  在点x0处的泰勒级数

特别的，取x0=0，得到的级数

![](http://d.hiphotos.baidu.com/baike/s%3D92/sign=ca8641966159252da7171106359bf968/9d82d158ccbf6c8193758f64bd3eb13532fa40ff.jpg)

称为麦克劳林级数。函数  的麦克劳林级数是x的`幂级数`


<h2 id="f827f2d518f96fb22d0eb7c8ff40c0cf"></h2>

# 幂级数 Power Series

用函数f(x) 在x=0处的各级导数，来描述函数f(x)

f(x) = a + a₁x + a₂x² + a₃x³ + ...

<h2 id="51b0719fd2c6dde89d85cbf4b01dc52a"></h2>

#### eˣ 的幂级数

因此 e⁰=1, (eˣ)'=eˣ , e^n的阶导数等于1

所以:
![][1]

<h2 id="2e56a9e615ddb27bcc2a5b0196ded3df"></h2>

#### sin, cos的级数

sinx 各级导数如下：

\ | 0|1|2|3|4|5|...
---|---|---|---|---|---|---|---
导数|sinx|cosx | -sinx | -cosx | sinx | cosx | ...
x=0取值|0|1|0|-1|0|1|...

所以,sinx 的幂级数构建如下:

![](./imgs/power_series_sin_cos.png)

我们看到，cosx的幂级数，都是偶次幂，所以 cos(-x)=cos(x), 这给了我们另一个观察奇/偶函数的视点。

<h2 id="2a1ea84dc72c240923cd72cc1d2b743e"></h2>

#### 欧拉公式 Euler's Great Formular

![](./imgs/e_ix.png)

我们看到:

`eⁱˣ= cosx + i·sinx` 

把 x 改成θ  , `eⁱᶿ= cosθ + i·sinθ`

函数图像:

![](./imgs/e_ix_sin_cos_fuc_pic.png)

<h2 id="67108d246d52df1f8ac79ca2d1a87255"></h2>

#### 几何级数 geometric series

`1 + x + x² + x³ + ...`

当 |x| < 1 时,

`1/(1-x) = 1 + x + x² + x³ + ...`

对等式求积分:

`-ln(1-x) = x + x²/2 + x³/3 + ...`


for r != 1 :

`1 + r + r²+ ... + rᵏ = (rᵏ⁺¹-1)/(r-1)`    (算法课程中提及)


---

[1]: ./imgs/ex_constructor.png

---






