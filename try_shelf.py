import shelve
from collector import sub_dict
s= shelve.open('dbnew',writeback = True)
sub_dict(s,['hi','cindy'],value = [])
print s
s.close()