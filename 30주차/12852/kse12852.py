n=int(input())

dp = [i for i in range(n+1)]

for i in range(2,n+1):
    if i%2 ==0:
        dp[i]=min(dp[i], dp[i//2])
    if i%3 ==0:
        dp[i]=min(dp[i], dp[i//3])
    dp[i]=min(dp[i],dp[i-1])+1

print(dp[n]-1)

while not n==0:
    print(n, end=' ')
    if dp[n] == dp[n-1]+1:
        n=n-1
    elif n%2==0 and dp[n]==dp[n//2]+1:
        n=n//2
    elif n%3==0 and dp[n]==dp[n//3]+1:
        n=n//3

"""
12345678910
1223433434
"""