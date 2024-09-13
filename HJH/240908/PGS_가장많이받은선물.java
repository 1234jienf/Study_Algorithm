package 자율팀스터디.d240908;

import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

class PGS_가장많이받은선물 {
	Map<String, Integer> friendsMap = new HashMap<>();
	int len;
	int[][] giftArr;
	int[] nowArr;
	StringTokenizer st;
	int[] scores;

	public int idx(String name) { return friendsMap.get(name); }

	public int solution(String[] friends, String[] gifts) {
		len = friends.length;
		giftArr = new int[len][len];
		nowArr = new int[len];
		scores = new int[len];

		for (int i = 0; i < len; i++)
			friendsMap.put(friends[i], i);

		String a, b;
		for (String gift : gifts) {
			st = new StringTokenizer(gift);
			a = st.nextToken();
			b = st.nextToken();
			giftArr[idx(a)][idx(b)]++;
			scores[idx(a)]++;
			scores[idx(b)]--;
		}

		for (int i = 0; i < len; i++) {
			for (int j = 0; j < len; j++) {
				System.out.print(giftArr[i][j]);
				System.out.print(" ");
			}
			System.out.println();
		}

		System.out.println("scores");
		for (int i = 0; i < len; i++) {
			System.out.print(scores[i]);
			System.out.print(" ");
		}

		for (int i = 0; i < len; i++) {
			for (int j = i + 1; j < len; j++) {
				if (giftArr[i][j] > giftArr[j][i]) {
					nowArr[i]++;
				}
				else if (giftArr[i][j] < giftArr[j][i]) {
					nowArr[j]++;
				}
				else {
					if (scores[i] > scores[j]) {
						nowArr[i]++;
					}
					else if (scores[i] < scores[j]) {
						nowArr[j]++;
					}
				}
			}
		}
		int ans = 0;
		for (int i = 0; i < len; i++) ans = ans > nowArr[i] ? ans : nowArr[i];

		return ans;
	}
}