package 자율팀스터디.d240810;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_2866 {
	static int r, c;
	static String[] datas;

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		r = Integer.parseInt(st.nextToken());
		c = Integer.parseInt(st.nextToken());
		datas = new String[r];

		for (int i = 0; i < r; i++) datas[i] = br.readLine();

		Node head = new Node(null);

		for (int i = 0; i < c; i++) {
			Node now = head;
			for (int j = r-1; j >= 0; j--) {
				if (now.kids.containsKey(datas[j].charAt(i))) {
				}
				else {
					now.kids.put(datas[j].charAt(i), new Node(now));
				}
				now = now.kids.get(datas[j].charAt(i));
			}
		}

		Queue<Node> q = new ArrayDeque<>();
		q.add(head);
		Set<Node> leafs = new HashSet<>();
		while (!q.isEmpty()) {
			Node now = q.poll();
			if(now.kids.isEmpty()) {
				leafs.add(now);
				continue;
			}
			for (Map.Entry<Character, Node> kid : now.kids.entrySet()) {
				q.add(kid.getValue());
			}
		}

		int count = 0;
		for (int i = 1; i < r; i++) {
			Set<Node> tmp = new HashSet<>();
			for (Node leaf : leafs) {
				tmp.add(leaf.parent);
			}
			if (tmp.size() != c) {
				break;
			}
			leafs = tmp;
			count += 1;
		}

		System.out.println(count);
	}

	static class Node{
		Node parent;
		Map<Character, Node> kids;
		Node(Node parent) {
			this.parent = parent;
			kids = new HashMap<>();
		}
	}
}