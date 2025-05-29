# Write your code here
import numpy
n = int(input())
a = list(map(int,input().split()))
sum = [0]
for num in a:
    sum.append(sum[-1]+num)
dp = [[[-1e30,-1e30] for _ in range(n)] for j in range(n)]
def solve(i,j,p):
    # print(i,j,p)
    if(i==j):
        dp[i][j][p]=a[i]
        return
    if dp[i][j][p]!=-1e30:
        return 
    # fremoval = a[i]
    opp = (p+1)%2
    solve(i+1,j,opp)
    solve(i,j-1,opp)
    if(dp[i+1][j][opp] > dp[i][j-1][opp]):
        dp[i][j][p] =sum[j+1]-sum[i]-dp[i][j-1][opp]
    else:
        dp[i][j][p] =sum[j+1]-sum[i]-dp[i+1][j][opp]
    
    return 

solve(0,n-1,0)

tot_sum = sum[n]
if dp[0][n-1][0] > tot_sum-dp[0][n-1][0]:
    print("Player 1 wins")
elif dp[0][n-1][0] == tot_sum-dp[0][n-1][0]:
    print("Its a draw")
else:
    print("Player 2 wins")