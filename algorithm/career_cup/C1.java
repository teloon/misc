import java.util.HashSet;
import java.util.ArrayList;

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
    
    public boolean c1_4(String str1, String str2){
        if(str1 == null || str2 == null || str1.length()==0 || str2.length()==0) return false;
        if(str1.length() != str2.length()) return false;
        int[] hit_map = new int[256];
        for(int cnt : hit_map) cnt = 0;
        for(int i=str1.length()-1; i>=0; --i){
            ++hit_map[str1.charAt(i)];
        }
        for(int i=str2.length()-1; i>=0; --i){
            if(hit_map[str2.charAt(i)] <= 0) return false;
            else{
                --hit_map[str2.charAt(i)];
            }
        }
        for(int i=0; i<256; ++i){
            if(hit_map[i] != 0) return false;
        }
        return true;
    }

    public String c1_5(String src){
        StringBuffer sb = new StringBuffer("");
        for(int i=src.length()-1; i>=0; --i){
            if(src.charAt(i) == ' ')
                sb.append("%20");
            else
                sb.append(src.charAt(i));
        }
        return sb.toString();
    }

    public void c1_6(byte[][] image, int dim){
        int st=0, rnd=0, i=0, curr_x, curr_y;
        byte temp;
        while((rnd+1)*2 <= dim){
            curr_x = rnd;
            for(curr_y=rnd; curr_y<dim-rnd-1; ++curr_y){
                temp = image[curr_x][curr_y];
                image[curr_x][curr_y] = image[dim-1-curr_y][curr_x];
                image[dim-1-curr_y][curr_x] = image[dim-1-curr_x][dim-1-curr_y];
                image[dim-1-curr_x][dim-1-curr_y] = image[curr_y][dim-1-curr_x];
                image[curr_y][dim-1-curr_x] = temp;
            }
            ++rnd;
        }
    }

    public void c1_7(int[][] mat){
        int M = mat.length;
        int N = mat[0].length;
        ArrayList<Integer> row_al = new ArrayList<Integer>();
        ArrayList<Integer> col_al = new ArrayList<Integer>();
        System.out.println("Initial Matrix:");
        for(int i=0; i<M; ++i){
            for(int j=0; j<N; ++j){
                System.out.print(mat[i][j]+ " ");
                if(mat[i][j] == 0){
                    row_al.add(i);
                    col_al.add(j);
                }
            }
            System.out.println();
        }
        for(int row : row_al)
            for(int col=0; col<N; ++col)
                mat[row][col] = 0;
        for(int col : col_al)
            for(int row=0; row<M; ++row)
                mat[row][col] = 0;
        System.out.println("Final Matrix:");
        for(int i=0; i<M; ++i){
            for(int j=0; j<N; ++j){
                System.out.print(mat[i][j]+ " ");
            }
            System.out.println();
        }
        
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
        String[] c1_4_testcase1 = {"dog", "an apple", "fuck the hats", "", null};
        String[] c1_4_testcase2= {"god", "apple na", "what the fuck", "", null};
        for(int i=c1_4_testcase1.length-1; i>=0; --i){
            System.out.format("Are \"%s\" and \"%s\" anagrams? %b\n", 
                                c1_4_testcase1[i], c1_4_testcase2[i], 
                                c1.c1_4(c1_4_testcase1[i], c1_4_testcase2[i]));
        }

        System.out.println("###Testing c1_5");
        String c1_5_testcase = "abc 123 hah";
        System.out.format("Origin String:%s\tResult String:%s\n", c1_5_testcase, c1.c1_5(c1_5_testcase));

        System.out.println("###Testing c1_7");
        int M = 5;
        int N = 6;
        int[][] mat = new int[M][N];
        for(int i=0,j=0; i<M ; ++i)
            for(j=0; j<N; ++j)
                mat[i][j] = 1;
        mat[2][3] = 0;
        mat[2][4] = 0;
        mat[1][3] = 0;
        c1.c1_7(mat);
    }
}
