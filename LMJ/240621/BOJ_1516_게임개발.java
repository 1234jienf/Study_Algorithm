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

//위상정렬
public class BOJ_1516_게임개발 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int[] time = new int[N + 1];
		int[] degree = new int[N + 1];
		List<Integer>[] adjList = new ArrayList[N + 1];

		for (int i = 1; i <= N; i++) {
			adjList[i] = new ArrayList<>();
		}

		for (int i = 1; i <= N; i++) {
			st = new StringTokenizer(br.readLine());
			time[i] = Integer.parseInt(st.nextToken());

			while (true) {
				int num = Integer.parseInt(st.nextToken());

				if (num == -1)
					break;

				adjList[num].add(i);
				degree[i]++;
			}
		}

		Queue<Integer> q = new LinkedList<>();
		int[] result = new int[N + 1];

		for (int i = 1; i <= N; i++) {
			if (degree[i] == 0) {
				q.add(i);
				result[i] = time[i];
			}
		}
		
		while(!q.isEmpty()) {
			int cur = q.poll();
			
			for(int i: adjList[cur]) {
				result[i] = Math.max(result[i], result[cur] + time[i]);
				degree[i]--;
				if(degree[i]==0)
					q.add(i);
			}
			
		}
		
		for(int i =1 ;i<=N;i++) {
			bw.append(result[i]+"\n");
		}
		
		bw.flush();
		bw.close();
		br.close();

	}
}
