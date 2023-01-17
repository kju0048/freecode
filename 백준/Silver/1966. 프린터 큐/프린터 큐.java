import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException{
		int N, M;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		int repN = Integer.parseInt(br.readLine());
		
		for(int i = 0 ; i < repN ; i++){
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());
			
			Queue<Integer> queue = new LinkedList<>();
			int[] nums = new int[N];
			
			st = new StringTokenizer(br.readLine());
			for(int j = 0 ; j < N ; j++) {
				nums[j] = Integer.parseInt(st.nextToken());
				queue.offer(nums[j]);
			}
		
			Arrays.sort(nums);	
			
			int index = M;
			int rank = 0;
			for(int j = N - 1 ; j >= 0 ; j--) {
				while(nums[j] != queue.peek()) {
					queue.offer(queue.poll());
					index = index == 0 ? queue.size() - 1 : --index;
				}
				
				queue.poll();
				rank++;
				
				if(index == 0) {
					sb.append(rank).append('\n');
					break;
				} else {
					index--;
				}				
			}
		}
		System.out.print(sb);
	}
}
