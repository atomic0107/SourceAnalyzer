'''
Created on Jan 26, 2019

@author: atomic
'''
import os
import re

def fnc_analyze(path):

    flag = 0
    print("fnc_analyze")
    print(path)
    file = open( path, 'r' )
    print("\n\n")
    brc_cnt = 0
    cnt = 0
    func_name = None
    func_list = []

    for line in file:
        cnt += 1
        line = line[:line.find("\n")]

        if(line.find("(") > -1):
            if (line.find("for") > -1):
                continue
            if (line.find("while") > -1):
                continue
            if(line.find(");") > -1):
                continue
            flag = 1
            fnc_line = line[:line.find("(")]
            func_name = line[fnc_line.rfind(" ")+1:line.find("(")]

        if flag == 1:
            if(line.find(")") > -1):
                flag = 2
                if(line.find(");") > -1):
                    flag = 0
                    continue
                if(line.find("{") > -1):
                    brc_cnt += 1
                    continue

        if flag == 2 :
            if(line.find("{") > -1):
                brc_cnt += 1
            if(line.find("}") > -1):
                brc_cnt -= 1
                if(brc_cnt==0):
                    flag = 3

        if( brc_cnt == 0):
            if flag > 2:
                #print(line + "\t" + str(cnt))
                print(func_name)
                func_list.append(func_name)
                flag = 0
    file.close()

    return func_list

def intr_func_analyze( path, func_list ):

    flag = 0
    print("intr_fnc_analyze")
    print(path)
    print("____________________________________________________")
    for cnt in range (0,len(func_list)-1):
        file = open( path, 'r' )
        cnt += 1
        print(func_list[cnt])
        print("____________________________________________________")

        flag = 0
        for line in file:
            line = line[:line.find("\n")]
            if flag == 1:
                if( line.find(");") > -1 ):
                    fnc_line = line[:line.find("(")]
                    func_name = line[fnc_line.rfind(" ")+1:line.find("(")]
                    print(func_name)
            else:
                if(line.find( func_list[cnt]) > -1 ):
                    line = line[line.find( func_list[cnt]):]
                    if( line.find("(") > -1 ):
                        if( line.find(");") > -1 ):
                            continue
                        print( line +"\t" + str(cnt))
                        flag = 1
        file.close()

def analyzer(path):
    func_list = fnc_analyze( path )
    intr_func_analyze( path, func_list )

def main():
    path = os.getcwd()
    print("↓ input source analyze path ")
    #path = input()
    path = path + "/udagawa.c"
    print(path)
    analyzer(path)

if __name__ == '__main__':
    main()


