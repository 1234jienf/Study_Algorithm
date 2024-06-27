import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// 한자리수: 1 ~ 9, 9개, 9글자
// 두자리수: 10 ~ 99, 90개, 180글자
// 세자리수: 100 ~ 999, 900개, 2700글자
public class BOJ_1790_수이어쓰기2 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());

		long numLen = 1; // 자릿수
		long numCnt = 9; // 글자수

		while (k > numLen * numCnt) {
			k -= numLen * numCnt;
			numLen++;
			numCnt *= 10;
		}
		
		k--; //k가 0부터 시작할 수 있도록
		long target = (long)Math.pow(10, (numLen-1)) + (k/numLen); //찾는 숫자
//		System.out.println(target);
		if (target > N) {
			System.out.println(-1);
		} else {
			int idx = (int) (k % numLen);
			System.out.println(String.valueOf(target).charAt(idx));
		}

	}
}
