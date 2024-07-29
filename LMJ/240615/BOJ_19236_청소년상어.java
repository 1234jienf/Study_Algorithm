import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_19236_청소년상어 {
	static class Shark {
		int x, y, dir, sum;

		Shark() {
		}

		public Shark(int x, int y, int dir, int sum) {
			this.x = x;
			this.y = y;
			this.dir = dir;
			this.sum = sum;
		}
	}

	static class Fish implements Comparable<Fish> {
		int x, y, id, dir;
		boolean isAlive = true;

		Fish() {
		}

		public Fish(int x, int y, int id, int dir, boolean isAlive) {
			this.x = x;
			this.y = y;
			this.id = id;
			this.dir = dir;
			this.isAlive = isAlive;
		}

		@Override
		public int compareTo(Fish f) {
			return this.id - f.id;
		}
	}

	static int[] dx = { -1, -1, 0, 1, 1, 1, 0, -1 };
	static int[] dy = { 0, -1, -1, -1, 0, 1, 1, 1 };
	static int maxSum = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int[][] map = new int[4][4];
		List<Fish> fishes = new ArrayList<>();

		// 물고기 입력
		for (int i = 0; i < 4; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 4; j++) {
				Fish f = new Fish();
				f.id = Integer.parseInt(st.nextToken());
				f.dir = Integer.parseInt(st.nextToken())-1;
				f.x = i;
				f.y = j;

				fishes.add(f);
				map[i][j] = f.id;
			}
		}

		// 물고기 id순으로 정렬
		Collections.sort(fishes);

		// 상어 (0,0) 투입
		Fish f = fishes.get(map[0][0] - 1);
		Shark shark = new Shark(0, 0, f.dir, f.id);
		f.isAlive = false;
		map[0][0] = -1;

		dfs(map, shark, fishes);
		System.out.println(maxSum);
	}

	static void dfs(int[][] map, Shark shark, List<Fish> fishes) {
		maxSum = Math.max(maxSum, shark.sum);

		fishes.forEach(e -> moveFish(e, map, fishes));

		for (int i = 1; i < 4; i++) {
			int nx = shark.x + dx[shark.dir] * i;
			int ny = shark.y + dy[shark.dir] * i;

			if (nx < 0 || nx >= 4 || ny < 0 || ny >= 4 || map[nx][ny] <= 0)
				continue;
			
			int[][] tmpMap = copyMap(map);
			List<Fish> tmpFishes = copyFishes(fishes);
			
			tmpMap[shark.x][shark.y] = 0;
			Fish f = tmpFishes.get(map[nx][ny]-1);
			Shark newShark = new Shark(f.x, f.y, f.dir, shark.sum + f.id);
			f.isAlive = false;
			tmpMap[f.x][f.y] = -1;
			
			dfs(tmpMap, newShark, tmpFishes);
		}
	}
	
	static void moveFish(Fish fish, int[][] map, List<Fish> fishes) {
        if (!fish.isAlive) return;

        for (int i = 0; i < 8; i++) {
            int nextDir = (fish.dir + i) % 8;
            int nx = fish.x + dx[nextDir];
            int ny = fish.y + dy[nextDir];

            if (0 <= nx && nx < 4 && 0 <= ny && ny < 4 && map[nx][ny] > -1) {
            	map[fish.x][fish.y] = 0;
                
                if (map[nx][ny] == 0) {
                    fish.x = nx;
                    fish.y = ny;
                } else {
                    Fish tmp = fishes.get(map[nx][ny] - 1);
                    tmp.x = fish.x;
                    tmp.y = fish.y;
                    map[fish.x][fish.y] = tmp.id;

                    fish.x = nx;
                    fish.y = ny;
                }

                map[nx][ny] = fish.id;
                fish.dir = nextDir;
                return;
            }
        }
	}
	
    static int[][] copyMap(int[][] arr) {
        int[][] tmp = new int[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
            	tmp[i][j] = arr[i][j];
            }
        }

        return tmp;
    }

    static List<Fish> copyFishes(List<Fish> fishes) {
        List<Fish> tmp = new ArrayList<>();
        fishes.forEach(e -> tmp.add(new Fish(e.x, e.y, e.id, e.dir, e.isAlive)));
        return tmp;
    }
	
}
