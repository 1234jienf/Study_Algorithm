package 자율팀스터디.d240810;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class BOJ_1644 {
	static boolean[] chae = new boolean[4000001];
	static List<Integer> primes = new ArrayList<>();

	public static void main(String[] args) throws Exception {
		int num;
		for (int i = 2; i < chae.length; i++) {
			if (!chae[i]) {
				primes.add(i);
				for (int j = 2; j <= 4000000; j++) {
					num = i * j;
					if (num <= 4000000) {
						chae[num] = true;
					}
					else {
						break;
					}
				}
			}
		}

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		num = Integer.parseInt(br.readLine());

		int l = 0;
		int r = 1;
		int sum = primes.get(0);
		int count = 0;
		while (l < r) {
			if (sum < num) {
				if (r == primes.size()) break;
				sum += primes.get(r++);
			} else if (sum == num) {
				count++;
				if (r == primes.size()) break;
				sum += primes.get(r++);
			}
			else {
				sum -= primes.get(l++);
			}
		}
		System.out.println(count);
	}
}