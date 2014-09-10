#!/usr/bin/env python
import argparse
import sys
import os
from module.walker import app

if  __name__=='__main__':
    parser = argparse.ArgumentParser(description="Searches for a file",epilog="Provide at least -t or -n argument to start with")
    #parser.add_argument("-w","--web",action="store_true", help="run as flask webapp")
    group = parser.add_argument_group('group','Atleast one of these options is need to search')
    group.add_argument("-t","--type", help="set file type")
    group.add_argument("-n","--name", help="search filename")
    parser.add_argument("-ex","--exclude",nargs='+', help="exclude path patterns")
    parser.add_argument("-s","--show",action="store_true",help="show files that start with '.'")
    parser.add_argument("-d","--directory", help="search directory")
    parser.add_argument("--setup",action="store_true",help="setup database")
    parser.add_argument("--cleanall",action="store_true",help="cleans database completely")
    args = parser.parse_args() 
    
    
    if args.type==None and args.name==None:
        os.system("python %s -h"%sys.argv[0])
	sys.exit(0)
    
    else :
        app_obj=app()
        app_obj.search(args.type,args.name,args.directory,args.exclude,args.show)
    