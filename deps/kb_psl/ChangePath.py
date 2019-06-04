import sys

#Set /usr/local/lib to be ahead of /usr/lib in path
#otherwise the wrong version fo six is used
sys.path.insert(1,'/usr/local/lib/python2.7/dist-packages')
