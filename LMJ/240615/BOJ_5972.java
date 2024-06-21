import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

// Baekjoon_5972_택배배송
public class BOJ_5972 {
	static final int INF = Integer.MAX_VALUE;
	static int N,M;
	static List<int[]>[] adjList;
	static int[] dist;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		adjList = new ArrayList[N+1];
		for(int i = 1; i<=N;i++) {
			adjList[i] = new ArrayList<>();
		}
		
		dist = new int[N+1];
		Arrays.fill(dist, INF);
		
		for(int i = 0; i<M;i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());
			adjList[a].add(new int[] {b,w});
			adjList[b].add(new int[] {a,w});
		}
		
		dijkstra(1);
		System.out.println(dist[N]);	
	}
	
	static void dijkstra(int start) {
		PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[1]-b[1]);
		boolean[] visit = new boolean[N+1];
		pq.add(new int[] {start,0});
		dist[start] = 0;
		
		while(!pq.isEmpty()) {
			int[] cur = pq.poll();
			
			if(visit[cur[0]]) {
				continue;
			}
			
			visit[cur[0]] = true;
			
			for(int[] n:adjList[cur[0]]) {
				if(!visit[n[0]] && dist[n[0]] > dist[cur[0]]+n[1]) {
					dist[n[0]] = dist[cur[0]] + n[1];
					pq.add(new int[] {n[0], dist[n[0]]});
				}
			}
			
		}
	}
}
