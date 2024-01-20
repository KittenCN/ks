### 背景知识：求解梯度

1. 手动求解

   1. 公式推导 --> 向量化

   2. 万能逼近算法：根据梯度的定义：在某一点的倒数=左边很近的点和右边很近的点确定直线的斜率

      ~~~python
      def dJ_debug(theta, X_b, y, epsilon=0.01):
          res = np.empty(len(theta))
          for i in range(len(theta)):
              theta_1 = theta.copy(); theta_2 = theta.copy()
              theta_1[i] += epsilon; theta_2 -= epsilon
              res[i] = (J(theta_1, X_b, y) - J(theta_2, X_b, y)) / (2*epsilon)
          return res
      ~~~

      **万能逼近公式可以作为求解出来的梯度的验证**

2. 自动求解

   1. pytorch中的梯度求解
   2. tensorflow中的梯度求解

3. 附录：各场景下的梯度值

### 梯度下降

0. 简单实现

   ~~~python
   import numpy as np
   import matplotlib.pylot as plt
   
   plot_x = np.linspace(-1, 6, 141)
   plot_y = (plot_x - 2.5) ** 2 - 1      # 模拟的损失函数
   plt.plot(plot_x, plot_y); plt.show()
   
   def dJ(theta):
       return 2 * (theta-2.5)        # theta位置损失函数的梯度（判断移动方向:-eta*gradient）
   def J(theta):                     # theta位置对应的损失函数（判断何时停止:变化后效果不大）
       return (theta - 2.5) ** 2 - 1
   
   def gradient_descent(theta, eta, epsilon):
       thetas = [theta]  # 所有走过的路
       while True:
           gradient = dJ(theta)          # 找到梯度
           last_theta = theta            # 保存更新前的theta值
           theta -= eta*gradient         # 得到新的theta值：根据方向更新theta
           thetas.append(theta)
           if abs(J(theta) - J(last_theta)) <=  epsilon:
               break
       plt.plot(plot_x, plot_y)
       plt.plot(np.array(thetas), J(np.array(thetas)), color="r")   # 走过的路和对应的值
       plt.show()
   theta = 0.0       # 怎么开始：初始化一个点
   eta = 0.1         # 怎么执行：学习率：一般不是固定不变的
   epsilon = 1e-8    # 怎么结束：更新一次效果增益达不到这个值，就退出
   gradient_descent(theta, eta, epsilon)
   
   # 后序探讨
   # 1. J函数越界问题
   #      如果eta取的不好，损失函数的方向是对的，但是步子太大了，损失函数就会越来越大
   #      当eta大到一定程度，损失函数的计算就会越界
   #      修改：将J函数用try包裹，越界就是float("Inf")   +   判断循环跳出条件再加一个最大迭代次数
   # 总结：
   #   1. 怎么开始：初始化一个theta值
   #         theta一般是一组向量
   #   2. 怎么执行：沿着梯度下降的方向，更新一小步
   #         - 一般每个方向上的theta沿着自己的方向上的梯度更新          (这个方向是性价比最高的方向)
   #         - 一般随着次数的增多学习率会有变化                        (大锤和小锤)
   #   3. 怎么结束：当损失函数的下降值小于阈值，认为差不多了            （止盈）
   #         - 一般还会搭配一个迭代次数：要是一直不小于阈值也能停止     （止损）
   # 深入讨论
   #   1. eta的变化：目标：大锤和小锤 也就是模拟退火的思想
   #         最简单的形式：eta = 1/i_iter         问题：当i_iter从1到2的时候，直接砍半了
   #         改进的形式    eta = a / (iter+b)     SGD中的eta方法   也是模拟退火的思想
   #            模拟退火：随时间有关    eta = t0 / (i_iter + t1) 
   ~~~

1. 线性回归

   ~~~python
   x  = 2 * np.random.random(size=100)
   y = x * 3. + 4. + np.random.normal(size=100)  # 构造数据
   x.reshae(-1, 1)  # 转成列向量
   
   def J(theta, X_b, y):        # 损失函数
       try:
           return np.sum((y-X_b.dot(theta)) ** 2) / len(X_b)  # MSE 公式
       except：
       	return float("Inf")
   def dJ_for(theta, X_b, y):   # for循环的笨办法求梯度
       res = np.empty(len(theta))
       res[0] = np.sum(X_b.dot(theta) - y)          # 比较特殊
       for i in range(1, len(theta)):  # 在特征上循环
           res[i] = (X_b.dot(theta) - y).dot(X_b[:, i])
       return res
   def dJ(theta, X_b, y):       # 向量化求梯度
       return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(X_b) 
   
   def gradient_descent(X_b, y, theta, eta, n_iters, epsilon):  # 比普通的多了 X_b, y两个工具参数
       i_iter = 0
       while i_iter < n_iters:
           gradient = dJ(theta, X_b, y)  # 找到梯度
           last_theta = theta            # 保存更新前的theta值
           theta -= eta*gradient         # 得到新的theta值：根据方向更新theta
           if abs(J(theta, X_b, y) - J(last_theta, X_b, y)) <=  epsilon:
               break
           i_iter += 1
   	return theta
       
   # 工具参数
   X_b = np.hstack([np.ones(len(X), 1), X])  # 注意X_b和X的不同
   # 梯度下降参数
   theta = np.zeros(X_b.shape[1])       # 怎么开始：初始化一个向量：特征值个数+1(常数项)
   eta = 0.1                            # 怎么执行：学习率：一般不是固定不变的
   epsilon = 1e-8                       # 怎么结束：更新一次效果增益达不到这个值，就退出
   theta_ = gradient_descent(theta, eta, n_iters, epsilon)
   
   # 后序探讨
   # 1. 注意X_b的变化，给X增加了一个维度
   #       背景：是在公式推导的过程中，把常数项也作为参数的一部分
   #       推论：如果把常数项也作为参数的一部分，X就需要增加一个维度
   #       操作：X_b = np.hstack([np.ones(len(X), 1), X])   在前面拼了一个都是1的列向量
   #       结果：X_b的维度变成：m行  2列   其中第一列都是1    就可以和  theta的 2行 1列 做点乘
   #       注意：因为X_b的第一列是1，所有theta的第一行是常数参数
   # 2. 使用梯度下降前最好先归一化
   #       需要明确：是否使用归一化，不影响最后的最优点，也不影响初始化的值
   #       不归一化：各个特征上的值不在同一个尺度上，每次求的梯度不是朝着靶心
   #       归一化：损失函数的等高线是一个正圆，每次的梯度都会朝着靶心
   # 3. 当特征数量很大的时候，梯度下降法相较正规方程的优势就会越明显
   # 4. 当样本量很大的时候，梯度的求解会很慢
   #       方法：随机梯度下降法改进批量梯度下降法：本质就是修改了X_b这个工具参数
   #       过程：梯度的方向最后还除以了一个m，其实是在一个样本的概念上，那直接把m去掉，只用一个样本
   #                  这个样本是随机选取的：
   #       结果：不能保证一定是下降最快的方向，甚至不能保证是下降最快的方向
   # SGD的讨论
   # 1. SGD中随机选取样本，为了平衡最外面的 1/m
   #     梯度的计算：此时梯度的计算X_b = X_b[random]   y = y[random]
   #     注意：当新的损失函数值不能保证一定是下降的方向时，止盈的目标就没有意义了，只有止损一个目标
   # 2. SGD中eta的更新采用模拟退火的思想
   # 3. 本质：每次循环其实只随机的检查了一个样本
   # 4. 随机梯度下降的威力：
   #     即使将迭代次数设置成  len(X_b)//3  样本量的1/3，也就是说整个算法只随机看了1/3的样本
   #     效果也很好
   # 5. 使用方式：随机的把所有样本看一遍
   #     将样本乱序排列：
   #         indexes = np.random.permutation(len(X_b))
   #         X_b_new = X_b[indexes]; y_new = y[indexes]
   #     此时迭代次数就是看的第几个样本即可
   # 6. 小批量梯度下降法：每次看k个
   ~~~

2. PCA

   ~~~python
   # 构造数据:PCA处理的数据没有y
   feature_1 = np.random.uniform(0., 100., size=100)                       # 第一个特征：100样本
   feature_2 = 0.75 * feature_1 + 3. + np.random.normal(0, 10., size=100)  # 第二个特征：与特征1有关
   X = np.hstack((feature_1, feature_2))  # 100个样本，2个特征
   
   # demean过程
   plt.scatter(X[:,0], X[:,1]); plt.show()
   X_demean = X-np.mean(X, axis=0)  # 行方向上求均值--->每一行一个均值--->列的均值
   plt.scatter(X_demean[:,0], X_demean[:,1]); plt.show()
   
   def f(w, X):        # 目标函数
       return np.sum((X.dot(w)**2)) / len(X)
   def df_math(w, X):  # 目标函数的梯度
       return X.T.dot(X.dot(w)) * 2. / len(X)
   def first_component(df, X, initial_w, eta, n_iters=1e4, epsilon=1e-8):  # 梯度上升
       w = w / np.linalg.norm(w)   # 每次让w是一个单位向量
       cur_iter = 0
       while cur_iter < n_iters:
           gradient = df(w, X)
           last_w = w
           w = w_ eta * gradient
           w = w / np.linalg.norm(w)   # 每次让w是一个单位向量
           if(abs(f(w, X)-f(last_w, X)) < epsilon):
               break
           cur_iter += 1
       return w
   
   # 主程序
   initial_w = np.random.random(X.shape[1])  # w不能从0开始
   w = first_component(df_math, X_demean, initial_w, eta=0.001)
   plt.scatter(X-demean[:, 0], X_demean[:, 1])
   plt.plot([0, w[0]*30], [0, w[1]*30], color="r"); plt.show()
   
   # 去掉第一主成分的分量：
   X2 = np.empty(X.shape)
   for i in range(len(X)):  # 所有的样本都要减去最大主成分的分量
       X2[i] = X[i] - X[i].dot(w) * w  # X[i].dot(w)模长   w 方向向量
   plt.scatter(X2[:,0], X2[:,1]); plt.show()
   # 后序探讨
   # 1. 不能标准化：
   #     demean：作用其实是标准化了一半
   #     需要保留方差的信息，才可以让方差最大
   # 2. w的更新
   #     w的初始化：不能从0开始，0是没有方向的
   #     w的更新：每次更新w后，需要让w变成单位向量，只关心最后theta也就是w的方向，单位向量的运算量很小
   # 3. 第二主成分
   #     本质：第二主成分就是所有的X去掉第一主成分的分量，之后的X再求第一主成分
   #     过程1：proj_len = X[i].dot(w)   每个样本点乘w得到映射到w方向上的模长*1   (点乘结果是一个数字)
   #     过程2：vector = proj_len * w    模长*w方向得到 w方向上的分量
   #     过程3：X[i] = X[i] - vector     每个样本-该样本在w方向上的分量
   #     过程4：再次对X求第一主成分  
   ~~~


### 附录

#### 线性回归

1. 损失函数

    $\sum_{i=1}^{m}\left(y^{(i)}-\theta_{0}-\theta_{1} X_{1}^{(i)}-\theta_{2} X_{2}^{(i)}-\ldots-\theta_{n} X_{n}^{(i)}\right)^{2}​$    最小

2. 损失函数的偏导

   $\nabla J(\theta)=\left(\begin{array}{c}\partial J / \partial \theta_{0} \\ \partial J / \partial \theta_{1} \\ \partial J / \partial \theta_{2} \\ \ldots \\ \partial J / \partial \theta_{n}\end{array}\right)=\left(\begin{array}{c}\sum_{i=1}^{m} 2\left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot(-1) \\ \sum_{i=1}^{m} 2\left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot\left(-X_{1}^{(i)}\right) \\ \sum_{i=1}^{m} 2\left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot\left(-X_{2}^{(i)}\right) \\ \cdots \\ \sum_{i=1}^{m} 2\left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot\left(-X_{n}^{(i)}\right)\end{array}\right)​$

3. 提出2，并且/m  为了消除样本数量的影响，现在的梯度随着样本量的增大会增大 得到结果

   $\nabla J(\theta)=\frac{2}{m}\left(\begin{array}{c}\sum_{i=1}^{m} \left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot(-1) \\ \sum_{i=1}^{m} \left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot\left(-X_{1}^{(i)}\right) \\ \sum_{i=1}^{m} \left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot\left(-X_{2}^{(i)}\right) \\ \cdots \\ \sum_{i=1}^{m} \left(y^{(i)}-X_{b}^{(i)} \theta\right) \cdot\left(-X_{n}^{(i)}\right)\end{array}\right)​$

4. 向量化

   $\nabla J(\theta)=\frac{2}{m}\cdot (X_b\theta-y)^T\cdot X_b ​$

   $\nabla J(\theta) = \frac{2}{m}\cdot X_b^T\cdot(X_b\theta-y)$                    $A^T\cdot B = B^T\cdot A$

5. 总结：此时的梯度函数其实对应的损失函数是 MSE 而不是最小二乘

#### PCA

1. 最大化目标：$f(X)=\frac{1}{m}\sum^m_{i=1}(X_1^{(i)}w_1 + X_2^{(i)}w2+...+X_n^{(i)}w_n)^2$

2. 求偏导：此时就可以计算了，但是需要循环

   $\nabla f=\left(\begin{array}{c}\frac{\partial f}{\partial w_{1}} \\ \frac{\partial f}{\partial w_{2}} \\ \ldots \\ \frac{\partial f}{\partial w_{n}}\end{array}\right)=\frac{2}{m}\left(\begin{array}{c}\sum_{i=1}^{m}\left(X_{1}^{(i)} w_{1}+X_{2}^{(i)} w_{2}+\ldots+X_{n}^{(i)} w_{n}\right) X_{1}^{(i)} \\ \sum_{i=1}^{m}\left(X_{1}^{(i)} w_{1}+X_{2}^{(i)} w_{2}+\ldots+X_{n}^{(i)} w_{n}\right) X_{2}^{(i)} \\ \cdots \\ \sum_{i=1}^{m}\left(X_{1}^{(i)} w_{1}+X_{2}^{(i)} w_{2}+\ldots+X_{n}^{(i)} w_{n}\right) X_{n}^{(i)}\end{array}\right)=\frac{2}{m}\left(\begin{array}{c}\sum_{i=1}^{m}\left(X^{(i)} w\right) X_{1}^{(i)} \\ \sum_{i=1}^{m}\left(X^{(i)} w\right) X_{2}^{(i)} \\ \ldots \\ \sum_{i=1}^{m}\left(X^{(i)} w\right) X_{n}^{(i)}\end{array}\right)$

3. 对偏导化简

   $\nabla f=\left(\begin{array}{c}\frac{\partial f}{\partial w_{1}} \\ \frac{\partial f}{\partial w_{2}} \\ \ldots \\ \frac{\partial f}{\partial w_{n}}\end{array}\right)=\frac{2}{m} \cdot\left(X^{(1)} w, \quad X^{(2)} w, \quad X^{(3)} w, \quad \ldots \quad X^{(m)} w\right)\cdot\left(\begin{array}{c}X_{1}^{(1)}\;\;\;X_{2}^{(1)}\;\;\;X_{3}^{(1)}\;\;\;\dots \;\;\;X_{n}^{(1)} \\ X_{1}^{(2)}\;\;\;X_{2}^{(2)}\;\;\;X_{3}^{(2)}\;\;\;\dots \;\;\;X_{n}^{(2)} \\ \cdots \\ X_{1}^{(m)}\;\;\;X_{2}^{(m)}\;\;\;X_{3}^{(m)}\;\;\;\dots \;\;\;X_{n}^{(m)} \end{array}\right)$

4. 右侧是两个大矩阵相乘：化简得到结果：两个矩阵相乘

   $\nabla f=\left(\begin{array}{c}\frac{\partial f}{\partial w_{1}} \\ \frac{\partial f}{\partial w_{2}} \\ \ldots \\ \frac{\partial f}{\partial w_{n}}\end{array}\right)=\frac{2}{m}\cdot (Xw)^T\cdot X=\frac{2}{m}\cdot X^T(Xw)$

#### 逻辑回归：没有解析解

##### 背景补充  $(log(\sigma(x)))'=1-\sigma(t)$

1. sigmoid的导数：

   $g'(z)=(-1)*(1+e^{-z})^{-2}*e^{-z}*(-1)=(1+e^{-z})^{-2}*e^{-z}​$ 

2. 根据复合函数求导：

   $(log(\sigma(x)))'=\frac{1}{\sigma(t)} * \sigma(t)'​$

3. 带入化简

   $(log(\sigma(x)))'=\frac{1}{(1+e^{-z})^{-1}} * (1+e^{-z})^{-2}*e^{-z}=\frac{e^{-t}}{1+e^{-t}}=1-\sigma(t)​$

#### 梯度推导

1. 损失函数：有两种理解方式

   $J(\theta)=-\frac{1}{m} \sum_{i=1}^{m}\left[y^{(i)} \log h_{\theta}\left(x^{(i)}\right)+\left(1-y^{(i)}\right) \log \left(1-h_{\theta}\left(x^{(i)}\right)\right)\right]​$      $h_{\theta}(x) = \frac{1}{1+e^{-x}}​$

2. 求导过程：https://www.cnblogs.com/lxs0731/p/8573044.html    视频：慕课机器学习 第九章第三集