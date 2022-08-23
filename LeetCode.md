# LeetCode

## 八. 双指针法

### 头尾指针

#### [345. 反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/)

~~~c++
class Solution {
public:
string reverseVowels(string str) {
    unordered_set<char> ss = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
    for (int i = 0, j = str.size() - 1; i < j;) {

        while (i < j && ss.find(str[j]) == ss.end()) {
            j--;
        }
        while (i < j && ss.find(str[i]) == ss.end()) {
            i++;
        }
        if (i < j) swap(s[i], s[j]);
        i ++, j -- ;
        }
        return str;
    }
};
~~~



#### [680. 验证回文字符串 Ⅱ](https://leetcode.cn/problems/valid-palindrome-ii/)

~~~c++
class Solution {
public:
    bool check(string& s, int i, int j) {
        while (i < j) {
            if (s[i] != s[j]) return false;
            i ++, j -- ;
        }
        return true;
    }

    bool validPalindrome(string s) {
        for (int i = 0, j = s.size() - 1; i < j; i ++, j -- )
            if (s[i] != s[j]) {
                if (check(s, i + 1, j) || check(s, i, j - 1)) return true;
                return false;
            }
        return true;
    }
};

~~~



#### [15. 三数之和](https://leetcode.cn/problems/3sum/)

~~~c++
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        vector<vector<int>> res;
        for(int i = 0; i < nums.size();i++){
            if(i && nums[i-1] == nums[i]) continue;
            for(int j = i + 1,k = nums.size()- 1; j < k; j++){
                if (j > i + 1 && nums[j - 1] == nums[j]) continue;
                //查找满足要求的最小k
                //试探法,如果k的下一个数满足要求,就使用下一个k
                while (j < k - 1 && nums[i] + nums[j] + nums[k - 1] >= 0) k--;
                if(nums[i] + nums[j] + nums[k] == 0){
                    res.push_back({nums[i],nums[j],nums[k]});
                }
            }
        }
        return res;
    }
};	
~~~



#### [16. 最接近的三数之和](https://leetcode.cn/problems/3sum-closest/)

~~~c++
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin() ,nums.end());
        pair<int, int> res = {INT_MAX,INT_MAX};
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i+1, k = nums.size() -1; j < k; j++) {
                while (k - 1 > j && nums[i] + nums[j] + nums[k - 1] >= target) {
                    k--;
                }
                int s = nums[i] + nums[j] + nums[k];
                res = min(res, make_pair(abs(s - target), s));
                if (k - 1 > j) {
                    int s = nums[i] + nums[j] + nums[k - 1];
                    res = min(res, make_pair(abs(s - target), s));
                } 
            }
        }
        return res.second;
    }
};
~~~



#### [18. 四数之和](https://leetcode.cn/problems/4sum/)

~~~c++
class Solution {
public:
    vector<vector<int>> fourSum(vector<int> &nums, int target) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); i++) {
            if (i && nums[i] == nums[i - 1]) continue;
            for (int j = i + 1; j < nums.size(); ++j) {
                if (j > i + 1 && nums[j - 1] == nums[j]) continue;
                for (int k = j + 1, u = nums.size() - 1; k < u; k++) {
                    if (k > j + 1 && nums[k - 1] == nums[k]) continue;
                    while (u - 1 > k && (long long)nums[i] + nums[j] + nums[k] + nums[u - 1] >= target) {
                        u--;
                    }
                    if ((long long )nums[i] + nums[j] + nums[k] == target - nums[u]) {
                        res.push_back({nums[i], nums[j], nums[k], nums[u]});
                    }
                }
            }
        }
        return res;
    }
};
~~~



#### [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)

~~~c++
class Solution {
public:
    int maxArea(vector<int> &nums) {
        int res = 0;
        for (int i = 0, j = nums.size() - 1; i < j;) {
            res = max(res, min(nums[i], nums[j]) * (j - i));
            if (nums[i] < nums[j]) {
                i++;
            } else {
                j--;
            }
        }
        return res;
    }
};
~~~



### 同向双指针、滑动窗口

#### [27. 移除元素](https://leetcode.cn/problems/remove-element/)

~~~c+
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int k = 0;
        for(int i = 0; i < nums.size();i++){
            if(nums[i]!= val){
                nums[k++] = nums[i];
            }
        }
        return k;
    }
};
~~~



#### [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)

~~~c++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        int k = 0;
        for(int i = 0; i < nums.size();i++){
            if(nums[k] != nums[i]) 
            nums[++k] = nums[i];
        }
        return k + 1;
    }
};
~~~



## 十. 图与搜索

### 图的建立与应用

[565](https://leetcode.cn/problems/array-nesting/)

### 深度优先搜索

#### [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/)(ac)

~~~c++
class Solution {
public:
    vector<string> ans;
    string path ="";

    string strs[10] = {
        "", "", "abc", "def",
        "ghi", "jkl", "mno",
        "pqrs", "tuv", "wxyz",
    };
    vector<string> letterCombinations(string digits) {
        if(digits.empty()) return ans;
        dfs(digits,0);
        return ans;
    }

    void dfs(string& digits,int u){
        if(u == digits.size()){
            ans.push_back(path);
            return;
        }
        for(auto& x :strs[digits[u] - '0']){
            path.push_back(x);
            dfs(digits,u+1);
            path.pop_back();
        }
    }

};
~~~



#### [397. 整数替换](https://leetcode.cn/problems/integer-replacement/)(ac)

~~~c++
class Solution {
public:
    typedef long long LL;
    int integerReplacement(int n) {
        return dfs(n);
    }

    int dfs(LL n){
        if(n == 1) return 0;
        if(n%2 == 0) return dfs(n/2) + 1;
        return min(dfs(n-1),dfs(n+1)) + 1;
    }
};
~~~



### 回溯法

#### [526. 优美的排列](https://leetcode.cn/problems/beautiful-arrangement/)(ac)

~~~C++

class Solution {
public:
    int res = 0;
    vector<bool> st;
    int countArrangement(int n) {
        st  =vector<bool> (n+1,false);
        dfs(n,1);
        return res;
    }
    
    void dfs(int n,int u){
        if(u == n + 1){
            res++;
            return;
        }

        for(int i = 1;i <=n;i++){
            if(!st[i] && (i%u == 0 || u%i == 0)){
                st[i] = true;
                dfs(n,u+1);
                st[i] = false;
            }
        }
    }
};
~~~



#### [401. 二进制手表](https://leetcode.cn/problems/binary-watch/)

#### [36. 有效的数独](https://leetcode.cn/problems/valid-sudoku/)

#### [37. 解数独](https://leetcode.cn/problems/sudoku-solver/)

#### [51](https://leetcode.cn/problems/n-queens/)、[52](https://leetcode.cn/problems/n-queens-ii/)、[77](https://leetcode.cn/problems/combinations/)、[39](https://leetcode.cn/problems/combination-sum/)、[216](https://leetcode.cn/problems/combination-sum-iii/)、[40](https://leetcode.cn/problems/combination-sum-ii/)、[46](https://leetcode.cn/problems/permutations/)、[47](https://leetcode.cn/problems/permutations-ii/)、[31](https://leetcode.cn/problems/next-permutation/)、[556](https://leetcode.cn/problems/next-greater-element-iii/)、[60](https://leetcode.cn/problems/permutation-sequence/)、[491](https://leetcode.cn/problems/increasing-subsequences/)、[78](https://leetcode.cn/problems/subsets/)、[90](https://leetcode.cn/problems/subsets-ii/)、[79](https://leetcode.cn/problems/word-search/)、[93](https://leetcode.cn/problems/restore-ip-addresses/)、[332](https://leetcode.cn/problems/reconstruct-itinerary/)

### 回溯法与表达式

[241](https://leetcode.cn/problems/different-ways-to-add-parentheses/)、[282](https://leetcode.cn/problems/expression-add-operators/)、[679](https://leetcode.cn/problems/24-game/)

### 回溯法与括号

[ 22](https://leetcode.cn/problems/generate-parentheses/)、[301](https://leetcode.cn/problems/remove-invalid-parentheses/)

### 回溯法与贪心

[ 488](https://leetcode.cn/problems/zuma-game/)

### 广度优先搜索

[133](https://leetcode.cn/problems/clone-graph/)、[200](https://leetcode.cn/problems/number-of-islands/)、[695](https://leetcode.cn/problems/max-area-of-island/)、[463](https://leetcode.cn/problems/island-perimeter/)、[542](https://leetcode.cn/problems/01-matrix/)、[130](https://leetcode.cn/problems/surrounded-regions/)、[417](https://leetcode.cn/problems/pacific-atlantic-water-flow/)、[529](https://leetcode.cn/problems/minesweeper/)、[127](https://leetcode.cn/problems/word-ladder/)、[126](https://leetcode.cn/problems/word-ladder-ii/)、[433](https://leetcode.cn/problems/minimum-genetic-mutation/)、[675](https://leetcode.cn/problems/cut-off-trees-for-golf-event/)

### 并查集

#### [547. 省份数量](https://leetcode.cn/problems/number-of-provinces/)(ac)

~~~c++
class Solution {
public:
    vector<int> p;
    int find(int x){
        if(p[x]!=x) p[x] = find(p[x]);
        return p[x];
    }
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n  = isConnected.size();
        for(int i = 0; i < n; i++){
            p.push_back(i);
        }
        int res = n;
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(isConnected[i][j] && find(i) != find(j)){
                    p[find(i)] = find(j);
                    res--;               
                }
            }
        }
        return res;
    }
};
~~~



#### [684. 冗余连接](https://leetcode.cn/problems/redundant-connection/)(ac)

~~~c++
class Solution {
public:
    vector<int> p;
    int find(int x){
        if(x!=p[x]) p[x] = find(x);
        return p[x];
    }
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        p.resize(n+1);
        for(int i = 1; i<= n; i++){
            p[i] = i;
        }

        for(auto& e :edges){
            int a = find(e[0]),  b = find(e[1]);
            if(a!=b) p[a] = b;
            else return e;            
        }

        return {};
    }
};
~~~



#### [685. 冗余连接 II](https://leetcode.cn/problems/redundant-connection-ii/)

### 拓扑排序

[ 399](https://leetcode.cn/problems/evaluate-division/)、[207](https://leetcode.cn/problems/course-schedule/)、[210](https://leetcode.cn/problems/course-schedule-ii/)

## 十一. 二分查找

### 二分查找应用(简单)

#### [374. 猜数字大小](https://leetcode.cn/problems/guess-number-higher-or-lower/)(ac)

~~~c++
图的建立与应用	class Solution {
public:
    int guessNumber(int n) {
        int l = 1, r = n;
        while(l < r)
        {
            int mid = (long long) l + r >> 1;
            if(guess(mid) <=0 ){
                r = mid;
            }else{
                l = mid + 1;
            }
            

        }
        return l;
    }
};
~~~



#### [35. 搜索插入位置](https://leetcode.cn/problems/search-insert-position/)(ac)

~~~c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int l = 0 ,r = nums.size()-1;
        while(l < r){
            int mid = l + r >> 1;
            if(nums[mid] >= target) r = mid;
            else l = mid+1;
        }
        if(nums[l] <  target) return l + 1;
        else return l;
    }
};
~~~



#### [278. 第一个错误的版本](https://leetcode.cn/problems/first-bad-version/)(ac)

~~~C++
class Solution {
public:
    int firstBadVersion(int n) {
        int l =0, r=n;
        while(l < r){
            int mid = l + (r-l)/2;
            if(isBadVersion(mid)) r = mid;
            else l = mid + 1;
        }
        return l;
    }
};
~~~



#### [367. 有效的完全平方数](https://leetcode.cn/problems/valid-perfect-square/)(ac)

~~~c++
class Solution {
public:
    bool isPerfectSquare(int num) {
        int l = 1, r = num;
        while(l < r)
        {
            int mid = (l + 1ll + r) >> 1;
            if(mid <= num/mid) l = mid;
            else r = mid - 1;
        }
        return r*r == num;
    }
};
~~~



#### [69. x 的平方根 ](https://leetcode.cn/problems/sqrtx/)(ac)

~~~c++
class Solution {
public:
    int mySqrt(int x) {
        int l = 0 , r = x;
        while(l < r){
            int mid = l + (r - l) /2 + 1;
            if(mid <= x/mid ) l = mid;
            else r = mid - 1;
        }
        return r;
    }
};
~~~



#### [441. 排列硬币](https://leetcode.cn/problems/arranging-coins/)(ac)

~~~c++
class Solution {
public:
    int arrangeCoins(int n) {
        long l = 1, r = n;
        
        while(l < r){
            long mid = l + r + 1 >> 1;
            if(((1+mid)*mid >> 1 ) < n) l = mid;
            else if ((1+mid)*mid >> 1 == n ) return mid;
            else r = mid -1;
        }
        return l;
    }
};
~~~



### 二分查找应用(中等)

#### [34. 在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/)(ac)

~~~c++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if(nums.empty()) return {-1,-1};
        int l = 0 ,r = nums.size()-1;
        
        while(l < r){
            int mid = l + r >> 1;
            if(nums[mid] >= target) r = mid;
            else l = mid+1;
        }
        int L = l;
        l = 0 ,r = nums.size()-1;
        while(l < r){
            int mid = l + r + 1 >> 1;
            if(nums[mid] <= target) l = mid;
            else r = mid - 1;
        }
        int R = r;
        if(nums[L] != target){
            L = -1;
        }
        if(nums[R] != target){
            R = -1;
        }
        return vector<int> {L,R};
        cout << L << ' ' << R;
    }
};
~~~



#### [540. 有序数组中的单一元素](https://leetcode.cn/problems/single-element-in-a-sorted-array/)(ac)

~~~c++
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        nums.push_back(nums.back()+1);
        // 将数组按对分组
        //对组号二分
        int l = 0, r= nums.size() /2 -1;
        while(l<r){
            int mid = l + r >> 1;
            if(nums[mid*2] != nums[mid*2+1]) r = mid;
            else l = mid + 1;
        }
        return nums[l*2];
    }
};
~~~



#### [275. H 指数 II](https://leetcode.cn/problems/h-index-ii/)

#### [436. 寻找右区间](https://leetcode.cn/problems/find-right-interval/)

~~~c++
//在区间数组中记录下标，并排序
//二分查找第一个比右端点大的区间
class Solution {
public:
    vector<int> findRightInterval(vector<vector<int>>& q) {
        int n = q.size();
        for(int i = 0; i < n; i++) q[i].push_back(i);
        sort(q.begin(),q.end());
        vector<int> res(n,-1);
        for(auto& x : q){
            int l = 0, r = n - 1;
            while(l < r){
                int mid = l + r >> 1;
                if(q[mid][0] >= x[1]) r = mid;
                else l = mid + 1;
            }
            if(q[r][0] >= x[1]) res[x[2]] = q[r][2];
        }
        return res;
    }
};
~~~



#### [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

#### [354. 俄罗斯套娃信封问题](https://leetcode.cn/problems/russian-doll-envelopes/)

#### [658. 找到 K 个最接近的元素](https://leetcode.cn/problems/find-k-closest-elements/)（ac)

~~~c++
// 堆
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        priority_queue<pair<int,int>> q;
        for(auto a:arr){
            q.push({abs(a-x),a});
            if(q.size() > k){
                q.pop();
            }
        }
        vector<int> res;
        while(q.size()){
            res.push_back(q.top().second);
            q.pop();
        }
        sort(res.begin(),res.end());
        return res;
    }
};

//
class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int T) {
        int l = 0, r = arr.size() - 1;
        while(l < r){
            int mid = l + r >> 1;
            if(arr[mid] >=T) r = mid;
            else l = mid + 1;
        }
        if(r){
            int x = arr[r-1], y = arr[r];
            if(make_pair(abs(x-T),x) < make_pair(abs(y-T),y)){
                r--;
            }
        }

        int i = r , j = r;
        for(int u = 0; u < k-1;u++){
            if(i-1 < 0) j++;
            else if (j + 1 >= arr.size()) i--;
            else{
                int x = arr[i-1],y = arr[j+1];
                if(make_pair(abs(x-T),x) < make_pair(abs(y-T),y)){
                    i--;
                }else{
                    j++;
                }
            }
        }
        vector<int> res;
        for(int u = i; u <=j; u++){
            res.push_back(arr[u]);
        }
        return res;
    }
};
~~~

#### [162. 寻找峰值](https://leetcode.cn/problems/find-peak-element/)(ac)

~~~c++
//寻找下落点
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while(l < r ){
            int mid = l + r >> 1;
            if(nums[mid] > nums[mid + 1]) r = mid;
            else l = mid + 1; 
        }
        return l;
    }
};
~~~



[4](https://leetcode.cn/problems/median-of-two-sorted-arrays/)

### 二分查找与旋转数组

#### [153. 寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/)(ac)

~~~c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r= nums.size() - 1;
        while(l < r){
            int mid = l + r + 1 >> 1;
            if(nums[mid] >=nums[0]) l = mid;
            else r = mid - 1;
        }
        if(r == nums.size()-1){
            return  nums[0];
        }else{
            return nums[r+1];
        }
    }
};
~~~



#### [154. 寻找旋转排序数组中的最小值 II](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array-ii/)(ac)

~~~c++
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        //去掉右边可能与左边重复数
        while(l < r &&nums[0] == nums[r]) r--;
        while(l<r){
            int mid = l + r + 1>> 1;
            if(nums[mid] >= nums[0]) l = mid;
            else r = mid - 1;
        }
        if(r < nums.size() - 1){
            return nums[r + 1];
        }else {
            return nums[0];
        }
    }
};
~~~



#### [33. 搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/)(ac)

~~~c++
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0, r = nums.size() - 1;
            while (l < r) {
                int mid = (l + r + 1) >> 1;
                if (nums[mid] >= nums[0]) l = mid;
                else r = mid - 1;
            }

            if (target >= nums[0]) {
                l = 0;
            } else {
                l = r + 1, r = nums.size() - 1;
            }
            while (l < r) {
                int mid = (l + r )>> 1;
                if (nums[mid] >= target) {
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }

            if (nums[r] == target) return r;
            return -1;
    }
};
~~~



#### [81. 搜索旋转排序数组 II](https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/)(ac)

~~~c++
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int l = 0, r = nums.size()-1;
        while(l < r&& nums[r] == nums[0]) r--;
        int R = r;
        while(l < r){
            int mid = l + r  + 1 >> 1;
            if(nums[mid] >= nums[0]) l = mid;
            else r = mid - 1;
        }
        if(target >= nums[0]){
            l = 0;
        }else{
            l = r + 1, r = R;
        }

        while(l < r){
            int mid = l + r >> 1;
            if(nums[mid] >=target) r = mid;
            else l = mid + 1;
        }
        if(nums[r]  == target) return true;
        else return false;
    }
};
~~~



### 二分查找与矩阵

#### [74. 搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/)(ac)

~~~c++
//按行展开后就是升序序列，二分即可
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if(matrix.empty() || matrix[0].empty()) return false;
        int n = matrix.size(), m = matrix[0].size();
        int l = 0, r = n*m - 1;
        while(l < r)
        {
            int mid = l + r >> 1;
            if(matrix[mid/m][mid%m] >= target) r = mid;
            else l = mid + 1;
        }
        return matrix[l/m][l%m] == target;

    }
};
~~~



#### [240. 搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/)(ac)

~~~c++
//对每一行二分，lower_bound：大于等于x的第一个数
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        for(const auto& row :matrix){
            auto it = lower_bound(row.begin(),row.end(),target);
            if(it != row.end() && *it == target) {
                return true;
            }
        }
        return false;
    }
};
~~~



### 二分答案法

[ 378](https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/)
[668](https://leetcode.cn/problems/kth-smallest-number-in-multiplication-table/)
[410](https://leetcode.cn/problems/split-array-largest-sum/)
[483](https://leetcode.cn/problems/smallest-good-base/)

#### [719. 找出第 K 小的数对距离](https://leetcode.cn/problems/find-k-th-smallest-pair-distance/)

