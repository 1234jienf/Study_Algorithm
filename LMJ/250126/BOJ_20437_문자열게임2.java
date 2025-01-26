import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ_20437_문자열게임2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc <= T; tc++) {
			// 입력
			String s = br.readLine();
			int k = Integer.parseInt(br.readLine());
			int N = s.length();

			// k가 1일 때
			if (k == 1) {
				System.out.println("1 1");
				continue;
			}

			// 알파벨 별 개수 저장
			int[] alpha = new int[26];
			for (int i = 0; i < N; i++) {
				alpha[s.charAt(i) - 'a']++;
			}

			int min = Integer.MAX_VALUE;
			int max = -1;
			for (int i = 0; i < N; i++) {
				if(alpha[s.charAt(i)-'a']<k) continue;
				
				int count = 1;
				for(int j = i+1; j<N; j++) {
					if(s.charAt(i)==s.charAt(j)) count++;
					// 어떤 문자가 정확히 k개라면 정답 갱신
					if(count == k) {
						min = Math.min(min, j-i+1);
						max = Math.max(max, j-i+1);
						break;
					}
				}
			}
			if(min==Integer.MAX_VALUE || max == -1) System.out.println("-1");
			else System.out.println(min + " " + max);
		}
		br.close();
	}
}
