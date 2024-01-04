# AP计算机科学Java子集
AP Java子集揭示了那些可能出现在AP Computer Science A考试中的Java特性。AP Java子集并非为限定计算机科学课程的内容而设——子集往往需要经过额外补充后才能涵盖典型的导论课纲的全部主题。例如，输入与输出必须是计算机编程课的一部分，但Java本身有许多处理输入和输出的方式。由于这种多变性，输入与输出的细节（使用`System.out.print`与`System.out.println`的基本文本输出例外）并不在AP考试中考察。  
  
本文说明了应试学生需要了解的Java子集。一些超纲但可能与计算机导论课相关的特性也有所提及。AP Java子集中排除的特性并不意味我们判断此种特性不重要或无价值。  
  
我们精心选择了AP Java子集来  
  
1. 令出题人能够编撰有意义的试题。  
2. 帮助学生备考。  
3. 令教师能够在此基础上开发不同的教学方式来教好AP计算机科学课程。  
  
为帮助学生备考，AP Java子集有意只包括较小的内容。不能带来重要功能或在编撰试题时可以用子集中其他机制替代的语言结构和库功能都在AP Java子集中略去了。  

AP Java子集就教师如何在课程中使用Java给出了较大的灵活度。例如，有些课程讲述如何使用streams或readers/writers来进行输入输出，另一些课程教授图形用户界面的构造，还有一些课程则依赖于专门的输入输出工具或库。对于AP考试而言，这些选择是有一定随意性的，对问题解决过程或掌握计算机科学概念也不重要。因此AP Java子集完全不涉及对于用户输入的处理。当然，这也意味着子集本身并不完备。为了完成实际的程序，教师还需在他们的课程中引入额外的机制。  
  
## 考试范围  
### 注释(Comments)  
`/* */`、`//`、`/** */`  
Javadoc `@param`与`@return`注释标签  
  
### 基本数据类型(Primitive Types)  
`int`  
`double`  
`boolean`  
  
### 运算符(Operators)  
算数：`+`、`-`、`*`、`/`、`%`  
自增自减：`++`、`--`  
赋值：`=`、`+=`、`-=`、`*=`、`/=`、`%=`  
关系：`==`、`!=`、`<`、`<=`、`>`、`>=`  
逻辑：`!`、`&&`、`||`  
类型转换：`(int)`、`(double)`  
字符串连接：`+`  
  
* 需要理解运算符优先级。  
* 自增和自减的值本身不被使用，而仅用到操作符的效果。仅使用后缀(`x++`)形式，运算符也不在其他表达式(`arr[x++]`)中使用。  
* 需要理解`&&`与`||`运算符的[短路求值](https://en.wikipedia.org/wiki/Short-circuit_evaluation)。  
* 需要理解将浮点数转换成整数时会直接把小数部分截去，但对正浮点数使用`(int)(x + 0.5)`、负浮点数使用`(int)(x - 0.5)`可以得到通常的四舍五入效果。  
* 需要理解`+`作为字符串连接操作符的特性，以及当连接字符串和非字符串对象时对于`toString`方法的调用。  
  
### 对象比较(Object Comparison)  
地址相等(`==`, `!=`)与内容相等(`equals`)  
`String CompareTo`  
  
### 转义字符(Escape Sequences)  
`\"`、`\\`、`\n`  
  
### 输入输出(Input / Output)  
`System.out.print`  
`System.out.println`  
  
* 用户输入并不包括在AP Java子集中。实践中有不少获取用户输入的方式，如通过`Scanner`读取输入，通过流从文件或者网址读取输入或从对话框输入。每种方法都各有其利弊。考试并不依赖于任何特定方法，相对而言，如果试题中一定要有输入的部分，会用`double x = /* 调用读取一个浮点数的方法 */;`或`double x = ...; //读取用户输入`。  
  
### 异常(Exceptions)  
`ArithmeticException`、`NullPointerException`、`IndexOutOfBoundsException`、`ArrayIndexOutOfBoundsException`、`IllegalArgumentException`  
  
### 数组(Arrays)  
一维数组  
二维数组，每行的元素数目相当  
初始化数组元素`{...}`  
二维数组同行元素储存在一起  
  
* 基本数据类型(`int[]`, `int[][]`)和对象(`Student[]`, `Student[][]`)的数组都会涉及。  
* 需要理解二维数组是以数组的数组这种形式存储的。对AP计算机科学考试而言，学生们可以认为二维数组每行的元素数目相当且同行元素储存在一起。例如对于`int[][] m = {{1, 2, 3}, {4, 5, 6}}`，`m.length`即行数为2，`m[0].length`即列数为3，`m[r][c]`表示第r行第c列的元素，`m[r]`表示第r行，是一个储存该行所有列元素的数组，类型为`int[]`。  
需要读取二维数组的行并将其赋值到一维数组、将其作为方法的参数传递或在循环里（包括for-each）遍历所有行。但不要求将二维数组的一整行替换掉。  
  
### 控制语句(Control Statements)  
`if`、`if/else`  
`while`、`for`  
`for(... : ...)`  
`return`  
  
### 变量(Variables)  
参数变量  
局部变量  
可见性(`private`)  
`static`：可见性(`public`, `private`)、`final`  
  
### 方法(Methods)  
可见性(`public`, `private`)  
`static`  
方法签名  
重载、重写  
参数传递  
  
* 不要求`main`方法和命令行参数。在主观题中没有对程序调用的要求。在AP计算机实验中的程序可能会出现对于`main`方法的调用，但`main`方法会尽可能的简单。  
* 要求理解`static`方法的适用范围。在考试中`static`方法总是显式或隐式的通过类来调用，而非通过对象来调用（即`ClassName.staticMethod()`或`staticMethod()`而非`obj.staticMethod()`）。  
  
### 构造器(Constructor)  
`super()`、`super(args)`  
  
* 如果子类的构造器没有显式调用父类的构造器。编译器则会自动添加一个对于父类无参数构造器的调用。  
* 要求实现对所有实例变量初始化的构造器。类中的常数则像这样直接初始化`public static final int MAX_SCORE = 5;`。不要求了解默认初始化的规则、直接初始化实例变量或初始化块。  
  
### 类(Classes)  
`new`  
可见性(`public`)  
用于读取的方法  
用于修改的方法  
设计、创建、修改类  
由父类创建子类  
~~抽象类~~~~abstract~~  
~~用类实现接口~~  
  
2020年开始，不再考查抽象类和接口`interface`。  
  
### 继承(Inheritance)  
理解继承层次关系  
设计、创建、修改子类  
  
### 包(Packages)  
```Plain Text
import packageName.className
```  
### 次要的面向对象内容(Miscellaneous OOP)  
继承(is-a)关系与组成(has-a)关系  
`null`  
`this`  
`super.method(args)`  
  
* 需要理解由子类到父类的转换是合法的，无需强制类型转换。强制类型转换不包含在AP Java子集中。数组类型兼容性以及数组间的强制转换亦不要求。  
* `this`的使用仅限于作为隐式参数的用法。不要求作为区分同名实例变量与参数变量的用法。  
  
### 标准Java库(Standard Java Library)  
`Object`  
`Integer`、`Double`  
`String`  
`Math`  
`List`、`ArrayList`  
  
* AP Java子集要求使用通用集合类和接口，但不要求学生实现通用类或方法。  
* 需要了解快速参考中列出的隶属Java标准库类与接口中的常数与方法。  
  
## 超纲但有用  
### 注释(Comments)  
Javadoc工具  
  
### 基本数据类型(Primitive Types)  
`char`、`byte`、`short`、`long`、`float`  
  
### 运算符(Operators)  
逻辑：`&`、`|`、`^`  
类型转换：`(char)`、`(float)`  
字符串连接：`StringBuilder`  
位移：`<<`、`>>`、`>>>`  
位运算：`~`、`&`、`|`、`^`  
条件：`?:`  
  
### 对象比较(Object Comparison)  
`equals`的实现  
`Comparable`  
  
### 转义字符(Escape Sequences)  
`\'`、`\t`、`\unnnn`  
  
### 输入输出(Input / Output)  
`Scanner`、`System.in`  
`System.out`、`System.err`  
`Stream`输入输出  
图形界面输入输出  
读取数目：`Integer.parseInt`、`Double.parseDouble`  
格式化输出：`System.out.printf`  
  
### 异常(Exceptions)  
`try/catch/finally`  
`throw`、`throws`  
`assert`  
  
### 数组(Arrays)  
`new type[]{...}`  
每行的元素数目不等的数组  
三维及高维数组  
  
### 控制语句(Control Statements)  
`switch`  
`break`、`continue`  
`do-while`  
  
### 变量(Variables)  
`final`参数变量  
`final`局部变量  
`final`成员变量  
  
### 方法(Methods)  
可见性(`protected`)  
`public static void main(String[] args)`  
命令行参数  
可变数量的参数  
`final`  
  
### 构造器(Constructor)  
实例变量的默认初始化  
初始化块  
`this(args)`  
  
### 类(Classes)  
`final`  
可见性(`private`, `protected`)  
嵌套类  
内部类  
枚举  
  
### 包(Packages)  
`import packageName.*`  
`static import`  
`package packageName`  
类的路径  
  
### 次要的面向对象内容(Miscellaneous OOP)  
`instanceof`  
`(class)`强制类型转换  
`this.var`、`this.method(args)`  
  
### 标准Java库(Standard Java Library)  
`clone`  
自动装箱  
`Collection`  
`Arrays`、`Collections`  