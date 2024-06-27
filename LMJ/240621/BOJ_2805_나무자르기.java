import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//이분탐색
public class BOJ_2805_나무자르기 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int start = 0, end = 0, target = 0;

		st = new StringTokenizer(br.readLine());
		int[] tree = new int[N];
		for (int i = 0; i < N; i++) {
			tree[i] = Integer.parseInt(st.nextToken());
			end = Math.max(end, tree[i]);
		}
		
		while(start<=end) {
			int mid = (start+end)/2;
			long sum = 0;
			
			for(int i = 0; i<N;i++) {
				if(tree[i]>mid) {
					sum+=tree[i]-mid;
				}
			}
			
			if(sum>=M) {
				target = Math.max(mid, target);
				start=mid+1;
			}else {
				end = mid-1;
			}
		}
		
		System.out.println(end);
	}
}
