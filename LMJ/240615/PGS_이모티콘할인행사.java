import java.io.*;
import java.util.*;

class PGS_이모티콘할인행사 {
    static int N, ans, sum;
    static int[] discount, emoticons;
    static int[][] users;
    public int[] solution(int[][] u, int[] e) {
        N = e.length;
        ans = 0;
        sum = 0;
        discount = new int[N];
        users = u;
        emoticons = e;
        
        dfs(0);
        
        return new int[]{ans,sum};
    }
    
    static void dfs(int x){
        if(x==N){
            simulation();
            return;
        }
        for(int i = 10; i <= 40; i+=10){
            discount[x] = i;
            dfs(x+1);
        }
    }
    
    static void simulation(){
        int tmpAns = 0;
        int tmpSum = 0;
        for(int[] user: users){
            int tmp = 0;
            for(int i=0; i<N;i++){
                if(discount[i]>=user[0]){
                    tmp+=emoticons[i]*(100-discount[i])/100;
                }
            }
            if(tmp>=user[1]){
                tmpAns++;
            }
            else{
                tmpSum+=tmp;
            }
        }
        
        if(tmpAns>ans){
            ans = tmpAns;
            sum = tmpSum;
        } else if(tmpAns==ans && tmpSum > sum){
            sum = tmpSum;
        }
    }
}