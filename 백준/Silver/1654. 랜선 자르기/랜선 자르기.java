import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int []arr = new int[n];
		long min = 0;
		long max = 0;
		
		for(int i = 0 ; i < n ; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			if(arr[i] > max) {
				max = arr[i];
			}
		}
		
		max++;
		long count;
		long mid;
		
		while(min < max) {
			count = 0;
			mid = (max + min) / 2;
			for(int i : arr) {
				count += i / mid;
			}
			if(count < k) {
				max = mid;
			} else {
				min = mid + 1;
			}
		}
		System.out.println(max - 1);
	}
}