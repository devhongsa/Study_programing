import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Random;
import java.util.Scanner;
import java.util.Stack;

public class test_java {
    public static void main(String[] args) {
        String koreanString = "안녕 하세요";
        String encodedString = "";
        String decodedString = "";

        try {
            // UTF-8로 인코딩 후 URL 인코딩
            encodedString = URLEncoder.encode(koreanString, StandardCharsets.UTF_8.toString());
            System.out.println(encodedString); // 출력: %EC%95%88%EB%85%95%ED%95%98%EC%84%B8%EC%9A%94
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        try {
            // URL 디코딩 후 UTF-8로 디코딩
            decodedString = URLDecoder.decode(encodedString, StandardCharsets.UTF_8.toString());
            System.out.println(decodedString); // 출력: 안녕하세요
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
}
