import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10986_나머지합 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		long result = 0;
		long[] sum = new long[N + 1]; 
		long[] cnt = new long[M];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i <= N; i++) {
			sum[i] = (sum[i - 1] + Integer.parseInt(st.nextToken())) % M;
        }
		
        for(int i=0; i<=N; i++) {
            cnt[(int)sum[i]]++;
        }
        
        for(long c : cnt) {
        	if(c>1) {
        		result += (c*(c-1))/2;
        	}
        }
		System.out.println(result);

	}
}
