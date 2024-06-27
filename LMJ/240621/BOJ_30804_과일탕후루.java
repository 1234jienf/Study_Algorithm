import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_30804_과일탕후루 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine()); // 탕후루 길이
		int[] fruits = new int[N]; // 입력된 탕후루
		Map<Integer, Integer> count = new HashMap<>(); // 종류별 탕후루 개수

		StringTokenizer st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			fruits[i] = Integer.parseInt(st.nextToken());
		}

		int start = 0;
		int ans = 0;

		for (int end = 0; end < N; end++) {
			count.put(fruits[end], count.getOrDefault(fruits[end],0)+1);
			
			while(count.size()>2) {
				count.put(fruits[start], count.get(fruits[start])-1);
				if(count.get(fruits[start])==0) {
					count.remove(fruits[start]);
				}
				start++;
			}
			
			ans = Math.max(ans, end - start + 1);
		}
		
		System.out.println(ans);

	}
}
