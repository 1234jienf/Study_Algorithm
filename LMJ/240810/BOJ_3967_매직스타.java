import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class BOJ_3967_매직스타 {
    static char[] star = new char[12];
    static boolean[] abc = new boolean[12];
    static boolean[] visit = new boolean[12];
    static boolean check = false;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int inx = 0;
        for (int i = 0; i < 5; i++) {
            String s = br.readLine();
            for (int j = 0; j < 9; j++) {
                if (s.charAt(j) != '.') {
                    if (s.charAt(j) != 'x') {
                        star[inx] = s.charAt(j);
                        abc[s.charAt(j) - 'A'] = true;
                        visit[inx] = true;
                    }
                    inx++;
                }
            }
        }

        dfs(0);

        bw.append(sb);
        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(int x) {
        if (check) {
            return;
        }
        if (x == 12) {
            checked();
            return;
        }

        if (visit[x]) {
            dfs(x + 1);
        } else {
            for (int i = 0; i < 12; i++) {
                if (!abc[i]) {
                    star[x] = (char) (i + 'A');
                    abc[i] = true;
                    visit[x] = true;
                    dfs(x + 1);
                    abc[i] = false;
                    visit[x] = false;
                }
            }
        }
    }

    static void checked() {
        if (convert(star[0]) + convert(star[2]) + convert(star[5]) + convert(star[7]) == 26
                && convert(star[7]) + convert(star[8]) + convert(star[9]) + convert(star[10]) == 26
                && convert(star[0]) + convert(star[3]) + convert(star[6]) + convert(star[10]) == 26
                && convert(star[1]) + convert(star[5]) + convert(star[8]) + convert(star[11]) == 26
                && convert(star[4]) + convert(star[6]) + convert(star[9]) + convert(star[11]) == 26
                && convert(star[1]) + convert(star[2]) + convert(star[3]) + convert(star[4]) == 26) {
            check = true;
            sb.append("...." + star[0] + "....\n");
            sb.append("." + star[1] + "." + star[2] + "." + star[3] + "." + star[4] + ".\n");
            sb.append(".." + star[5] + "..." + star[6] + "..\n");
            sb.append("." + star[7] + "." + star[8] + "." + star[9] + "." + star[10] + ".\n");
            sb.append("...." + star[11] + "....\n");
        }
    }

    static int convert(char c) {
        return c - 'A' + 1;
    }
}
