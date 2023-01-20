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
		int m = Integer.parseInt(st.nextToken());
		int []arr = new int[n];
		int min = 0;
		int max = 0;
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < n ; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
			if(arr[i] > max) {
				max = arr[i];
			}
		}
		
		max++;
		long count;
		int mid;
		
		while(min < max) {
			count = 0;
			mid = (max + min) / 2;
			for(int i : arr) {
				count += i - mid > 0 ? i - mid : 0; 
			}
			if(count < m) {
				max = mid;
			} else {
				min = mid + 1;
			}
		}
		System.out.println(max - 1);
	}
}
