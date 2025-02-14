package 자율팀스터디.d250209;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_27501 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static ArrayList<Integer>[] graph;
	static int[][] rgb;

	static int[][] dp;
	static int[] colors;

	static int n, a, b;
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());

		// 트리 입력
		graph = new ArrayList[n+1];
		for (int i = 1; i <= n; i++)
			graph[i] = new ArrayList<>();
		for (int i = 1; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			graph[a].add(b);
			graph[b].add(a);
		}

		// rgb 점수 입력
		rgb = new int[n+1][3];
		for (int i = 1; i <= n; i++) {
			st = new StringTokenizer(br.readLine());
			rgb[i][0] = Integer.parseInt(st.nextToken());
			rgb[i][1] = Integer.parseInt(st.nextToken());
			rgb[i][2] = Integer.parseInt(st.nextToken());
		}

		// dp 이용해서 채우기
		dp = new int[n+1][3];
		int rootColor = 0;
		int ans = 0;
		int tmp = 0;
		for (int i = 0; i < 3; i++) {
			tmp = makeDP(0, 1, i);
			if (ans < tmp) {
				rootColor = i;
				ans = tmp;
			}
		}

		// 색깔 복원 dfs
		colors = new int[n+1];
		Arrays.fill(colors, -1);
		colors[1] = rootColor;
		restoreColor(1);

		System.out.println(ans);
		StringBuilder route = new StringBuilder();
		for (int i = 1; i <= n; i++) {
			if (colors[i] == 0) {route.append('R');}
			else if (colors[i] == 1) {route.append('G');}
			else {route.append('B');}
		}
		System.out.println(route);
	}

	private static void restoreColor(int node) {
		int nextColor = 0;
		int nextNextColor = 0;
		for (int next : graph[node]) {
			if (colors[next] != -1) continue;
			nextColor = (colors[node]+1)%3;
			nextNextColor = (colors[node]+2)%3;
			if (dp[next][nextColor] > dp[next][nextNextColor]) {
				colors[next] = nextColor;
			} else {
				colors[next] = nextNextColor;
			}
			restoreColor(next);
		}
	}

	// parent에서 node로 온 것
	private static int makeDP(int parent, int node, int color) {
		// 이미 계산 값이 있다면 반환
		if (dp[node][color] != 0)
			return dp[node][color];

		int others = 0;
		int tmp = 0;
		for (int next : graph[node]) {
			if (next == parent) continue;
			tmp = makeDP(node, next, (color+1)%3);
			tmp = Math.max(tmp, makeDP(node, next, (color+2)%3));
			others += tmp;
		}

		dp[node][color] = others + rgb[node][color];
		return dp[node][color];
	}
}