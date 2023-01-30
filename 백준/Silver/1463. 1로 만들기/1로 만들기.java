import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Main {
	
	static int min(int x, int y) {
		return x > y ? y : x;
	}
	
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());        
        int []memo = new int[n+4];
        
        memo[0] = 0;
        memo[1] = 0;
        memo[2] = 1;
        memo[3] = 1;
        for(int i = 4 ; i < n+1 ; i++) {
        	if(i % 3 == 0 && i % 2 == 0) {
        		memo[i] = min(memo[i/3], memo[i/2]) + 1;
        	} else if(i % 3 == 0) {
        		memo[i] = memo[i/3] + 1;
        	} else if(i % 2 == 0) {
        		memo[i] = memo[i/2] + 1;
        	} else {
        		memo[i] = memo[i-1] + 1;
        	}
        	memo[i] = min(memo[i], memo[i-1] + 1);
        }
        System.out.print(memo[n]);
	}
}
