import java.io.*;

class Main {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String star = "";

        for (int i = N - 1; i >= 0; i--) {
            for (int j = N - 1; j > i; j--) {
                star += " ";
            }
            for (int k = 0; k <= (i * 2); k++) {
                star += "*";
            }
            star += "\n";
        }
        System.out.println(star);
    }
}