import java.util.HashSet

public class C1{
    
    public boolean c1_1(String str){
        HashSet<Character> hs = new HashSet<Character>();
        for(char c:str) hs.add(c);
        if(hs.size() == str.length)
            return true;
        else
            return false;
    }
    
    public static void main(String args[]){
        C1 c1 = new C1();
        boolean result;
        String str1="abcdef", str2="abbcde";
        System.out.println(str1+"has all unique characters? ")+c1.c1_1(str1);
        System.out.println(str2+"has all unique characters? ")+c1.c1_1(str2);
    }
}
