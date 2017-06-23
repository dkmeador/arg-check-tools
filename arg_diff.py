#!/usr/bin/python

import arg_sort
import sys,re

FLAGNOTFOUND = ['<FLAGNOTFOUND>']       # KeyNotFound for dictDiff
red_txt  ="\033[31m";
gre_txt  ="\033[92m"; 
norm_txt ="\033[00m";

def dict_diff(first, second):
    """ Return a dict of keys that differ with another config object.  If a value is
        not found in one fo the configs, it will be represented by FLAGNOTFOUND.
        @param first:   Fist dictionary to diff.
        @param second:  Second dicationary to diff.
        @return diff:   Dict of Key => (first.val, second.val)
    """
    diff = {}
    # Check all keys in first dict
    for key in first.keys():
        if (not second.has_key(key)):
            diff[key] = (first[key], FLAGNOTFOUND)
        elif (first[key] != second[key]):
            diff[key] = (first[key], second[key])
    # Check all keys in second dict to find missing
    for key in second.keys():
        if (not first.has_key(key)):
            diff[key] = (FLAGNOTFOUND, second[key])
    return diff

def array_diff(first, second):
    max_len = max(len(first), len(second))
    diff1_str = ""
    diff2_str = ""
    
    offset1 = 0
    offset2 = 0

    while ((offset1 < len(first)) | (offset2 < len(second))):
        if ((offset1 < len(first)) & (offset2 < len(second))):
            if (first[offset1] == second[offset2]):
                diff1_str += first[offset1] + " "
                diff2_str += first[offset1] + " "                
                offset1 += 1
                offset2 += 1                
            elif (first[offset1] < second[offset2]):
                diff1_str += red_txt + first[offset1]  + norm_txt + " "
                offset1 += 1
            else:
                diff2_str += gre_txt + second[offset2] + norm_txt + " "
                offset2 += 1
        elif (offset1 < len(first)):
            diff1_str += red_txt + first[offset1]  + norm_txt + " "
            offset1 += 1
        else:
            diff2_str += gre_txt + second[offset2] + norm_txt + " "
            offset2 += 1
            
    return [diff1_str,diff2_str]


if __name__ == "__main__":
    
    if len(sys.argv) != 3:
        print "ERROR: Command requires two argument files"
        print "Usage:"
        print sys.argv[0] + " <arg_file1> <arg_file2>"
        sys.exit(1)
    
    args1_list = open(sys.argv[1]).readlines()
    args2_list = open(sys.argv[2]).readlines()

    dict1_args = arg_sort.arg_sort(args1_list[0]);
    dict2_args = arg_sort.arg_sort(args2_list[0]);
    
    flag_diff = dict_diff(dict1_args,dict2_args)
    
    # display the sorted argument diff results            
    for flg in sorted(flag_diff.keys()):
        print "-" + flg
        line_diffs = array_diff(flag_diff[flg][0],flag_diff[flg][1])
        print "\t< " + line_diffs[0]
        print "\t> " + line_diffs[1]    
