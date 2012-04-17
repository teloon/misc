import java.util.Random;
import java.lang.Math;

public class Sort  {
    private int[] arr;
    private boolean reversed = false;

    public Sort(){}
    
    public Sort(boolean reversed){this.reversed = reversed;}

    public Sort(int[] arr){
        this.arr = arr;
    }
    
    public Sort(int[] arr, boolean reversed){
        this.arr = arr;
        this.reversed = reversed;
    }

    public void bubbleSort(){
       int arr_len=arr.length;
       for(int i=0,j=0; i<arr_len-1; ++i){
            for(j=i+1; j<arr_len; ++j){
                if(compare(arr[j], arr[i])){
                    swap(i, j);
                }
            }
       }
    }

    public void insertSort(){
       int arr_len=arr.length, temp;
       for(int i=1,j=0; i<arr_len; ++i){
           j = i;
           temp = arr[i];
           while(--j>=0 && compare(temp, arr[j])){
                arr[j+1] = arr[j];
           }
           arr[j+1] = temp;
       }
        
    }

    public void selectSort(){
       int arr_len=arr.length, sel_pos=-1, temp;
       for(int i=0,j=0; i<arr_len-1; ++i){
           sel_pos = i;
           for(j=i+1; j<arr_len; ++j){
                if(compare(arr[j], arr[sel_pos])) sel_pos = j;
           }
           temp = arr[i];
           arr[i] = arr[sel_pos];
           arr[sel_pos] = temp;
       }
    }

    public void shellSort(){
        int arr_len = arr.length;
        int step=0,sel=-1;
        for(step=0; step<arr_len; step=step*3+1);
        step = (step-1)/3;
        for(int i=0,j=0,k=0; step>=1; step=(step-1)/3){
             for(i=0; i<step; ++i){
                for(j=i; j<arr_len; j+=step){
                    sel = j;
                    for(k=j+step; k<arr_len; k+=step){
                        if(compare(arr[k], arr[sel]))
                            sel = k;
                    }
                    swap(j, sel);
                }
             }
        }
    }

    private void printArr(int[] arr, int len){
        System.out.print("Arr: ");
        for(int i=0; i<len; ++i)
            System.out.print(arr[i]+",");
        System.out.println();
    }

    public void mergeSort(){
        int arr_len=arr.length,size=1,i=0,j=0,k=0,tmp_arr_i=0;
        while(size<arr_len){
            int[] tmp_arr = new int[2*size];
            for(i=0; i+size<arr_len; i+=2*size){
                j = i;
                k = i+size;
                tmp_arr_i = 0;
                while(j<i+size && k<i+2*size && k<arr_len){
                    if(compare(arr[j], arr[k]))  tmp_arr[tmp_arr_i++] = arr[j++];
                    else tmp_arr[tmp_arr_i++] = arr[k++];
                }
                while(j<i+size && j<arr_len) tmp_arr[tmp_arr_i++] = arr[j++];
                while(k<i+2*size && k<arr_len) tmp_arr[tmp_arr_i++] = arr[k++];
                for(j=0,k=i; j<tmp_arr_i; ) arr[k++]=tmp_arr[j++];
                //printArr(tmp_arr, 2*size);
            }
            size *= 2;
        }
    }

    private int partition(int start, int end){
        int i=start-1, j=start, pivot=this.arr[end];
        for(; j<end; ++j){
            if(compare(this.arr[j], pivot)){
                ++i;
                swap(i, j);
            }
        }
        swap(i+1, end);
        return i+1;
    }

    private void doQS(int start, int end){
        if(start<end){
            int p = partition(start, end);
            doQS(start, p-1);
            doQS(p+1, end);
        }
    }

    public void quickSort(){
       doQS(0, arr.length-1);
    }

    public void siftDown(int curr, int end){
        int next_son = -1;
        int val = arr[curr];
        while(2*curr+1<=end){
            next_son = 2*curr+1;
            if(2*curr+2<=end && compare(arr[2*curr+1], arr[2*curr+2]))
                next_son = 2*curr+2;
            if(compare(val, arr[next_son])){
                arr[curr] = arr[next_son];
                curr = next_son;
            }
            else
                break;
        }
        arr[curr] = val;
    }

    public void heapSort(){
        for(int i=arr.length/2-1; i>=0; --i){
            siftDown(i, arr.length-1);
        }
        printArr();
        for(int i=arr.length-1; i>0; --i){
            swap(0, i);
            siftDown(0, i-1);
        }
        
    }

    public void countSort(int max){
        //range of elements in arr is [0, max]
        int[] cnt = new int[max+1];
        for(int i=0; i<max; ++i) cnt[i]=0;
        for(int v : arr) cnt[v]++;
        if(!reversed)
            for(int i=1; i<max; ++i) cnt[i]+=cnt[i-1];
        else
            for(int i=max-2; i>=0; --i) cnt[i]+=cnt[i+1];
        int[] newArr = new int[arr.length];
        for(int i=arr.length-1; i>=0; --i){
            newArr[cnt[arr[i]]-1] = arr[i];
            cnt[arr[i]]--;
        }
        arr = newArr;
        printArr(newArr, newArr.length);
    }

    public void bucketSort(int radixDigit){
        //implement by count sort
        int[] newArr = new int[arr.length];
        int[] cnt = new int[10];
        for(int i=0; i<10; ++i) cnt[i] = 0;
        for(int v : arr) cnt[getIndex(v, radixDigit)]++;
        if(!reversed)
            for(int i=1; i<10; ++i) cnt[i]+=cnt[i-1];
        else
            for(int i=8; i>=0; --i) cnt[i]+=cnt[i+1];
        for(int i=arr.length-1; i>=0; --i){
            newArr[cnt[getIndex(arr[i], radixDigit)]-1] = arr[i];
            cnt[getIndex(arr[i], radixDigit)]--;
        }
        arr = newArr;
        printArr();

    }

    private int getIndex(int val, int radixDigit){
        while(radixDigit>0){
            val /= 10;
            radixDigit--;
        }
        return val%10;
    }

    public void radixSort(int maxLen){
        for(int i=0; i<maxLen; ++i)
            bucketSort(i);
    }

    public void printArr(){
        int arr_len = arr.length;
        for(int i=0; i<arr_len; ++i){
            System.out.print(arr[i]+",");
        }
        System.out.println();
    }

    public void gen_randint(int num){
        final int MAX = 100;
        Random rand = new Random();
        arr = new int[num];
        for(int i=0; i<num; ++i){
            arr[i] = rand.nextInt(MAX);
        }
    }

    public static void main(String args[]){
        Sort st = new Sort(true);
        st.gen_randint(15);
        System.out.println(">>Before Sort:");
        st.printArr();
        //st.bubbleSort();
        //st.insertSort();
        //st.selectSort();
        //st.quickSort();
        //st.heapSort();
        //st.shellSort();
        //st.mergeSort();
        //st.countSort(100);
        st.radixSort(2);
        System.out.println(">>After Sort:");
        st.printArr();
    }


    private void swap(int i, int j){
        int temp = this.arr[i];
        this.arr[i] = arr[j];
        this.arr[j] = temp;
    }

    private boolean compare(int a, int b){
        return reversed?a>b:a<b;
    }
}
