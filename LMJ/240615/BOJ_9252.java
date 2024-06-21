import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

// Baekjoon_9252_LCS2
public class BOJ_9252 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String a = br.readLine();
		String b = br.readLine();
		int N = a.length();
		int M = b.length();
		String ans = "";

		int[][] dp = new int[N+1][M+1];
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= M; j++) {
				if(a.charAt(i-1)==b.charAt(j-1)) {
					dp[i][j] = dp[i-1][j-1] + 1;
				}
				else {
					dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
				}
			}
		}
		
		Stack<Character> s = new Stack<>();
		int now = dp[N][M];
		int x = N, y = M;
		
		while(x>0 && y>0 && now>0) {
			if(dp[x-1][y]==now)
				x--;
			else if(dp[x][y-1]==now)
				y--;
			else {
				x--;
				y--;
				now--;
				s.push(a.charAt(x));
			}
		}
		
		while(!s.isEmpty()) {
			ans+=s.pop();
		}
		
		System.out.println(dp[N][M]);
		System.out.println(ans);
		
	}
}
