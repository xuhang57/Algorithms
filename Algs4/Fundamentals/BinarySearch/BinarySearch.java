/*
 * Compilation: javac BinarySearch.java
 * Execution: java BinarySearch
 *
 */
import java.util.ArrayList;
import java.util.Collections;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.Scanner;

public class BinarySearch {
    /*
     *
     */
    public static int indexOf(ArrayList<Integer> a, int target) {
        int low = 0;
        int high = a.size() - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            System.out.println("Currently searching: " + a.get(mid));
            if (target < a.get(mid)) {
                high = mid - 1;
            } else if (target > a.get(mid)) {
                low = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
    
    public static void main(String[] args) throws IOException {

        Scanner s = null;
        ArrayList<Integer> nums = new ArrayList<>();
        try {
            s = new Scanner(new BufferedReader(new FileReader("./tinyW.txt")));

            while (s.hasNext()) {
                String num = s.next();
                nums.add(Integer.parseInt(num));
            }
        } finally {
            if (s!=null) {
                s.close();
            }
        }

        Collections.sort(nums);
        System.out.println("Integer list: " + nums);
        Scanner reader = new Scanner(System.in);
        System.out.println("Please type in the number you want to search:");
        int target = reader.nextInt();
        System.out.println("Start searching");
        int result = indexOf(nums, target);
        if (result == -1) {
            System.out.println("Cannot find target: " + target);
        } else {
            System.out.println("Found: " + nums.get(result));
        }
        reader.close();
    }
}

