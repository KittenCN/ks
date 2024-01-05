# AP Computer Science A 学习笔记  
## Java 语法  
(1) 布尔值叫 `boolean`，只能是 `true` 或 `false`，没有非 `0` 即 `true` 的概念。`boolean` 不能强转 `int`，实在要转可以用三目运算符。`if (...)` 里面只能是布尔值。  
  
(2) `int` 可以自动转 `double`，`double` 不能自动转 `int`，如：  
  
```java  
int x = 3;  
double d = x; // 可以  
x = d; // ERROR  
x = (int)d; // 可以。强转：丢弃小数部分  
```  
(3) `int` 型的范围是$[-2^{31}, 2^{31} - 1]​$ 。可以用 `Integer.MIN_VALUE`$-2^{31}​$ 和 `Integer.MAX_VALUE`$2^{31} - 1​$ 来查看。  
  
(4) 常量叫 `final`，类似于 C++的 `const`。  
  
(5) 可以小数模小数。如：`4.2 % 1.5` 结果是 `1.2`。  
  
  
  
## 类与对象（Classes and Objects）  
(1) AP 中，类全部都是 `public` 的。  
  
(2) AP 中，类里只有两种变量，一种是 `private`，一种是 `public static`。常量一般是 `public static final`。`public` 的数据都可以在类外面直接访问，`private` 的数据只能借助类里的方法（method）访问。`static` 的数据只会被创建一次，是所有实例（instances）**共用**的，例如可以当计数器来用，记录这个类一共被创建过多少个实例。  
  
(3) AP 中，类里只有三种方法：`private`，`public`，和 `public static`。`public static` 方法不针对任何实例，不能访问任何非 `static` 的变量（因为你不知道访问哪个对象的），也不能调用任何非 `static` 的方法（instance method）。如果有 `main` 函数，它必须是 `static` 的，且它所在类里的所有方法也必须是 `static` 的。AP 中认为 `static` 的方法只能用 `类名.方法名` 的形式访问，**不能用 ****实例名.方法名**** 的形式访问**。  
  
(4) constructor 前面必须写 `public`，如：  
  
```java  
public class Cat {  
    public Cat() {}  
}  
```  
(5) method overloading：同一个类中，多个方法名字相同，参数不同。注意，必须是参数不同，而不是返回值不同。事实上返回值可以相同也可以不同，与此处无关。  
  
(6) `this` 表示当前对象。在非 `static` 的方法（包括 constructor）里，非 `static` 的数据和方法前都可以加 `this.`。如：  
  
```java  
public class Rational {  
    private int num;  
    private int denom;  
    public Rational(int num, int denom) {  
        this.num = num;  
        this.denom = denom; // 变量重名时，可以用 this 来区分局部变量和类的数据  
    }  
}  
  
```  
(7) `int`, `double`, `boolean` 是基本类型，其他的对象和数组都是 reference 类型，如：`String`, `int[]`, `String[][]`, `Cat`（我们自己定义的）等。  
  
(8) 局部变量没有初始化会**在编译时就报错**（compile-time error）。类和数组里的数据如果不初始化，JavaJava 会自动将其赋为默认值，`int` 等的默认值是 `0`，`boolean` 的默认值是 `false`，reference 的默认值是 `null`（注意：`String` 的默认值也是 `null`，而不是空串）。  
  
(9) 传参时，如果传的是基本类型，则是一份传过去，无论方法里如何操作，外面的实参不会改变。如果传的是 reference 类型，则把指针一份，此时是**两根指针指向同一个对象**。实参的地址不变，内容有可能改变。  
  
  
  
## 继承与多态（Inheritance and Polymorphism）  
(1) 每个类只能有一个父类。多个类可以有同一个父类。可以多层继承，最后形成一个树形结构。  
  
(2) A 继承 B（A 是 subclass，B 是 superclass），则逻辑上需要满足“A **is a** B”的关系。比如：an `Employee` is a `Person`，a `Student` is a `Person`，a `GradStudent` is a `Student`。否则即使有这种需要，在 AP 考试里也认为不能用继承，比如说下面这段代码就被认为是错的：  
  
```java  
public class Tire extends Circle {  
    ...  
    // inherits methods that compute circumference and center point  
}  
  
```  
官方答案说，tire 是一个汽车部件，而 circle 是一个几何图形，所以不能说 tire is a circle。  
  
(3) 子类继承父类的所有 `public` 的变量和方法，**不继承** `private` 的变量和方法，但可以通过父类的 `public` 方法间接访问。（AP 中不考虑 `protected`）。  
  
(4) 子类的变量如果和从父类继承的变量重名，则在子类里默认该名字指子类里的变量，如果要访问父类的变量可以用 `super.xxx`。子类里这个变量是 `public` 还是 `private` 都没关系。  
  
(5) 子类可以重写从父类继承的方法，称为 method overriding（区分于 method overloading）。在重写时可以调用父类的同一方法，用法是 `super.xxx()`，称为 partial overriding。父类的 `private` 方法是不能被 overridden 的，因为它们根本没有被继承。所以总结来说就是：进行 overriding 时，**父类和子类里的这个方法都必须是 ****public**** 的**。此外，在 overriding 中，子类方法和父类方法的**返回值类型必须相同**，否则就不是 overriding。如果子类里有一个方法，和父类继承来的方法名字相同、参数类型相同，但返回值类型不同，会发生编译错误。  
  
(6) constructor 不继承。子类的 constructor 里，第一句话应先写 `super(...);`，即调用父类的 constructor。\*\*`super` 只能写在第一句话里\*\*。如果不写，JavaJava 默认帮你写一个 `super();`，此时如果父类里没有 default constructor（不带变量的 constructor），会发生编译错误。如果父类一个 consturctor 都没有，JavaJava 会帮你写一个 default constructor，那么此时还是可以调用 `super();` 的。如果子类一个 consturctor 都没有，JavaJava​ 会帮你写一个 default constructor，里面只有一句话，就是：`super();`。也就是说，如果父类和子类都没有 constructor，不会发生编译错误。  
  
(7) **父类 reference 可以指向子类对象**，反过来不可以。例如：  
  
```java  
// Student 是父类，GradStudent 和 UnderGrad 是子类。  
Student s = new Student();     // 正确  
Student g = new GradStudent(); // 正确  
Student u = new UnderGrad();   // 正确  
GradStudent g = new Student(); // 错误  
  
```  
当父类 reference 指向子类对象时，这个对象（这个 reference）**只能调用父类里有的方法**。但是**如果这个方法被重写过，调用的是重写后的版本**（也就是子类里的版本）。也就是说，某个方法能不能调用，取决于 the type of object reference（左边的），这是在编译时决定的；调用的具体是什么，取决于 the type of actual object（右边的），这是在运行时决定的。这种特性就被称为多态。注意，只有 overriding 会导致多态，也就是在运行是决定用哪个（也叫 dynamic binding 或 late binding）；overloading 不是多态，因为在编译时就决定好了（也叫 static binding 或 early binding）。  
  
关于多态有什么用，可以看下面这份代码：  
  
```java  
Student s = null;  
Student u = new UnderGrad(...);  
Student g = new GradStudent(...);  
String str = ...; // read user input  
if (str.equals("G")) {  
    s = g;  
} else if (str.equals("U")) {  
    s = u;  
} else {  
    s = new Student();  
}  
s.computeGrade(); // 在运行时才知道具体调用的是哪个  
  
```  
(8) 如果子类对象调用了某个被 partial overridden 的函数，通过函数里的 `super.xxx();` 回到了父类，在父类的这个函数里继续调用另一个被 overridden 过的函数，此时调用的还是子类里的。如：  
  
```java  
public class Dancer {  
    public void act() {  
        System.out.println("spin");  
        doTrick();  
    }  
    public void doTrick() {  
        System.out.println("float");  
    }  
}  
public class Acrobat extends Dancer {  
    public void act() {  
        super.act(); // partial overriding  
        System.out.println("flip");  
    }  
    public void doTrick() {  
        System.out.println("somersault");  
    }  
}  
  
---main()---  
Dancer a = new Acrobat();  
a.act();  
  
```  
该程序输出的结果是：  
  
```java  
spin  
somersault  
flip  
  
```  
(9) 在父类 reference 指向子类对象时，不能调用只在子类里有的方法，如果非要调用，则需要进行 casting。具体写法如下：  
  
```java  
// getID() 是一个只在 GradStudent 里有的方法，父类 Student 里没有  
Student s = new GradStudent();  
int x = s.getID(); // 错误  
int x = ((GradStudent)s).getID(); // casting，正确的  
int x = (GradStudent)s.getID(); // 错误，点的优先级比 casting 高  
  
```  
(10) 向方法传参时，规则和赋值是类似的。必须满足“实参 is a 形参”的关系。如果形参是父类，直接传就可以；如果形参是子类，实参是父类 reference 指向子类对象，那么需要 casting。  
  
  
  
## 一些标准类  
### `Object` 类  
(1) JavaJava​ 中，如果没有定义父类，则默认继承 `Object`。也就是说，所有继承关系是一棵树（而不是一个森林），`Object` 是这棵树的根节点。  
  
(2) `public String toString()` 是 `Object` 类的一个方法，它返回一个形如 `类名@地址` 的字符串，其中地址看上去就是一串无规则的字符。需要时，可以自己 override `toString` 方法。使用 `System.out.print(xxx)` 时，会调用该对象 `xxx` 的 `toString` 方法。当某个对象和字符串拼接时，也会调用该对象的 `toString` 方法，如 `"abc" + xxx` 就相当于 `"abc" + xxx.toString()`。当然，也可以自己主动调用 `toString`。  
  
(3) `public boolean equals(Object other)` 是 `Object` 类的一个方法。它判断 `other` 和当前对象是否是**同一个对象**。注意，“同一个对象”指的是指向同一块内存区域，而不仅仅是内容相同。JavaJava 中 `==` 也是判断两者是否是同一个对象。所以未被 overridden 时，`equals` 和 `==` 意思一样。例如：  
  
```java  
Date d1 = new Date("June", 4, 1989);  
Date d2 = d1; // 两个 reference 指向同一个对象  
Date d3 = new Date("June", 4, 1989);  
  
boolean b1 = d1.equals(d2); // true  
boolean b2 = d1.equals(d3); // false，虽然内容相同，但不是同一个对象  
boolean b3 = (d1 == d2);    // true  
boolean b4 = (d1 == d3);    // false  
  
```  
### `String` 类  
(1) `String` 是 JavaJava​ 自带的类。直接在代码里打出来的字符串，如 `"AvavaAva"`，被称为 string literals，它们都是 `String` 的实例。`String s = "abc";` 等价于 `String s = new String("abc");`。  
  
(2) `String` 对象是 **immutable** 的，也就是说一旦被创建，就不能更改。但是可以 **reassign a ****String**** reference**，如：  
  
```java  
String s = "Diana";  
s = "Ava";  
s = s + " is your father?!";  
System.out.print(s); // Ava is your father?!  
  
```  
注意，上面的代码中，`"Diana"` 和 `"Ava"` 没有被改变，它们只是被直接丢弃了。  
  
因为 `String` 是 immutable 的，所以 `String.xxx()` 这种方法都不会改变原串，只是返回一个新串。考试时可能给你一个你没见过的方法，比如 `s.toUpperCase();`，此时你要知道 `s` 里的内容没有被改变。只有 `s = s.toUpperCase();` 这样才会把 `s` 换掉。  
  
(3) 注意区分空指针（`null`）和空串（`""`）。如果 `String s` 是某个类的数据且未被初始化，那么默认是空指针，等价于初始化 `s = null;`。`s = new String();` 得到的是空串，等价于 `s = "";`。**空指针也是可以被打印的**，`s = null; System.out.print(s);` 会输出 `null`。  
  
(4) 字符串 `+`：`+` 左右两边只要有任意一边是 `String` 类型的，就会自动调用另一边的 `toString` 方法。如：  
  
```java  
int x = 3, y = 4;  
String s1 = x + y + "abc"; // 7abc  
String s2 = x + (y + "abc"); // 34abc  
String s3 = x + y; // ERROR，不能把 int 赋给 String  
  
```  
(5) `String` 类的 `equals` 方法被 overridden 过，比较两个串内容是否一样。`==` 仍然是判断是否是同一个对象。`s1.compareTo(s2)` 返回一个 `int`，若 `s1` 字典序较小则返回负数，若 `s1` 字典序较大则返回正数，若两串相等返回 `0`。ASCII 码的大小顺序是**数字 << 大写字母 <<​ 小写字母**。假设 `s1` 不为空指针，`s2` 为空指针，那么 `s1.equals(s2)` 和 `s1 == s2` 能正常执行并返回 `false`，`s1.compareTo(s2)` 则会发生 `NullPointerException`。  
  
(6) **所有相同的 string literals 是同一个对象**，所以用 `==` 比较时也是相同的。例如：  
  
```java  
String s1 = "ray";  
String s2 = "ray";  
String s3 = new String("ray");  
  
boolean b1 = (s1 == s2);    // true  
boolean b2 = (s1 == s3);    // false  
boolean b3 = s1.equals(s3); // true  
  
```  
(7) `length()`：返回字符串长度。  
  
(8) `substring(l, r)`：返回左闭右开区间 $[l, r)$ 的子串，要求$0\leq l\leq r \leq \texttt{s.length()}$  。其中$l = r$   时返回空串。也可以只传一个参数 `l`，此时默认 `r = s.length()`。  
  
(9) `indexOf(s)`：传进去一个字符串 `s`，返回该串里 `s` 第一次出现的位置（开头位置）。若该串里没有 `s` 则返回 `-1`。  
  
### 封装类（Wrapper Classes）  
(1) 把基本类型 `int`, `double` 封装成对象类型 `Integer` 和 `Double`。示意代码如下：  
  
```java  
public class Integer {  
    public static final int MAX_VALUE = 2147483647;  
    public static final int MIN_VALUE = -2147483648;  
    private int x;  
    public Integer(int _x) { x = _x; }  // boxing  
    public int intValue() { return x; } // unboxing  
    public String toString() { return "" + x; }  
    // ... 还有很多其他方法 AP 中不考  
}  
  
public class Double {  
    double x;  
    public Double(double _x) { x = _x; }      // boxing  
    public double doubleValue() { return x; } // unboxing  
    // ...  
}  
  
```  
(2) `Integer` 和 `Double` 都是 immutable 的。也就是说，这两个类都没有提供 `public void setValue(int x)` 这样的方法。同时，因为它是 immutable 的，如果直接赋值，它会被存在常量池里，**相同的值只创建一个对象**，类似于 string literals。  
  
(3) autoboxing and unboxing。需要注意的是，**当 ****==**** 两边都是封装类时，不发生 auto unboxing**。看例子：  
  
```java  
Integer x = 3; // autoboxing  
  
...f(Integer x) { ... }  
f(5); // autoboxing  
  
Integer x = 5;  
int y = x; // auto unboxing  
  
...f(int x) { ... }  
f(new Integer(5)); // auto unboxing  
  
public int giveMeFive() {  
    return new Integer(5); // auto unboxing  
}  
  
int a = 3;  
Integer A = 3;  
Integer B = 3;  
Integer C = new Integer(3);  
Integer D = 4;  
boolean b1 = (a == A); // true，auto unboxing，相当于 (a == A.intValue())  
boolean b2 = (A == B); // true，并没有发生 auto unboxing，而是因为相同的值在常量池里只创建一个对象，所以 A 和 B 就是一个对象  
boolean b3 = (A == C); // false，没有发生 auto unboxing，A 和 C 不是同一个对象  
boolean b4 = (A.intValue() == C.intValue()); // true，手动 unboxing  
boolean b5 = (A < D); // true，auto unboxing  
  
```  
(4) 在 Java 里 `int` 可以自动被转成 `double`。如 `int x = 1; double y = x;` 是可以通过编译的。同时，`double` 可以自动被转成 `Double`，也就是所谓的 autoboxing，例如 `Double x = 23.33;`。但是，`int` 不能被自动转成 `Double`。如 `Double x = 1;` 就会编译错误，必须改成 `Double x = 1.0;`。  
  
### `Math` 类  
(1) `static int abs(int x)` 和 `static double abs(double x)`：绝对值。  
  
(2) `static double pow(double base, double exp)`：求 $\texttt{base} ^ {\texttt{exp}}$。  
  
(3) `static double sqrt(double x)`：开根。  
  
(4) `static double random()`：返回一个 $[0, 1)$ 的随机小数。一般地，如果需要一个 $[l, r]$ 之间的整数，则调用 `(int)(Math.random() * (r - l + 1)) + l`。  
  
## 数组，Array List，和二维数组  
### 数组（Array)  
(1) 数组的定义：`int[] a = new int[10];`，或者 `int[] a; a = new int[10]`。也可以同时定义多个 Array：`int[] a = new int[10], b = new int[20];`。你可以理解成，`int[]` 是一种特殊的类型（不过，还有一种语法：`int a[] = new int[10];`，它是不符合我们的理解的，所以也不推荐使用）。`a` 是一个 reference，指向一个 `int[]` 类型的对象，也就是一个数组。数组可以静态初始化，例如：`int[] a = {2, 3, 3};`。数组长度不能变，里面的内容可以变。  
  
(2) 和其他 reference 一样，数组无论是在哪里定义的，都会被默认初始化。需要注意的是，如果数组里装的是 reference 类型（比如 `String` 或其他自己定义的类），那么每个位置上被初始化为了 `null`，此时还是不能直接使用的，需要逐个 `new` 出来。  
  
(3) 通过 `a.length` 获得数组长度。注意，数组中 `length` 是数据，不是方法，不加括号。  
  
(4) 有一种不通过下标遍历数组的方法，叫 foreach。以 `int` 类型的数组 `a` 为例：`for(int x: a) { ... }`，就相当于 `for(int i = 0; i < a.length; ++i) {int x = a[i]; ... }`。这里 `x` 相当于一个局部变量，**对 ****x**** 做的所有改变不会影响到数组**。如果数组里装的是 reference，用 foreach 时**可以通过调用这个对象的方法对它进行修改（数组里的对象会同时被修改），但如果令这个 reference 指向另一个对象，则不会影响数组**（简称数组里的对象能读，能改，不能换）。  
  
```java  
ArrayList  
```  
(1) 可以变长的数组。  
  
(2) **只能装对象**。例如 `ArrayList<int>` 是错的，需改成 `ArrayList<Integer>`。使用时会发生 autoboxing 和 auto unboxing，因此效率不如数组。  
  
(3) 定义：`ArrayList<String> a = new ArrayList<String>();`。其中 `<String>` 这个用法被称为泛型（generic），其实就是 C++中的模板。  
  
(4) 下标范围和数组一样，foreach 用法和数组一样。  
  
(5) 通过 `a.size()` 获得长度，相当于数组的 `.length`。  
  
总结一下：  
  
```java  
String s = ...;  
int n = s.length();  
  
int[] a = ...;  
int n = a.length;  
  
ArrayList<Integer> a = ...;  
int n = a.size();  
  
```  
(6) 如果要按下标访问，那么不能用 `[i]`，而需要调用方法：`get(i)` 或者 `set(i, obj)`。`set` 会返回原来该位置上的元素。  
  
(7) `boolean add(T obj)`：在最后加入一个元素 `obj`（`T` 表示元素类型，下同），返回 `true`。  
  
(8) `void add(int i, T obj)`：把元素 `obj` 插入到下标 `i`，后面的元素依次右移。$0\leq i\leq \texttt{a.size()}$ ，注意 `i` 可以等于 `a.size()`，也就是插入到最后。  
  
(9) `T remove(int i)` 把位置 `i` 上的元素删除并将它返回。  
  
(10) 数组没有 override `toString()` 方法，`ArrayList` override 过。所以只有 `ArrayList` 可以用 `System.out.print()` 打印出来，形如 `[2, 3, 3]`。  
  
### 二维数组  
(1) 定义：`int[][] a = new int[10][10]`。也可以先 `int[][] a = new int [10][]`，再逐行定义。每一行长度可以不一样。**每一行是一个独立的数组**（`a[i]` 里存的是这个数组的 reference），不同行之间内存不连续，可以通过对 reference 操作，对某两行进行交换，或者对某一行进行整体替换。  
  
(2) 对第一维用 foreach：`for(int[] row: a)`。此时的 `row` 是一个 reference，满足前面说过的“能读，能改，不能换”。至于二维数组里的每个对象能不能换，只取决于内层循环是不是 foreach，和外层循环无关。  
  
## 算法  
(1) random shuffle：  
  
```java  
int[] a = ...;  
for (int i = a.length - 1; i > 0; --i) {  
    int j = (int)(Math.random() * (i + 1)); // [0, i]。注意，包括 i  
    // swap(a[i], a[j])  
    int tmp = a[i];  
    a[i] = a[j];  
    a[j] = tmp;  
}  
  
```  
(2) AP 里的选择排序，是不额外开一个答案数组的，而是**直接在原数组上 ****swap****。所以它是不稳定的（例如你考虑数组 ****{2, 2, 1}****）。AP 不考察排序算法的稳定性，但是要理解后面元素的顺序是会被打乱的，考试时问你第 k​ 轮以后的序列，最好手动模拟一下。另外，AP 里每轮一般是先找好最小的位置再最后 ****swap**** 一次**，而不是每找到一个更小的元素就 `swap` 一下。  
  
(3) AP 里的插入排序也是不额外开数组的，通过把当前元素向前依次交换来实现（有点像冒泡）。当然，归并排序还是必须额外开数组的。  
  
(4) 选择排序的比较次数和交换次数都是一定的$\frac{n(n - 1)}{2}$  和 $n - 1$ 。插入排序不一定，顺序时最优$（n−1 和 0）$ ，恰好反序时最差（$\frac{n(n - 1)}{2}$  和 $\frac{n(n - 1)}{2}$ ）。在数组较为有序时，插入排序的比较次数小于选择排序，交换次数不一定。  
  
(5) 二分查找（找到某一元素或告知不存在，假设该元素唯一）的最坏情况比较次数：$\lfloor\log_2(n)\rfloor + 1$ 。其中 +1 是因为即使在只剩一个元素时，也要比较一下是不是要找的元素。有些题目保证要找的元素一定存在（比如猜数游戏），就不需要这个 +1了。可以用归纳法证明该结论。  
