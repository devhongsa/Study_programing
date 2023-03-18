import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();

        LinkedList<Integer> li = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            li.add(i);
        }

        LinkedList<Integer> res = new LinkedList<>();

        while (li.size() != 0) {
            for (int i = 0; i < k; i++) {
                if (i == k - 1) {
                    res.add(li.remove(0));
                } else {
                    li.addLast(li.removeFirst());
                }
            }
        }

        String s = "<";
        for (int i = 0; i < n; i++) {
            s += String.format("%d, ", res.get(i));
            if (i == n - 1) {
                s = s.substring(0, s.length() - 2) + ">";
            }
        }
        System.out.println(s);
    }
}

// // 숫자 뒤집기
// public class Main {
// public static void main(String[] args) {
// Scanner in = new Scanner(System.in);
// int n = in.nextInt();

// int a = 0;
// while (n != 0) {
// a = n % 10 + a * 10;
// n = n / 10;
// }
// System.out.println(a);
// }
// }

// // 백준 10818 최소, 최대 문제 Array
// public class Main {
// public static void main(String[] args) {
// Scanner in = new Scanner(System.in);
// int n = in.nextInt();

// ArrayList<Integer> array = new ArrayList<>();
// for (int i = 0; i < n; i++) {
// array.add(in.nextInt());
// }

// int min = 1000001;
// int max = -1000001;

// for (Integer num : array) {
// if (num > max) {
// max = num;
// }
// if (num < min) {
// min = num;
// }
// }

// System.out.printf("%d %d", min, max);
// }
// }

// // 백준 1021 큐 문제
// public class Main {
// public static void main(String[] args) {
// Scanner in = new Scanner(System.in);
// int n = in.nextInt();
// int nidx = in.nextInt();

// LinkedList<Integer> queue = new LinkedList<>();
// for (int i = 0; i < n; i++) {
// queue.add(i + 1);
// }

// ArrayList<Integer> idxList = new ArrayList<>();
// for (int i = 0; i < nidx; i++) {
// idxList.add(in.nextInt());
// }

// int count = 0;
// // System.out.println(queue.indexOf(3));
// for (Integer num : idxList) {
// if (queue.peek() == num) {
// queue.poll();
// continue;
// } else {
// if (queue.indexOf(num) > (double) queue.size() / 2) {
// while (queue.peek() != num) {
// queue.addFirst(queue.pollLast());
// count++;
// }
// queue.poll();
// } else {
// while (queue.peek() != num) {
// queue.addLast(queue.pollFirst());
// count++;
// }
// queue.poll();
// }

// }
// }
// System.out.println(count);
// }
// }

// // 백준 25556 스택 문제
// public class Main {
// public static void main(String[] args) {
// Scanner in = new Scanner(System.in);
// int n = in.nextInt();
// ArrayList<Integer> list = new ArrayList<>();
// for (int i = 0; i < n; i++) {
// list.add(in.nextInt());
// }

// Boolean isPossible = true;

// List<Stack<Integer>> stackList = new ArrayList<>();
// for (int i = 0; i < 4; i++) {
// Stack<Integer> stack = new Stack<>();
// stack.push(0);
// stackList.add(stack);
// }

// for (Integer number : list) {
// for (int i = 0; i < stackList.size(); i++) {
// if (stackList.get(i).peek() < number) {
// stackList.get(i).push(number);
// break;
// }
// if (i == stackList.size() - 1) {
// isPossible = false;
// }
// }
// }

// if (isPossible) {
// System.out.println("YES");
// } else {
// System.out.println("NO");
// }

// }
// }
