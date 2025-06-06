---
description: CoderFAN 资料库 基础算法
---

# 一、算法
## 1. 贪心
- 所谓贪心算法，当然是很贪心的算法。就是鼠目寸光地从局部看全局，首先得到局部的最优解，从而推导出全局的最优解。但是这种算法有时候并不适用，乱用会导致进入误区。
### 例题1
 在一个长n宽m的矩形中，有n*m数，若要从左下角走到右上角，且只能向右或向上走，问经过的数字之和最大是多少。      
 * 思路：  
 利用贪心的思想：从1开始，有两条路——2或3，因为2<3，所以选3,然后4、6。总和为14，最大。  

|    *  |   *   |
|  ---- | ----  |
|   3   |   6   |
|   2   |   4   |
|   1   |   3   |

 但有这样一个例子：可见贪心算法为了3-2得到的1舍去了去10的道路，14<1+2+10+6，真不愧是“贪心”算法啊！  

|    *  |   *   |
|  ---- | ----  |
|   10   |   6   |
|   2   |   4   |
|   1   |   3   |

好了，介绍的都介绍完了。接下来我们进入正题——删数问题！  

### 例题2
 有一个长度为n（n <= 240）的正整数，从中取出s（s < n）个数，使剩余的数保持原来的次序不变，求这个正整数经过删数之后最小是多少。  

 输入：178543 4  
 样例输出：13  

* 思路  
 那么刚拿到这道题如何去思考呢？我们可以先试着找规律。  
 如果要从178543中取出1个数，使这个数最小，应该取……  
 8  
 如果要从17543中取出1个数，使这个数最小，应该取……  
 7  
 如果要从1543中取出1个数，使这个数最小，应该取……  
 5  
 ……  
 可以发现：1，7，8是一个不降序数列（有相等的升序），也就是逐渐变多，而8，5，4，3是一个不升序数列（有相等的降序），逐渐减少。  
 8正好是升序数列的最后一个，也是降序数列的第一个。  
 其他几组也是同样的道理。  
  
 那么这样就好办了！我们只需要找到第一个升序数列的末尾并取出它就可以算成功完成了“局部的最优解”，再通过这个继续取出更多的数，直到取出s个数来，从局部的最优解进阶到全局的最优解，这一道题就完成了！  

* 代码
 ```cpp
 #include<cstdio>
#include<cstring>       //格式化输入输出头文件和字符串头文件
char n[250];        //利用字符数组来储存高精度数
int s,i,len,flag=1;
int main()
{
    scanf("%s %d",n,&s);
    len=strlen(n);             //这里是长度函数，取n的长度并赋值给len
    while(s!=0)              //只要s不是0，取数的工作就没有做完！
    {
        i=0;
        while(n[i]<=n[i+1]) //括号内的条件保证了不降序的条件，当它退出时，就是升序数列的末尾了
            i++;
        while(i<len-1)         //这时已经找到了要取出的数——n[i]，这是取出的过程
        {n[i]=n[i+1];i++;}         //其实这个循环可以用erase(i,1);代替
        len--;                //取出后数字长度减1
        s--;                   //消耗掉一次取出次数
    }
    for(int i=0;i<len;i++)         //输出时要小心最高位是0的问题！处理输出……
    {
        if(n[i]=='0'&&i<len-1&&flag==1)  //如果即将输出的这一位是0且是最高位而且不是最后一个
            continue;           //跳过
        else
        {printf("%c",n[i]);flag=0;}//输出并且明确n[i]不再是最高位
    }
    return 0;
}
```  


## 2. 动态规划
- 你有很多硬币，面额为1，2，4，8，....，2^k，每种面额的硬币有两个，要求凑出n元来，输出不同的凑硬币方案的数目。

    $\sum_{i=1}^{n}(2k-1) = 1 + 3+5+...+(2n-1) = n^2$

- 最长回文子序列 dp 相反之后做LCS
```java
for(int i=1;i<=X.length;i++){
    for (int j=1;j<=Y.length;j++){
        if(X[i-1]==Y[j-1]){
            c[i][j] = c[i-1][j-1]+1;
        }
        else{
            c[i][j] = max(c[i][j-1],c[i-1][j]);
        }
    }
}
```
- **找零钱问题**： 
    - 假设只有 1 分、 2 分、五分、 1 角、二角、 五角、 1 元的硬币。在超市结账时，如果需要找零钱，收银员希望将最少的硬币数找给顾客。那么，给定需要找的零钱数目，如何求得最少的硬币数呢？  
```java 
public class zhaolingqian {
    public int caldp(int n,int[] money){
        // dp[i] 金额为i时找的零钱数目
        int[] dp = new int[n + 5];
        for (int i = 1; i<dp.length; i++){
            dp[i] = Integer.MAX_VALUE; //!!!!!!!!!!!!
        }
        dp[0] = 0;
        for (int i = 0; i < money.length; i++){
            for (int j = money[i]; j <= n; j++){
                dp[j] = Math.min(dp[j - money[i]] + 1 , dp[j]);
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int[] money = {1,2,5,10,20,50,100};
        zhaolingqian zq = new zhaolingqian();
        System.out.println(zq.caldp(625, money)); //8
    }
}
```
## 3. 排序算法  
[各种排序算法原理与比较](/algorithms/other_algo/Sorting.md)  
[七大查找算法](/algorithms/other_algo/Searching.md)  
> 查找是在大量的信息中寻找一个特定的信息元素，在计算机应用中，查找是常用的基本运算，例如编译程序中符号表的查找。本文简单概括性的介绍了常见的七种查找算法，说是七种，其实二分查找、插值查找以及斐波那契查找都可以归为一类——插值查找。插值查找和斐波那契查找是在二分查找的基础上的优化查找算法。树表查找和哈希查找会在后续的博文中进行详细介绍。 >
>
> - **查找定义**：根据给定的某个值，在查找表中确定一个其关键字等于给定值的数据元素（或记录）。
>
> - **查找算法分类**：  
> 　　- 静态查找和动态查找；  
> 　　　　注：静态或者动态都是针对查找表而言的。动态表指查找表中有删除和插入操作的表。  
> 　　- 无序查找和有序查找。  
> 　　　　无序查找：被查找数列有序无序均可；  
> 　　　　有序查找：被查找数列必须为有序数列。
> - **平均查找长度**（Average Search Length，ASL）：需和指定key进行比较的关键字的个数的期望值，称为查找算法在查找成功时的平均查找长度。  
> 　　对于含有n个数据元素的查找表，查找成功的平均查找长度为：ASL = Pi*Ci的和。  
> 　　Pi：查找表中第i个数据元素的概率。  
> 　　Ci：找到第i个数据元素时已经比较过的次数。

- O(N)查找有哪些数据结构？
	- 答：顺序查找
- O(logN)查找有哪些数据结构？
	- 答：二分查找、斐波那契查找、二叉查找树（最坏有O(n)的复杂度）、红黑树。
- O(1)查找有哪些数据结构？
	- 答：hash（无冲突的情况）
- 其他：插值查找时间复杂度均为O(log2(log2n))。
#### 堆排序  
- 堆排序（使用大堆，升序）从基本实现原理来说也是一种选择排序。
- 所谓大根堆，就是根节点大于子节点的完全二叉树。
- 首先将所有元素都构建在一个初始堆中，并重建为大堆。这时当前堆中的最大元素就在堆的顶部，也就是数组a[0]，这时将该最大元素与数组中的最后一个元素交换，使其移到最末尾，表明该元素已经到应该在得位置了，之后的堆重建也不需要管他，所以last--，对缩小后的目标堆重建。就这样，将顶端最大的元素与最后一个元素不断的交换，交换后又不断的调用堆以重新维持最大堆的性质，最后，一个一个的，从大到小的，把堆中的所有元素都清理掉，也就形成了一个有序的序列。这就是堆排序的全部过程。
```java

public class heapSort {
    private int[] a = new int[100];

    public heapSort(int[] a) {
        this.a = a;
        this.size = a.length;
    }

    private int size;

    public static void swap(int[] a, int i, int j){
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
    public static void rebuild(int[] a, int rt, int size){
        int lchild = 2*rt + 1;
        if(lchild < size){
            int rchild = lchild + 1;
            if(rchild < size){
                if(a[lchild] < a[rchild]){  //>
                    lchild = rchild;
                }
            }

            if(a[rt] < a[lchild]){  //构建大根堆，升序
                swap(a,lchild, rt);
                rebuild(a, lchild, size);
            }
        }
    }

    public void sort(int[] a){
        for(int i=size-1; i>=0; i--){
            rebuild(a, i, size);
        }

        int last = size - 1;
        for(int i = 1; i<= size; i++,last--){
            swap(a, 0, last);
            rebuild(a,0,last);
            // display();
        }
    }

    public void display(){
        for(int i=0; i<size; i++){
            System.out.printf(a[i]+",");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] a = {5,3,1,2,4, 7,9,10,57,1};
        heapSort myhs = new heapSort(a);
        myhs.sort(a);
        myhs.display();
    }
}

```

- **快排**
```java
public class QuickSort {
    public void qsort(int[] a, int l, int r){
        if (l >= r) return ;
        int i = l, j = r, pivot = a[l];
        while(i < j){
            while(i < j && pivot < a[j])
                j--;
            a[i] = a[j];
            while(i < j && pivot > a[i])
                i++;
            a[j] = a[i];
        }
        a[i] = pivot;
        qsort(a, l, i);
        qsort(a, i+1, r);
    }

    public static void main(String[] args) {
        QuickSort quickSort = new QuickSort();
        int[] a = {5,2,3,1,4};
        quickSort.qsort(a,0,4);
        for (int i:a) {
            System.out.print(i + " ");
        }
    }

}

```

- **归并排序**
```java
public class Main {
 
	public static void main(String[] args) {
		int[] arr = {11,44,23,67,88,65,34,48,9,12};
		int[] tmp = new int[arr.length];    //新建一个临时数组存放
		mergeSort(arr,0,arr.length-1,tmp);
		for(int i=0;i<arr.length;i++){
			System.out.print(arr[i]+" ");
		}
	}
	
	public static void merge(int[] arr,int low,int mid,int high,int[] tmp){
		int i = 0;
		int j = low,k = mid+1;  //左边序列和右边序列起始索引
		while(j <= mid && k <= high){
			if(arr[j] < arr[k]){
				tmp[i++] = arr[j++];
			}else{
				tmp[i++] = arr[k++];
			}
		}
		//若左边序列还有剩余，则将其全部拷贝进tmp[]中
		while(j <= mid){    
			tmp[i++] = arr[j++];
		}
		
		while(k <= high){
			tmp[i++] = arr[k++];
		}
		
		for(int t=0;t<i;t++){
			arr[low+t] = tmp[t];
		}
	}
 
	public static void mergeSort(int[] arr,int low,int high,int[] tmp){
		if(low<high){
			int mid = (low+high)/2;
			mergeSort(arr,low,mid,tmp); //对左边序列进行归并排序
			mergeSort(arr,mid+1,high,tmp);  //对右边序列进行归并排序
			merge(arr,low,mid,high,tmp);    //合并两个有序序列
		}
	}
}	
```

- **不同条件下，排序方法的选择**
    1. 若n较小(如n≤50)，可采用直接插入或直接选择排序。
    　当记录规模较小时，直接插入排序较好；否则因为直接选择移动的记录数少于直接插人，应选直接选择排序为宜。
    2. 若文件初始状态基本有序(指正序)，则应选用直接插人、冒泡或随机的快速排序为宜；
    3. 若n较大，则应采用时间复杂度为O(nlgn)的排序方法：快速排序、堆排序或归并排序。
    - 快速排序是目前基于比较的内部排序中被认为是最好的方法，当待排序的关键字是随机分布时，快速排序的平均时间最短；
    - 堆排序所需的辅助空间少于快速排序，并且不会出现快速排序可能出现的最坏情况。这两种排序都是不稳定的。
    - 若要求排序稳定，则可选用归并排序。但本章介绍的从单个记录起进行两两归并的  排序算法并不值得提倡，通常可以将它和直接插入排序结合在一起使用。先利用直接插入排序求得较长的有序子文件，然后再两两归并之。因为直接插入排序是稳定 的，所以改进后的归并排序仍是稳定的。

    优先队列通常用堆排序来实现

## 4. 图论
### [图的遍历和图的连通性](/algorithms/base_algo/Graph_traversal_and_graph_connectivity.md)**    
    即BFS、DFS和Kruskal、Prim 算法
### 拓扑排序  
由AOV网构造拓扑序列的拓扑排序算法主要是循环执行以下两步，直到不存在入度为0的顶点为止。
(1) 选择一个入度为0的顶点并输出之；
(2) 从网中删除此顶点及所有出边。
循环结束后，若输出的顶点数小于网中的顶点数，则输出“有回路”信息，否则输出的顶点序列就是一种拓扑序列。
## 5. 数据结构
### 5.1 栈 
- 题目描述
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。  
栈的特性是先进后出，队列的是先进先出，知道这点，基本上都能想到怎么做了。。。 
还是说一下步骤：
    - 队列的push()操作，就直接在stack1上进行栈的push()操作即可；
    - 队列的pop()操作，其实就是得到stack1中最底下的那个元素，怎么得到呢？先把上面逐个退出的元素一个个放在另一个栈stack2中；
    - 当stack1为空的时候，stack2的栈顶元素，就是要取得的元素，用栈的pop()操作取出，在将该元素进行返回前，再将stack2中的元素，倒回到stack1中，然后将该元素返回，over.

```java
import java.util.Stack;

public class TwoStackQueue {

    Stack<Integer> s1 = new Stack<>();
    Stack<Integer> s2 = new Stack<>();

    public static void main(String[] args) {
        TwoStackQueue twoStackQueue = new TwoStackQueue();
        twoStackQueue.push(1);
        twoStackQueue.push(2);
        System.out.println(twoStackQueue.pop());
    }

    private int pop() {
        while(!s1.empty()){
            s2.push(s1.pop());
        }
        int res = s2.pop();
        //重新pop回去
        while(!s2.empty()){
            s1.push(s2.pop());
        }
        return res;

    }

    private void push(int i) {
        s1.push(i);
    }

}

```
### 5.2 链表
- 链表反转
    - 遍历反转法：递归反转法是从后往前逆序反转指针域的指向，而遍历反转法是从前往后反转各个结点的指针域的指向。
    - 基本思路是：将当前节点cur的下一个节点 cur.getNext()缓存到temp后，然后更改当前节点指针指向上一结点pre。也就是说在反转当前结点指针指向前，先把当前结点的指针域用tmp临时保存，以便下一次使用，其过程可表示如下：
    - pre：上一结点
    - cur: 当前结点
    - tmp: 临时结点，用于保存当前结点的指针域（即下一结点）  

```java
public class LinkedListReverse {
    private void Display(Node node){
        while (null != node){
            System.out.println(node.getData() + " ");
            node = node.getNext();
        }
        System.out.println("====");
    }
    private Node Reverse(Node head){
        if (head == null)
            return head;
        Node pre = head;
        Node cur = head.getNext();
        Node tmp;
        while(null != cur){
            tmp = cur.getNext();
            cur.setNext(pre);

            pre = cur;
            cur = tmp;
        }
        head.setNext(null);

        return pre;
    }
    public static void main(String[] args) {
        Node head = new Node(0);Node n1 = new Node(1);
        Node n2 = new Node(2);Node n3 = new Node(3);

        head.setNext(n1);n1.setNext(n2);
        n2.setNext(n3);n3.setNext(null);

        LinkedListReverse linkedListReverse = new LinkedListReverse();
        linkedListReverse.Display(head);

        Node rvs = linkedListReverse.Reverse(head);
        linkedListReverse.Display(rvs);
    }

}


class Node{
    private int data;
    private Node next;
}
```


- 判断一个单链表是否有环
    最常用方法：定义两个指针，同时从链表的头节点出发，一个指针一次走一步，另一个指针一次走两步。如果走得快的指针追上了走得慢的指针，那么链表就是环形链表；如果走得快的指针走到了链表的末尾（next指向 NULL）都没有追上第一个指针，那么链表就不是环形链表。  

- **使用异或交换两个整数或者字符串**  
    ```java
    public static String reverse(String s){
        char[] a = s.toCharArray();
        int first = 0, last = a.length-1;
        while(first < last){
            a[first] = (char)(a[first] ^ a[last]);
            a[last] = (char)(a[last] ^ a[first]);
            a[first] = (char)(a[last] ^ a[first]);
            first ++;
            last --;
        }
        return new String(a);
    }
    ```
### 5.3 树
#### BST转换为有序双向链表  
```java
 //双向链表的左边头结点和右边头节点
    static Node lhead = null;
    static Node rhead = null;
//    递归调用 左 根 右 遍历
    public static Node convert(Node rt){
       if (rt == null)  return null;
        //第一次运行时，它会使最左边叶子节点为链表第一个节点
       convert(rt.left);

       if (rhead == null){
           lhead = rhead = rt;
       }
       else{//把根节点插入到双向链表右边，rightHead向后移动
           rhead.right = rt;
           rt.left = rhead;
           rhead = rt;
       }
//把右叶子节点也插入到双向链表（rightHead已确定，直接插入）
       convert(rt.right);

       return lhead;
    }
```


#### 红黑树
- 节点是红色或黑色。
- 根是黑色。
- 所有叶子都是黑色（叶子是NIL节点）。
- 每个红色节点必须有两个黑色的子节点。（从每个叶子到根的所有路径上不能有两个连续的红色节点。）
- 从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点。
- 划分红黑的意义
    - 2-3 查找树需要用到 2- 节点和 3- 节点，红黑树使用红链接来实现 3- 节点。指向一个节点的链接颜色如果为红色，那么这个节点和上层节点表示的是一个 3- 节点，而黑色则是普通链接。
    
- RB-Tree
- 2-3查找树能保证在插入元素之后能保持树的平衡状态，最坏情况下即所有的子节点都是2-node，树的高度为lgN，从而保证了最坏情况下的时间复杂度。但是2-3树实现起来比较复杂，本文介绍一种简单实现2-3树的数据结构，即红黑树（Red-Black Tree）
- 红黑树的主要是想对2-3查找树进行编码，尤其是对2-3查找树中的3-nodes节点添加额外的信息。红黑树中将节点之间的链接分为两种不同类型，红色链接，他用来链接两个2-nodes节点来表示一个3-nodes节点。黑色链接用来链接普通的2-3节点。特别的，使用红色链接的两个2-nodes来表示一个3-nodes节点，并且向左倾斜，即一个2-node是另一个2-node的左子节点。这种做法的好处是查找的时候不用做任何修改，和普通的二叉查找树相同。
- 链接中还有动画演示。

### 5.4. 哈希表
- 哈希表就是一种以 键-值(key-indexed) 存储数据的结构，我们只要输入待查找的值即key，即可查找到其对应的值。
- 使用哈希查找有两个步骤:
	1. 使用哈希函数将被查找的键转换为数组的索引。在理想的情况下，不同的键会被转换为不同的索引值，但是在有些情况下我们需要处理多个键被哈希到同一个索引值的情况。所以哈希查找的第二个步骤就是处理冲突
	2. 处理哈希碰撞冲突。有很多处理哈希碰撞冲突的方法，本文后面会介绍拉链法和线性探测法。
- 实现哈希函数：以正整数与字符串为例
	- 获取正整数哈希值最常用的方法是使用除留余数法。即对于大小为素数M的数组，对于任意正整数k，计算k除以M的余数。M一般取素数。
	- 我们可以将组成字符串的每一个字符取值然后进行哈希 `for (int i = 0; i < value.length; i++) {h = 31 * h + val[i];}`
- 避免哈希冲突
	- 拉链法：其实就是将冲突后的数据依次存入链表中。
	- 线性探测法；开放寻址法中最简单的是线性探测法：当碰撞发生时即一个键的散列值被另外一个键占用时，直接检查散列表中的下一个位置即将索引值加1  

- Hashtable

## 6. 经典问题
### Top k 问题
- Top K
- 堆排序方法

	按照堆排序的方法排序之后输出前K个即可。  
	**时间复杂度**   
	`n*logK `   
	**适用场景**   
	实现的过程中，我们先用前K个数建立了一个堆，然后遍历数组来维护这个堆。这种做法带来了三个好处：（1）不会改变数据的输入顺序（按顺序读的）；（2）不会占用太多的内存空间（事实上，一次只读入一个数，内存只要求能容纳前K个数即可）；（3）由于（2），决定了它特别适合处理海量数据。

	这三点，也决定了它最优的适用场景。
- 快排方法

	用快排的partition思想，对数组进行不断分治，使得基准点pos刚好在K-1的位置上，此时前面的K个数字（0,K-1）就是要找的前K个数。

	**时间复杂度**   
	`n`

	**适用场景**   
	对照着堆排的解法来看，partition函数会不断地交换元素的位置，所以它肯定会改变数据输入的顺序；既然要交换元素的位置，那么所有元素必须要读到内存空间中，所以它会占用比较大的空间，至少能容纳整个数组；数据越多，占用的空间必然越大，海量数据处理起来相对吃力。

	但是，它的时间复杂度很低，意味着数据量不大时，效率极高。
### string 反转
除了普通的交换，还可以用异或的方法减少空间复杂度。  

```Java
public static String reverse(String s){
    char[] a = s.toCharArray();
    int first = 0, last = a.length-1;
    while(first < last){
        a[first] = (char)(a[first] ^ a[last]);
        a[last] = (char)(a[last] ^ a[first]);
        a[first] = (char)(a[last] ^ a[first]);
        first ++;
        last --;
    }
    return new String(a);
}
```
### 链表反转  
```java
    private Node Reverse(Node head){
        if (head == null)
            return head;
        Node pre = head;
        Node cur = head.getNext();
        Node tmp;
        while(null != cur){
            tmp = cur.getNext();
            cur.setNext(pre);

            pre = cur;
            cur = tmp;
        }
        head.setNext(null);

        return pre;
    }
```
### 两个线程交替输出1-100  
```java
//两个线程交替执行打印 1~100  
public class TwoThread {
    private int out = 1;

    private static boolean flag = false;

    private static Lock lock = new ReentrantLock();

    public static void main(String[] args) {
        TwoThread twoThread = new TwoThread();

        Thread t1 = new Thread(new PrintOdd(twoThread));
        Thread t2 = new Thread(new PrintEven(twoThread));

        t1.setName("Odd");
        t2.setName("Even");

        t1.start();
        t2.start();
    }

    public static class PrintOdd implements Runnable{
        private TwoThread num;

        public PrintOdd(TwoThread num) {
            this.num = num;
        }

        @Override
        public void run() {
            while (num.out <= 100){
                if (!flag) {
                    try{
                        lock.lock();
                        System.out.println(Thread.currentThread().getName() + ": " + num.out);
                        num.out ++;
                        flag = !flag;
                    } finally {
                        lock.unlock();
                    }
                } else {
                    try {
                        Thread.sleep(10);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }

    public static class PrintEven implements Runnable{
        private TwoThread num;

        public PrintEven(TwoThread num) {
            this.num = num;
        }

        @Override
        public void run() {
            while (num.out <= 100){
                if (flag) {
                    try{
                        lock.lock();
                        System.out.println(Thread.currentThread().getName() + ": " + num.out);
                        num.out ++;
                        flag = !flag;
                    } finally {
                        lock.unlock();
                    }
                } else {
                    try {
                        Thread.sleep(10);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }
}

```
### 小白鼠喝毒药
你只有 10 只小白鼠和一星期的时间，如何检验出哪个瓶子里有毒药？
有 1000 个一模一样的瓶子，其中有 999 瓶是普通的水，有一瓶是毒药。任何喝下毒药的生物都会在一星期之后死亡。现在，你只有 10 只小白鼠和一星期的时间，如何检验出哪个瓶子里有毒药？

- 根据2^10=1024，所以10个老鼠可以确定1000个瓶子具体哪个瓶子有毒。具体实现跟3个老鼠确定8个瓶子原理一样。
    - 000=0
    - 001=1
    - 010=2
    - 011=3
    - 100=4
    - 101=5
    - 110=6
    - 111=7
- 一位表示一个老鼠，0-7表示8个瓶子。也就是分别将1、3、5、7号瓶子的药混起来给老鼠1吃，2、3、6、7号瓶子的药混起来给老鼠2吃，4、5、6、7号瓶子的药混起来给老鼠3吃，哪个老鼠死了，相应的位标为1。如老鼠1死了、老鼠2没死、老鼠3死了，那么就是101=5号瓶子有毒。同样道理10个老鼠可以确定1000个瓶子


- 你只有 10 只小白鼠和一星期的时间，如何检验出哪个瓶子里有毒药？  

### LRU  
```java
package practice;

import java.util.HashMap;

public class LRUCache {

    class Node {
        int key;
        int val;
        Node pre;
        Node next;

        public Node (Integer k, Integer v){
            this.key = k;
            this.val = v;
        }
    }

    Node head; //null
    Node tail; //null

    HashMap<Integer, Node> map = new HashMap<>();

    int capacity;

    public LRUCache (int capacity) {
        this.capacity = capacity;
        head = new Node(null, null);
        tail = new Node(null, null);
        head.next = tail;
        tail.pre = head;
    }

    public int get(int key) {
        Node n = map.get(key);
        if (n == null)  return -999;
        n.pre.next = n.next;
        n.next.pre = n.pre;
        append(n);
        return n.val;
    }

    public void put(int key, int value) {
        Node n = map.get(key);
        if (n == null) {
            n = new Node(key, value);
            append(n);
            map.put(key, n);// no return
        } else {
          // update
            n.val = value;
            map.put(key, n);
            //remove
            n.pre.next = n.next;
            n.next.pre = n.pre;
            append(n);
            return;
        }

        if (map.size() == capacity ) {
            Node tmp = head.next;
            //remove
            head.next.pre = head;
            head.next = head.next.next;
            map.remove(tmp.key);

        }
    }

    private void append(Node n) {
        n.next = tail;
        n.pre = tail.pre;

        tail.pre.next = n;
        tail.pre = n;
    }
}

```
## 7. 大数据相关
### 7.1 如何对一个大文本进行按每行去重操作?
- 大数据相关面试题
    1. 给定a、b两个文件，各存放50亿个url，每个url各占64字节，内存限制是4G，让你找出a、b文件共同的url？ 
    方案1：可以估计每个文件安的大小为50G×64=320G，远远大于内存限制的4G。所以不可能将其完全加载到内存中处理。考虑采取分而治之的方法。 
    s 遍历文件a，对每个url求取 ，然后根据所取得的值将url分别存储到1000个小文件（记为 ）中。这样每个小文件的大约为300M。 
    s 遍历文件b，采取和a相同的方式将url分别存储到1000各小文件（记为 ）。这样处理后，所有可能相同的url都在对应的小文件（ ）中，不对应的小文件不可能有相同的url。然后我们只要求出1000对小文件中相同的url即可。 
    s 求每对小文件中相同的url时，可以把其中一个小文件的url存储到hash_set中。然后遍历另一个小文件的每个url，看其是否在刚才构建的hash_set中，如果是，那么就是共同的url，存到文件里面就可以了。 
    方案2：如果允许有一定的错误率，可以使用Bloom filter，4G内存大概可以表示340亿bit。将其中一个文件中的url使用Bloom filter映射为这340亿bit，然后挨个读取另外一个文件的url，检查是否与Bloom filter，如果是，那么该url应该是共同的url（注意会有一定的错误率）。 
  
    2. 有10个文件，每个文件1G，每个文件的每一行存放的都是用户的query，每个文件的query都可能重复。要求你按照query的频度排序。 
    方案1： 
    s 顺序读取10个文件，按照hash(query)%10的结果将query写入到另外10个文件（记为 ）中。这样新生成的文件每个的大小大约也1G（假设hash函数是随机的）。 
    s 找一台内存在2G左右的机器，依次对 用hash_map(query, query_count)来统计每个query出现的次数。利用快速/堆/归并排序按照出现次数进行排序。将排序好的query和对应的query_cout输出到文件中。这样得到了10个排好序的文件（记为 ）。 
    s 对 这10个文件进行归并排序（内排序与外排序相结合）。 
    方案2： 
    一般query的总量是有限的，只是重复的次数比较多而已，可能对于所有的query，一次性就可以加入到内存了。这样，我们就可以采用trie树/hash_map等直接来统计每个query出现的次数，然后按出现次数做快速/堆/归并排序就可以了。 
    方案3： 
    与方案1类似，但在做完hash，分成多个文件后，可以交给多个文件来处理，采用分布式的架构来处理（比如MapReduce），最后再进行合并。 
  
    3. 有一个1G大小的一个文件，里面每一行是一个词，词的大小不超过16字节，内存限制大小是1M。返回频数最高的100个词。 
    方案1：顺序读文件中，对于每个词x，取 ，然后按照该值存到5000个小文件（记为 ） 中。这样每个文件大概是200k左右。如果其中的有的文件超过了1M大小，还可以按照类似的方法继续往下分，知道分解得到的小文件的大小都不超过1M。对 每个小文件，统计每个文件中出现的词以及相应的频率（可以采用trie树/hash_map等），并取出出现频率最大的100个词（可以用含100个结点 的最小堆），并把100词及相应的频率存入文件，这样又得到了5000个文件。下一步就是把这5000个文件进行归并（类似与归并排序）的过程了。 
  
    4. 海量日志数据，提取出某日访问百度次数最多的那个IP。 
    方案1：首先是这一天，并且是访问百度的日志中的IP取出来，逐个写入到一个大文件中。注意到IP是32位的，最多有 个 IP。同样可以采用映射的方法，比如模1000，把整个大文件映射为1000个小文件，再找出每个小文中出现频率最大的IP（可以采用hash_map进 行频率统计，然后再找出频率最大的几个）及相应的频率。然后再在这1000个最大的IP中，找出那个频率最大的IP，即为所求。 
  
    5. 在2.5亿个整数中找出不重复的整数，内存不足以容纳这2.5亿个整数。 
    方案1：采用2-Bitmap（每个数分配2bit，00表示不存在，01表示出现一次，10表示多次，11无意义）进行，共需内存 内存，还可以接受。然后扫描这2.5亿个整数，查看Bitmap中相对应位，如果是00变01，01变10，10保持不变。所描完事后，查看bitmap，把对应位是01的整数输出即可。 
    方案2：也可采用上题类似的方法，进行划分小文件的方法。然后在小文件中找出不重复的整数，并排序。然后再进行归并，注意去除重复的元素。 
  
    6. 海量数据分布在100台电脑中，想个办法高校统计出这批数据的TOP10。 
    方案1： 
    s 在每台电脑上求出TOP10，可以采用包含10个元素的堆完成（TOP10小，用最大堆，TOP10大，用最小堆）。比如求TOP10大，我们首先取前 10个元素调整成最小堆，如果发现，然后扫描后面的数据，并与堆顶元素比较，如果比堆顶元素大，那么用该元素替换堆顶，然后再调整为最小堆。最后堆中的元 素就是TOP10大。 
    s 求出每台电脑上的TOP10后，然后把这100台电脑上的TOP10组合起来，共1000个数据，再利用上面类似的方法求出TOP10就可以了。 
  
    7. 怎么在海量数据中找出重复次数最多的一个？ 
    方案1：先做hash，然后求模映射为小文件，求出每个小文件中重复次数最多的一个，并记录重复次数。然后找出上一步求出的数据中重复次数最多的一个就是所求（具体参考前面的题）。 
  
    8. 上千万或上亿数据（有重复），统计其中出现次数最多的钱N个数据。 
    方案1：上千万或上亿的数据，现在的机器的内存应该能存下。所以考虑采用hash_map/搜索二叉树/红黑树等来进行统计次数。然后就是取出前N个出现次数最多的数据了，可以用第6题提到的堆机制完成。 
  
    9. 1000万字符串，其中有些是重复的，需要把重复的全部去掉，保留没有重复的字符串。请怎么设计和实现？ 
    方案1：这题用trie树比较合适，hash_map也应该能行。 
  
    10. 一个文本文件，大约有一万行，每行一个词，要求统计出其中最频繁出现的前10个词，请给出思想，给出时间复杂度分析。 
    方案1：这题是考虑时间效率。用trie树统计每个词出现的次数，时间复杂度是O(n*le)（le表示单词的平准长度）。然后是找出出现最频繁的 前10个词，可以用堆来实现，前面的题中已经讲到了，时间复杂度是O(n*lg10)。所以总的时间复杂度，是O(n*le)与O(n*lg10)中较大 的哪一个。 
  
    11. 一个文本文件，找出前10个经常出现的词，但这次文件比较长，说是上亿行或十亿行，总之无法一次读入内存，问最优解。 
    方案1：首先根据用hash并求模，将文件分解为多个小文件，对于单个文件利用上题的方法求出每个文件件中10个最常出现的词。然后再进行归并处理，找出最终的10个最常出现的词。 
  
    12. 100w个数中找出最大的100个数。 
    方案1：在前面的题中，我们已经提到了，用一个含100个元素的最小堆完成。复杂度为O(100w*lg100)。 
    方案2：采用快速排序的思想，每次分割之后只考虑比轴大的一部分，知道比轴大的一部分在比100多的时候，采用传统排序算法排序，取前100个。复杂度为O(100w*100)。 
    方案3：采用局部淘汰法。选取前100个元素，并排序，记为序列L。然后一次扫描剩余的元素x，与排好序的100个元素中最小的元素比，如果比这个 最小的要大，那么把这个最小的元素删除，并把x利用插入排序的思想，插入到序列L中。依次循环，知道扫描了所有的元素。复杂度为O(100w*100)。 
  
    13. 寻找热门查询： 
    搜索引擎会通过日志文件把用户每次检索使用的所有检索串都记录下来，每个查询串的长度为1-255字节。假设目前有一千万个记录，这些查询串的重复 读比较高，虽然总数是1千万，但是如果去除重复和，不超过3百万个。一个查询串的重复度越高，说明查询它的用户越多，也就越热门。请你统计最热门的10个 查询串，要求使用的内存不能超过1G。 
    (1) 请描述你解决这个问题的思路； 
    (2) 请给出主要的处理流程，算法，以及算法的复杂度。 
    方案1：采用trie树，关键字域存该查询串出现的次数，没有出现为0。最后用10个元素的最小推来对出现频率进行排序。 
  
    14. 一共有N个机器，每个机器上有N个数。每个机器最多存O(N)个数并对它们操作。如何找到 个数中的中数？ 
    方案1：先大体估计一下这些数的范围，比如这里假设这些数都是32位无符号整数（共有 个）。我们把0到 的整数划分为N个范围段，每个段包含 个整数。比如，第一个段位0到 ，第二段为 到 ，…，第N个段为 到 。 然后，扫描每个机器上的N个数，把属于第一个区段的数放到第一个机器上，属于第二个区段的数放到第二个机器上，…，属于第N个区段的数放到第N个机器上。 注意这个过程每个机器上存储的数应该是O(N)的。下面我们依次统计每个机器上数的个数，一次累加，直到找到第k个机器，在该机器上累加的数大于或等于 ，而在第k-1个机器上的累加数小于 ，并把这个数记为x。那么我们要找的中位数在第k个机器中，排在第 位。然后我们对第k个机器的数排序，并找出第 个数，即为所求的中位数。复杂度是 的。 
    方案2：先对每台机器上的数进行排序。排好序后，我们采用归并排序的思想，将这N个机器上的数归并起来得到最终的排序。找到第n个便是所求。复杂度是n(i)的。 
  
    15. 最大间隙问题 
    给定n个实数 ，求着n个实数在实轴上向量2个数之间的最大差值，要求线性的时间算法。 
    方案1：最先想到的方法就是先对这n个数据进行排序，然后一遍扫描即可确定相邻的最大间隙。但该方法不能满足线性时间的要求。故采取如下方法： 
    s 找到n个数据中最大和最小数据max和min。 
    s 用n-2个点等分区间[min, max]，即将[min, max]等分为n-1个区间（前闭后开区间），将这些区间看作桶，编号为 ，且桶 的上界和桶i+1的下届相同，即每个桶的大小相同。每个桶的大小为： 。实际上，这些桶的边界构成了一个等差数列（首项为min，公差为 ），且认为将min放入第一个桶，将max放入第n-1个桶。 
    s 将n个数放入n-1个桶中：将每个元素 分配到某个桶（编号为index），其中 ，并求出分到每个桶的最大最小数据。 
    s 最大间隙：除最大最小数据max和min以外的n-2个数据放入n-1个桶中，由抽屉原理可知至少有一个桶是空的，又因为每个桶的大小相同，所以最大间隙 不会在同一桶中出现，一定是某个桶的上界和气候某个桶的下界之间隙，且该量筒之间的桶（即便好在该连个便好之间的桶）一定是空桶。也就是说，最大间隙在桶 i的上界和桶j的下界之间产生 。一遍扫描即可完成。 
  
    16. 将多个集合合并成没有交集的集合：给定一个字符串的集合，格式如： 。要求将其中交集不为空的集合合并，要求合并完成的集合之间无交集，例如上例应输出 。 
    (1) 请描述你解决这个问题的思路； 
    (2) 给出主要的处理流程，算法，以及算法的复杂度； 
    (3) 请描述可能的改进。 
    方案1：采用并查集。首先所有的字符串都在单独的并查集中。然后依扫描每个集合，顺序合并将两个相邻元素合并。例如，对于 ， 首先查看aaa和bbb是否在同一个并查集中，如果不在，那么把它们所在的并查集合并，然后再看bbb和ccc是否在同一个并查集中，如果不在，那么也把 它们所在的并查集合并。接下来再扫描其他的集合，当所有的集合都扫描完了，并查集代表的集合便是所求。复杂度应该是O(NlgN)的。改进的话，首先可以 记录每个节点的根结点，改进查询。合并的时候，可以把大的和小的进行合，这样也减少复杂度。 
  
    17. 最大子序列与最大子矩阵问题 
    数组的最大子序列问题：给定一个数组，其中元素有正，也有负，找出其中一个连续子序列，使和最大。 
    方案1：这个问题可以动态规划的思想解决。设 表示以第i个元素 结尾的最大子序列，那么显然 。基于这一点可以很快用代码实现。 
    最大子矩阵问题：给定一个矩阵（二维数组），其中数据有大有小，请找一个子矩阵，使得子矩阵的和最大，并输出这个和。 
    方案1：可以采用与最大子序列类似的思想来解决。如果我们确定了选择第i列和第j列之间的元素，那么在这个范围内，其实就是一个最大子序列问题。如何确定第i列和第j列可以词用暴搜的方法进行。  
  

### 7.2 如何给100亿个数字排序?
给100亿个数字排序，100亿个 int 型数字放在文件里面大概有 37.2GB，非常大，内存一次装不下了。那么肯定是要拆分成小的文件一个一个来处理，最终在合并成一个排好序的大文件。
1. 把这个37GB的大文件，用哈希分成1000个小文件，每个小文件平均38MB左右（理想情况），把100亿个数字对1000取模，模出来的结果在0到999之间，每个结果对应一个文件，所以我这里取的哈希函数是 h = x % 1000，哈希函数取得"好"，能使冲突减小，结果分布均匀。
2. 拆分完了之后，得到一些几十MB的小文件，那么就可以放进内存里排序了，可以用快速排序，归并排序，堆排序等等。

3. 1000个小文件内部排好序之后，就要把这些内部有序的小文件，合并成一个大的文件，可以用二叉堆来做1000路合并的操作，每个小文件是一路，合并后的大文件仍然有序。

    - 首先遍历1000个文件，每个文件里面取第一个数字，组成 (数字, 文件号) 这样的组合加入到堆里（假设是从小到大排序，用小顶堆），遍历完后堆里有1000个 (数字，文件号) 这样的元素
    - 然后不断从堆顶拿元素出来，每拿出一个元素，把它的文件号读取出来，然后去对应的文件里，加一个元素进入堆，直到那个文件被读取完。拿出来的元素当然追加到最终结果的文件里。
    - 按照上面的操作，直到堆被取空了，此时最终结果文件里的全部数字就是有序的了。
