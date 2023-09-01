#include<stdio.h>
int exists_subsets(int set[], int n, int sum)
{
    if (sum == 0)
        return 1;
    if (n == 0)
        return 0;
    if (set[n - 1] > sum)
        return isSubsetSum(set, n - 1, sum);
    return isSubsetSum(set, n - 1, sum)
           || isSubsetSum(set, n - 1, sum - set[n - 1]);
}
    int isSubsetSum(int set[], int sum, int n, int exists_subsets)
    {
        if(exists_subsets == 0){
            printf("-1");
            break;
        }
        bool subset[sum + 1][n + 1];
        int count[sum + 1][n + 1];
 
        for (int i = 0; i <= n; i++)
        {
            subset[0][i] = true;
            count[0][i] = 0;
        }
        for (int i = 1; i <= sum; i++)
        {
            subset[i][0] = false;
            count[i][0] = -1;
        }
 
        for (int i = 1; i <= sum; i++)
        {
            for (int j = 1; j <= n; j++)
            {
                subset[i][j] = subset[i][j - 1];
                count[i][j] = count[i][j - 1];
                if (i >= set[j - 1])
                {
                    subset[i][j] = subset[i][j] ||
                                subset[i - set[j - 1]][j - 1];
 
                    if (subset[i][j])
                        count[i][j] = max(count[i][j - 1],
                                    count[i - set[j - 1]][j - 1] + 1);
                }
            }
        }
 
        return count[sum][n];
    }
 
int main(){
    
}