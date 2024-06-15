import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

//Baekjoon_20055_컨베이어벨트위의로봇
public class BOJ_20055 {
	static int N, K, cnt, time;
	static int[] belt;
	static boolean[] visit;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		cnt=0;
		time=0;

		belt = new int[2 * N];
		visit = new boolean[N];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < 2 * N; i++) {
			belt[i] = Integer.parseInt(st.nextToken());
		}

		simulation();
		
		System.out.println(time);
	}

	static void simulation() {
		
		while(cnt<K) {
			
		int tmp = belt[2*N-1];
		for(int i = 2*N-1; i>0;i--) {
			belt[i] = belt[i-1];
		}
		belt[0] = tmp;
		
		for(int i = N-1; i>0;i--) {
			visit[i] = visit[i-1];
		}
		visit[0] = false;
		visit[N-1] = false;
		
		for(int i = N-1 ; i>=1;i--) {
			if(visit[i-1] && !visit[i] && belt[i]>=1) {
				visit[i-1]=false;
				visit[i]=true;
				belt[i]--;
				if(belt[i]<=0)
					cnt++;
			}
		}
		
		if(belt[0]>0) {
			visit[0] = true;
			belt[0]--;
			if(belt[0]<=0)
				cnt++;
		}
		
		time++;
		
		}
		
	}
}
