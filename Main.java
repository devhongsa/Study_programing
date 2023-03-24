import java.util.Scanner;
import java.util.Arrays;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Stack;
import java.io.IOError;
import java.util.Collection;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 백준 2830번 행성x3, 
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        long[] arr = new long[20];

        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            int k = num;
            int cnt = 0;
            while (k > 0) {
                arr[cnt] += k % 2;
                k = k / 2;
                cnt += 1;
            }
        }

        long answer = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > 0) {
                answer += arr[i] * (n - arr[i]) * (1 << i);
            }
        }

        System.out.println(answer);
    }
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// // 백준 9012번 스택
// public class Main {
// public static void main(String[] args) throws IOException {
// Stack<String> stack = new Stack<>();

// BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

// int n = Integer.parseInt(br.readLine());

// for (int i = 0; i < n; i++) {
// String s = br.readLine();
// stack.clear();
// for (char c : s.toCharArray()) {
// if (stack.size() == 0) {
// stack.push(String.valueOf(c));
// continue;
// }
// if (c == '(') {
// stack.push(String.valueOf(c));
// } else {
// if (stack.peek().equals("(")) {
// stack.pop();
// } else {
// stack.push(String.valueOf(c));
// }
// }
// }
// if (stack.size() == 0) {
// System.out.println("YES");
// } else
// System.out.println("NO");
// }
// }
// }

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// // 백준 1260번 그래프 DFS, BFS 탐색
// public class Main {
// static StringBuilder sb = new StringBuilder();
// static Scanner scan = new Scanner(System.in);

// static int N, M, V;
// static int[][] adj;
// static ArrayList<Integer>[] adj2;
// static boolean[] visit;

// static void input() {
// N = scan.nextInt();
// M = scan.nextInt();
// V = scan.nextInt();
// adj = new int[N + 1][N + 1];
// adj2 = new ArrayList[N + 1];

// for (int i = 1; i <= N; i++) {
// adj2[i] = new ArrayList<Integer>();
// }
// for (int i = 1; i <= M; i++) {
// int x = scan.nextInt(), y = scan.nextInt();
// adj[x][y] = 1;
// adj[y][x] = 1;

// adj2[x].add(y);
// adj2[y].add(x);
// }
// // 인접행렬은 정렬이 필요없지만, 인접리스트는 정렬을 해줘야함.
// // 인접행렬은 순회를 돌때 처음부터 순서대로 도니까 정렬이 필요없음. 반면 인접리스트는 입력이 들어온순서대로 리스트 구성되어있으므로
// // 정렬되지않은상태임.
// for (int i = 1; i <= N; i++) {
// Collections.sort(adj2[i]);
// }
// }

// // 인접행렬일때 DFS
// static void dfs(int x) {
// visit[x] = true;
// sb.append(x).append(" ");
// for (int y = 1; y <= N; y++) {
// if (adj[x][y] == 0)
// continue;
// if (visit[y])
// continue;
// dfs(y);
// }
// }

// // 인접리스트일때 DFS
// static void dfs2(int x) {
// visit[x] = true;
// sb.append(x).append(" ");
// for (int y : adj[x]) {
// if (visit[y])
// continue;
// dfs(y);
// }
// }

// // 인접행렬일때 BFS
// static void bfs(int x) {
// Queue<Integer> que = new LinkedList<>();

// que.add(x);
// visit[x] = true;

// while (!que.isEmpty()) {
// x = que.poll();
// sb.append(x).append(" ");
// for (int y = 1; y <= N; y++) {
// if (adj[x][y] == 0)
// continue;
// if (visit[y])
// continue;

// que.add(y);
// visit[y] = true;
// }
// }
// }

// // 인접리스트일때 BFS
// static void bfs2(int x) {
// Queue<Integer> que = new LinkedList<>();

// que.add(x);
// visit[x] = true;

// while (!que.isEmpty()) {
// x = que.poll();
// sb.append(x).append(" ");
// for (int y : adj[x]) {
// if (adj[x][y] == 0)
// continue;
// if (visit[y])
// continue;

// que.add(y);
// visit[y] = true;
// }
// }
// }

// static void pro() {
// visit = new boolean[N + 1];
// dfs(V);
// sb.append('\n');
// for (int i = 1; i <= N; i++)
// visit[i] = false;
// bfs(V);

// System.out.println(sb);
// }

// public static void main(String[] args) {
// input();
// pro();
// }
// }

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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
