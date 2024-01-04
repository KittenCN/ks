# 3\. AP计算机2009年考试：多项选择  
Consider the following code segment.  
  
```Plain Text  
int value = 15;  
while (value < 28)  
{  
    System.out.println(value);  
    value++;  
}  
  
```  
What are the first and last numbers output by the code segment?    
  
 `15` `27`  
  
 `15` `28`  
  
 `16` `27`  
  
 `16` `28`  
  
 `16` `29`  
  
---  
A teacher put three bonus questions on a test and awarded 5 extra points to anyone who answered all three bonus questions correctly and no extra points otherwise. Assume that the `boolean` variables `bonusOne`, `bonusTwo`, and `bonusThree` indicate whether a student has answered the particular question correctly. Each variable was assigned `true` if the answer was correct and `false` if the answer was incorrect.  
  
Which of the following code segments will properly update the variable `grade` based on a student’s performance on the bonus questions?  
  
I.  
  
```Plain Text  
if (bonusOne && bonusTwo && bonusThree)  
    grade += 5;  
  
```  
II.  
  
```Plain Text  
if (bonusOne || bonusTwo || bonusThree)  
    grade += 5;  
  
```  
III.  
  
```Plain Text  
if (bonusOne)  
    grade += 5;  
if (bonusTwo)  
    grade += 5;  
if (bonusThree)  
    grade += 5;  
  
```  
 I only  
  
 II only  
  
 III only  
  
 I and III  
  
 II and III  
  
---  
Assume that an array of integer values has been declared as follows and has been initialized.  
  
```Plain Text  
int[] arr = new int[10];  
```  
Which of the following code segments correctly interchanges the value of `arr[0]` and `arr[5]`?    
  
  
  
`arr[0] = 5;`  
`arr[5] = 0;`  
  
  
  
`arr[0] = arr[5];`  
`arr[5] = arr[0];`  
  
  
  
`int k = arr[5];`  
`arr[0] = arr[5];`  
`arr[5] = k;`  
  
  
  
`int k = arr[0];`  
`arr[0] = arr[5];`  
`arr[5] = k;`  
  
  
  
`int k = arr[5];`  
`arr[5] = arr[0];`  
`arr[0] = arr[5];`  
  
---  
Consider the following code segment.  
  
```Plain Text  
ArrayList items = new ArrayList();  
items.add("A");  
items.add("B");  
items.add("C");  
items.add(0,"D");  
items.remove(3);  
items.add(0, "E");  
  
```  
What is printed as a result of executing the code segment?    
  
  
  
```Plain Text  
[A, B, C, E]  
```  
```Plain Text  
[A, B, D, E]  
```  
```Plain Text  
[E, D, A, B]  
```  
```Plain Text  
[E, D, A, C]  
```  
```Plain Text  
[E, D, C, B]  
```  
---  
When designing a class hierarchy, which of the following should be true of a superclass?    
  
 A superclass should contain the data and functionality that are common to all subclasses that inherit from the superclass.  
  
 A superclass should be the largest, most complex class from which all other subclasses are derived.  
  
 A superclass should contain the data and functionality that are only required for the most complex class.  
  
 A superclass should have public data in order to provide access for the entire class hierarchy.  
  
 A superclass should contain the most specific details of the class hierarchy.  
  
---  
```Plain Text  
int k = a random number such that 1 <= k <= n;  
  
for (int p = 2; p <= k; p++)  
    for (int r = 1; r < k; r++)  
        System.out.println("Hello");  
  
```  
What is the minimum number of times that `Hello` will be printed?    
  
  
  
```Plain Text  
0  
```  
```Plain Text  
1  
```  
```Plain Text  
2  
```  
```Plain Text  
n-1  
```  
```Plain Text  
n-2  
```  
---  
What is the maximum number of times that `Hello` will be printed?    
  
  
  
```Plain Text  
2  
```  
```Plain Text  
n - 1  
```  
```Plain Text  
n - 2  
```  
```Plain Text  
(n - 1) * (n - 1)  
```  
```Plain Text  
n * n  
```  
---  
Consider the following instance variable and incomplete method. The method `calcTotal` is intended to return the sum of all values in `vals`.  
  
```Plain Text  
private int[] vals;  
  
public int calcTotal()  
{  
    int total = 0;  
  
    /* missing code */  
  
    return total;  
}  
  
```  
Which of the code segments shown below can be used to replace /\* missing code \*/ so that `calcTotal` will work as intended?  
  
I.  
  
```Plain Text  
for (int pos = 0; pos < vals.length; pos++)  
{  
    total += vals[pos];  
}  
  
```  
II.  
  
```Plain Text  
for (int pos = vals.length; pos > 0; pos--)  
{  
    total += vals[pos];  
}  
  
```  
III.  
  
```Plain Text  
int pos = 0;  
while (pos < vals.length)  
{  
    total += vals[pos];  
    pos++;  
}  
  
```  
 I only  
  
 II only  
  
 III only  
  
 I and III  
  
 II and III  
  
---  
Consider the following code segment.  
  
```Plain Text  
String str = "abcdef";  
for (int rep = 0; rep < str.length() - 1; rep++)  
{  
    System.out.print(str.substring(rep, rep + 2));  
}  
  
```  
What is printed as a result of executing this code segment?    
  
  
  
```Plain Text  
abcdef  
```  
```Plain Text  
aabbccddeeff  
```  
```Plain Text  
abbccddeef  
```  
```Plain Text  
abcbcdcdedef  
```  
 Nothing is printed because an `IndexOutOfBoundsException` is thrown.  
  
---  
Consider the following method.  
  
```Plain Text  
public void numberCheck(int maxNum)  
{  
    int typeA = 0;  
    int typeB = 0;  
    int typeC = 0;  
  
    for (int k = 1; k <= maxNum; k++)  
    {  
        if (k % 2 == 0 && k % 5 == 0)  
            typeA++;  
        if (k % 2 == 0)  
            typeB++;  
        if (k % 5 == 0)  
            typeC++;  
    }  
  
    System.out.println(typeA + " " + typeB + " " + typeC);  
}  
  
```  
What is printed as a result of the call `numberCheck(50)`?    
  
 `5` `20` `5`  
  
 `5` `20` `10`  
  
 `5` `25` `5`  
  
 `5` `25` `10`  
  
 `30` `25` `10`  
  
---  
Consider the following method that is intended to modify its parameter `nameList` by replacing all occurrences of `name` with `newValue`.  
  
```Plain Text  
public void replace(ArrayList nameList,  
                String name, String newValue)  
{  
    for (int j = 0; j < nameList.size(); j++)  
    {  
        if ( /* expression */ )  
        {  
            nameList.set(j, newValue);  
        }  
    }  
}  
  
```  
Which of the following can be used to replace /\* expression \*/ so that `replace` will work as intended?    
  
  
  
```Plain Text  
nameList.get(j).equals(name)  
```  
```Plain Text  
nameList.get(j) == name  
```  
```Plain Text  
nameList.remove(j)  
```  
```Plain Text  
nameList[j] == name  
```  
```Plain Text  
nameList[j].equals(name)  
```  
---  
Consider the following incomplete method.  
  
```Plain Text  
public int someProcess(int n)  
{  
    /* body of someProcess */  
}  
  
```  
The following table shows several examples of input values and the results that should be produced by calling `someProcess`.  
  
|Input Value `n`|Value Returned by `someProcess(n)`|  
| ----- | ----- |  
|3|30|  
|6|60|  
|7|7|  
|8|80|  
|9|90|  
|11|11|  
|12|120|  
|14|14|  
|16|160|  
  
Which of the following code segments could be used to replace /\* body of someProcess \*/ so that method will produce the results shown in the table?  
  
I.  
  
```Plain Text  
if ((n % 3 == 0) && (n % 4 == 0))  
    return n * 10;  
else  
    return n;  
  
```  
II.  
  
```Plain Text  
if ((n % 3 == 0) || (n % 4 == 0))  
    return n * 10;  
  
return n;  
  
```  
III.  
  
```Plain Text  
if (n % 3 == 0)  
    if (n % 4 == 0)  
        return n * 10;  
  
return n;  
  
```  
 I only  
  
 II only  
  
 III only  
  
 I and III  
  
 II and III  
  
---  
Consider the following method.  
  
```Plain Text  
// precondition: x >= 0  
public void mystery(int x)  
{  
    if ((x / 10) != 0)  
    {  
        mystery(x / 10);  
    }  
  
    System.out.print(x % 10);  
}  
  
```  
Which of the following is printed as a result of the call `mystery(123456)`?    
  
  
  
```Plain Text  
16  
```  
```Plain Text  
56  
```  
```Plain Text  
123456  
```  
```Plain Text  
654321  
```  
 Many digits are printed due to infinite recursion  
  
---  
Consider the following instance variables and incomplete method that are part of a class that represents an item. The variables `years` and `months` are used to represent the age of the item, and the value for `months` is always between `0` and `11`, inclusive. Method `updateAge` is used to update these variables based on the parameter `extraMonths` that represents the number of months to be added to the age.  
  
```Plain Text  
private int years;  
private int months; // 0 <= months <= 11  
  
// precondition: extraMonths >= 0  
public void updateAge(int extraMonths)  
{  
    /* body of updateAge */  
}  
  
```  
Which of the following code segments could be used to replace /\* body of updateAge \*/ so that the method will work as intended?  
  
I.  
  
```Plain Text  
int yrs = extraMonths % 12;  
int mos = extraMonths / 12;  
  
years = years + yrs;  
month = months + mos;  
  
```  
II.  
  
```Plain Text  
int totalMonths = years * 12 + months + extraMonths;  
years = totalMonths / 12;  
months = totalMonths % 12;  
  
```  
III.  
  
```Plain Text  
int totalMonths = months + extraMonths;  
years = years + totalMonths / 12;  
months = totalMonths % 12;  
  
```  
 I only  
  
 II only  
  
 III only  
  
 II and III only  
  
 I, II, and III  
  
---  
Consider the following method.  
  
```Plain Text  
public String inRangeMessage(int value)  
{  
    if (value < 0 || value > 100)  
        return "Not in range";  
    else  
        return "In range";  
}  
  
```  
Consider the following code segments that could be used to replace the body of `inRangeMessage`.  
  
I.  
  
```Plain Text  
if (value < 0)  
{  
    if (value > 100)  
        return "Not in range";  
    else  
        return "In range";  
}  
else  
    return "In range";  
  
```  
II.  
  
```Plain Text  
if (value < 0)  
    return "Not in range";  
else if (value > 100)  
    return "Not in range";  
else  
    return "In range";  
  
```  
III.  
  
```Plain Text  
if (value >= 0)  
    return "In range";  
else if (value <= 100)  
    return "In range";  
else  
    return "Not in range";  
  
```  
Which of the replacements will have the same behavior as the original version of `inRangeMessage`?  
  
 I only  
  
 II only  
  
 III only  
  
 I and III  
  
 II and III  
  
---  
Consider the following class declaration.  
  
```Plain Text  
public class SomeClass  
{  
    private int num;  
  
    public SomeClass(int n)  
    {  
        num = n;  
    }  
  
    public void increment(int more)  
    {  
        num = num + more;  
    }  
  
    public int getNum()  
    {  
        return num;  
    }  
}  
  
```  
The following code segment appears in another class.  
  
```Plain Text  
SomeClass one = new SomeClass(100);  
SomeClass two = new SomeClass(100);  
SomeClass three = one;  
  
one.increment(200);  
  
System.out.println(one.getNum() + " " + two.getNum() + " " +  
                three.getNum());  
  
```  
What is printed as a result of executing the code segment?  
  
  
  
```Plain Text  
100 100 100  
```  
```Plain Text  
300 100 100  
```  
```Plain Text  
300 100 300  
```  
```Plain Text  
300 300 100  
```  
```Plain Text  
300 300 300  
```  
---  
The following incomplete method is intended to sort its array parameter `arr` in increasing order.  
  
```Plain Text  
// postcondition: arr is sorted in increasing order  
public static void sortArray(int[] arr)  
{  
    int j, k;  
  
    for (j = arr.length - 1; j > 0; j--)  
    {  
        int pos = j;  
  
        for ( /* missing code */ )  
        {  
            if (arr[k] > arr[pos])  
            {  
                pos = k;  
            }  
        }  
        swap(arr, j, pos);  
    }  
}  
  
```  
Assume that `swap(arr, j, pos)` exchange the values of `arr[j]` and `arr[pos]`. Which of the following could be used to replace /\* missing code \*/ so that executing the code segment sorts the values in array `arr`?  
  
  
  
```Plain Text  
k = j - 1; k > 0; k--  
```  
```Plain Text  
k = j - 1; k >= 0; k--  
```  
```Plain Text  
k = 1; k < arr.length; k++  
```  
```Plain Text  
k = 1; k > arr.length; k++  
```  
```Plain Text  
k = 0; k <= arr.length; k++  
```  
---  
Assume that `x` and `y` are boolean variables and have been properly initialized.  
  
```Plain Text  
(x && y) || !(x && y)  
```  
The result of evaluating the expression above is best described as  
  
 always `true`  
  
 always `false`  
  
 `true` only when `x` is `true` and `y` is `true`  
  
 `true` only when `x` and `y` have the same value  
  
 `true` only when `x` and `y` have different values  
  
---  
Assume that the following variable declarations have been made.  
  
`double d = Math.random();`  
`double r;`  
  
Which of the following assigns a value to `r` from the uniform distribution over the range `0.5 <= r < 5.5`?  
  
  
  
```Plain Text  
r = d + 0.5;  
```  
```Plain Text  
r = d + 0.5 * 5.0;  
```  
```Plain Text  
r = d * 5.0;  
```  
```Plain Text  
r = d * 5.0 + 0.5;  
```  
```Plain Text  
r = d * 5.5;  
```  
---  
Consider the following instance variables and method that appear in a class representing student information.  
  
```Plain Text  
private int assignmentsCompleted;  
private double testAverage;  
  
public boolean isPassing()  
{ /* implementation not shown */ }  
  
```  
A student can pass a programming course if at least one of the following conditions is met.  
  
* The student has a test average that is greater than or equal to 90.  
* The student has a test average that is greater than or equal to 75 and has at least 4 completed assignments.  
  
Consider the following proposed implementations of the `isPassing` method.  
  
I.  
  
```Plain Text  
if (testAverage >= 90)  
    return true;  
if (testAverage >= 75 && assignmentsCompleted >= 4)  
    return true;  
return false;  
  
```  
II.  
  
```Plain Text  
boolean pass = false;  
if (testAverage >= 90)  
    pass = true;  
if (testAverage >= 75 && assignmentsCompleted >= 4)  
    pass = true;  
return pass;  
  
```  
III.  
  
```Plain Text  
return (testAverage >= 90) ||  
        (testAverage >= 75 && assignmentsCompleted >= 4);  
  
```  
Which of the implementations will correctly implement method `isPassing`?  
  
 I only  
  
 II only  
  
 I and III only  
  
 II and III only  
  
 I, II, and III  
  
---  
**21-25题涉及当前已被移出考试范围的GridWorld case study。**  
  
Consider the following code segment.  
  
```Plain Text  
int k = 0;  
while (k < 10)  
{  
    System.out.print((k % 3) + " ");  
    if ((k % 3) == 0)  
        k = k + 2;  
    else  
        k++;  
}  
  
```  
What is printed as a result of executing the code segment?  
  
  
  
```Plain Text  
0 2 1 0 2  
```  
```Plain Text  
0 2 0 2 0 2  
```  
```Plain Text  
0 2 1 0 2 1 0  
```  
```Plain Text  
0 2 0 2 0 2 0  
```  
```Plain Text  
0 1 2 1 2 1 2  
```  
---  
Consider the following method. Method `allEven` is intended to return `true` if all elements in array `arr` are even numbers; otherwise, it should return `false`.  
  
```Plain Text  
public boolean allEven(int[] arr)  
{  
    boolean isEven = /* expression */;  
  
    for (int k = 0; k < arr.length; k++)  
    {  
        /* loop body */  
    }  
  
    return isEven;  
}  
  
```  
Which of the following replacements for /\* expression \*/ and /\* loop body \*/ should be used so that method `allEven` will work as intended?  
  
 `false` `if ((arr[k] % 2) == 0)isEven = true;`  
  
 `false` `if ((arr[k] % 2) != 0)isEven = false; else isEven = true;`  
  
 `true` `if ((arr[k] % 2) != 0)isEven = false;`  
  
 `true` `if ((arr[k] % 2) != 0)isEven = false; else isEven = true;`  
  
 `true` `if ((arr[k] % 2) == 0)isEven = false; else isEven = true;`  
  
---  
Consider the following code segment.  
  
```Plain Text  
int x = /* some integer value */;  
int y = /* some integer value */;  
  
boolean result = (x < y);  
  
result = ( (x >= y) && !result );  
  
```  
Which of the following best describes the conditions under which the value of `result` will be `true` after the code segment is executed?  
  
 Only when `x < y`  
  
 Only when `x >= y`  
  
 Only when `x` and `y` are equal  
  
 The value will always be `true`  
  
 The value will never be `true`  
  
---  
Consider the following code segment.  
  
```Plain Text  
for (int outer = 0; outer < n; outer++)  
{  
    for (int inner = 0; inner <= outer; inner++)  
    {  
        System.out.print(outer + " ");  
    }  
}  
  
```  
if `n` has been declared as an integer with the value 4, what is printed as a result of executing the code segment?  
  
  
  
```Plain Text  
0 1 2 3  
```  
```Plain Text  
0 0 1 0 1 2  
```  
```Plain Text  
0 1 2 2 3 3 3  
```  
```Plain Text  
0 1 1 2 2 2 3 3 3 3  
```  
```Plain Text  
0 0 1 0 1 2 0 1 2 3  
```  
---  
Consider the following class declarations.  
  
```Plain Text  
public class Base  
{  
    private int myVal;  
  
    public Base()  
    { myVal = 0; }  
  
    public Base(int x)  
    { myVal = x; }  
}  
  
public class Sub extends Base  
{  
    public Sub()  
    { super(0); }  
}  
  
```  
Which of the following statements will NOT compile?  
  
  
  
```Plain Text  
Base b1 = new Base();  
```  
```Plain Text  
Base b2 = new Base(5);  
```  
```Plain Text  
Base s1 = new Sub();  
```  
```Plain Text  
Sub s2 = new Sub();  
```  
```Plain Text  
Sub s3 = new Sub(5);  
```  
---  
Assume that `a` and `b` are variables of type `int`. The expression  
  
```Plain Text  
!(a < b) && !(a > b)  
```  
is equivalent to which of the following?  
  
  
  
```Plain Text  
true  
```  
```Plain Text  
false  
```  
```Plain Text  
a == b  
```  
```Plain Text  
a != b  
```  
```Plain Text  
!(a < b) && (a > b)  
```  
---  
Consider the following code segment.  
  
```Plain Text  
int a = 24;  
int b = 30;  
while (b != 0)  
{  
    int r = a % b;  
    a = b;  
    b = r;  
}  
  
System.out.println(a);  
  
```  
What is printed as a result of executing the code segment?  
  
  
  
```Plain Text  
0  
```  
```Plain Text  
6  
```  
```Plain Text  
12  
```  
```Plain Text  
24  
```  
```Plain Text  
30  
```  
---  
Consider the following method.  
  
```Plain Text  
public int sol(int lim)  
{  
    int s = 0;  
  
    for (int outer = 1; outer <= lim; outer++)  
    {  
        for (int inner = outer; inner <= lim; inner++)  
        {  
            s++;  
        }  
    }  
  
    return s;  
}  
  
```  
What values is returned as a result of the call `sol(10)`?  
  
  
  
```Plain Text  
20  
```  
```Plain Text  
45  
```  
```Plain Text  
55  
```  
```Plain Text  
100  
```  
```Plain Text  
385  
```  
---  
Consider the following incomplete method. Method `findNext` is intended to return the index of the first occurrence of the value `val` beyond the position `start` in array `arr`.  
  
```Plain Text  
// returns index of first occurrence of val in arr  
// after position start;  
// returns arr.length if val is not found  
public int findNext(int[] arr, int val, int start)  
{  
    int pos = start + 1;  
  
    while ( /* condition */ )  
        pos++;  
  
    return pos;  
}  
  
```  
For example, consider the following code segment.  
  
`int[] arr = {11, 22, 100, 33, 100, 11, 44, 100};`  
`System.out.println(findNext(arr, 100, 2));`  
  
The execution of the code segment should result in the value 4 being printed.  
  
Which of the following expressions could be used to replace /\* condition \*/ so that `findNext` will work as intended?  
  
  
  
```Plain Text  
(pos < arr.length) && (arr[pos] != val)  
```  
```Plain Text  
(arr[pos] != val) && (pos < arr.length)  
```  
```Plain Text  
(pos < arr.length) || (arr[pos] != val)  
```  
```Plain Text  
(arr[pos] == val) && (pos < arr.length)  
```  
```Plain Text  
(pos < arr.length) || (arr[pos] == val)  
```  
---  
Consider the following code segments.  
  
I.  
  
```Plain Text  
int k = 1;  
while (k < 20)  
{  
    if (k % 3 == 1)  
        System.out.print(k + " ");  
  
    k = k + 3;  
}  
  
```  
II.  
  
```Plain Text  
for (int k = 1; k < 20; k++)  
{  
    if (k % 3 == 1)  
        System.out.print(k + " ");  
}  
  
```  
III.  
  
```Plain Text  
for (int k = 1; k < 20; k = k + 3)  
{  
    System.out.print(k + " ");  
}  
  
```  
Which of the code segments above will produce the following output?  
`1 4 7 10 13 16 19`  
  
 I only  
  
 II only  
  
 I and II only  
  
 II and III only  
  
 I, II, and III  
  
---  
Consider the following two methods that appear within a single class.  
  
```Plain Text  
public void changeIt(int[] list, int num)  
{  
    list = new int[5];  
    num = 0;  
  
    for (int x = 0; x < list.length; x++)  
        list[x] = 0;  
}  
  
public void start()  
{  
    int[] nums = {1, 2, 3, 4, 5};  
    int value = 6;  
  
    changeIt(nums, value);  
  
    for (int k = 0; k < nums.length; k++)  
        System.out.print(nums[k] + " ");  
  
    System.out.print(value);  
}  
  
```  
What is printed as a result of the call `start()`?  
  
  
  
```Plain Text  
0 0 0 0 0 0  
```  
```Plain Text  
0 0 0 0 0 6  
```  
```Plain Text  
1 2 3 4 5 6  
```  
```Plain Text  
1 2 3 4 5 0  
```  
 “changeIt“ will throw an exception.  
  
---  
Consider the following declaration of the class `NumSequence`, which has a constructor that is intended to initialize the instance variable `seq` to an `ArrayList` of `numberOfValues` random floating-point values in the range \[0.0, 1.0).  
  
```Plain Text  
public class NumSequence  
{  
    private ArrayList seq;  
  
    // precondition: numberOfValues > 0  
    // postcondition: seq has been initialized to an ArrayList of  
    //                length numberOfValues; each element of seq  
    //                contains a random Double in the range [0.0, 1.0)  
    public NumSequence(int numberOfValues)  
    {  
        /* missing code */  
    }  
}  
  
```  
Which of the following code segments could be used to replace /\* missing code \*/ so that the constructor will work as intended?  
  
I.  
  
```Plain Text  
ArrayList seq = new ArrayList();  
for (int k = 0; k < numberOfValues; k++)  
    seq.add(new Double(Math.random()));  
  
```  
II.  
  
```Plain Text  
seq = new ArrayList();  
for (int k = 0; k < numberOfValues; k++)  
    seq.add(new Double(Math.random()));  
  
```  
III.  
  
```Plain Text  
ArrayList temp = new ArrayList();  
for (int k = 0; k < numberOfValues; k++)  
    seq.add(new Double(Math.random()));  
  
seq = temp;  
  
```  
 II only  
  
 III only  
  
 I and II  
  
 I and III  
  
 II and III  
  
---  
Consider the following code segment.  
  
```Plain Text  
double a = 1.1;  
double b = 1.2;  
  
if ((a + b) * (a - b) != (a * a) - (b * b))  
{  
    System.out.println("Mathematical error!");  
}  
  
```  
Which of the following best describes why the phrase `"Mathematical error!"` would be printed? (Remember that mathematically (a+b)∗(a−b)=a^2−b^2.)  
  
 Precedence rules make the `if` condition true.  
  
 Associativity rules make the `if` condition true.  
  
 Roundoff error makes the `if` condition true.  
  
 Overflow makes the `if` condition true.  
  
 A compiler bug or hardware error has occurred.  
  
---  
Consider the following recursive method.  
  
```Plain Text  
public static String recur(int val)  
{  
    String dig = " " + (val % 3);  
  
    if (val / 3 > 0)  
        return dig + recur(val / 3);  
  
    return dig;  
}  
  
```  
What is printed as a result of executing the following statement?  
`System.out.println(recur(32));`  
  
  
  
```Plain Text  
20  
```  
```Plain Text  
102  
```  
```Plain Text  
210  
```  
```Plain Text  
1020  
```  
```Plain Text  
2101  
```  
---  
Consider the following method.  
  
```Plain Text  
public String goAgain(String str, int index)  
{  
    if (index >= str.length())  
        return str;  
  
    return str + goAgain(str.substring(index), index + 1);  
}  
  
```  
What is printed as a result of executing the following statement?  
`System.out.println(goAgain("today", 1));`  
  
  
  
```Plain Text  
today  
```  
```Plain Text  
todayto  
```  
```Plain Text  
todayoday  
```  
```Plain Text  
todayodayay  
```  
```Plain Text  
todayodaydayayy  
```  
