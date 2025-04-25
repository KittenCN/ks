# AP计算机科学考试Java快速参考    
#### class java.lang.Object    
`boolean equals(Object other)`    
`String toString()`    
    
#### class java.lang.Integer    
`Integer(int value)`    
`int intValue()`    
`Integer.MIN_VALUE`：int或Integer可以表示的最小值    
`Integer.MAX_VALUE`：int或Integer可以表示的最大值    
    
#### class java.lang.Double    
`Double(double value)`    
`double doubleValue()`    
    
#### class java.lang.String    
`int length()`    
`String substring(int from, int to)`：返回从`from`到`to - 1`的子串    
`String substring(int from)`：返回从`from`到`length()`的子串    
`int indexOf(String str)`：返回第一次出现`str`的位置，未找到则返回`-1`    
`int compareTo(String other)`：`this`小于`other`返回负数，等于返回`0`，大于返回正数    
    
#### class java.lang.Math    
`static int abs(int x)`    
`static double abs(double x)`    
`static double pow(double base, double exponent)`    
`static double sqrt(double x)`    
`static double random()`：返回在范围\[0.0, 1.0)之间的`double`    
    
#### class java.util.ArrayList implements java.util.List    
`int size()`    
`boolean add(E obj)`：在末尾添加`obj`，返回`true`    
`void add(int index, E obj)`：在位置`index`插入`obj`，之后元素后移一位，`index`需小于总长    
`E get(int index)`    
`E set(int index, E obj)`：在位置`index`替换`obj`，返回被替换掉的元素    
`E remove(int index)`：删除位置`index`的元素并返回，之后元素前移一位    
    
