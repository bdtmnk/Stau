import os
import numpy as np
from glob import glob
import uproot


PROCESSES = [
#	"TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8",
#	"TTToHadronic_TuneCP5_13TeV-powheg-pythia8",
#	"TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8",
#	"VVTo2L2Nu_13TeV_amcatnloFXFX_madspin_pythia8",
#	"W1JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
#	"W2JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
#	"W3JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
#	"W4JetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
#	"WGToLNuG_TuneCP5_13TeV-madgraphMLM-pythia8",
#	"WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8",
#	"WW_TuneCP5_13TeV-pythia8",
#	"WZ_TuneCP5_13TeV-pythia8",
#	"ZZ_TuneCP5_13TeV-pythia8"
	"DY1JetsToLL_M-50",
	"DY2JetsToLL_M-50",
	"DY3JetsToLL_M-50",
	"DY4JetsToLL_M-50",
	"DYJetsToLL_M-10to50",
	"DYJetsToLL_M-50",
#	"WToMuNu_M-200_TuneCP5_13TeV-pythia8",
#	"WWTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8",
#	"WWToLNuQQ_NNPDF31_TuneCP5_13TeV-powheg-pythia8",
#	"WW_TuneCP5_13TeV-pythia8",
#	"WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8",
#	"WZ_TuneCP5_13TeV-pythia8",
#	"WminusHToTauTau_M125_13TeV_powheg_pythia8",
#	"WplusHToTauTau_M125_13TeV_powheg_pythia8",
#	"ZZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8",
#	"ZZTo4L_TuneCP5_13TeV_powheg_pythia8",
#	"ZZ_TuneCP5_13TeV-pythia8",
#	"WZ_TuneCP5_13TeV-pythia8",
#	"WW_TuneCP5_13TeV-pythia8"	
]

for proc in PROCESSES:
	_files = glob(proc+"*.root") 
	sizes = []
	for _file in _files:
		sizes.append(os.stat(_file).st_size)
		try:
			root_file = uproot.open(_file)['mutau']
		except Exception: os.remove(_file)
		try:
			if len(root_file.keys())==0:os.remove(_file)
		except Exception: pass
	for ind_file in range(len(_files)):
		size = sizes[ind_file]
		if size < np.mean(sizes):
			try:os.remove(_file)		
			except Exception:pass
		
