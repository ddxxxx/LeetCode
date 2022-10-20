# LeetCode

## 八. 双指针法

### 头尾指针

#### [345. 反转字符串中的元音字母](https://leetcode.cn/problems/reverse-vowels-of-a-string/)（ac)

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



#### [680. 验证回文字符串 Ⅱ](https://leetcode.cn/problems/valid-palindrome-ii/)(ac)

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



#### [15. 三数之和](https://leetcode.cn/problems/3sum/)(ac)

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



#### [16. 最接近的三数之和](https://leetcode.cn/problems/3sum-closest/)(Ac)

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



#### [18. 四数之和](https://leetcode.cn/problems/4sum/)(ac)

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



#### [11. 盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/)(ac)

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

#### [27. 移除元素](https://leetcode.cn/problems/remove-element/)(ac)

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



#### [26. 删除有序数组中的重复项](https://leetcode.cn/problems/remove-duplicates-from-sorted-array/)(ac)

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



#### [80. 删除有序数组中的重复项 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/)(ac)

~~~C++
//我们定义一个指针 kk，表示新数组的末尾，然后从前往后扫描原数组，如果当前数不等于 nums[k]nums[k] 且不等于 nums[k−1]nums[k−1]，则将当前数插入新数组的末尾。
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if(nums.size() < 3) return nums.size();
        int k = 1;
        for (int i = 2; i < nums.size(); i++) {
            if(nums[i] != nums[k-1]){
                nums[++k] = nums[i];
            }
        }
        k++;
        return k;
    }
};
~~~



#### [83. 删除排序链表中的重复元素](https://leetcode.cn/problems/remove-duplicates-from-sorted-list/)(ac)

~~~c++
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(!head) return head;
        auto p = head;
        while(p->next){
            if(p->val == p->next->val) p->next = p->next->next;
            else p = p->next;
        }
        return head;
    }
};
~~~



#### [82. 删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/)(ac)

~~~c++

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(0);
        dummy->next = head;
        ListNode* p = dummy;
        while (p->next)
        {
            ListNode* q = p->next;
            while (q && q->val == p->next->val)
                q = q->next;
            if (p->next->next == q) p = p->next;
            else p->next = q;
        }
        return dummy->next;
    }
};
~~~



#### [187. 重复的DNA序列](https://leetcode.cn/problems/repeated-dna-sequences/)(ac)

~~~c++
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        unordered_map<string,int> hash;
        vector<string> res;
        for(int i = 0; i+10 <= s.size();i++){
            hash[s.substr(i,10)]++;
        }

        for(auto x:hash){
            if(x.second > 1){
                res.push_back(x.first);
            }
        }

        return res;
    }
};
~~~



#### [611. 有效三角形的个数](https://leetcode.cn/problems/valid-triangle-number/)(ac)

~~~c++
class Solution {
public:
    int triangleNumber(vector<int> &nums) {
        int res = 0;
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i - 1, k = 0; j > 0 && k < j; j--) {
                while (k < j && nums[k] + nums[j] <= nums[i]) k++;
                res += j - k;
            }
        }
        return res;
    }
};
~~~



#### [674. 最长连续递增序列](https://leetcode.cn/problems/longest-continuous-increasing-subsequence/)(ac)

~~~c++
// 双指针
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int res = 0;
        for(int i = 0; i < nums.size(); i++){
            int j = i + 1;
            while(j < nums.size() && nums[j] > nums[j-1]) {
                j++;
            }
            res = max(res,j - i);
        }
        return res;
    }
};


// 单调栈
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int res = 0;
        stack<int> stk;
        for( int i = 0; i < nums.size(); i++ ) {
            while(stk.size() && stk.top() >= nums[i]){
                while(stk.size()){
                    stk.pop();
                }
            }
            stk.push(nums[i]);
            res = max(res,(int)stk.size());
        }
        return res;
    }
};
~~~



#### [643. 子数组最大平均数 I](https://leetcode.cn/problems/maximum-average-subarray-i/)(ac)

~~~c++
class Solution {
public:
    double findMaxAverage(vector<int> &nums, int k) {
        double res = -1e5;
        for (int i = 0, sum = 0, j = 0; i < nums.size(); i++) {
            sum += nums[i];
            while (i - j + 1 > k) {
                sum -= nums[j++];
            }
            if (i >= k - 1) res = max(res, sum / (double) k);
        }
        return res;
    }
};
~~~



#### [209. 长度最小的子数组](https://leetcode.cn/problems/minimum-size-subarray-sum/)(ac)

~~~ c++
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int res = INT_MAX;
        for (int i = 0, sum = 0, j = 0; i < nums.size(); i++) {
            sum += nums[i];
            while(sum - nums[j] >= target) sum -= nums[j++];
            if(sum>=target) res = min(res,i-j+1);
        }
        if (res == INT_MAX) res = 0;
        return res;
    }
};
~~~



#### [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/)(ac)

~~~c++
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int res = 0;
        unordered_map<char,int> cnt;
        for(int i = 0, j = 0; i <s.size(); i++){
            cnt[s[i]]++;
            while(cnt[s[i]] > 1){
                cnt[s[j]]--;
                j++;
            }
            res = max(res,i-j+1);
        }
        return res;
    }
};
~~~



#### [438. 找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/)(ac)

~~~c++
class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> res;
        unordered_map<char,int> cnt;
        for(auto x:p){
            cnt[x] ++;
        }

        int tot = cnt.size();

        for(int i = 0, j = 0, satisify = 0; i < s.size(); i++){
            if(--cnt[s[i]] == 0) satisify ++;
            while(i-j+1 > p.size()){
                // 若删之前j字符满足要求，删除之后就不满足要求
                if(cnt[s[j]] == 0){
                    satisify--;
                }
                cnt[s[j++]]++;
            }
            if(satisify == tot) res.push_back(j);
        }
        return res;
    }
};
~~~



#### [567. 字符串的排列](https://leetcode.cn/problems/permutation-in-string/)(ac)

~~~c++
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> cnt;
        for(auto c : s1){
            cnt[c] ++;
        }
        int tot = cnt.size();

        for(int i = 0, j = 0, satisfy = 0; i < s2.size(); i++){
            if(--cnt[s2[i]] == 0) satisfy++;
            while(i - j + 1 > s1.size()){
                if(cnt[s2[j]] == 0){
                    satisfy --;
                }
                cnt[s2[j++]] ++;
            }

            if(satisfy == tot) return true;
        }

        return false;
    }
};
~~~



#### [424. 替换后的最长重复字符](https://leetcode.cn/problems/longest-repeating-character-replacement/)(ac)

~~~c++
class Solution {
public:
    int characterReplacement(string s, int k) {
        int res = 0;
        for (char c = 'A'; c <= 'Z'; c ++){
            int cnt = 0;
            // 对于当前字符c，求出滑动窗口内和c相同字符的个数cnt
            // 当滑动窗口大小减去cnt > k时
            // 更新滑动窗口
            for (int i = 0, j = 0; i < s.size(); i++) {
                if(s[i] == c) cnt ++;
                while (i - j + 1 - cnt > k)
                {
                    // s[j] == c 时，删除s[j],则cnt就要减少
                    if(s[j] == c) cnt--;
                    j++;
                }
                res = max(res,i-j+1);
            }
        }
        return res;
    }
};
~~~



### 分段双指针

#### [86. 分隔链表](https://leetcode.cn/problems/partition-list/)(ac)

~~~c++
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *before = new ListNode(0);
        ListNode *after = new ListNode(0);
        ListNode *pb = before, *pa = after;

        for (ListNode *p = head; p; p = p->next){
            if (p->val < x)
            {
                pb->next = p;
                pb = p;
            }
            else
            {
                pa->next = p;
                pa = p;
            }
        }
        pb->next = after->next;
        pa->next = nullptr;
        return before->next;
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

[133](https://leetcode.cn/problems/clone-graph/)、[695](https://leetcode.cn/problems/max-area-of-island/)、[463](https://leetcode.cn/problems/island-perimeter/)、[542](https://leetcode.cn/problems/01-matrix/)、[130](https://leetcode.cn/problems/surrounded-regions/)、[417](https://leetcode.cn/problems/pacific-atlantic-water-flow/)、[529](https://leetcode.cn/problems/minesweeper/)、[127](https://leetcode.cn/problems/word-ladder/)、[126](https://leetcode.cn/problems/word-ladder-ii/)、[433](https://leetcode.cn/problems/minimum-genetic-mutation/)、[675](https://leetcode.cn/problems/cut-off-trees-for-golf-event/)

#### [200. 岛屿数量](https://leetcode.cn/problems/number-of-islands/)

~~~c++
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int cnt = 0;
        int n = grid.size(), m = grid[0].size();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(grid[i][j] == '1'){
                    cnt++;
                    bfs(i,j,grid);
                }
            }
        }
        return cnt;
    }

    void bfs(int i, int j, vector<vector<char>>& grid){
        int n = grid.size(), m = grid[0].size();
        int dx[4] = {0,-1,0,1}, dy[4] = {-1,0,1,0};
        grid[i][j] = '0';
        queue<pair<int,int>> q;
        q.push({i,j});
        while(q.size()){
            auto t = q.front();
            q.pop();
            int x = t.first, y = t.second;
            for(int i = 0; i < 4; i++){
                int a = x + dx[i], b = y + dy[i];
                if(a >= 0 && a < n && b >=0 && b < m && grid[a][b] == '1'){
                    grid[a][b] = '0';
                    q.push({a,b});
                }
            }
        }
    }
};
~~~



#### [130. 被围绕的区域](https://leetcode.cn/problems/surrounded-regions/)

~~~c++
class Solution {
public:
    vector<vector<bool>> st;
    void solve(vector<vector<char>>& board) {
        int n = board.size(),m = board[0].size();
        
        for(int i = 0; i < n; i++){
            vector<bool> tmp;
            for(int j = 0; j < m; j++ ){
                tmp.push_back(false);
            }
            st.push_back(tmp);
        }

        for(int i = 0;i < n;i++){
            if(board[i][0] == 'O') bfs(i,0,board);
            if(board[i][m-1] == 'O') bfs(i,m-1,board);
        }

        for(int i = 0; i < m; i++){

            if(board[0][i] == 'O') bfs(0,i,board);
            if(board[n-1][i] == 'O') bfs(n-1,i,board);
        }
        
        for(int i= 0; i < n; i++){
            for(int j = 0; j < m; j++){
                if(st[i][j] == false){
                    board[i][j] = 'X';
                }
            }
        }
    }

    void bfs(int i, int j, vector<vector<char>>& board){
        int n = board.size(),m = board[0].size();
        st[i][j] = true;
        int dx[4] = {-1,0,1,0},dy[4] = {0,1,0,-1};
        queue<pair<int,int>> q;
        q.push({i,j});
        while(q.size()){
            auto t = q.front();
            q.pop();
            int x = t.first, y = t.second;
            for(int i =0; i < 4;i ++){
                int a = x + dx[i], b = y + dy[i];
                if(a >=0 && a < n && b >= 0 && b < m && board[a][b] == 'O' && !st[a][b]){
                    st[a][b] = true;
                    q.push({a,b});
                }
            }
        }
    }
};
~~~



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

