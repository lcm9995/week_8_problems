class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_val = amount +1
        arr = [max_val]*(max_val)
        arr[0]=0 #base case
        for coin in coins:
            for x in range(coin, max_val):
                arr[x]=min(arr[x], arr[x-coin]+1)
        if arr[amount] != max_val:
            return arr[amount] 
        return -1