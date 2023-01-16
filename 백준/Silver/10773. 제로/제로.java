import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int check;
		int sum = 0;
		Stack<Integer> stack = new Stack<>();
		for(int i = 0 ; i < N ; i++) {
			check = Integer.parseInt(br.readLine());
			if (check == 0) {
				sum -= stack.peek();
				stack.pop();
			} else {
				stack.push(check);
				sum += stack.peek();
			}
		}
	
		
		System.out.println(sum);
	}
}
