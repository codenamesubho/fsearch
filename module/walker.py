#module imports
import os
#from ipdb import set_trace
import time
import sys

class app:
    def search(self,tag=None,name=None,dir=None,ex=None,show=False):
        count=0
        
        print "\n\n__________________________________________________________________________"
        print "\n Filetype = %s,\n Filename = %s,\n Search in : %s ,\n exclude path : %s"%(tag,name,dir,ex)
        print "\n\tSearching......\n\n"
        print "\n----------------------------------------------------------------------------"
        
        if dir==None:
	  dir='/home/'+os.getlogin()
	else:
	  if not(os.path.isdir(dir)):
	    print ("Woah!! "+dir+" seems to be invalid path,re-check the path and try again!\n")
	    sys.exit(1)
        if tag != None and '.' in tag:
	  tag= tag[1:]
	  
        time_start=time.time()
        
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
	if count==0:
	  print "No files found, try refining your search options."
	time_end= time.time()
	print "\n----------------------------------------------------------------------------"
        
	print "\n\nTotal results found: %d, Search-time: %0.3fs\n\n"%(count,time_end-time_start)
