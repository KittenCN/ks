---
description: CoderFAN 资料库 CSA 历史真题
---

# 4\. AP计算机2008年练习卷：多项选择  
Consider the following method.  
  
```java  
public static int mystery(int[] arr)  
{  
    int x = 0;  
  
    for (int k = 0; k < arr.length; k = k + 2)  
        x = x + arr[k];  
  
    return x;  
}  
```  
Assume that the array nums has been declared and initialized as follows.  
  
```java  
int[] nums = {3, 6, 1, 0, 1, 4, 2};  
  
```  
What value will be returned as a result of the call `mystery(nums)`?  
  
  
  
```java  
5  
```  
```java  
6  
```  
```java  
7  
```  
```java  
10  
```  
```java  
17  
```  
---  
Consider the following partial Class declaration.  
  
```java  
public class SomeClass  
{  
    private int myA;  
    private int myB;  
    private int myC;  
  
    // Constructor(s) not shown  
  
    public int getA()  
    { return myA; }  
  
    public void setB(int value)  
    { myB = value; }  
}  
```  
The following declaration appears in another Class.  
  
```java  
SomeClass obj = new SomeClass();  
```  
Which of the following code segments will compile without error?  
  
  
  
```java  
int x = obj.getA();  
  
```  
```java  
int x;  
obj.getA(x);  
  
```  
```java  
int x = obj.myA;  
  
```  
```java  
int x = SomeClass.getA();  
  
```  
```java  
int x getA;(obj)  
```  
---  
Which of the following Changes to `SomeClass` will allow other Classes to access but not modify the value of `myC`?  
  
 Make `myC` public.    
  
 Include the method:  
`public int getC()   {return myC;}   `  
  
 Include the method:  
`private int getC()   {return myC;}   `  
  
 Include the method:  
`public void getC(int x)   {x = myC;}   `  
  
 Include the method:  
`private void getC(int x)   {x = myC;}`  
  
---  
Consider the following code segment.  
  
```java  
int x = 7;  
int y = 3;  
  
if ((x < 10) && (y < 0))  
    System.out.println("Value is: " + x * y);  
else  
    System.out.println("Value is: " + x / y);  
```  
What is printed as a result of executing the code segment?  
  
  
  
```java  
Value is: 21  
  
```  
```java  
Value is: 2.3333333  
  
```  
```java  
Value is: 2  
  
```  
```java  
Value is: 0  
  
```  
```java  
Value is: 1  
```  
---  
Consider the following method.  
  
```java  
public ArrayList<Integer> mystery(int n)  
{  
    ArrayList<Integer> seq = new ArrayList<Integer>();  
  
    for (int k = l; k <= n; k++)  
        seq.add(new Integer(k * k + 3));  
  
    return seq;  
}  
```  
Which of the following is printed as a result of executing the following statement?  
  
```java  
System.out.println(mystery(6));  
```  
```java  
[3, 4, 7, 12, 19, 28]  
  
```  
```java  
[3, 4, 7, 12, 19, 28, 39]  
  
```  
```java  
[4, 7, 12, 19, 28, 39]  
  
```  
```java  
[39, 28, 19, 12, 7, 4]  
  
```  
```java  
[39, 28, 19, 12, 7, 4, 3]  
```  
---  
Consider the following method that is intended to determine if the `double` values `d1` and `d2` are close enough to be considered equal. For example, given a `tolerance` of `0.001`, the values `54.32271` and `54.32294` would be considered equal.  
  
```java  
/** @return true if d1 and d2 are within the specified tolerance,  
* false otherwise  
*/  
  
public boolean almostEqual(double d1, double d2, double tolerance)  
  
{  
    /* missing code */  
}  
```  
Which of the following should replace `/* missing code */` so that `almostEqual` will work as intended?  
  
  
  
```java  
return (d1 - d2) <= tolerance;  
  
```  
```java  
return ((dl + d2) / 2) <= tolerance;  
  
```  
```java  
return (d1 - d2) >= tolerance;  
  
```  
```java  
return ((dl + d2) / 2) >= tolerance;  
  
```  
```java  
return Math.abs(dl - d2) <= tolerance;  
```  
---  
Consider the following class declaration.  
  
```java  
public class Person  
{  
    private String myName;  
    private int myYearOfBirth;  
  
    public Person(String name, int yearOfBirth)  
    {  
        myName = name;  
        myYearOfBirth = yearOfBirth;  
    }  
  
    public String getName()  
    { return myName; }  
  
    public void setName(String name)  
    { myName = name; }  
  
    // There may be instance variables, constructors, and methods that are not shown.  
  
}  
```  
Assume that the following declaration has been made.  
  
```java  
Person student = new Person("Thomas", 1995);  
  
```  
Which of the following statements is the most appropriate for changing the name of `student` from `"Thomas"` to `"Tom"`?  
  
  
  
```java  
student = new Person("Tom", 1995);  
  
```  
```java  
student.myName = "Tom";  
  
```  
```java  
student.getName("Tom");  
  
```  
```java  
student.setName("Tom");  
  
```  
```java  
Person.setName("Tom");  
```  
---  
Consider the following class declaration.  
  
```java  
public class Student  
{  
    private String myName;  
    private int myAge;  
  
    public Student()  
    { /* implementation not shown */ }  
  
    public Student(String name, int age)  
    { /* implementation not shown */ }  
  
    // No other constructors  
}  
```  
Which of the following declarations will compile without error?  
  
I. `Student a = new Student();`  
II. `Student b = new Student("Juan", 15);`  
III. `Student c = new Student("Juan", "15");`  
  
 I only  
  
 II only  
  
 I and II only  
  
 I and III only  
  
 I, II, and III  
  
---  
Consider the following method that is intended to return the sum of the elements in the array `key`.  
  
```java  
public static int sumArray(int[] key)  
{  
    int sum = O;  
    for (int i = 1; i <= key.length; i++)  
    {  
        /* missing code */  
    }  
    return sum;  
}  
```  
Which of the following statements should be used to replace `/* missing code */` so that `sumArray` will work as intended?  
  
  
  
```java  
sum = key[i];  
  
```  
```java  
sum += key[i - 1];  
  
```  
```java  
sum += key[i];  
  
```  
```java  
sum += sum + key[i - 1];  
  
```  
```java  
sum += sum + key[i];  
```  
---  
Consider the following instance variable and methods. You may assume that `data` has been initialized with length > 0. The methods are intended to return the index of an array element equal to `target`, or `-1` if no such element exists.  
  
```java  
private int[] data;  
public int seqSearchRec(int target)  
{  
    return seqSearchRecHelper(target, data.length - 1);  
}  
  
private int seqSearchRecHelper(int target, int last)  
{  
    // Line 1  
  
    if (data[last] == target)  
        return last;  
    else  
        return seqSearchRecHelper(target, last - 1);  
}  
```  
For which of the following test cases will the call `seqSearchRec(5)` always result in an error?  
  
I. `data` contains only one element.  
II. `data` does not contain the value 5.  
III. `data` contains the value 5 multiple times.  
  
 I only  
  
 II only  
  
 III only  
  
 I and II only  
  
 I, II, and III  
  
---  
Which of the following should be used to replace `// Line 1` in `seqSearchRecHelper` so that `seqSearchRec` will work as intended?  
  
  
  
```java  
if (last <= 0)return -1;  
  
```  
```java  
if (last < 0)return -1;  
  
```  
```java  
if (last < data.length)return -1;  
  
```  
```java  
while (last < data.length)  
  
```  
```java  
while (last >= 0)  
```  
---  
Consider the following method.  
  
```java  
public String mystery(String input)  
{  
    String output = "";  
  
    for (int k = 1; k < input.length(); k = k + 2)  
    {  
        output += input.substring(k, k + 1);  
    }  
  
    return output;  
}  
```  
What is returned as a result of the call `mystery("computer")`?  
  
  
  
```java  
"computer"  
```  
```java  
"cmue"  
```  
```java  
"optr"  
```  
```java  
"ompute"  
```  
 Nothing is returned because an `IndexOutOfBoundsException` is thrown.  
  
---  
Consider the following code segment.  
  
```java  
int[] arr = {7, 2, 5, 3, 0, 10};  
for (int k = 0, k < arr.length - 1; k++)  
{  
    if (arr[k] > arr[k + 1])  
        System.out.print(k + " " + arr[k] + " ");  
}  
```  
What will be printed as a result of executing the code segment?  
  
  
  
```java  
0 2 2 3 3 0  
  
```  
```java  
0 7 2 5 3 3  
  
```  
```java  
0 7 2 5 5 10  
  
```  
```java  
1 7 3 5 4 3  
  
```  
```java  
7 2 5 3 3 0  
```  
---  
Consider the following interface and class declarations.  
  
```java  
public interface Vehicle  
{  
    /** @return the mileage traveled by this Vehicle  
    */  
    double getMileage();  
}  
  
public class Fleet  
{  
    private ArrayList<Vehicle> myVehiCles;  
  
    /** @return the mileage traveled by all vehicles in this Fleet  
    */  
    public double getTotalMileage()  
    {  
        double sum = 0.0;  
  
        for (Vehicle v : myVehicles)  
        {  
            sum += /* expression */ ;  
        }  
  
        return sum;  
    }  
  
    // There may be instance variables, constructors, and methods that are not shown.  
}  
```  
Which of the following can be used to replace `/* expression */` so that `getTotalMileage` returns the total of the miles traveled for all vehicles in the fleet?  
  
  
  
```java  
getMileage(v)  
  
```  
```java  
myVehicles[v].getMileage()  
  
```  
```java  
Vehicle.get(v).getMileage()  
  
```  
```java  
myVehicles.get(v).getMileage()  
  
```  
```java  
v.getMileage()  
```  
---  
Consider the following method, `isSorted`, which is intended to return `true` if an array of integers is sorted in nondecreasing order and to return `false` otherwise.  
  
```java  
/** @param data an array of integers  
* @return true if the values in the array appear in sorted (nondecreasing) order  
*/  
public static boolean isSorted(int[] data)  
{  
    /* missing code */  
}  
```  
Which of the following can be used to replace `/* missing code */` so that isSorted will work as intended?  
  
I.  
  
```java  
for (int k = 1; k < data.length; k++)  
{  
    if (data[k - 1] > data[k])  
        return false;  
}  
return true;  
```  
II.  
  
```java  
for (int k = 0; k < data.length; k++)  
{  
    if (data[k] > data[k + 1])  
        return false;  
}  
return true;  
```  
III.  
  
```java  
for (int k = 0; k < data.length - 1; k++)  
{  
    if (data[k] > data[k + 1])  
        return false;  
    else  
        return true;  
}  
return true;  
```  
 I only  
  
 II only  
  
 III only  
  
 I and II only  
  
 I and III only  
  
---  
Consider the following incomplete method that is intended to return an array that contains the contents of its first array parameter followed by the contents of its second array parameter.  
  
```java  
public static int[] append(int[] a1, int[] a2)  
{  
    int[] result = new int[a1.length + a2.length];  
  
    for (int j = 0; j < a1.length; j++)  
        result[j] = a1[j];  
    for (int k = 0; k < a2.length; k++)  
        result[ /* index */ ] = a2[k];  
  
    return result;  
}  
```  
Which of the following expressions can be used to replace `/* index */` so that `append` will work as intended?  
  
  
  
```java  
j  
```  
```java  
k  
```  
```java  
k + a1.length - 1  
```  
```java  
k + a1.length  
```  
```java  
k + a1.length + 1  
```  
---  
Consider the following code segment.  
  
```java  
int[] arr = {1, 2, 3, 4, 5, 6, 7};  
  
for (int k = 3; k < arr.length - 1; k++)  
    arr[k] = arr[k + 1];  
```  
Which of the following represents the contents of `arr` as a result of executing the code segment?  
  
  
  
```java  
{1, 2, 3, 4, 5, 6, 7}  
```  
```java  
{1, 2, 3, 5, 6, 7}  
```  
```java  
{1, 2, 3, 5, 6, 7, 7}  
```  
```java  
{1, 2, 3, 5, 6, 7, 8}  
```  
```java  
{2, 3, 4, 5, 6, 7, 7}  
```  
---  
Assume that `myList` is an `ArrayList` that has been correctly constructed and populated with objects. Which of the following expressions produces a valid random index for myList?  
  
  
  
```java  
(int)(Math.random() * myList.size()) - 1  
```  
```java  
(int)(Math.random() * myList.size())  
```  
```java  
(int)(Math.random() * myList.size()) + 1  
```  
```java  
(int)(Math.random() * (myList.size() + 1))  
```  
```java  
Math.random(myList.size())  
```  
---  
Assume that `a` and `b` have been defined and initialized as `int` values. The expression  
  
```java  
!(!(a != b) && (b > 7))  
  
```  
is equivalent to which of the following?  
  
  
  
```java  
(a != b) || (b < 7)  
```  
```java  
(a != b) || (b <= 7)  
```  
```java  
(a == b) || (b <= 7)  
```  
```java  
(a != b) && (b <= 7)  
```  
```java  
(a == b) && (b > 7)  
```  
---  
Consider the following method.  
  
```java  
public static void arrayMethod(int nums[])  
{  
    int j = 0;  
    int k = nums.length — 1;  
  
    while (j < k)  
    {  
        int x = nums[j];  
        nums[j] = nums[k];  
        nums[k] = x;  
        j++;  
        k--;  
    }  
}  
```  
Which of the following describes what the method `arrayMethod()` does to the array `nums`?  
  
 The array `nums` is unchanged.  
  
 The first value in `nums` is copied to every location in the array.  
  
 The last value in `nums` is copied to every location in the array.  
  
 The method generates an `ArrayIndexOutOfBoundsException`.  
  
 The contents of the array `nums` are reversed.  
  
---  
**21-25题涉及当前已被移出考试范围的GridWorld case study。**  
  
Assume that the array `arr` has been defined and initialized as follows.  
  
```java  
int[] arr = /* initial values for the array */ ;  
  
```  
Which of the following will correctly print all of the odd integers contained in `arr` but none of the even integers contained in `arr`?  
  
 `for (int x : arr)if (x % 2 == 1)System.out.println(x);`    
  
 `for (int k = 1; k < arr.length; k++)if (arr[k] % 2 == 1)System.out.println(arr[k]);`    
  
 `for (int x : arr)if (x % 2 == 1)System.out.println(arr[x]);`    
  
 `for (int k = 0; k < arr.length; k++)if (arr[k] % 2 == 1)System.out.println(k);`    
  
 `for (int x : arr)if (arr[x] % 2 == 1)System.out.println(arr[x]);`    
  
---  
```java  
public static int mystery(int n)  
{  
    int x = 1;  
    int y = 1;  
  
    // Point A  
  
    while (n > 2)  
    {  
        x = x + y;  
  
        // Point B  
  
        y = x - y;  
        n--;  
    }  
  
    // Point C  
  
    return x;  
}  
```  
What value is returned as a result of the call `mystery(6)`?  
  
  
  
```java  
1  
```  
```java  
5  
```  
```java  
6  
```  
```java  
8  
```  
```java  
13  
```  
---  
Which of the following is true of method `mystery`?  
  
 `x` will sometimes be `1` at `// Point B`.    
  
 `x` will never be `1` at `// Point C`.    
  
 `n` will never be greater than `2` at `// Point A`.    
  
 `n` will sometimes be greater than `2` at `// Point C`.    
  
 `n` will always be greater than `2` at `// Point B`.    
  
---  
Consider the following code segment.  
  
```java  
for (int k = 1; k <= 100; k++)  
    if ((k % 4) == 0)  
        System.out.println(k);  
```  
Which of the following code segments will produce the same output as the code segment above?  
  
 `for (int k = 1; k <= 25; k++)System.out.println(k);`    
  
 `for (int k = 1; k <= 100; k = k + 4)System.out.println(k);`    
  
 `for (int k = 1; k <= 100; k++)System.out.println(k % 4);`    
  
 `for (int k = 4; k <= 25; k = 4 * k)System.out.println(k);`    
  
 `for (int k = 4; k <= 100; k = k + 4)System.out.println(k);`    
  
---  
Consider the following method.  
  
```java  
public static String scramble(String word, int howFar)  
{  
    return word.substring(howFar + 1, word.length()) +  
        word.substring(0, howFar);  
}  
```  
What value is returned as a result of the call `scramble("compiler", 3)`?  
  
  
  
```java  
"compiler"  
```  
```java  
"pilercom"  
```  
```java  
"ilercom"  
```  
```java  
"ilercomp"  
```  
 No value is returned because an `IndexOutOfBoundsException` will be thrown.  
  
---  
Consider the following method.  
  
```java  
public void mystery(int[] data)  
{  
    for (int k = 0; k < data.length - 1; k++)  
        data[k + 1] = data[k] + data[k + 1];  
}  
```  
The following code segment appears in another method in the same class.  
  
```java  
int[] values = {5, 2, 1, 3, 8};  
mystery(values);  
for (int v : values)  
    System.out.print(v + " ");  
System.out.println();  
```  
What is printed as a result of executing the code segment?  
  
  
  
```java  
5 2 1 3 8  
```  
```java  
5 7 3 4 11  
```  
```java  
5 7 8 11 19  
```  
```java  
7 3 4 11 8  
```  
 Nothing is printed because an `ArrayIndexOutOfBoundsException` is thrown during the execution of method `mystery`.  
  
---  
Consider the following method.  
  
```java  
public int compute(int n, int k)  
{  
    int answer = 1;  
  
    for (int i = 1; i <= k; i++)  
        answer *= n;  
  
    return answer;  
}  
```  
Which of the following represents the value returned as a result of the call `compute(n, k)`?  
  
 nk  
  
 n!  
  
 nk  
  
 2k  
  
 kn  
  
---  
Consider the following code segment.  
  
```java  
int sum = 0;  
int k = 1;  
while (sum < 12 || k < 4)  
    sum += k;  
  
System.out.println(sum);  
```  
What is printed as a result of executing the code segment?  
  
  
  
```java  
6  
```  
```java  
10  
```  
```java  
12  
```  
```java  
15  
```  
 Nothing is printed due to an infinite loop.  
  
---  
Consider the following class declarations.  
  
```java  
public class Point  
{  
    private double x; // x-coordinate  
    private double y; // y-coordinate  
  
    public Point()  
    {  
        x = 0;  
        y = 0;  
    }  
  
    public Point(double a, double b)  
    {  
        x = a;  
        y = b;  
    }  
  
    // There may be instance variables, constructors, and methods that are not shown.  
}  
  
public class Circle  
{  
    private Point center;  
    private double radius;  
  
    /** Constructs a circle where (a, b) is the center and r is the radius.  
    */  
    public Circle(double a, double b, double r)  
    {  
        /* missing code */  
    }  
}  
```  
Which of the following replacements for `/* missing code */` will correctly implement the `Circle` constructor?  
  
I.  
  
```java  
center = new Point();  
radius = r;  
  
```  
II.  
  
```java  
center = new Point(a, b);  
radius = r;  
  
```  
III.  
  
```java  
center = new Point();  
center.x = a;  
center.y = b;  
radius = r;  
```  
 I only  
  
 II only  
  
 III only  
  
 II and III only  
  
 I, II, and III  
  
---  
Consider the following code segment.  
  
```java  
int num = 2574;  
int result = 0;  
  
while (num > 0)  
{  
    result = result * 10 + num % 10;  
    num /= 10;  
}  
System.out.println(result);  
```  
What is printed as a result of executing the code segment?  
  
  
  
```java  
2  
```  
```java  
4  
```  
```java  
18  
```  
```java  
2574  
```  
```java  
4752  
```  
---  
Consider the following method.  
  
```java  
public void test(int x)  
{  
    int y;  
  
    if (x % 2 == 0)  
        y = 3;  
    else if (x > 9)  
        y = 5;  
    else  
        y = 1;  
  
    System.out.println("y = " + y);  
}  
```  
Which of the following test data sets would test each possible output for the method?  
  
 8, 9, 12  
  
 7, 9, 11  
  
 8, 9, 11  
  
 8, 11, 13  
  
 7, 9, 10  
  
---  
Consider the following code segment.  
  
```java  
int x = 1;  
while ( /* missing code */ )  
{  
    System.out.print(x + " ");  
    x = x + 2;  
}  
```  
Consider the following possible replacements for `/* missing code */`.  
  
I. `x < 6`  
II. `x != 6`  
III. `x < 7`  
  
Which of the proposed replacements for `/* missing code */` will cause the code segment to print only the values `1 3 5`?  
  
 I only  
  
 II only  
  
 I and II only  
  
 I and III only  
  
 I, II, and III  
  
---  
Assume that `x` and `y` have been declared and initialized with `int` values. Consider the following Java expression.  
  
```java  
(y > 10000) || (x > 1000 && x < 1500)  
```  
Which of the following is equivalent to the expression given above?  
  
 `(y > 10000 || x > 1000) && (y > 10000 || x < 1500)`    
  
 `(y > 10000 || x > 1000) || (y > 10000 || x < 1500)`    
  
 `(y > 10000) && (x > 1000 || x < 1500)`    
  
 `(y > 10000 || x > 1000) || (y > 10000 && x < 1500)`    
  
  
  
```java  
(y > 10000 || x > 1000) && (y > 10000 && x < 1500)  
```  
---  
Consider the following recursive method.  
  
```java  
public int recur(int n)  
{  
    if (n <= 10)  
        return n * 2;  
    else  
        return recur(recur(n / 3));  
}  
```  
What value is returned as a result of the call `recur(27)`?  
  
  
  
```java  
8  
```  
```java  
9  
```  
```java  
12  
```  
```java  
16  
```  
```java  
18  
```  
---  
Consider the following recursive method.  
  
```java  
public static void whatsItDo(String str)  
{  
    int len = str.length();  
    if (len > 1)  
    {  
        String temp = str.substring(0, len - 1);  
        whatsItDo(temp);  
        System.out.println(temp);  
    }  
}  
```  
What is printed as a result of the call `whatsItDo("WATCH")`?  
  
 `WATC   WAT   WA   W`    
  
 `WATCH   WATC   WAT   WA`    
  
 `W`  
`WA`  
`WAT`  
`WATC`    
  
 `W`  
`WA`  
`WAT`  
`WATC`  
`WATCH`    
  
 `WATCH   WATC   WAT   WA`  
`W`  
`WA`  
`WAT`  
`WATC`  
`WATCH`  
