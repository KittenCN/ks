---
description: CoderFAN 资料库 算法资料 Hello 算法
---

# 列表

「列表 list」是一个抽象的数据结构概念，它表示元素的有序集合，支持元素访问、修改、添加、删除和遍历等操作，无须使用者考虑容量限制的问题。列表可以基于链表或数组实现。

- 链表天然可以看作一个列表，其支持元素增删查改操作，并且可以灵活动态扩容。
- 数组也支持元素增删查改，但由于其长度不可变，因此只能看作一个具有长度限制的列表。

当使用数组实现列表时，**长度不可变的性质会导致列表的实用性降低**。这是因为我们通常无法事先确定需要存储多少数据，从而难以选择合适的列表长度。若长度过小，则很可能无法满足使用需求；若长度过大，则会造成内存空间浪费。

为解决此问题，我们可以使用「动态数组 dynamic array」来实现列表。它继承了数组的各项优点，并且可以在程序运行过程中进行动态扩容。

实际上，**许多编程语言中的标准库提供的列表是基于动态数组实现的**，例如 Python 中的 `list` 、Java 中的 `ArrayList` 、C++ 中的 `vector` 和 C# 中的 `List` 等。在接下来的讨论中，我们将把“列表”和“动态数组”视为等同的概念。

## 列表常用操作

### 初始化列表

我们通常使用“无初始值”和“有初始值”这两种初始化方法：

- "Python"

    ```python title="list.py"
   // 初始化列表
   // 无初始值
    nums1: list[int] = []
   // 有初始值
    nums: list[int] = [1, 3, 2, 5, 4]
    ```

- "C++"

    ```cpp title="list.cpp"
    /* 初始化列表 */
    // 需注意，C++ 中 vector 即是本文描述的 nums
    // 无初始值
    vector<int> nums1;
    // 有初始值
    vector<int> nums = { 1, 3, 2, 5, 4 };
    ```

- "Java"

    ```java title="list.java"
    /* 初始化列表 */
    // 无初始值
    List<Integer> nums1 = new ArrayList<>();
    // 有初始值（注意数组的元素类型需为 int[] 的包装类 Integer[]）
    Integer[] numbers = new Integer[] { 1, 3, 2, 5, 4 };
    List<Integer> nums = new ArrayList<>(Arrays.asList(numbers));
    ```

- "C#"

    ```csharp title="list.cs"
    /* 初始化列表 */
    // 无初始值
    List<int> nums1 = [];
    // 有初始值
    int[] numbers = [1, 3, 2, 5, 4];
    List<int> nums = [.. numbers];
    ```

- "Go"

    ```go title="list_test.go"
    /* 初始化列表 */
    // 无初始值
    nums1 := []int{}
    // 有初始值
    nums := []int{1, 3, 2, 5, 4}
    ```

- "Swift"

    ```swift title="list.swift"
    /* 初始化列表 */
    // 无初始值
    let nums1: [Int] = []
    // 有初始值
    var nums = [1, 3, 2, 5, 4]
    ```

- "JS"

    ```javascript title="list.js"
    /* 初始化列表 */
    // 无初始值
    const nums1 = [];
    // 有初始值
    const nums = [1, 3, 2, 5, 4];
    ```

- "TS"

    ```typescript title="list.ts"
    /* 初始化列表 */
    // 无初始值
    const nums1: number[] = [];
    // 有初始值
    const nums: number[] = [1, 3, 2, 5, 4];
    ```

- "Dart"

    ```dart title="list.dart"
    /* 初始化列表 */
    // 无初始值
    List<int> nums1 = [];
    // 有初始值
    List<int> nums = [1, 3, 2, 5, 4];
    ```

- "Rust"

    ```rust title="list.rs"
    /* 初始化列表 */
    // 无初始值
    let nums1: Vec<i32> = Vec::new();
    // 有初始值
    let nums: Vec<i32> = vec![1, 3, 2, 5, 4];
    ```

- "C"

    ```c title="list.c"
    // C 未提供内置动态数组
    ```

- "Zig"

    ```zig title="list.zig"
    // 初始化列表
    var nums = std.ArrayList(i32).init(std.heap.page_allocator);
    defer nums.deinit();
    try nums.appendSlice(&[_]i32{ 1, 3, 2, 5, 4 });
    ```

### 访问元素

列表本质上是数组，因此可以在 $O(1)$ 时间内访问和更新元素，效率很高。

- "Python"

    ```python title="list.py"
   // 访问元素
    num: int = nums[1] // 访问索引 1 处的元素

   // 更新元素
    nums[1] = 0   // 将索引 1 处的元素更新为 0
    ```

- "C++"

    ```cpp title="list.cpp"
    /* 访问元素 */
    int num = nums[1];  // 访问索引 1 处的元素

    /* 更新元素 */
    nums[1] = 0;  // 将索引 1 处的元素更新为 0
    ```

- "Java"

    ```java title="list.java"
    /* 访问元素 */
    int num = nums.get(1);  // 访问索引 1 处的元素

    /* 更新元素 */
    nums.set(1, 0);  // 将索引 1 处的元素更新为 0
    ```

- "C#"

    ```csharp title="list.cs"
    /* 访问元素 */
    int num = nums[1];  // 访问索引 1 处的元素

    /* 更新元素 */
    nums[1] = 0;  // 将索引 1 处的元素更新为 0
    ```

- "Go"

    ```go title="list_test.go"
    /* 访问元素 */
    num := nums[1]  // 访问索引 1 处的元素

    /* 更新元素 */
    nums[1] = 0     // 将索引 1 处的元素更新为 0
    ```

- "Swift"

    ```swift title="list.swift"
    /* 访问元素 */
    let num = nums[1] // 访问索引 1 处的元素

    /* 更新元素 */
    nums[1] = 0 // 将索引 1 处的元素更新为 0
    ```

- "JS"

    ```javascript title="list.js"
    /* 访问元素 */
    const num = nums[1];  // 访问索引 1 处的元素

    /* 更新元素 */
    nums[1] = 0;  // 将索引 1 处的元素更新为 0
    ```

- "TS"

    ```typescript title="list.ts"
    /* 访问元素 */
    const num: number = nums[1];  // 访问索引 1 处的元素

    /* 更新元素 */
    nums[1] = 0;  // 将索引 1 处的元素更新为 0
    ```

- "Dart"

    ```dart title="list.dart"
    /* 访问元素 */
    int num = nums[1];  // 访问索引 1 处的元素

    /* 更新元素 */
    nums[1] = 0;  // 将索引 1 处的元素更新为 0
    ```

- "Rust"

    ```rust title="list.rs"
    /* 访问元素 */
    let num: i32 = nums[1];  // 访问索引 1 处的元素
    /* 更新元素 */
    nums[1] = 0;             // 将索引 1 处的元素更新为 0
    ```

- "C"

    ```c title="list.c"
    // C 未提供内置动态数组
    ```

- "Zig"

    ```zig title="list.zig"
    // 访问元素
    var num = nums.items[1]; // 访问索引 1 处的元素

    // 更新元素
    nums.items[1] = 0; // 将索引 1 处的元素更新为 0  
    ```

### 插入与删除元素

相较于数组，列表可以自由地添加与删除元素。在列表尾部添加元素的时间复杂度为 $O(1)$ ，但插入和删除元素的效率仍与数组相同，时间复杂度为 $O(n)$ 。

- "Python"

    ```python title="list.py"
   // 清空列表
    nums.clear()

   // 在尾部添加元素
    nums.append(1)
    nums.append(3)
    nums.append(2)
    nums.append(5)
    nums.append(4)

   // 在中间插入元素
    nums.insert(3, 6) // 在索引 3 处插入数字 6

   // 删除元素
    nums.pop(3)       // 删除索引 3 处的元素
    ```

- "C++"

    ```cpp title="list.cpp"
    /* 清空列表 */
    nums.clear();

    /* 在尾部添加元素 */
    nums.push_back(1);
    nums.push_back(3);
    nums.push_back(2);
    nums.push_back(5);
    nums.push_back(4);

    /* 在中间插入元素 */
    nums.insert(nums.begin() + 3, 6);  // 在索引 3 处插入数字 6

    /* 删除元素 */
    nums.erase(nums.begin() + 3);      // 删除索引 3 处的元素
    ```

- "Java"

    ```java title="list.java"
    /* 清空列表 */
    nums.clear();

    /* 在尾部添加元素 */
    nums.add(1);
    nums.add(3);
    nums.add(2);
    nums.add(5);
    nums.add(4);

    /* 在中间插入元素 */
    nums.add(3, 6);  // 在索引 3 处插入数字 6

    /* 删除元素 */
    nums.remove(3);  // 删除索引 3 处的元素
    ```

- "C#"

    ```csharp title="list.cs"
    /* 清空列表 */
    nums.Clear();

    /* 在尾部添加元素 */
    nums.Add(1);
    nums.Add(3);
    nums.Add(2);
    nums.Add(5);
    nums.Add(4);

    /* 在中间插入元素 */
    nums.Insert(3, 6);

    /* 删除元素 */
    nums.RemoveAt(3);
    ```

- "Go"

    ```go title="list_test.go"
    /* 清空列表 */
    nums = nil

    /* 在尾部添加元素 */
    nums = append(nums, 1)
    nums = append(nums, 3)
    nums = append(nums, 2)
    nums = append(nums, 5)
    nums = append(nums, 4)

    /* 在中间插入元素 */
    nums = append(nums[:3], append([]int{6}, nums[3:]...)...) // 在索引 3 处插入数字 6

    /* 删除元素 */
    nums = append(nums[:3], nums[4:]...) // 删除索引 3 处的元素
    ```

- "Swift"

    ```swift title="list.swift"
    /* 清空列表 */
    nums.removeAll()

    /* 在尾部添加元素 */
    nums.append(1)
    nums.append(3)
    nums.append(2)
    nums.append(5)
    nums.append(4)

    /* 在中间插入元素 */
    nums.insert(6, at: 3) // 在索引 3 处插入数字 6

    /* 删除元素 */
    nums.remove(at: 3) // 删除索引 3 处的元素
    ```

- "JS"

    ```javascript title="list.js"
    /* 清空列表 */
    nums.length = 0;

    /* 在尾部添加元素 */
    nums.push(1);
    nums.push(3);
    nums.push(2);
    nums.push(5);
    nums.push(4);

    /* 在中间插入元素 */
    nums.splice(3, 0, 6);

    /* 删除元素 */
    nums.splice(3, 1);
    ```

- "TS"

    ```typescript title="list.ts"
    /* 清空列表 */
    nums.length = 0;

    /* 在尾部添加元素 */
    nums.push(1);
    nums.push(3);
    nums.push(2);
    nums.push(5);
    nums.push(4);

    /* 在中间插入元素 */
    nums.splice(3, 0, 6);

    /* 删除元素 */
    nums.splice(3, 1);
    ```

- "Dart"

    ```dart title="list.dart"
    /* 清空列表 */
    nums.clear();

    /* 在尾部添加元素 */
    nums.add(1);
    nums.add(3);
    nums.add(2);
    nums.add(5);
    nums.add(4);

    /* 在中间插入元素 */
    nums.insert(3, 6); // 在索引 3 处插入数字 6

    /* 删除元素 */
    nums.removeAt(3); // 删除索引 3 处的元素
    ```

- "Rust"

    ```rust title="list.rs"
    /* 清空列表 */
    nums.clear();

    /* 在尾部添加元素 */
    nums.push(1);
    nums.push(3);
    nums.push(2);
    nums.push(5);
    nums.push(4);

    /* 在中间插入元素 */
    nums.insert(3, 6);  // 在索引 3 处插入数字 6

    /* 删除元素 */
    nums.remove(3);    // 删除索引 3 处的元素
    ```

- "C"

    ```c title="list.c"
    // C 未提供内置动态数组
    ```

- "Zig"

    ```zig title="list.zig"
    // 清空列表
    nums.clearRetainingCapacity();

    // 在尾部添加元素
    try nums.append(1);
    try nums.append(3);
    try nums.append(2);
    try nums.append(5);
    try nums.append(4);

    // 在中间插入元素
    try nums.insert(3, 6); // 在索引 3 处插入数字 6

    // 删除元素
    _ = nums.orderedRemove(3); // 删除索引 3 处的元素
    ```

### 遍历列表

与数组一样，列表可以根据索引遍历，也可以直接遍历各元素。

- "Python"

    ```python title="list.py"
   // 通过索引遍历列表
    count = 0
    for i in range(len(nums)):
        count += nums[i]

   // 直接遍历列表元素
    for num in nums:
        count += num
    ```

- "C++"

    ```cpp title="list.cpp"
    /* 通过索引遍历列表 */
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        count += nums[i];
    }

    /* 直接遍历列表元素 */
    count = 0;
    for (int num : nums) {
        count += num;
    }
    ```

- "Java"

    ```java title="list.java"
    /* 通过索引遍历列表 */
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        count += nums.get(i);
    }

    /* 直接遍历列表元素 */
    for (int num : nums) {
        count += num;
    }
    ```

- "C#"

    ```csharp title="list.cs"
    /* 通过索引遍历列表 */
    int count = 0;
    for (int i = 0; i < nums.Count; i++) {
        count += nums[i];
    }

    /* 直接遍历列表元素 */
    count = 0;
    foreach (int num in nums) {
        count += num;
    }
    ```

- "Go"

    ```go title="list_test.go"
    /* 通过索引遍历列表 */
    count := 0
    for i := 0; i < len(nums); i++ {
        count += nums[i]
    }

    /* 直接遍历列表元素 */
    count = 0
    for _, num := range nums {
        count += num
    }
    ```

- "Swift"

    ```swift title="list.swift"
    /* 通过索引遍历列表 */
    var count = 0
    for i in nums.indices {
        count += nums[i]
    }

    /* 直接遍历列表元素 */
    count = 0
    for num in nums {
        count += num
    }
    ```

- "JS"

    ```javascript title="list.js"
    /* 通过索引遍历列表 */
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        count += nums[i];
    }

    /* 直接遍历列表元素 */
    count = 0;
    for (const num of nums) {
        count += num;
    }
    ```

- "TS"

    ```typescript title="list.ts"
    /* 通过索引遍历列表 */
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        count += nums[i];
    }

    /* 直接遍历列表元素 */
    count = 0;
    for (const num of nums) {
        count += num;
    }
    ```

- "Dart"

    ```dart title="list.dart"
    /* 通过索引遍历列表 */
    int count = 0;
    for (var i = 0; i < nums.length; i++) {
        count += nums[i];
    }
    
    /* 直接遍历列表元素 */
    count = 0;
    for (var num in nums) {
        count += num;
    }
    ```

- "Rust"

    ```rust title="list.rs"
    // 通过索引遍历列表
    let mut _count = 0;
    for i in 0..nums.len() {
        _count += nums[i];
    }

    // 直接遍历列表元素
    _count = 0;
    for num in &nums {
        _count += num;
    }
    ```

- "C"

    ```c title="list.c"
    // C 未提供内置动态数组
    ```

- "Zig"

    ```zig title="list.zig"
    // 通过索引遍历列表
    var count: i32 = 0;
    var i: i32 = 0;
    while (i < nums.items.len) : (i += 1) {
        count += nums[i];
    }

    // 直接遍历列表元素
    count = 0;
    for (nums.items) |num| {
        count += num;
    }
    ```

### 拼接列表

给定一个新列表 `nums1` ，我们可以将其拼接到原列表的尾部。

- "Python"

    ```python title="list.py"
   // 拼接两个列表
    nums1: list[int] = [6, 8, 7, 10, 9]
    nums += nums1 // 将列表 nums1 拼接到 nums 之后
    ```

- "C++"

    ```cpp title="list.cpp"
    /* 拼接两个列表 */
    vector<int> nums1 = { 6, 8, 7, 10, 9 };
    // 将列表 nums1 拼接到 nums 之后
    nums.insert(nums.end(), nums1.begin(), nums1.end());
    ```

- "Java"

    ```java title="list.java"
    /* 拼接两个列表 */
    List<Integer> nums1 = new ArrayList<>(Arrays.asList(new Integer[] { 6, 8, 7, 10, 9 }));
    nums.addAll(nums1);  // 将列表 nums1 拼接到 nums 之后
    ```

- "C#"

    ```csharp title="list.cs"
    /* 拼接两个列表 */
    List<int> nums1 = [6, 8, 7, 10, 9];
    nums.AddRange(nums1);  // 将列表 nums1 拼接到 nums 之后
    ```

- "Go"

    ```go title="list_test.go"
    /* 拼接两个列表 */
    nums1 := []int{6, 8, 7, 10, 9}
    nums = append(nums, nums1...)  // 将列表 nums1 拼接到 nums 之后
    ```

- "Swift"

    ```swift title="list.swift"
    /* 拼接两个列表 */
    let nums1 = [6, 8, 7, 10, 9]
    nums.append(contentsOf: nums1) // 将列表 nums1 拼接到 nums 之后
    ```

- "JS"

    ```javascript title="list.js"
    /* 拼接两个列表 */
    const nums1 = [6, 8, 7, 10, 9];
    nums.push(...nums1);  // 将列表 nums1 拼接到 nums 之后
    ```

- "TS"

    ```typescript title="list.ts"
    /* 拼接两个列表 */
    const nums1: number[] = [6, 8, 7, 10, 9];
    nums.push(...nums1);  // 将列表 nums1 拼接到 nums 之后
    ```

- "Dart"

    ```dart title="list.dart"
    /* 拼接两个列表 */
    List<int> nums1 = [6, 8, 7, 10, 9];
    nums.addAll(nums1);  // 将列表 nums1 拼接到 nums 之后
    ```

- "Rust"

    ```rust title="list.rs"
    /* 拼接两个列表 */
    let nums1: Vec<i32> = vec![6, 8, 7, 10, 9];
    nums.extend(nums1);
    ```

- "C"

    ```c title="list.c"
    // C 未提供内置动态数组
    ```

- "Zig"

    ```zig title="list.zig"
    // 拼接两个列表
    var nums1 = std.ArrayList(i32).init(std.heap.page_allocator);
    defer nums1.deinit();
    try nums1.appendSlice(&[_]i32{ 6, 8, 7, 10, 9 });
    try nums.insertSlice(nums.items.len, nums1.items); // 将列表 nums1 拼接到 nums 之后
    ```

### 排序列表

完成列表排序后，我们便可以使用在数组类算法题中经常考查的“二分查找”和“双指针”算法。

- "Python"

    ```python title="list.py"
   // 排序列表
    nums.sort() // 排序后，列表元素从小到大排列
    ```

- "C++"

    ```cpp title="list.cpp"
    /* 排序列表 */
    sort(nums.begin(), nums.end());  // 排序后，列表元素从小到大排列
    ```

- "Java"

    ```java title="list.java"
    /* 排序列表 */
    Collections.sort(nums);  // 排序后，列表元素从小到大排列
    ```

- "C#"

    ```csharp title="list.cs"
    /* 排序列表 */
    nums.Sort(); // 排序后，列表元素从小到大排列
    ```

- "Go"

    ```go title="list_test.go"
    /* 排序列表 */
    sort.Ints(nums)  // 排序后，列表元素从小到大排列
    ```

- "Swift"

    ```swift title="list.swift"
    /* 排序列表 */
    nums.sort() // 排序后，列表元素从小到大排列
    ```

- "JS"

    ```javascript title="list.js"
    /* 排序列表 */  
    nums.sort((a, b) => a - b);  // 排序后，列表元素从小到大排列
    ```

- "TS"

    ```typescript title="list.ts"
    /* 排序列表 */
    nums.sort((a, b) => a - b);  // 排序后，列表元素从小到大排列
    ```

- "Dart"

    ```dart title="list.dart"
    /* 排序列表 */
    nums.sort(); // 排序后，列表元素从小到大排列
    ```

- "Rust"

    ```rust title="list.rs"
    /* 排序列表 */
    nums.sort(); // 排序后，列表元素从小到大排列
    ```

- "C"

    ```c title="list.c"
    // C 未提供内置动态数组
    ```

- "Zig"

    ```zig title="list.zig"
    // 排序列表
    std.sort.sort(i32, nums.items, {}, comptime std.sort.asc(i32));
    ```

## 列表实现

许多编程语言内置了列表，例如 Java、C++、Python 等。它们的实现比较复杂，各个参数的设定也非常考究，例如初始容量、扩容倍数等。感兴趣的读者可以查阅源码进行学习。

为了加深对列表工作原理的理解，我们尝试实现一个简易版列表，包括以下三个重点设计。

- **初始容量**：选取一个合理的数组初始容量。在本示例中，我们选择 10 作为初始容量。
- **数量记录**：声明一个变量 `size` ，用于记录列表当前元素数量，并随着元素插入和删除实时更新。根据此变量，我们可以定位列表尾部，以及判断是否需要扩容。
- **扩容机制**：若插入元素时列表容量已满，则需要进行扩容。先根据扩容倍数创建一个更大的数组，再将当前数组的所有元素依次移动至新数组。在本示例中，我们规定每次将数组扩容至之前的 2 倍。

- "Python"
```python title="list.py"
class MyList:
    """列表类"""

    def __init__(self):
        """构造方法"""
        self._capacity: int = 10 // 列表容量
        self._arr: list[int] = [0] * self._capacity // 数组（存储列表元素）
        self._size: int = 0 // 列表长度（当前元素数量）
        self._extend_ratio: int = 2 // 每次列表扩容的倍数

    def size(self) -> int:
        """获取列表长度（当前元素数量）"""
        return self._size

    def capacity(self) -> int:
        """获取列表容量"""
        return self._capacity

    def get(self, index: int) -> int:
        """访问元素"""
       // 索引如果越界，则抛出异常，下同
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]

    def set(self, num: int, index: int):
        """更新元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num

    def add(self, num: int):
        """在尾部添加元素"""
       // 元素数量超出容量时，触发扩容机制
        if self.size() == self.capacity():
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1

    def insert(self, num: int, index: int):
        """在中间插入元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
       // 元素数量超出容量时，触发扩容机制
        if self._size == self.capacity():
            self.extend_capacity()
       // 将索引 index 以及之后的元素都向后移动一位
        for j in range(self._size - 1, index - 1, -1):
            self._arr[j + 1] = self._arr[j]
        self._arr[index] = num
       // 更新元素数量
        self._size += 1

    def remove(self, index: int) -> int:
        """删除元素"""
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
       // 将索引 index 之后的元素都向前移动一位
        for j in range(index, self._size - 1):
            self._arr[j] = self._arr[j + 1]
       // 更新元素数量
        self._size -= 1
       // 返回被删除的元素
        return num

    def extend_capacity(self):
        """列表扩容"""
       // 新建一个长度为原数组 _extend_ratio 倍的新数组，并将原数组复制到新数组
        self._arr = self._arr + [0] * self.capacity() * (self._extend_ratio - 1)
       // 更新列表容量
        self._capacity = len(self._arr)

    def to_array(self) -> list[int]:
        """返回有效长度的列表"""
        return self._arr[: self._size]
```  

- "C++"
```cpp title="list.cpp"
/* 列表类 */
class MyList {
  private:
    int *arr;             // 数组（存储列表元素）
    int arrCapacity = 10; // 列表容量
    int arrSize = 0;      // 列表长度（当前元素数量）
    int extendRatio = 2;   // 每次列表扩容的倍数

  public:
    /* 构造方法 */
    MyList() {
        arr = new int[arrCapacity];
    }

    /* 析构方法 */
    ~MyList() {
        delete[] arr;
    }

    /* 获取列表长度（当前元素数量）*/
    int size() {
        return arrSize;
    }

    /* 获取列表容量 */
    int capacity() {
        return arrCapacity;
    }

    /* 访问元素 */
    int get(int index) {
        // 索引如果越界，则抛出异常，下同
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        return arr[index];
    }

    /* 更新元素 */
    void set(int index, int num) {
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        arr[index] = num;
    }

    /* 在尾部添加元素 */
    void add(int num) {
        // 元素数量超出容量时，触发扩容机制
        if (size() == capacity())
            extendCapacity();
        arr[size()] = num;
        // 更新元素数量
        arrSize++;
    }

    /* 在中间插入元素 */
    void insert(int index, int num) {
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        // 元素数量超出容量时，触发扩容机制
        if (size() == capacity())
            extendCapacity();
        // 将索引 index 以及之后的元素都向后移动一位
        for (int j = size() - 1; j >= index; j--) {
            arr[j + 1] = arr[j];
        }
        arr[index] = num;
        // 更新元素数量
        arrSize++;
    }

    /* 删除元素 */
    int remove(int index) {
        if (index < 0 || index >= size())
            throw out_of_range("索引越界");
        int num = arr[index];
        // 将索引 index 之后的元素都向前移动一位
        for (int j = index; j < size() - 1; j++) {
            arr[j] = arr[j + 1];
        }
        // 更新元素数量
        arrSize--;
        // 返回被删除的元素
        return num;
    }

    /* 列表扩容 */
    void extendCapacity() {
        // 新建一个长度为原数组 extendRatio 倍的新数组
        int newCapacity = capacity() * extendRatio;
        int *tmp = arr;
        arr = new int[newCapacity];
        // 将原数组中的所有元素复制到新数组
        for (int i = 0; i < size(); i++) {
            arr[i] = tmp[i];
        }
        // 释放内存
        delete[] tmp;
        arrCapacity = newCapacity;
    }

    /* 将列表转换为 Vector 用于打印 */
    vector<int> toVector() {
        // 仅转换有效长度范围内的列表元素
        vector<int> vec(size());
        for (int i = 0; i < size(); i++) {
            vec[i] = arr[i];
        }
        return vec;
    }
};
```  

- "Java"
```java title="list.java"
/* 列表类 */
class MyList {
    private int[] arr; // 数组（存储列表元素）
    private int capacity = 10; // 列表容量
    private int size = 0; // 列表长度（当前元素数量）
    private int extendRatio = 2; // 每次列表扩容的倍数

    /* 构造方法 */
    public MyList() {
        arr = new int[capacity];
    }

    /* 获取列表长度（当前元素数量） */
    public int size() {
        return size;
    }

    /* 获取列表容量 */
    public int capacity() {
        return capacity;
    }

    /* 访问元素 */
    public int get(int index) {
        // 索引如果越界，则抛出异常，下同
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException("索引越界");
        return arr[index];
    }

    /* 更新元素 */
    public void set(int index, int num) {
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException("索引越界");
        arr[index] = num;
    }

    /* 在尾部添加元素 */
    public void add(int num) {
        // 元素数量超出容量时，触发扩容机制
        if (size == capacity())
            extendCapacity();
        arr[size] = num;
        // 更新元素数量
        size++;
    }

    /* 在中间插入元素 */
    public void insert(int index, int num) {
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException("索引越界");
        // 元素数量超出容量时，触发扩容机制
        if (size == capacity())
            extendCapacity();
        // 将索引 index 以及之后的元素都向后移动一位
        for (int j = size - 1; j >= index; j--) {
            arr[j + 1] = arr[j];
        }
        arr[index] = num;
        // 更新元素数量
        size++;
    }

    /* 删除元素 */
    public int remove(int index) {
        if (index < 0 || index >= size)
            throw new IndexOutOfBoundsException("索引越界");
        int num = arr[index];
        // 将将索引 index 之后的元素都向前移动一位
        for (int j = index; j < size - 1; j++) {
            arr[j] = arr[j + 1];
        }
        // 更新元素数量
        size--;
        // 返回被删除的元素
        return num;
    }

    /* 列表扩容 */
    public void extendCapacity() {
        // 新建一个长度为原数组 extendRatio 倍的新数组，并将原数组复制到新数组
        arr = Arrays.copyOf(arr, capacity() * extendRatio);
        // 更新列表容量
        capacity = arr.length;
    }

    /* 将列表转换为数组 */
    public int[] toArray() {
        int size = size();
        // 仅转换有效长度范围内的列表元素
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = get(i);
        }
        return arr;
    }
}
```  
