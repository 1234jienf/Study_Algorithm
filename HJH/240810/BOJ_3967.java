package 자율팀스터디.d240810;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class BOJ_3967 {
	static int[] star = new int[12];
	static int si = 0;
	static Set<Integer> nums;
	static int[][] lines = new int[][] {
		new int[] {1, 2, 3, 4},
		new int[] {1, 5, 8, 11},
		new int[] {4, 6, 9, 11},
		new int[] {0, 2, 5, 7},
		new int[] {0, 3, 6, 10},
		new int[] {7, 8, 9, 10},
	};

	public static int ti(char c) {
		if (c == 'x') return -1;
		return c - 'A' + 1;
	}

	public static void extract(String s, int index) {
		star[si++] = ti(s.charAt(index));
		nums.remove(star[si-1]);
	}

	private static boolean valid() {
		for (int[] line : lines) {
			int sum = 0;
			for (int dot : line) {
				sum += star[dot];
			}
			if (sum != 26) return false;
		}
		return true;
	}

	public static void dfs(int depth) {
		if (depth == 12) {
			if (valid()) {
				show();
				System.exit(0);
			}
			return;
		}
		if (star[depth] != -1) {
			dfs(depth + 1);
			return;
		}
		for (int i = 1; i <= 12; i++) {
			if (nums.contains(i)) {
				nums.remove(i);
				star[depth] = i;
				dfs(depth + 1);
				star[depth] = -1;
				nums.add(i);
			}
		}
	}

	private static char tc(int starNum) {
		return (char)(starNum - 1 + 'A');
	}

	private static void show() {
		System.out.printf("....%c....\n", tc(star[0]));
		System.out.printf(".%c.%c.%c.%c.\n", tc(star[1]), tc(star[2]), tc(star[3]), tc(star[4]));
		System.out.printf("..%c...%c..\n", tc(star[5]), tc(star[6]));
		System.out.printf(".%c.%c.%c.%c.\n", tc(star[7]), tc(star[8]), tc(star[9]), tc(star[10]));
		System.out.printf("....%c....\n", tc(star[11]));
	}

	// 네 개의 점 중 하나만 -1일 때 채워주는 함수
	private static boolean fillLine(int[] line) {
		int counter = 0;
		int negative = -1;
		int sum = 0;
		for (int dot : line) {
			if (star[dot] == -1) {
				counter += 1;
				negative = dot;
			}
			else {
				sum += star[dot];
			}
		}
		if (counter == 1) {
			nums.remove(26-sum);
			star[negative] = 26 - sum;
			return true;
		}
		return false;
	}

	private static void fill() {
		for (int i = 0; i < 6; i++) {
			boolean result = fillLine(lines[i]);
			if (result) i = -1;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		nums = new HashSet<>();
		for (int i = 1; i <= 12; i++) {
			nums.add(i);
		}

		String s;
		s = br.readLine();
		extract(s, 4);

		s = br.readLine();
		extract(s, 1);
		extract(s, 3);
		extract(s, 5);
		extract(s, 7);

		s = br.readLine();
		extract(s, 2);
		extract(s, 6);

		s = br.readLine();
		extract(s, 1);
		extract(s, 3);
		extract(s, 5);
		extract(s, 7);

		s = br.readLine();
		extract(s, 4);

		fill();
		dfs(0);
	}

}