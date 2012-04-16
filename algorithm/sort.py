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

def partition(arr, start, end, oprt):
    pivot = arr[end]
    i,j = start-1, start
    while j<end:
        if oprt(arr[j], pivot):
            i += 1
            arr[i],arr[j] = arr[j], arr[i]
        j += 1
    arr[i+1],arr[end] = arr[end], arr[i+1]
    return i+1

def do_qs(arr, start, end, oprt):
    if(start<end):
        p = partition(arr, start, end, oprt)
        do_qs(arr, start, p-1, oprt)
        do_qs(arr, p+1, end, oprt)


def quick_sort_recur(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    do_qs(arr, 0, len(arr)-1, oprt)

def quick_sort(arr, reverse=False):
    oprt = operator.gt if reverse else operator.lt
    split_list = [(0, len(arr)-1),]
    while split_list:
        start,end = split_list.pop()
        if(start<end):
            i,j = start-1, start
            pivot = arr[end]
            while j<end:
                if oprt(arr[j], arr[end]):
                    i += 1
                    arr[i],arr[j] = arr[j],arr[i]
                j += 1
            arr[i+1],arr[end] = arr[end],arr[i+1]
            split_list.append((start, i))
            split_list.append((i+2, end))

def sift_down(arr, sub_root, arr_end, oprt):
    # sub_root: root index of the subtree that needs adjustment
    # arr_end: end index of the array that needs adjustment
    curr = sub_root
    sub_root_val = arr[sub_root]
    next_son = -1
    while curr<=(arr_end-1)/2:
        next_son = 2*curr+1
        if 2*curr+2<=arr_end and oprt(arr[2*curr+1], arr[2*curr+2]): # (2*curr+2) is the right son
            next_son = 2*curr+2
        if oprt(sub_root_val, arr[next_son]):
            arr[curr] = arr[next_son]
            curr = next_son
        else: break;
    arr[curr] = sub_root_val

def print_heap(arr):
    print ">> Heap is built:"
    depth = 0
    for i,val in enumerate(arr):
        print val,
        if i==pow(2, depth+1)-2:
            print ""
            depth += 1
    print ""

def heap_sort(arr, reverse=False):
    """
    >>> heap_sort([3,4,2,1])
    [1, 2, 3, 4]
    """
    oprt = operator.gt if reverse else operator.lt
    arr_len = len(arr)
    # build head
    for i in range(arr_len/2-1, -1, -1):
        sift_down(arr, i, arr_len-1, oprt)
    #print_heap(arr)
    for i in range(arr_len-1): #the last two(root and left son) is reversely sorted
        arr[0], arr[-1*i-1] = arr[-1*i-1], arr[0]
        sift_down(arr, 0, arr_len-i-2, oprt)
    print arr


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
    reverse = False
#    print_sort(bubble_sort, arr)
#    print_sort(select_sort, arr)
#    print_sort(merge_sort, arr)
#    print_sort(shell_sort, arr)
#    print_sort(insertion_sort, arr)
#    print_sort(quick_sort_recur, arr, reverse)
    print_sort(quick_sort, arr, reverse)
#    print_sort(heap_sort, arr, reverse)
    import doctest
    doctest.testmod()
