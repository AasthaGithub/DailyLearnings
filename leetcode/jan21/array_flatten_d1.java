// import org.apache.commons.lang3.ArrayUtils;
// int index= ArrayUtils.indexOf(arr, ele);
// import java.util.Arrays;
// Arrays.asList(arr).indexOf(ele);
import java.util.stream.IntStream; 

class Solution {
    
    public static int findIndex(int arr[], int t) 
    { 
        int len = arr.length; 
        return IntStream.range(0, len) 
            .filter(i -> t == arr[i]) 
            .findFirst() // first occurrence 
            .orElse(-1); // No element found 
    } 
    public static int find_next(int[] arr, int ele){
        int index = findIndex(arr,ele);
        if (index == -1 || index==arr.length-1)  return -1;
        else{
            return arr[index+1];
        }
    }
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int arr_len = arr.length;
        int pcs_len = 0;
        
        for (int[] piece : pieces){
            
            pcs_len += piece.length;
            if (piece.length > 1){
                int i = 0;
                while(i < piece.length -1){
                    if (find_next(arr, piece[i]) != piece[i+1]){
                        return false;
                    }
                }
            } // checked for long pieces
            
            else{
                int index = findIndex(arr, piece[0]);
                 //System.out.println(piece[0] + " " +index);
                if (index == -1)  {
                    System.out.println("inside single ele");
                    return false;
                }
            } // checked for single element piece
            
        } // checked for every pieces
        
        if (arr_len!= pcs_len){
            return false;
        }
        return true;
    }
}




// Fast & Simple Without Hashmap
class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int i = 0;
        while (i < arr.length) {
            boolean found = false;
            for (int[] piece : pieces) {
                if (piece[0] == arr[i]) {
                    found = true;
                    ++i;
                    for (int k = 1; k <= piece.length - 1; ++k) {
                        if (piece[k] != arr[i]) {
                            return false;
                        }
                        ++i;
                    }
                    break;
                }
            }
            if(!found) {
                return false;
            }
        }
        return true;
    }
}



// With hashMap

class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        
        Map<Integer, int[]> map = new HashMap<>();
        for(int[] piece: pieces) {
            map.put(piece[0], piece);
        }
        
        for(int i=0; i<arr.length; i++) {
            if(map.containsKey(arr[i])) {
                
                if(map.get(arr[i]).length>1 && i!=arr.length-1) {
                    
                    int[] a = map.get(arr[i]);                
                    for(int j=1; j<a.length; j++) {
                        if(arr[++i]!= a[j])
                            return false;
                    }
                }                
                
            } else return false;
        }
        return true;
        
    }
}


// mark visited approach

class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        StringBuilder array=normalize(arr);
    for(int[] slide:pieces){
        StringBuilder s=normalize(slide);
        int pos=array.indexOf(String.valueOf(s));
        if(pos!=-1){
            int len=s.length();
            for (int i=pos;i<pos+len;i++){
                array.setCharAt(i,'#');
            }
        }else{
            return false;
        }
    }
    for(int i=0;i<array.length();i++){
        if(array.charAt(i)!='#')
            return false;
    }
    return true;
}

public StringBuilder normalize(int[] arr){
    StringBuilder sb=new StringBuilder("#");
    for(int x:arr){
        sb.append(x);
        sb.append("#");
    }
    return sb;
}
        
    }




// Least Space complexity (SC)

class Solution {
    class  Piece implements Comparable<Piece>{
        int firstElement;
        int[] allElements;

        Piece(int firstElement){
            this.firstElement = firstElement;
        }

        Piece(int firstElement,int[] allElements){
            this.firstElement = firstElement;
            this.allElements = allElements;
        }
        @Override
        public int compareTo(Piece o) {
            return Integer.compare(this.firstElement,o.firstElement);
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Piece piece = (Piece) o;
            return firstElement == piece.firstElement;
        }

        @Override
        public int hashCode() {
            return Objects.hash(firstElement);
        }
    }
    
    public boolean canFormArray(int[] arr, int[][] pieces) {
        int[] finalResult = new int[arr.length];
        int fp=0;
        List<Piece> pieceList = new ArrayList<>();
        for(int i=0;i<pieces.length;i++){
            int[] curr = pieces[i];
            pieceList.add(new Piece(curr[0],curr));
        }
        Collections.sort(pieceList);
        for(int i=0; i<arr.length;i++){
            int index = Collections.binarySearch(pieceList,new Piece(arr[i]));
            if(index>=0){
                for(int f=0; f<pieceList.get(index).allElements.length;f++){
                    if(fp<finalResult.length){
                        finalResult[fp++] = pieceList.get(index).allElements[f];
                    }else{
                        return false;
                    }
                }
            }
        }

        for(int i=0,j=0;i<arr.length && j<finalResult.length;i++,j++){
            if(arr[i] != finalResult[j]){
                return false;
            }
        }

        return true;
    }
}

// Less Space-  no normalize, mark Visited approach

class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        StringBuilder sb = new StringBuilder();
        for(int x : arr){
            sb.append(x);
            sb.append("#");
        }
        for(int i = 0; i < pieces.length; i++){
            StringBuilder res = new StringBuilder();
            for(int j = 0; j < pieces[i].length; j++){
                res.append(String.valueOf(pieces[i][j]));
                res.append("#");
            }
            if(!sb.toString().contains(res.toString())){
                return false;
            }
        }
        return true;
    }
}
