import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

//크루스칼 알고리즘 : 모든 정점들을 가장 적은 비용으로 연결하기 위한 알고리즘
public class BOJ_10021_WateringtheFields {
	static int N, C;
	static int[] p;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken()); // 정점 수
		C = Integer.parseInt(st.nextToken()); // 최소 설치 비용

		int[] x = new int[N];
		int[] y = new int[N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			x[i] = Integer.parseInt(st.nextToken());
			y[i] = Integer.parseInt(st.nextToken());
		}

		// 크루스칼 1단계 : 간선을 정렬(오름차순)
		List<int[]> edges = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			for (int j = i + 1; j < N; j++) {
				int dx = x[i] - x[j];
				int dy = y[i] - y[j];
				int dist = dx * dx + dy * dy;
				if (dist >= C) {
					edges.add(new int[] { i, j, dist });
				}
			}
		}

		Collections.sort(edges, (o1, o2) -> o1[2] - o2[2]);

		// 크루스칼 2단계: N-1개의 간선을 뽑아야 하는데, 사이클이 발생하지 않도록 뽑자
		p = new int[N];
		for (int i = 0; i < N; i++) {
			makeset(i);
			p[i] = i;
		}

		int ans = 0; //최소비용
		int pick = 0; //뽑은 간선의 수

		for (int[] edge : edges) {
			int u = edge[0];
			int v = edge[1];
			int cost = edge[2];

			if (findset(u) != findset(v)) {
				union(u, v);
				ans += cost;
				pick++;

				// 모든 노드가 연결되면 종료
				if (pick == N - 1)
					break;
			}
		}

		// 모든 농장을 연결할 수 없는 경우
		if (pick != N - 1) {
			ans = -1;
		}

		System.out.println(ans);
	}

	static void union(int x, int y) {
		p[y] = x;
	}

	static int findset(int x) {
		if (x != p[x]) {
			p[x] = findset(p[x]);
		}
		return p[x];
	}

	static void makeset(int i) {
		p[i] = i;
	}
}
