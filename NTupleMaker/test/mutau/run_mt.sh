#!/bin/bash

./condorsub_seq_leptau.sh SynchNTupleProducer_2017 analysisMacroSynch_lept_mt_DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8.conf DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8 mt 20

./condorsub_seq_leptau.sh SynchNTupleProducer_2017 analysisMacroSynch_lept_mt_GluGluHToTauTau_M125_13TeV_powheg_pythia8.conf GluGluHToTauTau_M125_13TeV_powheg_pythia8 mt 20

./condorsub_seq_leptau.sh SynchNTupleProducer_2017 analysisMacroSynch_lept_mt_SUSYGluGluToHToTauTau_M-120_TuneCP5_13TeV-pythia8.conf SUSYGluGluToHToTauTau_M-120_TuneCP5_13TeV-pythia8 mt 20



#./condorsub_seq_leptau.sh SynchNTupleProducer_2017 analysisMacroSynch_lept_mt_DATA_SingleMuon.conf DATA_MuB mt 20