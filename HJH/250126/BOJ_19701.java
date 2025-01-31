import java.io.*;
import java.util.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;

	static ArrayList<Edge>[] graph;

	static int[][] dists;

	static int v, e;
	static int a, b, t, k;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		v = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		graph = new ArrayList[v+1];
		dists = new int[2][v+1];
		for (int i = 0; i <= v; i++) {
			graph[i] = new ArrayList<>();
			dists[0][i] = Integer.MAX_VALUE;
			dists[1][i] = Integer.MAX_VALUE;
		}
		dists[0][1] = 0;
		dists[1][1] = 0;

		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			t = Integer.parseInt(st.nextToken());
			k = Integer.parseInt(st.nextToken());
			graph[a].add(new Edge(b, t, k));
			graph[b].add(new Edge(a, t, k));
		}

		dijk();
		StringBuilder sb = new StringBuilder();
		for (int i = 2; i <= v; i++) {
			sb.append(Math.min(dists[0][i], dists[1][i])).append("\n");
		}
		System.out.println(sb.toString());
	}

	private static void dijk() {

		Queue<Edge> q = new LinkedList<>();
		q.add(new Edge(1, 0, 0));
		while (!q.isEmpty()) {
			Edge now = q.poll();
			if (dists[now.don][now.to] != now.len)
				continue;
			for (Edge next : graph[now.to]) {
				// 돈까스를 안먹고 진행
				if (dists[now.don][next.to] > now.len + next.len) {
					dists[now.don][next.to] = now.len + next.len;
					q.add(new Edge(next.to, dists[now.don][next.to], now.don));
				}
				// 가능할 시 돈까스를 먹고 진행
				if (now.don == 0) {
					if (dists[1][next.to] > now.len + next.len - next.don) {
						dists[1][next.to] = now.len + next.len - next.don;
						q.add(new Edge(next.to, dists[1][next.to], 1));
					}
				}
			}
		}
	}

	static class Edge {
		public int to, len, don;

		public Edge(int to, int len, int don) {
			this.to = to;
			this.len = len;
			this.don = don;
		}

	}
}