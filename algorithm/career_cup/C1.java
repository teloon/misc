import java.util.HashSet;

public class C1{
    
    public boolean c1_1(String str){
        //condition all characters in str must be letters
        int char_idx[] = new int[52];
        for(int i=0; i<52; ++i) char_idx=0;
        char ch;
        for(int i=str.length()-1; i>=0; --i){
            ch = str.charAt(i)
            if Character.isUpperCase(ch){
                if char_idx[ch-'A']>0:
                    return true;
                char_idx[ch-'A'] += 1;
            }else{
                if char_idx[ch-'a']>0:
                    return true;
                char_idx[ch-'a'] += 1;
            }
            return false;
        }
            hs.add(str.charAt(i));
        if(hs.size() == str.length())
            return true;
        else
            return false;
    }
    
    public static void main(String args[]){
        C1 c1 = new C1();
        boolean result;
        String str1="abcdef", str2="abbcde";
        System.out.println(str1+" has all unique characters? "+c1.c1_1(str1));
        System.out.println(str2+" has all unique characters? "+c1.c1_1(str2));
    }
}
