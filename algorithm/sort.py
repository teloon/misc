#!/usr/bin/env python
#-*- coding:utf8 -*-

"""
    a bunch of sort algorithms
"""

import operator, random, sys, time, copy

random_arr = lambda size:[random.randint(0, 100) for i in xrange(size)]

def bubble_sort(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    arr_len = len(arr)
    for i in xrange(arr_len):
        for j in xrange(i+1, arr_len):
            if oprt(arr[j], arr[i]):
                arr[i],arr[j] = arr[j],arr[i] #swap values in postion i and j
    return arr

def select_sort(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    arr_len = len(arr)
    for i in xrange(arr_len):
        sel = i
        for j in xrange(i+1, arr_len):
            if oprt(arr[j], arr[sel]):
                sel = j
        if sel != i:
            arr[sel],arr[i] = arr[i],arr[sel]
    return arr

def insertion_sort(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    arr_len = len(arr)
    temp = 0
    for i in range(1, arr_len):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            if oprt(temp, arr[j]):
                arr[j+1] = arr[j]
            else:
                j += 1
                break
        arr[j] = temp
    return arr


def shell_sort(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    arr_len = len(arr)
    step = 1
    while step<arr_len: step=3*step+1
    step = (step-1)/3 # step sequence by Knuth,1973(O(N^1.5)): (3^k - 1)/2, k=1,2,3,4... 
    while step>= 1:
        for sub_seq_beg in xrange(step):
            #select sort
            for i in xrange(sub_seq_beg, arr_len, step):
                sel = i
                for j in xrange(i+step, arr_len, step):
                    if oprt(arr[j], arr[sel]) :
                        sel = j
                arr[sel], arr[i] = arr[i], arr[sel]
        step = (step-1)/3
    return arr

def merge_sort(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    grp_size = 1
    tmp_arr = []
    arr_len = len(arr)
    while grp_size<arr_len:
        tmp_arr = copy.deepcopy(arr)
        start_pos = 0
        del arr[:]
        while start_pos+grp_size<arr_len:
            grp_idx1, grp_idx2 = start_pos, start_pos+grp_size
            while grp_idx1<start_pos+grp_size and grp_idx2<start_pos+2*grp_size and grp_idx2<arr_len:
                if oprt(tmp_arr[grp_idx1], tmp_arr[grp_idx2]):
                    arr.append(tmp_arr[grp_idx1])
                    grp_idx1 += 1
                else:
                    arr.append(tmp_arr[grp_idx2])
                    grp_idx2 += 1
            while grp_idx1<start_pos+grp_size:
                arr.append(tmp_arr[grp_idx1])
                grp_idx1 += 1
            while grp_idx2<start_pos+2*grp_size and grp_idx2<arr_len:
                arr.append(tmp_arr[grp_idx2])
                grp_idx2 += 1
            start_pos += grp_size*2
        while start_pos<arr_len: #tend to be ignored
            arr.append(tmp_arr[start_pos])
            start_pos += 1
        del tmp_arr[:]
        grp_size *= 2
    return arr

def quick_sort_recur(arr, start, end, oprt):
    if end-start==1: #be careful with the recursion base
        if not oprt(arr[start], arr[end]):
            arr[start], arr[end] = arr[end], arr[start]
        return
    if end-start<1:
        return
    #always choose arr[start] as the pivot (assume uniform distribution)
    pivot = arr[start]
    low,high = start+1,end
    while low<high:
        while low<=end and oprt(arr[low], pivot): low += 1;
        while high>=start+1 and not oprt(arr[high], pivot): high -= 1;
        if low<high:
            arr[low],arr[high] = arr[high],arr[low]
    arr[start],arr[high] = arr[high],arr[start]
    if high-1-start<end-low:
        quick_sort_recur(arr, start, high-1, oprt)
        quick_sort_recur(arr, low, end, oprt)
    else:
        quick_sort_recur(arr, low, end, oprt)
        quick_sort_recur(arr, start, high-1, oprt)

def quick_sort(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    quick_sort_recur(arr, 0, len(arr)-1, oprt)


def print_sort(sort_func, arr, reverse=False):
    print "###", sort_func.__name__, " ###"
    print ">> Before:", arr
    st = time.time()
    sort_func(arr, reverse)
    print ">> After:", arr
    print ">> Time Usage: %.5f, array size: %d" % ((time.time()-st), len(arr))


if __name__=="__main__":
    arr = random_arr(30)
#    arr = [3,7,2,3,7,4,1,0,8,5,6]
    reverse = True
#    print_sort(bubble_sort, arr)
#    print_sort(select_sort, arr)
#    print_sort(merge_sort, arr)
#    print_sort(shell_sort, arr)
#    print_sort(insertion_sort, arr)
    print_sort(quick_sort, arr, reverse)
