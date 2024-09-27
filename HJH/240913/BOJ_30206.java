package 자율팀스터디.d240915;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_30206 {
	static int n, m;
	static int MOD = 1000000007;
	static int[] cnts = new int[200001];
	static boolean[] visited = new boolean[200001];
	static ArrayList<Integer>[] graph;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		int a, b;
		graph = new ArrayList[n + 1];
		for (int i = 0; i <= n; i++)
			graph[i] = new ArrayList<>();

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			graph[a].add(b);
			graph[b].add(a);
		}

		Queue<Integer> nodeQ = new ArrayDeque<>();
		Queue<Integer> depthQ = new ArrayDeque<>();
		nodeQ.add(1);
		depthQ.add(0);
		visited[1] = true;
		int now, depth;
		while (!nodeQ.isEmpty()) {
			now = nodeQ.poll();
			depth = depthQ.poll();
			cnts[depth]++;

			for (int next : graph[now]) {
				if (visited[next]) continue;
				visited[next] = true;
				nodeQ.add(next);
				depthQ.add(depth + 1);
			}
		}
		long ans = 1L;
		for (int i = 0; i < 200001; i++) {
			if (cnts[i] == 0)
				break;
			ans = ans * (cnts[i]+1) % MOD;
		}
		System.out.println(ans-1);
	}
}