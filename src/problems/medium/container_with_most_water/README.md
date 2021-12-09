Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2

Efficient Solution:  

Approach: Given an array of heights of lines of boundaries of the container, find the maximum water that can be stored in a container. So start with the first and last element and check the amount of water that can be contained and store that container. Now the question arises is there any better boundaries or lines that can contain maximum water. So there is a clever way to find that. Initially, there are two indices the first and last index pointing to the first and the last element (which acts as boundaries of the container), if the value of first index is less than the value of last index increase the first index else decrease the last index. As the decrease in width is constant, by following the above process the optimal answer can be reached.

Algorithm: 
Keep two index, first = 0 and last = n-1 and a value max_area that stores the maximum area.
Run a loop until first is less than the last.
Update the max_area with maximum of max_area and min(array[first] , array[last])*(last-first)
if the value at array[first] is greater the array[last] then update last as last – 1 else update first as first + 1
Print the maximum area.

```c++
// C++ code for Max
// Water Container
#include<iostream>
using namespace std;
 
int maxArea(int A[], int len)
{
    int l = 0;
    int r = len -1;
    int area = 0;
     
    while (l < r)
    {
        // Calculating the max area
        area = max(area, min(A[l],
                        A[r]) * (r - l));
                         
            if (A[l] < A[r])
                l += 1;
                 
            else
                r -= 1;
    }
    return area;
}
 
// Driver code
int main()
{
    int a[] = {1, 5, 4, 3};
    int b[] = {3, 1, 2, 4, 5};
     
    int len1 = sizeof(a) / sizeof(a[0]);
    cout << maxArea(a, len1);
     
    int len2 = sizeof(b) / sizeof(b[0]);
    cout << endl << maxArea(b, len2);
}
 
```

```python

# Python3 code for Max
# Water Container
def maxArea( A):
    l = 0
    r = len(A) -1
    area = 0
     
    while l < r:
        # Calculating the max area
        area = max(area, min(A[l],
                        A[r]) * (r - l))
     
        if A[l] < A[r]:
            l += 1
        else:
            r -= 1
    return area
 
# Driver code
a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]
 
print(maxArea(a))
print(maxArea(b))
```