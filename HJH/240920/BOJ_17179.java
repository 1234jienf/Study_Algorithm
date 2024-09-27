import java.io.*;
import java.util.*;

public class Main {
	static int n, m, l;
	static int[] cuttable;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());

		cuttable = new int[m + 1];
		for (int i = 0; i < m; i++) {
			cuttable[i] = Integer.parseInt(br.readLine());
		}
		cuttable[m] = l;
		Arrays.sort(cuttable);

		StringBuilder ans = new StringBuilder();
		for (int i = 0; i < n; i++) {
			int num = Integer.parseInt(br.readLine());
			ans.append(sol(num)).append("\n");
		}

		System.out.println(ans);
	}

	private static int sol(int num) {
		int left = 0, right = l + 1;
		int mid;
		while (left + 1 != right) {
			mid = (left + right) / 2;
			if (check(num, mid)) left = mid;
			else right = mid;
		}
		return left;
	}

	// len 길이로 자르면 num개 이상의 조각이 나오는가?
	private static boolean check(int num, int len) {
		num += 1;
		int lastpoint = 0;
		int cnt = 0;
		for (int i = 0; i < cuttable.length; i++) {
			if (cuttable[i] - lastpoint >= len) {
				lastpoint = cuttable[i];
				cnt++;
			}
		}
		return cnt >= num;
	}
}