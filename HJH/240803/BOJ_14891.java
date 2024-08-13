import java.io.*;
import java.util.*;

public class Main {
	static int[] gears = new int[4];
	static int n;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int i = 0; i < 4; i++) {
			String gear = br.readLine();
			int num = 0;
			for (char letter : gear.toCharArray()) {
				num <<= 1;
				num |= letter == '1'? 1 : 0;
			}
			gears[i] = num;
		}

		n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			rotate(Integer.parseInt(st.nextToken()) - 1,
				Integer.parseInt(st.nextToken()),
				0);
		}
		int ans = 0;
		for (int i = 3; i >= 0; i--) {
			ans <<= 1;
			ans |= ((gears[i]>>7) & 1);
		}
		System.out.println(ans);
	}

	static void rotate(int ith, int dir, int to) {
		if (to == 0) {
			if (ith - 1 >= 0) {
				if ((extractBit(ith-1, 5) ^ extractBit(ith, 1)) == 1) {
					rotate(ith - 1, -dir, -1);
				}
			}
			if (ith + 1 < 4) {
				if ((extractBit(ith, 5) ^ extractBit(ith + 1, 1)) == 1) {
					rotate(ith + 1, -dir, 1);
				}
			}
		}
		else if (to == -1) {
			if (ith - 1 >= 0) {
				if ((extractBit(ith-1, 5) ^ extractBit(ith, 1)) == 1) {
					rotate(ith - 1, -dir, to);
				}
			}
		}
		else {
			if (ith + 1 < 4) {
				if ((extractBit(ith, 5) ^ extractBit(ith + 1, 1)) == 1) {
					rotate(ith + 1, -dir, to);
				}
			}
		}

		rotateGear(ith, dir);
	}

	private static void rotateGear(int ith, int dir) {
		int from = -1, to = -1;
		int tmp = 0;
		if (dir == 1) {
			from = 0; to = 7;
		}
		else {
			from = 7; to = 0;
		}
		tmp = gears[ith] >> from & 1;
		if (dir == 1) gears[ith] >>= 1;
		else {
			gears[ith] &= ~(1 << 7);
			gears[ith] <<= 1;
		}
		gears[ith] |= (tmp << to);
	}

	// ith 번째 기어의 jth 번째 이진수가 1인지 0인지
	// 짜다보니 비효율의 끝판왕
	static int extractBit(int ith, int jth) {
		return (gears[ith] >> jth) & 1;
	}

}