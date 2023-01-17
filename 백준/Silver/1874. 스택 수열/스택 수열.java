import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int n = Integer.parseInt(br.readLine());
		Stack<Integer> stack = new Stack<>();
		int []arr = new int[n];
		for(int i = 0 ; i < n ; i++) {
			arr[i] = Integer.parseInt(br.readLine());
		}
		int index = 0;
		int num = 0;
		while(index < n && num <= n) {
			if(stack.empty()) {
				stack.push(++num);
				sb.append('+').append('\n');
				continue;
			}
			if(stack.peek() == arr[index]) {
				stack.pop();
				index++;
				sb.append('-').append('\n');
			} else {
				stack.push(++num);
				sb.append('+').append('\n');
			}
		}
		if(stack.empty()) {
			System.out.print(sb);
		} else {
			System.out.println("NO");
		}
	}
}
