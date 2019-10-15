
#/store/user/ocolegro/TauTrees_131018_2016samples_oldfwk/
FullSignals2016 = '/eos/uscms/store/user/ocolegro/TauTrees_231018_2016samples_v3_FullSignal/merged/'
#MC2016 		= '/eos/uscms/store/user/ocolegro/TauTrees_151018_2016samples/merged/'
#/eos/uscms/store/user/ocolegro/TauTrees_151018_2016samples_2/merged/'#'/eos/uscms/store/user/ocolegro/TauTrees_151018_2016samples_2/merged/'###'/eos/uscms/store/user/ocolegro/TauTrees_131018_2016samples_nojosn/merged/'
#Data2016        = '/eos/uscms/store/user/ocolegro/TauTrees_151018_2016samples/merged/'
#/eos/uscms/store/user/ocolegro/TauTrees_151018_2016samples_2/merged/'#'/eos/uscms/store/user/ocolegro/TauTrees_151018_2016samples_2/merged/'##'/eos/uscms/store/user/ocolegro/TauTrees_131018_2016samples_nojosn/merged/'
#/eos/uscms/store/user/ocolegro/TauTrees_131018_2016samples_oldfwk/merged/'
#3###From latest presentation!!! in october
#FullSignals2017 = '/eos/uscms/store/user/ocolegro/TauTrees_111018_2017samples_deepcsv_2_nojson_2_STUDY_3_FILLALL_SIGNALS/merged/'
#MC2017 		= '/eos/uscms/store/user/ocolegro/TauTrees_241018_2017samples_v3/merged/'#/eos/uscms/store/user/ocolegro/TauTrees_111018_2017samples_deepcsv_2_nojson_2_STUDY_3_SIGNALS_NewSysts/merged/'
#Data2017 	= '/eos/uscms/store/user/ocolegro/TauTrees_241018_2017samples_v3/merged/'#/eos/uscms/store/user/ocolegro/TauTrees_111018_2017samples_deepcsv_2_nojson_2_STUDY_3/merged/' 
MC2016='/eos/uscms//store/user/ocolegro/TauTrees0591218_2016samples_v5/merged/'
Data2016='/eos/uscms//store/user/ocolegro/TauTrees0591218_2016samples_v5/merged/'
MC2016='/eos/uscms/store/user/ocolegro/Tau1491218_2016samples_v4/merged/'
Data2016='/eos/uscms/store/user/ocolegro/Tau1491218_2016samples_v4/merged/'
FullSignals2017 = '/eos/uscms/store/user/ocolegro/TauTrees_111018_2017samples_deepcsv_2_nojson_2_STUDY_3_FILLALL_SIGNALS/merged/'
MC2017          = '/eos/uscms/store/user/ocolegro/TauTrees_271018_2017samples_v3/merged/'
Data2017        = '/eos/uscms/store/user/ocolegro/TauTrees_271018_2017samples_v3/merged/'
#
MC2016		= '/eos/uscms/store/user/ocolegro/Tau1491218_2016samples_v4/merged/'
Data2016          = '/eos/uscms/store/user/ocolegro/Tau1491218_2016samples_v4/merged/'

MC2017          = '/eos/uscms/store/user/ocolegro/TauTrees_271018_2017samples_v3/merged/'
Data2017	= '/eos/uscms/store/user/ocolegro/TauTrees_271018_2017samples/merged/'

MC2017='/eos/uscms//store/user/ocolegro/TauTrees0591218_2017samples_v4/merged/'
Data2017='/eos/uscms//store/user/ocolegro/TauTrees0591218_2017samples_v4/merged/'
FullSignals2017='/eos/uscms//store/user/ocolegro/TauTrees0591218_2017samples_v4/merged/'

MC2017='/eos/uscms/store/user/ocolegro/Tau07012019_2017samples_v4/merged/'
Data2017='/eos/uscms/store/user/ocolegro/Tau07012019_2017samples_v4/merged/'
FullSignals2017='/eos/uscms/store/user/ocolegro/TauTrees_111018_2017samples_deepcsv_2_nojson_2_STUDY_3_FILLALL_SIGNALS/merged/'

MC2016='/eos/uscms/store/user/ocolegro/Tau07012019_2016samples_v4/merged/'
#MC2016='/eos/uscms/store/user/ocolegro/testing55/merged/'
Data2016='/eos/uscms/store/user/ocolegro/Tau07012019_2016samples_v4/merged/'
FullSignals2016 = '/eos/uscms/store/user/ocolegro/TauTrees_231018_2016samples_v3_FullSignal/merged/'
#FullSignals2016='/eos/uscms//store/user/ocolegro/Tau07012019_2016samples_v4/merged/'

offlineMetCut = 200#00000

xsecs = {
'90': 477.249
,'100': 270.819
,'125': 131.64
,'150': 63.2353
,'175': 37.269
,'200': 22.0346
}
xsecsRH = {
'90': 160
,'100': 96.5
,'125': 43.0
,'150': 23.32
,'175': 12.5
,'200': 8.15
}

def makeSystString(mc_cut,syst='TES',var='DWN'):
  syst_variation = syst+var
  mc_cut_var = mc_cut.replace('pfMET','pfMET_'+syst_variation)
  mc_cut_var = mc_cut_var.replace('MT2_lester','MT2_lester_'+syst_variation)
  mc_cut_var = mc_cut_var.replace('tauMTMet_1','tauMTMet_'+syst_variation+'_1')
  mc_cut_var = mc_cut_var.replace('tauMTMet_2','tauMTMet_'+syst_variation+'_2')
  if(syst == 'TES') :  mc_cut_var = mc_cut_var.replace('tauRecoPt_1','tauRecoPt_'+syst_variation+'_1')
  if(syst == 'TES') :  mc_cut_var = mc_cut_var.replace('tauRecoPt_2','tauRecoPt_'+syst_variation+'_2')
  if(syst == 'TES') : mc_cut_var = mc_cut_var.replace('nLooseTaus','nLooseTaus_'+syst_variation)
  if('JE' in syst) :  mc_cut_var = mc_cut_var.replace('NJets','NJets_'+syst_variation)
  if('JE' in syst) :  mc_cut_var = mc_cut_var.replace('NBJetsCSV','NBJets_'+syst_variation)
    
  return mc_cut_var
