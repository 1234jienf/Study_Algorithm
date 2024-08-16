import java.io.*;
import java.util.*;

public class Main {
	static int n, q;
	static List<Node>[] graph;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		q = Integer.parseInt(st.nextToken());

		graph = new ArrayList[n+1];
		for (int i = 0; i <= n; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 1; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());

			graph[a].add(new Node(b, c));
			graph[b].add(new Node(a, c));
		}

		StringBuilder ans = new StringBuilder();
		for (int i = 0; i < q; i++) {
			st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			ans.append(sol(k, v)).append("\n");
		}

		System.out.println(ans);
	}

	static int sol(int k, int v){
		boolean[] visited = new boolean[n + 1];
		Queue<Integer> q = new LinkedList<>();
		Queue<Integer> qv = new LinkedList<>();
		visited[v] = true;
		q.add(v);
		qv.add(Integer.MAX_VALUE);
		int count = -1;
		while(!q.isEmpty()) {
			int now = q.poll();
			int value = qv.poll();
			if (value >= k) {
				count++;
			}
			for (Node next : graph[now]) {
				if (visited[next.v]) continue;
				visited[next.v] = true;
				q.add(next.v);
				qv.add(Math.min(value, next.e));
			}
		}
		return count;
	}

	static class Node{
		public int v, e;

		public Node(int v, int e) {
			this.v = v;
			this.e = e;
		}
	}

}