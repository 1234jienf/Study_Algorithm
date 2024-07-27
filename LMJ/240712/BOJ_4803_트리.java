import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_4803_트리 {
	static int N, M;
	static List<Integer>[] tree;
	static boolean[] visit;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int TC = 1;

		while (true) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());

			if (N == 0 && M == 0)
				break;

			tree = new ArrayList[N + 1];
			for (int i = 0; i <= N; i++) {
				tree[i] = new ArrayList<>();
			}

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());

				tree[a].add(b);
				tree[b].add(a);
			}

			int tree = 0;
			visit = new boolean[N + 1];
			for (int i = 1; i <= N; i++) {
				if (!visit[i]) {
					tree += check(i);
				}
			}

			sb.append("Case " + TC + ": ");

			if (tree == 0) {
				sb.append("No trees.\n");
			} else if (tree == 1) {
				sb.append("There is one tree.\n");
			} else {
				sb.append("A forest of " + tree + " trees.\n");
			}
			TC++;
		}

		bw.write(sb + "");
		bw.flush();
		bw.close();

	}

	// 트리 특징

	static int check(int root) {
		Queue<Integer> q = new LinkedList<Integer>();
		q.add(root);
		visit[root] = true;
		int node = 0, edge = 0;

		while (!q.isEmpty()) {
			int cur = q.poll();
			node++;
			visit[cur] = true;

			for (int n : tree[cur]) {
				edge += 1;
				if (!visit[n]) {
					q.add(n);
				}
			}
		}

		return 2 * (node - 1) == edge ? 1 : 0;
	}
}
