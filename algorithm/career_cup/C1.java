import java.util.HashSet;

public class C1{

    public boolean c1_1(String str){
        //condition all characters in str must be letters
        int char_idx[] = new int[52];
        for(int i=0; i<52; ++i) char_idx[i]=0;
        char ch;
        for(int i=str.length()-1; i>=0; --i){
            ch = str.charAt(i);
            if(Character.isUpperCase(ch)){
                if(char_idx[ch-'A']>0)
                    return false;
                char_idx[ch-'A'] += 1;
            }else{
                if(char_idx[ch-'a']>0)
                    return false;
                char_idx[ch-'a'] += 1;
            }
        }
        return true;
    }

    public String c1_2(String src_str){
        StringBuffer sb = new StringBuffer("");
        for(int i=src_str.length()-2; i>=0; --i){
            sb.append(src_str.charAt(i));
        }
        sb.append(src_str.charAt(src_str.length()-1));
        return sb.toString();
    }

    public String c1_3(String src_str){
        if(src_str==null || src_str.length()==0) return src_str;
        StringBuffer sb = new StringBuffer("");
        boolean is_find = false;
        char ch;
        int str_len = src_str.length();
        for(int i=0, j=0; i<str_len; ++i){
            ch = src_str.charAt(i);
            is_find = false;
            for(j=sb.length()-1; j>=0; --j){
                if(sb.charAt(j) == ch){
                    is_find = true;
                    break;
                }
            }
            if(!is_find){
                sb.append(ch);
            }
        }
        return sb.toString();
    }
    
    public static void main(String args[]){
        C1 c1 = new C1();
        boolean result;
        String str1="abcdef", str2="abbcde", str3="abcdef\0";

        System.out.println("###Testing c1_1");
        System.out.println(str1+" has all unique characters? "+c1.c1_1(str1));
        System.out.println(str2+" has all unique characters? "+c1.c1_1(str2));

        System.out.println("###Testing c1_2");
        System.out.println("Origin String:" + str3 + "\nAfter reversing:" + c1.c1_2(str3));
        
        System.out.println("###Testing c1_3");
        String[] c1_3_testcase = {"abcbca", null, "a", "", "ab"};
        for(String test_str : c1_3_testcase){
            System.out.println("Test String:" + test_str + "-->" + c1.c1_3(test_str));
        }

        System.out.println("###Testing c1_4");
    }
}
