# 预备知识
函数和参数方程是用数学术语来描述现实世界的主要工具.  
许多函数由于他们所描述的形态而具有重要的性质.  
三角函数：循环，重复的活动  
指数、对数和逻辑斯谛函数：增长和衰减  
多项式函数：用来近似这些函数或其它函数  
## 直线
增量  斜率 平行线和垂直线  
线性方程： 点斜式， 斜距式，一般式  
依据散点图求一条拟合数据的特殊曲线类型的过程就是回归分析，该曲线就是回归曲线.  
  
## 函数与图形
函数是数学术语描述现实世界的主要工具.  
定义: 从集合D到集合R的一个函数是对D中每个元素指定R中 **唯一** 确定的元素的一种规则.  
D是定义域，而R是包含值域的一个集合.  
函数表示符号: $y=f(x)$  
区间: 端点，内点，开区间，闭区间  
平面上的点$(x,y)$，其坐标为函数$y=f(x)$的输入-输出对，构成函数的图形。  
函数性质：增/减函数，奇/偶函数  
分段定义的函数  
移位图形：  
  y:  加——图形下移  减——图形上移  
  x:  加——图形左移  减——图形右移  
复合函数:  
  
## 指数函数
设$a$是不等于1的正实数，函数$f(x)=a^x$是底为$a$的指数函数。  
指数法则:  
$a^x a^y = a^{x+y}$  
$\frac{a^x}{a^y}=a^{x-y}$  
$(a^x)^y=(a^y)^x=a^{xy}$  
$a^x  b^x = (ab)^x$  
$\frac{a^x}{b^x}=(\frac{a}{b})^x$  
  
自然指数函数，以$e$为底. 可以把$e$定义为函数$f(x)=(1+\frac{1}{x})^x$当$x$无穷增大时的极限.  
指数函数 $y=y\_0 e^{kx}$ ，其中$k$是一非零常数，常被用作指数增长和衰减的模型.$k>0$为指数增长模型，$k<0$为指数衰减模型.  
  
## 反函数和对数函数
一对一函数： 函数$f(x)$在定义域上一对一的，若每当$a \ne b$时， $f(a) \ne f(b)$  
水平直线法则  
反函数：由逆转一对一函数的定义域和值域定义的函数就是$f$的逆函数.  
反函数测试:函数$f$和$g$是反函数对，当且仅当$f(g(x))=x$并且$g(f(x))=x$.这时$g=f^{-1}$,而且$f=g^{-1}$  
求反函数：1. 借助y对x解方程$y=f(x)$  2.交换x和y，得到的公式将是$y=f^{-1}(x)$.  
对数函数：底为a的对数函数$y=\log\_ax$是底为a的指数函数$y=a^x$ $(a>0,a \ne 1)$的反函数.  
自然对数函数：$\log\_ex$ 写作 $\ln x$.  
普通对数函数：$\log\_{10}x$ 写作$\lg x$.  
对数函数的性质  
1. $a^x$与$\log\_ax$互为反函数   $e^{\ln x}=x$  $\ln e^x = x$,  
2. 对任何实数$x>0$, $y>0$  
   乘积法则:  $\log_a{xy} = \log\_ax + \log\_ay$  
   商法则： $\log\_\frac{x}{y} = \log\_ax - \log\_ay$  
   幂法则： $\log_a{x^y} = y\log\_axy$  
3. $a^x = e^{x\ln a}$  
4. 换底公式 $\log_ax = \frac{\ln x}{\ln a}$  $(a>0,a \ne 1)$  
  
## 三角函数及其反函数
弧度： 圆两半径夹角所对的弧与半径的比值.  
      度到弧度  —— 乘以$\frac{\pi}{180}$  
      弧度到度  —— 乘以$\frac{180}{\pi}$  
当弧度为$\theta$的角置于半径为r的圆的标准位置时：  
      正弦 $\sin \theta = \frac{y}{r}$   余割 $\csc \theta = \frac{r}{y}$  
      余弦 $\cos \theta = \frac{x}{r}$   正割 $\sec \theta = \frac{r}{x}$  
      正切 $\tan \theta = \frac{y}{x}$   余切 $\cot \theta = \frac{x}{y}$  
特殊弧度的三角函数值  
周期性:  
      周期为$2\pi$： $\sin x$   $\cos x$   $\csc x$   $\sec x$  
      周期为$\pi$：  $\tan x$   $\cot x$  
周期函数: 函数$f(x)$是周期函数，如果存在正数p使得对每个x值都有$f(x+p)=f(x)$,最小的p值就是$f$的周期.  
一个高等微积分定理:我们在数学建模中用到的每个周期函数都可以表示为正弦和余弦的代数组合.  
三角函数图形的变换:  
    移位，拉伸，压缩和反射  
    $y=af(b(x+c))+d$  
    a: 垂直伸展和压缩，关于x轴的反射  
    b: 水平伸展和压缩，关于y轴的反射  
    c: 垂直移位  
    d: 水平移位  
恒等式：  
    $\cos^2\theta + \sin^2\theta = 1$  
    $1 +\tan^2\theta = \sec^2\theta$   $1 +\cot^2\theta = \csc^2\theta$  
    $\sin(A+B)=\sin A \cos B + \cos A\sin B$  
    $\cos(A+B)=\cos A \cos B - \sin A\sin B$  
    $\sin(A-B)=\sin A \cos B - \cos A\sin B$  
    $\cos(A-B)=\cos A \cos B + \sin A\sin B$  
    $\sin(2x) = 2\sin x\cos x$  
    $\cos(2x) = \cos^2 x - \sin^2 x = 2\cos^2 x - 1 = 1 - 2\sin^2 x$  
余弦定理： 如果a,b,c是三角形ABC的三条边，又如果$\theta$是c边的对角，那么：  
    $c^2 = a^2 + b^2 - 2ab\cos \theta$  
    如果$\theta$为$\frac{\pi}{2}$，则成为毕达哥拉斯定理.  
反三角函数：六个函数需要限制定义域，才有反函数  
  
适当的选择反函数的定义域和值域使得这些函数具有以下关系：  
$\sec^{-1} x = \cos^{-1} \frac{1}{x}$  
$\csc^{-1} x = \sin^{-1} \frac{1}{x}$  
$\cot^{-1} x = \frac{\pi}{2} - \tan^{-1} x$  
  
## 参数方程
对于无法用函数表示的曲线(比如：x对应多个y),用参数方程解决  
定义： 如果x和y都有t值的区间上的函数$x=f(t)$, $y=g(t)$给出，那么由这些方程定义的点集(x,y)=$(f(t),g(t))$是一条参数曲线，方程成为曲线的参数方程.    
  
## 对变化进行建模  
            实际问题的数据 ---简化---> 模型----分析--->数学结论---翻译--->预测/解释  
               ^                                                      |  
               +------------------------检验---------------------------+  
  
  
# 极限和连续  
某些函数输入连续变化时则输出也连续变化——输入变化越小则输出变化也越小，另一些则不管怎么控制输入，他们的函数值可能出现跳跃或非常不规范。极限的概念给出了区别这些性态的一种精确的方法.  
我们还用极限来定义函数图形的切线，这个几何应用立即导致函数的导数这一重要概念.  
## 变化率和极限  
平均和瞬时变化率，导出极限的概念.把瞬时变化率作为平均变化率的极限.  
割线  切线  
极限值不依赖于在$x\_0$处函数是怎么定义的.  
恒等函数$f(x)=x$的极限对于任何值$x\_0$为$\lim_{x\to{x\_0}f(x)}=x\_0$  
常数函数$f(x)=k$的极限对于任何值$x\_0$为$\lim_{x\to{x\_0}f(x)}=k$  
    
极限不存在：  
- 跳跃函数  
- 函数无限增大  
- 函数无限振动  $\sin \frac{1}{x}$  
  
极限的精确定义:  
$f(x)$定义在$x\_0$的一个可能不包括$x\_0$的开区间上，我们说当$x$趋于$x\_0$时$f(x)$趋于极限L，并记为$\lim_{x\to{x\_0}}f(x)=L$. 如果对任何数$\epsilon > 0$，存在相应的数 $\delta > 0$使得对所有满足 $0<|x-x\_0|<\delta$的x，都有$|f(x)-L|<\epsilon $  
  
## 求极限和单侧极限
**定理一**、极限法则：  
  如果L, M, c和k都是实数，且$\lim_x\to{c}f(x)=L$和$\lim_x\to{c}g(x)=M$,那么  
  1. 和法则  $\lim_{x\to{c}}(f(x)+g(x))=L+M$  
  2. 差法则  $\lim_{x\to{c}}(f(x)-g(x))=L-M$  
  3. 积法则  $\lim_{x\to{c}}(f(x)g(x))=LM$  
  4. 乘常数  $\lim_{x\to{c}}kf(x)=kL$  
  5. 商法则  $\lim_{x\to{c}}\frac{f(x)}{g(x)}=\frac{L}{M}$  
  6. 幂法则 如果r和s都是整数，且$s \ne 0$,那么$\lim_{x\to c}f(x)^{\frac{r}{s}}=L^\frac{r}{s}$  
  
**定理二**、可用代入法求多项式的极限  
如果$P(x)=a\_nx^n + a\_{n-1}x^{n-1}...+a\_0$，那么$\lim_{x\to{c}}P(x)=a\_nc^n + a\_{n-1}c^{n-1}...+a\_0$  
**定理三**、可用代入法求有理函数的极限，如果分母的极限不等于零  
如果$P(x)$和$Q(x)$都是多项式，且$Q(c) \ne 0$,那么$\lim_{x\to{c}}{\frac{P(x)}{Q(x)}} = \frac{P(c)}{Q(c)}$.  
  
代数地消去零分母  
**定理四**、三明治(夹逼)定理：  
假设在包含c在内的某个开区间中除x=c处的所有x，有$g(x)\leqslant f(x)\leqslant h(x)$.又假设$\lim\_{x\to{c}} g(x) = \lim\_{x\to{c} }h(x) = L$, 那么$\lim\_{x\to{c}} f(x)=L$  
  
单侧极限：左侧极限，右侧极限  
**定理五**、单侧极限与双侧极限之间的关系：当x->c时函数$f(x)$有极限当且仅当$f$的左侧极限和右侧极限存在且相等.  
**定理六**、$\lim\_{\theta \to{0}} {\frac{\sin \theta}(\theta)} = 1$  
  
## 与无穷相关的极限
要分析x->$\infty$时的有理函数(多项式的商)以及具有有趣极限性态的函数的图形，采用的工具是水平渐近线和垂直渐近线.
**定理七**、$x \to \pm \infty$的极限法则
如果L, M, c和k都是实数，且$\lim_x\to{\pm \infty}f(x)=L$和$\lim_x\to{\pm \infty}g(x)=M$,那么
1. 和法则  $\lim_{x\to{\pm \infty}}(f(x)+g(x))=L+M$
2. 差法则  $\lim_{x\to{\pm \infty}}(f(x)-g(x))=L-M$
3. 积法则  $\lim_{x\to{\pm \infty}}(f(x)g(x))=LM$
4. 乘常数  $\lim_{x\to{\pm \infty}}kf(x)=kL$
5. 商法则  $\lim_{x\to{\pm \infty}}\frac{f(x)}{g(x)}=\frac{L}{M}$
6. 幂法则 如果r和s都是整数，且$s \ne 0$,那么$\lim\_{x\to{\pm \infty}}f(x)^{\frac{r}{s}}=L^\frac{r}{s}$
  
## 连续性
在一点连续：
内点: 函数$f(x)$在定义域的内点c处是连续的，如果$\lim\_{x\to{c}}f(x)=f(c)$  
端点: 函数$f(x)$在定义域的左端点a或右端点b是连续的，如果分别有$\lim\_{x\to{a^+}}f(x)=f(a)$和$\lim\_{x\to{b^-}}f(x)=f(b)$  
  
连续性检验：  
函数$f(x)$在$x=c$处连续，当且仅当它满足以下条件  
1. $f(c)$存在  
2. $\lim\_{x\to{c}}f(x)$存在  
3. $\lim\_{x\to{c}}f(x)=f(c)$  
  
间断： 可去间断，跳跃间断，振荡间断，无穷间断  
连续函数：是在定义域中每一点连续的函数.  
代数组合  
**定理八**、连续函数的性质  
如果函数$f$和$g$在$x=c$连续，那么下列$f$和$g$的组合在$x=c$都是连续的  
1. 和      $f + g$  
2. 差      $f - g$  
3. 积      $f \cdot g$  
4. 乘常数   $kf$  
5. 商      $\frac{f}{g}$倘若$g(c) \ne 0$  
  
**定理九** 连续函数的复合函数  
如果$f$在$c$连续而$g$在$c$连续，那么复合函数$g{\circ}f$在$c$处连续。  
  
**定理十** 连续函数的中值定理  
在闭区间[a,b]上连续的函数一定取到$f(a)$和$f(b)$之间的每一个值.  
  
## 切线  
定义：曲线$y=f(x)$在点$(x\_0, f(x\_0))的斜率是$m=$\lim_{h\to{0}}\frac{f(x\_0+h)-f(x\_0)}{h}$(倘若这个极限存在)，曲线在点P的切线就是过点P且以m为斜率的直线.  
  
变化率：在一点出的导数  
表达式$\frac{f(x\_0+h)-f(x\_0)}{h}$称为$f$在$x\_0$处增量为$h$的差商.如果${h\to{0}}$时，差商有极限，那么这个极限就称为$f$在$x\_0$处的导数.  
**导数是微积分所考虑的两个最重要的对象之一**  
  
下面5个陈述描述的是同一件事情：  
1. $y=f(x)$在$x=x\_0$处的斜率  
2. 曲线$y=f(x)$在$x=x\_0$处的切线的斜率  
3. $f(x)$在$x=x\_0$关于$x$的变化率  
4. $f$在$x=x\_0$的导数  
5. $\lim_{h\to{0}}\frac{f(x\_0+h)-f(x\_0)}{h}$  
  
# 导数
导数的这个极限度量了函数在该点的变化率.  
## 作为函数的导数
导函数：函数$f(x)$关于变量$x$的导数$f'$,它在$x$处的值为$f'(x)=\lim_{h\to{0}}\frac{f(x\_0+h)-f(x\_0)}{h}$, 如果该极限存在的话.  
如果在一个特定的点$x$处$f'$存在，我们就说$f$在$x$是可微的(有导数)，如果在$f$的定义域的所有点处$f'$都存在，我们就说$f$是可微的.计算导数的过程称为微分.  
  
**法则1** 常数函数的导数  $f(x)=c$，则$f'(x) = 0$  
**法则2** 正整数幂法则 如果n是正整数，$f(x)=x^n$，则$f'(x) = nx^{n-1}$  
**法则3** 乘常数法则 如果$u$是$x$的可微函数，而$c$是一常数,则$(cu)' = cu'$  
**法则4** 导数和法则 如果$u$和$v$是$x$的可微函数，则$u+v$在$u$和$v$都是可微的每点也是可微的，有$(u+v)' = u'+v'$  
  
**定理一** 可微性蕴含这连续性: 如果$f$在$x=c$处有导数，那么$f$在$x=c$处连续.  
**定理二** 导数的中间值性质: 如果$a$和$b$是$f$在其上可微的区间中的两个点，那么$f'$一定取到$f'(a)$和$f'(b)$中间的每一个值.  
定理二是说，一个函数不可能是一个区间上的导函数除非该函数具有中间值性质，何时函数是导函数的问题是整个微积分的中心问题之一.  
  
高阶导数  
  
## 积、商、负幂的导数  
**法则5** 导数的积法则  如果$u$和$v$在$x$可微，则他们的积$uv$在x也是可微的，有$(uv)' = uv'+vu'$  
**法则6** 导数的商法则  如果$u$和$v$在$x$可微，又$v(x) \ne 0$,则他们的商$u/v$在x也是可微的，有$(u/v)' = \frac{vu'-uv'}{v^2}$  
**法则7** 负整数次幂法则  如果n是负整数，且$x \ne 0$,则$(x^n)' = nx^{n-1}$  
  
## 三角函数的导数
$(\sin x)' = \cos x$  
$(\cos x)' = -\sin x$  
$(\tan x)' = \sec^2 x$  
$(\cot x)' = -\csc^2 x$  
$(\sec x)' = \sec x \tan x$  
$(\csc x)' = -\csc x \cot x$  
因为六个基本三角函数在定义域上都是可微的，所以我们可以用直接代入法来计算三角函数的许多代数组合和复合函数的极限.  
  
## 链式法则
**什么函数的导数会是导数的积的形式？** 答案就在称为链式法则求复合函数导数的法则中.  
**定理三** 链式法则  
如果$f(u)$在点$u=g(u)$可微而$g(x)$在$x$可微，那么复合函数$(f \circ g)(x)=f(g(x))$在$x$可微,而且$(f \circ g)'(x)=f'(g(x))\cdot g'(x)$  
参数化曲线的斜率  
如果三个导数都存在，且$x'(t) \ne 0 $, 则$y'(x)=\frac{y'(t)}{x'(t)}$  
二阶导数为 则$y''(x)=\frac{(y'(x))'(t)}{x'(t)}$  
  
## 隐函数微分法
由$F(x, y)=0$定义的函数在什么情况下是可微的?  
隐函数求导的四个步骤：  
1. 把y当做x的可微函数处理，方程两边对x求导数  
2. 对$dy/dx$并项到等式的一边  
3. 提出因子$dy/dx$  
4. 解出$dy/dx$  
  
**定理四** 有理幂法则  如果n是-有理数，那么在$x^{n-1}$的定义域的每个内点处$x^n$是可微的，且$(x^n)' = nx^{n-1}$  
  
## 相关变化率
用另一个你能求得的速率来求出一个你不容易求得其速率的问题称之为相关变化率问题.  
求解方法：  
1. 画一个图并给变量和常量命名，用t表示时间，假设所有的变量都是t的可微函数  
2. 记下数值信息  
3. 写下要你求的东西  
4. 写出把变量联系起来的方程  
5. 求关于t的导数  
6. 求值  
  
  
# 导数的应用
关键技能就是 **中值定理**，这条定理及其推论提供了进入积分计算的通道.  
  
## 函数的极值
能从函数的导数获悉的最重要事情之一就是该函数在给定区间上是否取到其最大值或最小值，以及如果取到的话，这些值在何处取到.  
  
**定义** 绝对极值  
设$f$是定义域为D的函数，$c \in D$, 则$f(c)$是  
a) $f$在D上的绝对最大值，当且仅当对一切的 $c \in D$有$f(x) \leqslant f(c)$  
a) $f$在D上的绝对最小值，当且仅当对一切的 $c \in D$有$f(x) \geqslant f(c)$  
极值可能出现在区间的端点和内点处  
  
**定理一** 连续函数的极值定理  
如果$f(x)$是闭区间I上的连续函数，那么$f(x)$在I的某些点处既能取到其绝对最大值M也能取到其绝对最小值m，即存在I中的$x\_1$和$x\_2$使得$f(x\_1) = m$，$f(x\_2) = M$，以及对I中任何其他的x有$m \leqslant f(x)\geqslant M$  
注意: 定理中要求区间是闭的以及函数是连续的是至关重要的条件，没有这些条件，定理的结论不一定成立.  
  
**定理二** 局部极值  
如果$f(x)$是其定义域的内点c点取到局部最大值或局部最小值，又若在c点$f'$存在，那么$f'(c)=0$.  
定理二告诉我们函数$f$可能取到极值(局部或全局)的点只可能是：  
1. 使得$f' = 0$内点  
2. $f'$没有定义的内点  
3. $f$的定义域端点  
  
多数求极值的问题是求闭区间上连续函数的绝对极值。定理一保证闭区间上连续函数的绝对极值一定存在，定理二告诉我们去那里找 .  
  
**定义** 函数$f$的定义域中的一点称为f的临界点，如果在该点出$f'=0$或$f'$不存在.  
  
## 中值定理和微分方程
**什么样的函数可以有另外一个函数作为自己的导数？**  
中值定理本身把函数在区间上的平均变化率和该区间内一点处的瞬时变化率联系起来.  
**定理三** Rolle定理  
假设$y=f(x)$在[a,b]的每一点连续，又假设它在(a,b)的每一点可微。如果$f(a)=f(b)=0$，那么(a,b)中至少有一个数c， $f'(c) = 0$  
**定理四** 中值定理(就是在斜线上的Rolle定理)  
假设$y=f(x)$在[a,b]的上连续而且在区间(a,b)的内点处可微，那么(a,b)中至少有一个数c，使得 $f'(c) = \frac{f(b)-f(a)}{b-a}$成立.  
中值定理的重要性不在于识别确定c而在于其他地方的应用.  
**推论1** 导数为零的函数一定是常数函数  
如果在区间I上每一点上$f'(x)=0$，那么对于I上的一切$x$有$f(x)=C$,其中C是常数.  
**推论2** 在区间上具有相同导函数的函数互相差一个常数  
如果在区间I上每一点上$f'(x)=g'(x)$，那么存在常数C使得对I中一个$x$，$f(x)=g(x)+C$成立.  
  
### 微分方程
微分方程就是把未知函数及其一个或多个导数联系在一起的方程。一个函数称为微分方程的一个解，若该函数的导数满足该微分方程.  
  
## 图形的形状
**推论三** 增函数和减函数的一阶导数检验法  
假设$f$在[a,b]上连续并在(a,b)上可微，如果在(a,b)的每一点处$f'>0$,那么$f$在[a,b]上是增函数， 如果在(a,b)的每一点处$f'<0$,那么$f$在[a,b]上是减函数  
  
局部极值的一阶导数检验法：在临界点x=c处  
1. $f$有局部最小值，如果$f'$在c从负变成正  
2. $f$有局部最大值，如果$f'$在c从正变成负  
3. $f$有没有局部极值，如果$f'$在c两边正负号相同  
  
$y'$和$y''$一起就告诉我们函数图形的形状.  
  
**定义** 凹性  
可微函数$y=f(x)$的图形是  
a) 在开区间I上凹向上的，如果$y'$在I上递增 ----- 也即 $y‘’>0$  
b) 在开区间I上凹向下的，如果$y'$在I上递减 ------也即 $y‘’<0$  
**定义** 拐点  
一点称为函数的拐点，如果函数在该点有切线，而且在该点改变函数的凹性.  
**定理五** 局部极值的二阶导数检验法  
1. 如果$f'(c)=0$且(f''(c) < 0)，那么$f$在$x=c$取到有局部最大值  
2. 如果$f'(c)=0$且(f''(c) > 0)，那么$f$在$x=c$取到有局部最小值  
缺点，当$f''(c)=0$或者$f''$不存在时失灵，用之前的一阶导数检验法.  
  
从函数的导数了解函数  
  
## 自治微分方程的图形解
可以把油管道输怎样确定图形的形状的知识点作为图形地求解微分方程的基础，要这样做的出发点的概念就是相直线和平衡点的概念.  
$y^2=2x+1$的微分方程为$dy/dx=1/2y$,这一微分方程，其中$dy/dx$只是y的函数，称为自治微分方程.  
**定义** 平衡点或静止点  
如果$dy/dx=g(y)$是自治微分方程，那么使dy/dx=0的y值称为平衡点或静止点.  
因此平衡点就是一些这样的点，因变量在这些点不发生变化，所以y处于静止状态。强调的是dy/dx=0的y值，而不是之前所强调的x值.  
  
## 线性化和微分
有时我们可以用能给出在特定应用中我们所需要的精度且较容易的比较简单的函数来近似复杂的函数。  
这里讨论的近似函数成为线性化，他们是建立在切线的基础上的.  
**定义** 线性化：如果$f$在$x=a$可微，那么近似函数$L(x)=f(a)+f'(a)(x-a)$就是$f$在$a$的线性化.  
线性化的效用在于他有能力在整个区间上用比较简单的函数来替代复杂的函数，当然接下来我们就需要知道误差有多大.  
**定义** 微分：设$y=f(x)$是一个可微函数，微分dx是一个自变量，微分dy是$dy=f'(x)dx$。  
和自变量dx不同，变量dy永远是因变量，它既依赖d，又依赖dx.  
如果$dx \ne 0$，那么微分dy和微分dx的商就等于导数$f'(x)$。因为$\frac{dy}{dx}=\frac{f'(x)dx}{dx}=f'(x)$。有时候记为$df=f'(x)dx$来代替$dy=f'(x)dx$，称$df$为$f$的微分.  
  
绝对、相对和百分比变化  
  
|         | 真的变化 |            估计的变化 |  
| --- | --- | --- |  
| 绝对变化| $\Delta f =f(a+dx) - f(a)$ | $df=f'(a)dx$ |  
| 相对变化| $\frac{\Delta f}{f(a)}$ | $\frac{df}{f(a)}$ |  
| 百分比变化| $\frac{\Delta f}{f(a)} \times 100$ | $\frac{df}{f(a)} \times 100$ |  
  
方程$df=f'(x)dx$告诉我们对不同的$x$值处的输入变化$f$的输出变化有多敏感.在$x$处的$f'$的值愈大，给定的变化$dx$的影响愈大.  
  
如果$y=f(x)$在$x=a$可微而x从a变成$a+\Delta x$,那么$f$的变化$\Delta y$由形为$\Delta y = f'(a)\Delta x + \epsilon \Delta x$的等式给出，其中当$\Delta x \to 0$时$\epsilon x \to 0$  
  
# 积分
## 不定积分、微分方程和建模
### 求反导数：不定积分
**定义**：一个函数的反导数  
一个函数$F(x)$称为另一个函数$f(x)$的反导数。如果$F'(x)=f(x)$对于$f$定义域中的$x$成立，$f$的全体反导数所组成的集合称为$f$关于$x$的不定积分，记作$\int f(x)dx$。其中$\int $称为积分号，函数$f$称为积分的被积函数，而$x$称为积分变量.  
$\int f(x)dx = F(x) + C $  
  
已知函数的导数以及在某个特殊点$x\_0$处的值 $y\_0$，求$x$的函数$y$的问题为初值问题.  
  
## 积分法则；替换积分法
**不定积分法则**  
1. 常数倍法则： $\int kf(x)dx = k\int f(x)dx$ (k依赖于x时不成立)  
2. 负法则： $\int -f(x)dx = -\int f(x)dx$  
3. 和与差法则: $\int [f(x) \pm g(x)]dx  = \int f(x)dx \pm \int g(x)dx$  
### $\sin^2 x$和$\cos^2 x$
$\int \sin^2 xdx = \int \frac{1-\cos 2x}{2} dx = \frac{x}{2} - \frac{\sin 2x}{4} + C $  
$\int \sin^2 xdx = \int \frac{1+\cos 2x}{2} dx = \frac{x}{2} + \frac{\sin 2x}{4} + C $  
### 积分形式的幂法则
$\int u^n du = \frac{u^{n+1}}{n+1} + C$ ($n \ne -1$, n为有理数)  
### 替换法(应用链式法则)
当$f$和$g'$是连续函数，为求积分$\int f(g(x))g'(x)dx$，采用下列步骤  
1. 做替换$u=g(x)$，则$du=g'(x)dx$，得到积分$\int f(u)du$  
2. 对$u$积分  
3. 在上一步的结果中用g(x)替代$u$  
替换法的成功依赖与找到一个替换，用它把一个我们不能直接求出的积分改变称可以求出的.  
  
## 黎曼和定积分
**定义** 定积分作为黎曼和的极限  
设$f$是定义在闭区间[a, b]上的一个函数，对于[a, b]的任意划分P，设$c\_k$是在子区间[$x\_{k-1}$, $x\_k$]上任意选取的数.如果存在一个数I，使得不论划分P怎样和$c\_k$如何选取，都有$\lim\_{||P||\to0}\sum_{k=1}^nf(c\_k)\Delta x\_k = I$,则称$f$在[a,b]上可积的，而I称为$f$在区间[a,b]上的定积分.  
**定理一** 定积分的存在性  
所有连续函数都是可积的，即，如果一个函数$f$在区间[a,b]是连续的，则它在[a,b]上的定积分存在.  
符号$\int_a^bf(x)dx$读作“从a到b,$f(x)dx$的积分”  
**定义** 如果$y=f(x)$是闭区间[a,b]上的非负及可积的函数，则从a到b的曲线$y=f(x)$下的面积是从a到b,$f$的积分 $A=\int\_a^bf(x)dx$.  
这个定义从两个方面起作用：我们可以用积分计算面积，也可以用面积计算微分.  
**定义** 平均(中)值  若$f$在[a,b]上可积，则它在[a,b]上的平均(中值)是$av(f)=\frac{1}{b-a}\int\_a^bf(x)dx$  
**定积分的性质**  
1. 积分的次序 $\int\_a^bf(x)dx$ = -$\int\_b^af(x)dx$  
2. 零：      $\int\_a^af(x)dx$ = 0  
3. 常倍数    $\int\_a^b kf(x)dx$ = $k \int\_a^bf(x)dx$  
4. 和与差    $\int\_a^b(f(x)\pm g(x))dx$=$\int\_a^b(x)dx$ \pm $\int\_a^b g(x)dx$  
5. 可加性    $\int\_a^bf(x)dx$ + $\int\_b^cf(x)dx$=$\int\_a^c f(x)dx$  
6. 最大-最小不等式   $min f \cdot (b-a) \leqslant \int\_a^b f(x)dx \leqslant max f \cdot (b-a)$  
7. 控制 在[a,b]上$f(x) \geqslant x(g)$推导出$\int\_a^b f(x)dx  
 \geqslant \int\_a^b g(x)dx$  
  
## 中值定理和基本定理
积分学的两个重要定理：定积分的中值定理断言闭区间上的连续函数在该区间上至少取一次平均值，基本定理连接了积分法和微分法。  
### 定积分的中值定理
**定理2** 定积分的中值定理  
如果$f$在[a,b]上连续，则在[a,b]中的某点c， $f(c) = \frac{1}{b-a}\int\_a^bf(x)dx$  
**定理3** 微积分的基本定理，部分1  
如果$f$在[a,b]上连续，则函数$F(x)=\int\_a^xf(t)dt$,在[a,b]的每个点x有导数，并且$\frac{dF}{dx}=\frac{d}{dx}\int\_a^xf(t)dt=f(x)$  
**定理3（续）** 微积分的基本定理，部分2  
如果$f$在[a,b]的每个点连续，而$F$是$f$在[a,b]的任何一个反导数，则$\int\_a^bf(x)dx=F(b)-F(a)$.基本定理的这一部分称为积分求值定理.  
  
## 定积分的变量替换
由变量替换求定积分有两种方法，且都有效.一种是由变量替换求对应的不定积分，再用所得的一个反导数通过基本定理求定积分的值.另一种方法是使用现在要学习的公式.  
**定积分的变量替换**
公式 $\int\_a^bf(g(x))\cdot g'(x)dx=\int\_{g(a)}^{g(b)}f(u)du$  
如何使用它，做替换$u=g(x)$, $du=g'(x)dx$并且以$g(a)$到$g(b)$积分.  
  
## 数值积分
当我们不能用反导数求定积分时，我们转向本节叙述的梯形法和Simpson法这类的数值方法.  
  
梯形法： 为逼近$\int\_a^bf(x)dx$，用$T=\frac{h}{2}(y\_0 + 2y\_1 + ... + 2y\_{n-1} + 2y\_n)$,各y是$f$在分点$x\_0=a, x\_1=a+h,...x\_{n-1}=a+(n-1)h, x\_n=b$的函数值，其中$h=(b-a)/n$。  
梯形逼近的误差： 如果$f''$连续并且M是$|f''|$的值在[a,b]的一个上界，则$|E\_T \leqslant \frac{b-a}{12}h^2M$，其中$h=(b-a)/n$。  
  
Simpson法(用抛物线逼近)：为逼近$\int\_a^bf(x)dx$，用$T=\frac{h}{3}(y\_0 + 4y\_1 + 2y\_1 + 4y\_3... + 2y\_{n-2} + 4y\_{n-1} + y\_n)$,各y是$f$在分点$x\_0=a, x\_1=a+h,x\_2=a+2h,...x\_{n-1}=a+(n-1)h, x\_n=b$的函数值，其中n是偶数,$h=(b-a)/n$。  
  
Simpson法的误差： 如果$f^{(4)}$连续并且M是$|f^{(4)}|$在[a,b]的一个上界，则$|E\_s\leqslant \frac{b-a}{180}h^4M$，其中$h=(b-a)/n$。  
  
# 超越函数和微分方程
## 对数
对数的性质在微积分和建模中会永远保持其重要性.  
**定义** 自然对数函数  $\ln x = \int_1^x\frac{1}{t}dt, x > 0$  
$y=\ln x$的导数  $\frac{d}{dx}\ln x=\frac{1}{x}, x>0$  
积分$\int \frac{1}{u}du = \ln |u| + C$  
  
对数微分法:如果在求导之前在等式两端取自然对数，这就使得我们在求导之前利用对数法则化简公式，这个过程称为对数求导法.  
$\frac{d}{dx}\log_au=\frac{1}{\ln a}\frac{1}{u}\frac{du}{dx}$.  
  
## 指数函数
**定理一** 反函数的导数法则  
如果$f$在区间上的每个点是可微的而且$df/dx$在I上从不为零，则$f^{-1}$在区间$f(I)$上的每个点都是可微的，$df^{-1}/dx$在任一特定点$f(a)$的值是$df/dx$在a的值的倒数$(\frac{df^{-1}}{dx})\_{x=f(a)} = \frac{1}{(\frac{df}{dx})\_{x=a}}$,简言之$(f^{-1})'=\frac{1}{f'}$  
  
  
# 积分技术 洛必达法则和反常积分
本章的目的之一是指出如何把不熟悉的积分改变成我们可以识别的。  
## 基本积分公式
1. $\int du=u+C$  
2. $\int kdu=ku+C$  
3. $\int (du+dv)= \int du + \int dv$  
4. $\int u^udu = \frac{u^{n+1}}{n+1} + C (n \ne -1)$  
5. $\int \frac{du}{u} = \ln |u| + C $  
6. $\int \sin u du = -\cos u + C $  
7. $\int \cos u du = \sin u + C $  
8. $\int \sec^2 u du = \tan u + C $  
9. $\int \csc^2 u du = -\cot u + C $  
10. $\int \sec u \tan u du = \sec u + C $  
11. $\int \csc u \cot u du = -\csc u + C $  
12. $\int \tan u du = -\ln |\cos u| + C = \ln |\sec u| + C$  
13. $\int \cot u du = \ln |\sin u| + C = -ln |\csc u| + C$  
14. $\int e^u du = e^u + C $  
15. $\int a^u du = \frac{a^u}{\ln a} + C (a > 0, a \ne 1)$  
16. $\int \sin h u du = \cos h u + C $  
17. $\int \cos h u du = \sin h u + C $  
18. $\int \frac{du}{\sqrt {a^2-u^2}} = \sin^{-1}(\frac{u}{a}) + C $  
19. $\int \frac{du}{a^2+u^2} =\frac{1}{a} \tan^{-1}(\frac{u}{a}) + C $  
20. $\int \frac{du}{u \sqrt{u^2-a^2}} =\frac{1}{a} \sec^{-1}|\frac{u}{a}| + C $  
21. $\int \frac{du}{\sqrt{a^2+u^2}} =\sin h^{-1}(\frac{u}{a}) + C $  
22. $\int \frac{du}{\sqrt{u^2-a^2}} =\cos h^{-1}(\frac{u}{a}) + C $  
  
代数处理： 必须经常改变积分以便和标准公式相匹配.  
1. 做变量替换实现化简  
2. 配平方根  
3. 利用三角恒等式  
4. 消去平方根  
5. 化简假分式  
6. 分开分式  
7. 乘以1的一种表示  
  
## 分部积分
分部积分公式： $\int udv = uv - \int vdu$  
对应定积分形式 $\int_{v\_1}^{v\_2} udv = (u\_2v\_2 - u\_1v\_1) \int_{u\_1}^{u\_2} vdu$  
适当选择$u$和$v$，第二个积分可能比第一个更容易求，这就是这个公式的重要性理由.  
何时：如果变量替换行不通时，尝试分部积分  
怎样: 从形如$\int f(x)g(x)dx$的积分触发，使他与形如$\int udv$的积分匹配，为此选择$dv$是被积分的函数中包含$dx$以及$f(x)$和$g(x)$的那一部分.  
原则: 上述公式的右端应该给出一个新的积分，你必须容易积分$dv$以便得到右端.  
  
## 部分分式
把一个有理函数$f(x)/g(x)$成功写成部分分式之和依赖于两件事情:  
1. $f(x)$的阶必须低于$g(x)$的阶  
2. 必须知道$g(x)$的因子.  
  
## 三角替换
1. $x=a\tan \theta$ 把$a^2+x^2$带换成$a^2\sec^2 \theta$  
2. $x=a\sin \theta$ 把$a^2-x^2$带换成$a^2\cos^2 \theta$  
3. $x=a\sec \theta$ 把$x^2-a^2$带换成$a^2\tan^2 \theta$  
  
## 积分表  Monte Carlo积分
  
## 洛必达法则
### 不定型 0/0
**定理一** 洛必达法则(第一种形式)  
假设$f(a)=g(a)=0$, $f'(a)$和$g'(a)$存在，并且$g'(a) \ne 0$则$\lim\_{x\to a}\frac{f(x)}{g(x)} = \frac{f'(a)}{g'(a)}$  
**定理二** 洛必达法则(加强形式)  
假设$f(a)=g(a)=0$, $f$和$g$在包含$a$的一个开区间I上是可微的，且当$x \ne a$时，在I上$g'(a) \ne 0$则$\lim\_{x\to a}\frac{f(x)}{g(x)}$存在时，$\lim\_{x\to a}\frac{f(x)}{g(x)} = lim\_{x\to a}\frac{f'(a)}{g'(a)}$  
当我们使用洛必达法则时，要观察从$\frac{0}{0}$到非$\frac{0}{0}$的变化，这正是求出极限的时机.  
### 不定型 $\infty/\infty$、 $\infty \cdot 0$, $\infty -\infty$
也采用洛必达法则  
### 不定型 $1^\infty$, $0^0$, $\infty ^0 $
使用洛必达法则求出对数的极限，再取指数揭示原来函数的行为.  
$\lim\_{x \to a}\ln f(x) = L \Rightarrow \lim\_{x \to a}\ln f(x) = \lim\_{x \to a} e^{\ln f(x)} = e^{\lim\_{x \to a} \ln f(x)} = e^L$  
  
## 反常积分
### 无穷积分限
**定义** 有无穷积分限的反常积分  
有无穷积分限的积分都是反常积分  
1. 如果$f(x)$在[a, $\infty $)是连续的，则 $\int\_a^{\infty}f(x)dx = \lim\_{b \to \infty}\int\_a^{b}f(x)dx$  
2. 如果$f(x)$在（-$\infty $, b]是连续的，则 $\int\_{-\infty}^bf(x)dx = \lim\_{a \to -\infty}\int\_a^{b}f(x)dx$  
3. 如果$f(x)$在（-$\infty $, $\infty $)是连续的，则 $\int\_{-\infty}^{\infty}f(x)dx = \int\_{-\infty}^cf(x)dx + \int\_c^{\infty}f(x)dx$ c为任意实数.  
  
**定义** 无界不连续函数限的反常积分  
有积分区间的一个点，变得无穷的函数的积分是反常积分  
1. 如果$f(x)$在(a, b])是连续的，则 $\int\_a^bf(x)dx = \lim\_{c \to a^+}\int\_c^{b}f(x)dx$  
2. 如果$f(x)$在[a, b)是连续的，则 $\int\_{a}^bf(x)dx = \lim\_{c \to b^-}\int\_a^{c}f(x)dx$  
3. 如果$f(x)$在[a, c)$\cup$(c, b]是连续的，则 $\int\_{a}^{b}f(x)dx = \int\_{a}^cf(x)dx + \int\_c^{b}f(x)dx$.  
  
**定理三** 直接比较判别法  
设$f$和$g$在[a, $\infty$)上连续且对所有$x \geqslant a$有$0  \leqslant f(x) \leqslant g(x) $，则  
1. 若$\int\_a^{\infty}g(x)dx$收敛，则$\int\_a^{\infty}f(x)dx$收敛  
2. 若$\int\_a^{\infty}f(x)dx$发散，则$\int\_a^{\infty}g(x)dx$发散  
  
**定理四** 极限比较判别法  
如果整函数$f$和$g$在[a, $\infty$)上连续，并且$\lim_{x\to \infty}\frac{f(x)}{g(x)} = L$， $0< L < \infty $,则$int\_a^{\infty}f(x)dx$和$int\_a^{\infty}g(x)dx$二者同时收敛或同时发散.  
  
# 无穷级数
无穷级数是一个威力强大的工具的基础，这个工具使我们能把许多函数表示成"无穷多项式"，并告诉我们把他们截断成有限多项式时带来多少误差.  
## 数列的极限
一个中心问题是序列有无极限.  
**定义1** 序列  
数的无穷序列是一个函数，它的定义域是大于或等于某个整数$n\_0$的整数集.  
记号: 我们把第n项为$a\_n$的序列表示成{$a\_n$}  
**定义** (收敛，发散，极限)  
极限序列{$a\_n$}收敛到数L，如果每个整数$\epsilon$,都对应有一个整数N，使得对所有n： n>N $\Rightarrow$ |$a\_n - L$| < $\epsilon$,如果这样的数L不存在，我们就说{$a\_n$}发散.  
### 序列极限的计算
**定理1** 序列极限定理  
设{$a\_n$}和{$b\_n$}是实数序列，A和B是实数，若$\lim\_{n \to \infty}a\_n = A $和$\lim\_{n \to \infty}b\_n = B $则下列规则成立:  
1. 和       $\lim\_{n \to \infty}(a\_n+b\_n) = A + B$  
2. 差       $\lim\_{n \to \infty}(a\_n-b\_n) = A - B$  
3. 积       $\lim\_{n \to \infty}(a\_n\cdot b\_n) = A \cdot B$  
4. 常倍数    $\lim\_{n \to \infty}(k\cdot b\_n) = k \cdot B$  
5. 商        $\lim\_{n \to \infty}\frac{a\_n}{b\_n} = \frac{A}{B}$  
  
**定理2** 序列的夹逼定理  
**定理3** 序列的连续函数定理  
**定理4** 序列的洛必达法则  
### 常见极限
1. $\lim\_{n \to \infty}\frac{\ln n}{n} = 0$  
2. $\lim\_{n \to \infty}\sqrt[n]{n} = 1$  
3. $\lim\_{n \to \infty}x^{1/n} = 1$  (x>0)  
4. $\lim\_{n \to \infty}x^{n} = 0$ ($|x| < 1$)  
5. $\lim\_{n \to \infty}(1 + \frac{x}{n})^{n} = e^x$ 任何x  
6. $\lim\_{n \to \infty}\frac{x^n}{n!} = 0$ 任何x  
  
## 子序列，有界序列和皮卡方法
如果一个序列保持其次序出现在另一个序列里，则称第一序列为第二个序列的子序列.  
单调有界序列
## 无穷级数
## 非负项级数
##




# 平面向量和极坐标函数
## 平面向量
标量
有向线段表示，箭形表示作用方向，而长度给出大小.  
平面上的一个向量有有向线段。两个向量是相等(相同)的，如果他们有相同的长度和方向.  
如果平面上的一个向量v等于起点在原点(0,0),终点在(v1,v2),则v的分量形式是v=<v1,v2>。  
向量PQ的长度或大小是|v|=$sqrt{v\_1^2+v\_2^2}$  
长度为零的唯一向量是零向量 0=<0,0>  
任何长度为1的向量v是单位向量.  
与正x轴形成角$\theta$的单位向量表示为 $v=<\cos \theta, \sin \theta>$  
向量的代数运算：主要是向量的加法和数乘.  
向量运算的性质： 设u,v,w是向量，而a，b是数  
1, u+v=v+u   2. (u+v)+w = u+(v+w) 3. u+0=u  4. u+(-u)=0 5. 0u=0  
6, 1u=u  7,a(bu)=(ab)u  8, a(u+v)=au+av  9, (a+b)u=au+bu  
标准单位向量 i=<1,0> j=<0,1> v=<a,b>=ai+bj  
若$v \ne 0$则  
1. $\frac{v}{|v|}$是一个和v同方向的单位向量  
2. 等式$v=|v|\frac{v}{|v|}$借助v的长度和方向表示v.  
切线，法线，切向量，法向量  
## 点积
点积也叫数量积，因为乘积的结果是一个数，而不是向量.  
**定理1** 两个向量之间的夹角  
两个非零向量u=<$u\_1,u\_2$>和v=<$v\_1,v\_2$>的夹角由$\theta = \cos^{-1}\frac{u\_1v\_1 + u\_2v\_2}{|u||v|}$给出.  
**定义** 点积(内积)：两个向量u=<$u\_1,u\_2$>和v=<$v\_1,v\_2$>的点积(内积)是数$u\cdot v=u\_1v\_1 + u\_2v\_2$  
推论：两个非零向量u和v的夹角是$\theta = \cos^{-1}\frac{u\cdot v}{|u||v|}$.  
向量u和v正交，当且仅当$u\cdot v=0$  
数$|u|\cos \theta$称为u在v方向上的数值分量。小结如下：  
1. u在v上的向量投影 $proj_vu=\frac{u\cdot v}{|v|^2}v$  
2. u在v上的数值分量 $|u|\cos \theta = \frac{u\cdot v}{|v|} = u\cdot \frac{v}{|v|}$  
把一个向量写成正交向量的和：$u=proj_vu+(u-proj_vu)=\frac{u\cdot v}{|v|^2}v+(u-\frac{u\cdot v}{|v|^2}v)$  
  
## 向量-值函数
利用向量计算研究平面上一个运动物体的路径，速度和加速度.  