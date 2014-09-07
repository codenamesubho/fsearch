import os
from ipdb import set_trace
import argparse
from db_module.db import db
#import threading
import time
class app:
    def search(self,tag=None,name=None,dir=None,ex=None,show=False):
        time_start=time.time()
        count=0
        obj=db()
        print "\n\n__________________________________________________________________________"
        print "\nFiletype = %s,\n Filename = %s,\n Search in : %s ,\n exclude path : %s"%(tag,name,dir,ex)
        print "\nSearching......\n\n"
        print "\n----------------------------------------------------------------------------"
        if dir==None:
	  dir='/home/'+os.getlogin()
	
        for root,dirs,files in os.walk(dir):
	
	    if show==False:
	      files = [f for f in files if not f[0] == '.']
	      dirs[:] = [d for d in dirs if not d[0] == '.']
            
            root_path=root[len(dir):]
            if ex!=None:
	      [dirs.remove(exclude) for exclude in ex if exclude in dirs]
		
            for filename in files:
                filetype=filename.split('.')
                filetype=filetype[-1]
                
                if (ex!=None and all(d not in root_path for d in ex)) or (ex==None):
		  
		  if ((tag!=None and filetype==tag) and (name!=None and name.lower() in filename.lower())) or ((tag==None) and (name!=None and name.lower() in filename.lower())) or ((tag!=None and tag == filetype) and (name==None)):
		      count+=1
		      print str(count)+'->\t'+root+'/'+filename+'\n'
		
		#else:
		#  print dirs
	time_end= time.time()
	print "\n----------------------------------------------------------------------------"
        
	print "\n\nTotal results found: %d, Search-time: %0.3f ns\n\n"%(count,time_end-time_start)

if  __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w","--web",action="store_true", help="run as flask webapp")
    parser.add_argument("-t","--type", help="set file type")
    parser.add_argument("-n","--name", help="search filename")
    parser.add_argument("-ex","--exclude",nargs='+', help="exclude path patterns")
    parser.add_argument("-s","--show",action="store_true",help="show files that start with '.'")
    parser.add_argument("-d","--directory", help="search directory")
    parser.add_argument("--setup",action="store_true",help="setup database")
    parser.add_argument("--cleanall",action="store_true",help="cleans database completely")
    args = parser.parse_args() 
    obj=db()
    if args.cleanall:
        obj.cleanall()
	
    if args.setup:
        obj.setup()

    else :
        app_obj=app()
        app_obj.search(args.type,args.name,args.directory,args.exclude,args.show)
    