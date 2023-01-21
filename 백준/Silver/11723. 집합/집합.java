import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
		String oper;
		int num = 0;
		boolean []bitL = new boolean[20];
		int ret = Integer.parseInt(br.readLine());
		for(int i = 0 ; i < ret ; i++) {
			st = new StringTokenizer(br.readLine());
			oper = st.nextToken();
			if(!(oper.contains("all") || oper.contains("empty"))) {
				num = Integer.parseInt(st.nextToken());
			}
			
			switch(oper) {
			case "add":
				bitL[num - 1] = true;
				break;
			case "remove":
				bitL[num - 1] = false;
				break;
			case "check":
				if(bitL[num - 1]) {
					sb.append("1\n");
				} else {
					sb.append("0\n");
				}
				break;
			case "toggle":
				if(bitL[num - 1]) {
					bitL[num - 1] = false;
				} else {
					bitL[num - 1] = true;
				}
				break;
			case "all":
				for(int j = 0 ; j < 20 ; j++) {
					bitL[j] = true;
				}
				break;
			case "empty":
				for(int j = 0 ; j < 20 ; j++) {
					bitL[j] = false;
				}
				break;
			}
		}
		System.out.print(sb.toString());
		br.close();
	}
}
