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

public class BOJ_15591_MooTube(Silver) {
	static int N;
	static StringBuilder sb;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());
		int Q = Integer.parseInt(st.nextToken());

		List<int[]>[] adjList = new ArrayList[N + 1];

		for (int i = 1; i <= N; i++) {
			adjList[i] = new ArrayList<>();
		}

		for (int i = 0; i < N - 1; i++) {
			st = new StringTokenizer(br.readLine());
			int p = Integer.parseInt(st.nextToken());
			int q = Integer.parseInt(st.nextToken());
			int r = Integer.parseInt(st.nextToken());
			adjList[p].add(new int[] { q, r });
			adjList[q].add(new int[] { p, r });
		}

		for (int i = 0; i < Q; i++) {
			st = new StringTokenizer(br.readLine());
			int k = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			bfs(k, v, adjList);
		}

		bw.append(sb);
		bw.flush();
		bw.close();
		br.close();
	}

	static void bfs(int k, int v, List<int[]>[] abjList) {
		int result = 0;
		Queue<Integer> q = new LinkedList<>();
		q.add(v);
		boolean[] visit = new boolean[N+1];
		visit[v] = true;
		
		while(!q.isEmpty()) {
			int cur = q.poll();
			for(int[] nxt : abjList[cur]) {
				if(!visit[nxt[0]] && nxt[1]>=k) {
					visit[nxt[0]] = true;
					result++;
					q.add(nxt[0]);
				}
			}
		}
		
		sb.append(result+"\n");
	}
}
