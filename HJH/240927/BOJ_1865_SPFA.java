package 자율팀스터디.d240928;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class BOJ_1865_SPFA {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int TC, n, m, w;
	static List<int[]> graph[];
	static int[] dist;

	private static void input() throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		w = Integer.parseInt(st.nextToken());
		graph = new ArrayList[n + 1];
		for (int i = 0; i <= n; i++)
			graph[i] = new ArrayList<>();
		dist = new int[n + 1];
		Arrays.fill(dist, Integer.MAX_VALUE);

		int s, e, t;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			graph[s].add(new int[] {e, t});
			graph[e].add(new int[] {s, t});
		}
		for (int i = 0; i < w; i++) {
			st = new StringTokenizer(br.readLine());
			s = Integer.parseInt(st.nextToken());
			e = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			graph[s].add(new int[] {e, -t});
		}
	}

	private static boolean spfa(int start) {
		dist[start] = 0;
		// 최소값 갱신. 릴랙세이션
		Queue<Integer> q = new ArrayDeque<>();
		boolean[] inque = new boolean[n+1];
		int[] cnt = new int[n+1];
		q.add(start);
		inque[start] = true;

		int now, next, cost;
		while (!q.isEmpty()) {
			now = q.poll();
			inque[now] = false;
			for (int[] edge : graph[now]) {
				next = edge[0];
				cost = edge[1];

				if (dist[next] > dist[now] + cost) {
					dist[next] = dist[now] + cost;
					if (!inque[next]) {
						q.add(next);
						inque[next] = true;
						cnt[next]++;
						if (cnt[next] > n)
							return true;
					}
				}
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
					if (ans = spfa(i)) {
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