import java.util.*;
class Solution {
    public int solution(int k, int n, int[][] reqs) {
        // 상담별 {시작 시간, 종료시간} 리스트
        List<List<Integer[]>> list = new ArrayList<>();
        // 초기화
        for(int i = 0; i<=k; i++){
            list.add(new ArrayList<>());
        }
        for(int[] req : reqs){
            int start = req[0];
            int end = start + req[1];
            int type = req[2];
            list.get(type).add(new Integer[]{start,end});
        }
        
        // 상담 유형별, 멘토 수별 대기시간 배열
        int[][] arr = new int[k+1][n-k+1];
        for(int i = 1; i<=k; i++){
            cal(arr[i], list.get(i));
        }
        
        return dfs(n-k, arr, 1);
    }
    
    // 멘토 수에 따른 대기 시간 계산
    static void cal(int[] arr, List<Integer[]> list) {
        for(int i = 0; i < arr.length; i++) {
            int count = i + 1;  // 멘토 수
            PriorityQueue<Integer> endTimes = new PriorityQueue<>();
            int totalTime = 0; // 총 대기 시간
            
            for(Integer[] time : list) {
                int start = time[0];
                int end = time[1];
                
                // 종료된 상담 제거
                while(!endTimes.isEmpty() && endTimes.peek() <= start) {
                    endTimes.poll();
                }
                
                // 상담원이 부족한 경우 대기
                if(endTimes.size() >= count) {
                    int earlyEnd = endTimes.poll();
                    totalTime += earlyEnd - start;
                    endTimes.add(earlyEnd + (end - start));
                } else {
                    endTimes.add(end);
                }
            }
            arr[i] = totalTime;
        }
    }
    
    // 가능한 멘토 조합 dfs 탐색
    // max: 현재 배정 가능한 남은 멘토 수
    // arr: 각 유형별, 멘토 수별 대기시간 배열
    // type: 현재 처리중인 상담 유형
    static int dfs(int max, int[][] arr, int type) {
        int minTotal = Integer.MAX_VALUE;
        for(int i = 0; i <= max; i++) {
          int value = arr[type][i];
            // 마지막 유형이 아닌 경우 재귀
            if (type < arr.length - 1) {
                value += dfs(max - i, arr, type + 1);
            }
            // 최소 대기 시간 갱신
            minTotal = Math.min(minTotal, value);
        }
        return minTotal;
    }
}