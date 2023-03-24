import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Scanner;
import java.util.Stack;

public class test_java {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
        ArrayList<Integer> arr2 = new ArrayList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        String s = "hi hello";

        arr.add(1);
        arr.add(2);
        arr.add(13);
        arr2.add(14);
        arr2.add(11);
        arr2.add(12);
        Collections.frequency(arr, "A");
        arr.addAll(arr2);

        arr.sort(Comparator.reverseOrder());

        System.out.println(arr);
    }
}
