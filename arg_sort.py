#!/usr/bin/python

import sys,re

def arg_sort(arg):
    # Find all substrings of the following formats:
    # 1: -flag
    # 2: -flag value
    # 3: -flag "value1 value2 value3 etc"
    arg = " ".join(arg.split()) # remove extra spaces

    arg_list = re.findall('-(\w+)(?:\s+((?:"(?:[^"]*)")|(?:\w+)))?', arg)

    # create a dict to uniquify the flags incase the flag is used more than once
    arg_dict = dict()
    for arg_stmt in ( arg_list ):
        flag  = arg_stmt[0]
        fargs = arg_stmt[1]
        
        # if we have not see this flag before, create a new
        # key with a value of an empty list
        if flag not in arg_dict:
            arg_dict[flag] = []
        #subargs = re.findall('(?:(-\S+)\s+)?([^-]\S+)',fargs)
        if fargs.startswith('"') and fargs.endswith('"'):
            fargs = fargs[1:-1] # remove quotes
            subargs = re.findall('(-\S+\s+[^-^+]\S*)|(\S+)',fargs)
            for subarg in (sorted(subargs)):
                arg_dict[flag].append("".join(subarg))
        elif (len(fargs)):
            arg_dict[flag].append(fargs)

    return arg_dict


def arg_print(arg_dict):
    # display the sorted argument results            
    for flg in sorted(arg_dict.keys()):
        print "-" + flg
        for subflg in (arg_dict[flg]):
            print '\t' + subflg
            
def arg_jrun_string(arg_dict):
    cmd = ""
    # display the sorted argument results            
    for flg in sorted(arg_dict.keys()):
        cmd += "-" + flg + " "
        subcmd = ""
        prev_subcmd = "" # used for filter duplicate subcmds
        for subflg in (arg_dict[flg]):
            if (prev_subcmd != subflg): 
                subcmd += subflg + " "
            prev_subcmd = subflg;
        if (len (arg_dict[flg]) > 1):
            cmd += "\"" + subcmd + "\""
        else:
            cmd += subcmd
    return cmd

def arg_make_string(arg_dict):
    cmd = ""
    # display the sorted argument results            
    for flg in sorted(arg_dict.keys()):
        cmd += flg.toUpperCase() + "="
        subcmd = ""
        prev_subcmd = "" # used for filter duplicate subcmds
        for subflg in (arg_dict[flg]):
            if (prev_subcmd != subflg): 
                subcmd += subflg + " "
            prev_subcmd = subflg;
        if (len (arg_dict[flg]) > 1):
            cmd += "\"" + subcmd + "\""
        else:
            cmd += subcmd
    return cmd


if __name__ == "__main__":
    mylines = [ arg_sort(line) for line in sys.stdin]
    for arg in (mylines):
        arg_print(arg)
        #print arg_jrun_string(arg)
