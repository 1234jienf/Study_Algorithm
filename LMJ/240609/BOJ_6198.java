import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

//Baekjoon_6198_옥상정원꾸미기
public class BOJ_6198 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		long answer = 0;
		Stack<Integer> stack = new Stack<>();
		
		for(int i = 0;i<N;i++) {
			int top = Integer.parseInt(br.readLine());
			while(!stack.isEmpty() && stack.peek()<=top) {
					stack.pop();
			}
			answer+=stack.size();
			stack.add(top);
			
		}
		
		System.out.println(answer);
	}//main
}
