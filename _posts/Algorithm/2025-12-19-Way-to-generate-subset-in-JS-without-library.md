# Way to generate subset in JS without library

Python has useful built-in libraries such as `itertools.combinations` that make solving subset or combination problems straightforward.
However, when solving algorithm problems with TypeScript or JavaScript, we need to implement this logic ourselves.

This post covers **both combinations (fixed-size subsets)** and **subsets (power set)** using DFS (Depth-First Search), without relying on any external libraries.

---

## Combination (Fixed-size subset) using DFS

Below is a reusable and efficient implementation for generating subsets of a fixed size.
This pattern is especially useful for combination-based problems on platforms like LeetCode.

### Implementation

```ts
const generateSubsets = (nums: number[], size: number): number[][] => {
    const res: number[][] = []
    const path: number[] = []

    const dfs = (start: number = 0) => {
        // When the subset reaches the desired size, record it
        if (path.length === size) {
            res.push([...path])
            return
        }

        // Pruning: stop if there are not enough remaining elements
        if (path.length + (nums.length - start) < size) return

        for (let i = start; i < nums.length; i++) {
            path.push(nums[i])
            dfs(i + 1)
            path.pop()
        }
    }

    dfs()
    return res
}
```

---

## How it works (Combination)

This function generates **combinations**, not all subsets.

Key points:

1. `path` represents the current subset being built.
2. `dfs(start)` ensures elements are chosen in increasing index order, avoiding duplicates.
3. A subset is added to the result **only when its length equals `size`**.
4. Smaller subsets (length < size) exist only as intermediate states and are never returned.

This is an important distinction:
the algorithm does not generate all subsets and then filter them — it only *accepts* valid combinations.

---

## Pruning for performance

```ts
if (path.length + (nums.length - start) < size) return
```

This line is critical for performance.

It means:

* If the number of remaining elements is insufficient to reach the target size,
* Stop exploring this branch immediately.

This avoids unnecessary recursive calls and significantly improves efficiency for larger inputs.

---

## Combination example walkthrough

Given:

```ts
array = [2, 5, 7]
size = 2
```

Valid combinations:

```
[2, 5]
[2, 7]
[5, 7]
```

During execution:

* `[2]` and `[5]` are intermediate paths
* They are **not stored**
* Only paths that reach length `2` are added to the result

This image illustrates the decision tree traversal:

```
array = [2, 5, 7]
```
![subnet\_decision\_tree](https://github.com/yeoung004/yeoung004.github.io/blob/main/_posts/Algorithm/subnet_decison_tree.png?raw=true)

---

## Time and space complexity (Combination)

* Time complexity:
  **O(C(n, k))**, where `n` is `nums.length` and `k` is `size`

* Space complexity:

  * Call stack depth: `O(k)`
  * Result storage: `O(C(n, k))`

This is optimal for combination generation since all valid results must be produced.

---

## Subset (Power set) using DFS

In contrast to combinations, a **subset (power set)** includes **all possible subsets**, regardless of their size.

Key differences:

* No fixed size
* Every DFS state is a valid subset
* The total number of subsets is `2^n`

---

### Implementation (Subset / Power Set)

```ts
const subsets = (nums: number[]): number[][] => {
    const res: number[][] = []
    const path: number[] = []

    const dfs = (start: number) => {
        // The current path itself is a valid subset
        res.push([...path])

        for (let i = start; i < nums.length; i++) {
            path.push(nums[i])
            dfs(i + 1)
            path.pop()
        }
    }

    dfs(0)
    return res
}
```

---

## How it works (Subset)

This DFS represents the classic idea:

> For each element, choose it or skip it

Key points:

1. `res.push([...path])` is executed at **every DFS state**
2. There is **no size restriction**
3. Intermediate paths are also final results
4. The empty array `[]` is a valid subset

---

## Subset example

```ts
subsets([1, 2, 3])
```

Result:

```
[]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
```

Total subsets: `2³ = 8`

---

## Time and space complexity (Subset)

* Time complexity:
  **O(2ⁿ)**

* Space complexity:

  * Call stack depth: `O(n)`
  * Result storage: `O(2ⁿ)`

This is expected and unavoidable, since all subsets must be generated.

---

## Summary

* **Combination**

  * Fixed size
  * Push result only when `path.length === k`
  * Time complexity: `O(C(n, k))`

* **Subset (Power set)**

  * No size restriction
  * Push result at every DFS state
  * Time complexity: `O(2ⁿ)`
