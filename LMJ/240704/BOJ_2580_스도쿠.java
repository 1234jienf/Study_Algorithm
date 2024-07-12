import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class BOJ_2580_스도쿠 {
	static int[][] map = new int[9][9];
	static StringBuilder sb;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		for(int i = 0; i<9;i++) {
			st = new StringTokenizer(br.readLine());
			for(int j = 0; j<9;j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		dfs(0,0);
		
		bw.append(sb);
		bw.flush();
		bw.close();
		br.close();
	}
	
	
	static void dfs(int row, int col) {
		
		if(col==9) {
			dfs(row+1, 0);
			return;
		}
		
		if(row==9) {
			sb = new StringBuilder();
			for(int i = 0; i<9;i++) {
				for(int j = 0; j<9;j++) {
					sb.append(map[i][j]+" ");
				}
				sb.append("\n");
			}
			return;
		}
		
		if(map[row][col]==0) {
			for(int i = 1; i<=9;i++) {
				if(check(row, col, i)) {
					map[row][col] = i;
					dfs(row, col+1);
				}
			}
			map[row][col] = 0;
			return;
		}
		
		dfs(row, col+1);
		
	}
	
	static boolean check(int row, int col, int x) {
		
		for(int i = 0; i<9;i++) {
			if(map[row][i]==x || map[i][col]==x) {
				return false;
			}
		}
		
		for(int i = row/3*3; i<row/3*3+3;i++) {
			for(int j = col/3*3; j<col/3*3+3;j++) {
				if(map[i][j]==x) {
					return false;
				}
			}
		}
		
		return true;
	}
}
