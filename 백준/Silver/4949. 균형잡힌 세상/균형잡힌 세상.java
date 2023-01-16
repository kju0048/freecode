import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str;
		String ans;
		Stack<String> stack = new Stack<>();
		do {
			str = br.readLine();
			if(str.equals("."))
				break;
			ans = "yes";
			stack.clear();
			for(int i = 0 ; i < str.length(); i++) {
				if (str.charAt(i) == '(') {
					stack.push("(");
				} else if (str.charAt(i) == '[') {
					stack.push("[");
				} else if (str.charAt(i) == ')') {
					if(stack.empty() == true) {
						ans = "no";
						break;
					}
					if(stack.peek().equals("(")) {
						stack.pop();
					} else {
						ans = "no";
						break;
					}
				} else if (str.charAt(i) == ']') {
					if(stack.empty() == true) {
						ans = "no";
						break;
					}
					if(stack.peek().equals("[")) {
						stack.pop();
					} else {
						ans = "no";
						break;
					}
				}
			}
			if(!stack.empty())
				ans = "no";
			System.out.println(ans);
		}while(!str.equals("."));
	}
}