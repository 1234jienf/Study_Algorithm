import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//Baekjoon_1105_팔
public class BOJ_1105 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		String a = st.nextToken();
		String b = st.nextToken();

		int ans = 0;

		if (a.length() == b.length()) {
			for (int i = 0; i < a.length(); i++) {
				if(a.charAt(i)==b.charAt(i)) {
					if(a.charAt(i)=='8')
						ans++;
				}
				else {
					break;
				}
			}
		}
		
		System.out.println(ans);

	}
}
