// Time Complexity : O (m+n) 
// Space Complexity : O (1) no extra space
// Did this code successfully run on Leetcode : Yes
// Any problem you faced while coding this : no 

public class prob3 {

    public static boolean findIn2dArray(int[][] matrix, int target){
        if(matrix == null || matrix.length == 0) return false;
        int m = matrix.length; int n = matrix[0].length;
        int i = 0; int j = n - 1;
        while(i < m && j >= 0){
            if(matrix[i][j] == target) return true;
            else if (target < matrix[i][j]){
                j--;
            }else{
                i++;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        
    }
    
}