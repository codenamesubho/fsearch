from distutils.core import setup

#This is a list of files to install, and where
#(relative to the 'root' dir, where setup.py is)
#You could be more specific.
files = [""]

setup(name = "fsearch",
    version = "1.0",
    description = "Search for files in linux",
    author = "Subhendu Ghosh",
    author_email = "subho.prp@gmail.com",
    url = "https://github.com/Subho-bcrec/fsearch",
    #Name the folder where your packages live:
    #(If you have other packages (dirs) or modules (py files) then
    #put them into the package directory - they will be found 
    #recursively.)
    packages = ['module'],
    #'package' package must contain files (see list above)
    #I called the package 'package' thus cleverly confusing the whole issue...
    #This dict maps the package name =to=> directories
    #It says, package *needs* these files.
    package_data = {'modules' : files },
    #'runner' is in the root.
    scripts = ["fsearch"],
    long_description = """This app can be used to search for files in your linux system""", 
    license='GPLv2',
    platforms ='Linux'
    
    #
    #This next part it for the Cheese Shop, look a little down the page.
    #classifiers = []     
) 
