# Sorting Algorithms

排序演算法的複雜度速查：

![Sorting Algorithms Complexity](assets/sorting-algorithms-complexity.png)

## 複雜度總覽

`n` 代表陣列長度；`k` 代表 Counting Sort 的值域大小。

| 演算法 | Best | Average | Worst | Space | Stable | In-place |
| --- | ---: | ---: | ---: | ---: | :---: | :---: |
| Bubble Sort | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | 是 | 是 |
| Selection Sort | `O(n²)` | `O(n²)` | `O(n²)` | `O(1)` | 否 | 是 |
| Insertion Sort | `O(n)` | `O(n²)` | `O(n²)` | `O(1)` | 是 | 是 |
| Merge Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(n)` | 是 | 否 |
| Quick Sort | `O(n log n)` | `O(n log n)` | `O(n²)` | `O(log n)`* | 否 | 是 |
| Heap Sort | `O(n log n)` | `O(n log n)` | `O(n log n)` | `O(1)` | 否 | 是 |
| Counting Sort | `O(n + k)` | `O(n + k)` | `O(n + k)` | `O(k)` | 可 | 否 |

\* Quick Sort 的遞迴堆疊平均為 `O(log n)`，最差情況可能到 `O(n)`。

## Java 實作

以下方法都會直接由小到大排序輸入陣列。

```java
class SortingAlgorithms {
    // 1. Bubble Sort
    // 重複把較大的元素往右推；若一輪沒有交換，代表已排序完成。
    static void bubbleSort(int[] nums) {
        for (int end = nums.length - 1; end > 0; end--) {
            boolean swapped = false;

            for (int i = 0; i < end; i++) {
                if (nums[i] > nums[i + 1]) {
                    swap(nums, i, i + 1);
                    swapped = true;
                }
            }

            if (!swapped) return;
        }
    }

    // 2. Selection Sort
    // 每次找出未排序區間的最小值，放到區間開頭。
    static void selectionSort(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] < nums[minIndex]) {
                    minIndex = j;
                }
            }

            swap(nums, i, minIndex);
        }
    }

    // 3. Insertion Sort
    // 將目前元素插入前方已排序的區間，適合資料大致已排序的情況。
    static void insertionSort(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            int value = nums[i];
            int j = i - 1;

            while (j >= 0 && nums[j] > value) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = value;
        }
    }

    // 4. Merge Sort
    // Divide and conquer：切半排序，再以雙指標合併兩個已排序區間。
    static void mergeSort(int[] nums) {
        int[] buffer = new int[nums.length];
        mergeSort(nums, buffer, 0, nums.length - 1);
    }

    private static void mergeSort(int[] nums, int[] buffer, int left, int right) {
        if (left >= right) return;

        int middle = left + (right - left) / 2;
        mergeSort(nums, buffer, left, middle);
        mergeSort(nums, buffer, middle + 1, right);
        merge(nums, buffer, left, middle, right);
    }

    private static void merge(
            int[] nums, int[] buffer, int left, int middle, int right) {
        int i = left;
        int j = middle + 1;
        int write = left;

        while (i <= middle && j <= right) {
            if (nums[i] <= nums[j]) {
                buffer[write++] = nums[i++];
            } else {
                buffer[write++] = nums[j++];
            }
        }
        while (i <= middle) buffer[write++] = nums[i++];
        while (j <= right) buffer[write++] = nums[j++];

        for (int index = left; index <= right; index++) {
            nums[index] = buffer[index];
        }
    }

    // 5. Quick Sort
    // 選擇 pivot，將小於 pivot 的元素移到左側，其餘移到右側後遞迴處理。
    static void quickSort(int[] nums) {
        quickSort(nums, 0, nums.length - 1);
    }

    private static void quickSort(int[] nums, int left, int right) {
        if (left >= right) return;

        int pivotIndex = partition(nums, left, right);
        quickSort(nums, left, pivotIndex - 1);
        quickSort(nums, pivotIndex + 1, right);
    }

    private static int partition(int[] nums, int left, int right) {
        int pivot = nums[right];
        int smaller = left;

        for (int i = left; i < right; i++) {
            if (nums[i] <= pivot) {
                swap(nums, smaller++, i);
            }
        }

        swap(nums, smaller, right);
        return smaller;
    }

    // 6. Heap Sort
    // 建立 max heap，每次把最大值移到陣列尾端。
    static void heapSort(int[] nums) {
        int n = nums.length;

        for (int i = n / 2 - 1; i >= 0; i--) {
            siftDown(nums, i, n);
        }

        for (int end = n - 1; end > 0; end--) {
            swap(nums, 0, end);
            siftDown(nums, 0, end);
        }
    }

    private static void siftDown(int[] nums, int root, int size) {
        while (2 * root + 1 < size) {
            int child = 2 * root + 1;
            if (child + 1 < size && nums[child] < nums[child + 1]) {
                child++;
            }
            if (nums[root] >= nums[child]) return;

            swap(nums, root, child);
            root = child;
        }
    }

    // 7. Counting Sort
    // 適合非負整數且值域不大的資料；負數可透過 offset 處理。
    static void countingSort(int[] nums) {
        if (nums.length == 0) return;

        int max = nums[0];
        for (int value : nums) {
            if (value < 0) {
                throw new IllegalArgumentException("Only non-negative integers are supported");
            }
            max = Math.max(max, value);
        }

        int[] count = new int[max + 1];
        for (int value : nums) count[value]++;

        int write = 0;
        for (int value = 0; value < count.length; value++) {
            while (count[value]-- > 0) {
                nums[write++] = value;
            }
        }
    }

    private static void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

## Java 標準函式庫的排序方法

實際開發通常直接使用 Java 內建 API，不需要自行實作排序。以下範例需要：

```java
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
```

### 1. 排序原始型別陣列

`Arrays.sort` 會直接修改原本的陣列，適用於 `int[]`、`long[]`、`double[]` 等原始型別陣列，也支援指定區間 `[fromIndex, toIndex)`。

```java
int[] nums = {5, 2, 4, 1, 3};

Arrays.sort(nums);
// nums = [1, 2, 3, 4, 5]

int[] partial = {5, 2, 4, 1, 3};
Arrays.sort(partial, 1, 4);
// 只排序 index 1 到 3：partial = [5, 1, 2, 4, 3]
```

需要平行排序大量資料時，可以使用 `Arrays.parallelSort`：

```java
int[] nums = {5, 2, 4, 1, 3};
Arrays.parallelSort(nums);
```

### 2. 排序物件陣列

物件陣列可以使用自然順序，或傳入 `Comparator` 自訂排序規則。

```java
String[] names = {"Charlie", "Alice", "Bob"};

Arrays.sort(names);
// [Alice, Bob, Charlie]

Arrays.sort(names, Comparator.reverseOrder());
// [Charlie, Bob, Alice]
```

### 3. 排序 `List`

`List.sort` 會直接修改 List；傳入 `null` 表示使用元素的自然順序。

```java
List<Integer> nums = new java.util.ArrayList<>(List.of(5, 2, 4, 1, 3));

nums.sort(null);
// [1, 2, 3, 4, 5]

nums.sort(Comparator.reverseOrder());
// [5, 4, 3, 2, 1]
```

`Collections.sort` 也可以使用，但現在通常優先寫 `list.sort(...)`：

```java
java.util.Collections.sort(nums); // 自然順序
java.util.Collections.sort(nums, Comparator.reverseOrder());
```

注意：`List.of(...)` 建立的是不可修改 List，不能直接呼叫排序；需要先複製成可修改的 `ArrayList`。

### 4. 使用 `Comparator` 排序物件

以學生的分數由高到低排序；分數相同時，再依姓名由小到大排序：

```java
class Student {
    String name;
    int score;

    Student(String name, int score) {
        this.name = name;
        this.score = score;
    }
}

List<Student> students = new java.util.ArrayList<>(List.of(
        new Student("Alice", 90),
        new Student("Bob", 90),
        new Student("Charlie", 80)
));

students.sort(
        Comparator.comparingInt((Student s) -> s.score)
                .reversed()
                .thenComparing(s -> s.name)
);
```

常用的 `Comparator` 組合方法：

```java
Comparator.comparingInt((Student s) -> s.score); // 依 int 欄位排序
Comparator.comparing((Student s) -> s.name);     // 依 Comparable 欄位排序
Comparator.reverseOrder();                       // 反向自然順序
comparator.reversed();                           // 將既有規則反轉
comparator.thenComparing(otherComparator);       // 第一個相同時使用下一個規則
Comparator.nullsLast(comparator);                // null 放最後
```

### 5. Stream 排序

`Stream.sorted` 不會修改原本的集合，而是產生排序後的 Stream。需要結果時再收集成 List 或陣列。

```java
List<String> names = List.of("Charlie", "Alice", "Bob");

List<String> sortedNames = names.stream()
        .sorted()
        .collect(Collectors.toList());

List<String> reverseNames = names.stream()
        .sorted(Comparator.reverseOrder())
        .collect(Collectors.toList());
```

原始型別陣列也可以透過 `IntStream` 排序：

```java
int[] nums = {5, 2, 4, 1, 3};
int[] sorted = Arrays.stream(nums).sorted().toArray();
```

### 快速選擇

| 資料型別 | 建議方法 | 是否修改原資料 |
| --- | --- | :---: |
| `int[]`、`long[]` | `Arrays.sort(array)` | 是 |
| 大型原始型別陣列 | `Arrays.parallelSort(array)` | 是 |
| 物件陣列 | `Arrays.sort(array, comparator)` | 是 |
| 可修改的 `List` | `list.sort(comparator)` | 是 |
| 需要保留原 `List` | `list.stream().sorted(...)` | 否 |

## 怎麼選

1. 一般情況：優先使用 `O(n log n)` 的 Merge Sort、Quick Sort 或 Heap Sort。
2. 需要穩定排序：選 Merge Sort；相同 key 的元素會保留原本的相對順序。
3. 記憶體很有限：選 Heap Sort，額外空間為 `O(1)`。
4. 資料幾乎已排序：Insertion Sort 可能很有效率，最佳情況為 `O(n)`。
5. 值域很小且是整數：Counting Sort 可達到 `O(n + k)`，但要留意 `k` 不宜過大。
6. 實際 Java 專案通常直接使用 `Arrays.sort(nums)`；面試或學習時才需要手寫上述實作。

## 常見注意事項

- Quick Sort 的 pivot 若經常選到最大或最小值，會退化成 `O(n²)`；實作上可使用隨機 pivot 或三數取中。
- Merge Sort 的合併必須使用 `<=`，才能維持穩定排序。
- 遞迴版本的 Quick Sort 在極端輸入可能造成遞迴深度過深。
- Counting Sort 不是比較排序，只有在值域 `k` 合理時才比 `O(n log n)` 排序更有優勢。
