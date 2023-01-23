import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st;
		
		int []arr = new int[Integer.parseInt(br.readLine())];
		
		st = new StringTokenizer(br.readLine());
		for(int i = 0 ; i < arr.length ; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		
		int sum = 0;
		int all = 0;
		for(int i : arr) {
			sum += i;
			all += sum;
		}
		System.out.println(all);
	}
}
