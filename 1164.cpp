#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <unordered_map>
#include <set>
using namespace std;
typedef long long ll;
const int N = 3e5 + 100;

int n, m;
int dp[N];
int main() {
    cin >> n >> m;
    dp[0] = 1;
    for(int i = 1; i <= n; ++i) {
        int x; cin >> x;
        for(int j = m; j >= x; --j) {
            dp[j] += dp[j - x];
        }
    }
    cout << dp[m] << endl;
    return 0;
}
