import java.io.*;
import java.util.*;

public class Main {
	static int n, m, x;
	static int INF = Integer.MAX_VALUE;
	static List<Node>[] graphIn;
	static List<Node>[] graphOut;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		x = Integer.parseInt(st.nextToken());

		graphIn = new ArrayList[n+1];
		graphOut = new ArrayList[n+1];
		for (int i = 0; i <= n; i++) {
			graphIn[i] = new ArrayList<>();
			graphOut[i] = new ArrayList<>();
		}

		int a, b, c;
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Integer.parseInt(st.nextToken());
			graphIn[a].add(new Node(b, c));
			graphOut[b].add(new Node(a, c));
		}

		int[] distsIn = dijkIn();
		int[] distsOut = dijkOut();
		int dist, ans = 0;
		for (int i = 1; i <= n; i++) {
			dist = distsIn[i] + distsOut[i];
			ans = ans >= dist? ans : dist;
		}
		System.out.println(ans);

	}

	private static int[] dijkIn() {
		int[] ans = new int[n + 1];
		Arrays.fill(ans, INF);
		ans[x] = 0;

		PriorityQueue<Node> pq = new PriorityQueue<>((a, b) ->
			Integer.compare(a.e, b.e));
		pq.add(new Node(x, 0));
		Node now;
		int dist;
		while (!pq.isEmpty()) {
			now = pq.poll();

			for (Node next : graphIn[now.v]) {
				dist = now.e + next.e;
				if (ans[next.v] > dist) {
					ans[next.v] = dist;
					pq.add(new Node(next.v, dist));
				}
			}
		}

		return ans;
	}


	private static int[] dijkOut() {
		int[] ans = new int[n + 1];
		Arrays.fill(ans, INF);
		ans[x] = 0;

		PriorityQueue<Node> pq = new PriorityQueue<>((a, b) ->
				Integer.compare(a.e, b.e));
		pq.add(new Node(x, 0));
		Node now;
		int dist;
		while (!pq.isEmpty()) {
			now = pq.poll();

			for (Node next : graphOut[now.v]) {
				dist = now.e + next.e;
				if (ans[next.v] > dist) {
					ans[next.v] = dist;
					pq.add(new Node(next.v, dist));
				}
			}
		}

		return ans;
	}

	static class Node {
		int v, e;

		public Node(int v, int e) {
			this.v = v;
			this.e = e;
		}
	}
}