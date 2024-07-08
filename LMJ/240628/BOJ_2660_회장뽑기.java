import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

//플로이드 와샬
public class BOJ_2660_회장뽑기 {
	static final int INF = 98754321;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder first = new StringBuilder();
		StringBuilder second = new StringBuilder();
		StringTokenizer st;

		int N = Integer.parseInt(br.readLine());
		int[][] arr = new int[N + 1][N + 1];

		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				if (i != j) {
					arr[i][j] = INF;
				}
			}
		}

		while (true) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			if (a == -1 && b == -1)
				break;

			arr[a][b] = arr[b][a] = 1;
		}

		for (int k = 1; k <= N; k++) {
			for (int i = 1; i <= N; i++) {
				for (int j = 1; j <= N; j++) {
					if (arr[i][j] > arr[i][k] + arr[k][j]) {
						arr[i][j] = arr[i][k] + arr[k][j];
					}
				}
			}
		}

		int readerScore = INF;
		int[] score = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			int tmp = 0;
			for (int j = 1; j <= N; j++) {
				if (arr[i][j] != INF) {
					tmp = Math.max(tmp, arr[i][j]);
				}
			}
			score[i] = tmp;
			readerScore = Math.min(readerScore, tmp);
		}
		
		first.append(readerScore+" ");

		int readerNum = 0;
		for (int i = 1; i <= N; i++) {
			if(readerScore == score[i]) {
				readerNum++;
				second.append(i+" ");
			}
		}
		
		first.append(readerNum+"\n");

		bw.write(first.toString());
		bw.write(second.toString()+"\n");
		bw.flush();
		bw.close();
		br.close();
	}
}
