import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;

public class test_java {
    public static void main(String[] args) {
        HashMap<String, Integer> hm = new HashMap<>();
        hm.put("I", 1);
        hm.put("V", 5);
        hm.put("X", 10);
        hm.put("L", 50);
        hm.put("C", 100);
        hm.put("D", 500);
        hm.put("M", 1000);

        Stack<Integer> stack = new Stack<>();

        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();

        for (int i = 0; i < s.length(); i++) {
            Integer num = hm.get(s.substring(i, i + 1));
            if (stack.empty()) {
                stack.add(num);
            } else {
                if (num > stack.peek()) {
                    stack.add(num - stack.pop());
                } else {
                    stack.add(num);
                }
            }
        }

        int answer = 0;

        for (Integer n : stack) {
            answer += n;
        }

        System.out.println(answer);
    }
}
