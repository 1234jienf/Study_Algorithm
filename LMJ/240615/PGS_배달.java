import java.io.*;
import java.util.*;

//다익스트라
class PGS_배달 {
    static List<int[]>[] adjList; //인접리스트
    static int[] dist;//최단 시간
    static int n;
    static final int INF = Integer.MAX_VALUE;
    public int solution(int N, int[][] road, int K) {
        int answer = 0;
        n = N;
        adjList = new ArrayList[n+1];
        for(int i = 1; i <= n; i++){
            adjList[i] = new ArrayList<>();
        }
        
        dist = new int[n+1];
        Arrays.fill(dist, INF);
        
        for(int[] r : road){
            adjList[r[0]].add(new int[]{r[1], r[2]});
            adjList[r[1]].add(new int[]{r[0], r[2]});
        }
        
        dijkstra(1);
        
        for(int i = 1; i<=n;i++){
            if(dist[i]<=K){
                answer++;
            }
        }

        return answer;
    }
    
    static void dijkstra(int start){
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[1]-b[1]);
        boolean[] visit = new boolean[n+1];
        pq.add(new int[]{start,0});
        dist[start] = 0;
        
        while(!pq.isEmpty()){
            int[] cur = pq.poll();
            if(visit[cur[0]])
                continue;
            visit[cur[0]] = true;
            
            for(int[] n: adjList[cur[0]]){
                if(!visit[n[0]] && dist[n[0]] > dist[cur[0]] + n[1]){
                    dist[n[0]] = dist[cur[0]] + n[1];
                    pq.add(new int[]{n[0], dist[n[0]]});
                } 
            }
        }
    }
}