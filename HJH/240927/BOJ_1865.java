package 자율팀스터디.d240928;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_1865 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int TC, n, m, w;
	static List<int[]> graph;
	static int[] dist;

	private static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		w = Integer.parseInt(st.nextToken());
		graph = new ArrayList<>();
		dist = new int[n + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);

		int s, e, t;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			graph.add(new int[] {s, e, t});
			graph.add(new int[] {e, s, t});
		}
		for (int i = 0; i < w; i++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			graph.add(new int[] {s, e, -t});
		}
	}

	private static boolean bellmanFord(int start) {
		dist[start] = 0;
		int now, next, cost, nextCost;
		// 최소값 갱신. 릴랙세이션
		for (int v = 1; v <= n; v++) {
			for (int e = 0; e < graph.size(); e++) {
				now = graph.get(e)[0];
				next = graph.get(e)[1];
				cost = graph.get(e)[2];
				nextCost = dist[now] + cost;
				if (dist[now] != Integer.MAX_VALUE && dist[next] > nextCost) {
					dist[next] = nextCost;
				}
			}
		}
		// 음수 사이클 존재 확인
		for (int e = 0; e < graph.size(); e++) {
			now = graph.get(e)[0];
			next = graph.get(e)[1];
			cost = graph.get(e)[2];
			nextCost = dist[now] + cost;
			if (dist[now] != Integer.MAX_VALUE && dist[next] > nextCost) {
				return true;
			}
		}
		return false;
	}


	public static void main(String[] args) throws Exception {
		TC = Integer.parseInt(br.readLine());
		boolean ans = false;
		for (int testCase = 0; testCase < TC; testCase++) {
			input();
			for (int i = 1; i <= n; i++) {
				if (dist[i] == Integer.MAX_VALUE) {
					if (ans = bellmanFord(i)) {
						System.out.println("YES");
						break;
					}
				}
			}
			if (!ans) {
				System.out.println("NO");
			}
		}
	}


	class Node {
		int v, e;
		public Node(int v, int e) {
			this.v = v;
			this.e = e;
		}
	}
}