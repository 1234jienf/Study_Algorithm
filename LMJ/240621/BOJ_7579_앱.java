import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_7579_앱 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[] memory = new int[N+1];
		int[] cost = new int[N+1];
		int sum = 0;

		StringTokenizer st1 = new StringTokenizer(br.readLine());
		StringTokenizer st2 = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			memory[i] = Integer.parseInt(st1.nextToken());
			cost[i] = Integer.parseInt(st2.nextToken());
			sum += cost[i];
		}

		int[][] dp = new int[sum+1][N+1];

		// 최대비용 i로 메모리를 최대한 사용한다
		for (int j = 1; j <= N; j++) {
			//최대비용 i
			for (int i = 0; i <= sum; i++) {
				if(i>=cost[j]) {
					dp[i][j] = Math.max(memory[j]+dp[i-cost[j]][j-1], dp[i][j-1]);
				} else {
					dp[i][j] = dp[i][j-1];
				}
			}
		}
		
		for(int i = 0; i<=sum;i++) {
			if(dp[i][N]>=M) {
				System.out.println(i);
				break;
			}
		}
		
		br.close();

	}
}
