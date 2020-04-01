# coding: utf-8
#import pandas as pd
import uproot
#root_file = uproot.open("file = uproot.recreate("tmp.root", compression=uproot.ZLIB(4))
rootf_file = uproot.open("DYJetsToLL_M-50_13TeV-12Apr2018_TEST.root")
with uproot.recreate("example.root") as f:
    f['varvar'] = uproot.newtree({"branch": "float32"})
    f['varvar'].extend({"branch":rootf_file['mutau/T']['met_ex']**2})
    
get_ipython().magic(u'save current_session ~0/')
