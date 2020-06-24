/*
https://leetcode.com/discuss/interview-question/703151/Microsoft-or-OA-2020-or-Days-of-week

I/P: s="Wed", K=2
O/P: Fri

k<500
*/

import java.util.Map;
import java.util.HashMap;

class Test1 {
    public static void main(String[] args) {
        String[] days = {
            "MONDAY",
            "TUESDAY",
            "WEDNESDAY",
            "THURSDAY",
            "FRIDAY",
            "SATURDAY",
            "SUNDAY"
        };

        Map<String, Integer> map = new HashMap<>();
        for(int i=0; i<days.length; i++) {
            map.put(days[i], i);
        }
        helper(days, 2, "WEDNESDAY", map);
    }

    private static void helper(String[] days, int n, String day, Map<String, Integer> map) {
        int dayIndex = -1;
        if (map.containsKey(day)) {
            dayIndex = map.get(day);
        }
        int processedIndex = n % 7; // create new index by modding it with no. of days
        int dayIndexNew = (dayIndex+2) % days.length;  // get the index of the day using processedIndex
        String returnDay = days[dayIndexNew];
        System.out.println(returnDay);
    }
}
