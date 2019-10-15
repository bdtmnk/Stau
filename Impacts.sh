rm $1/workspace.root
#!/bin/sh
# $1 = mass
# creating workspace
combineTool.py -M T2W -i $1/$2 -o workspace.root
# computing impacts 
combineTool.py -M Impacts -m 300 --allPars --doInitialFit --robustFit 1 -t -1 --rMin -5 --rMax 5 --expectSignal=0 -d $1/workspace.root
#combineTool.py -M Impacts -m 300 --allPars --robustFit 1 --doFits -t -1 --rMin -5 --rMax 5 --expectSignal=1 -d $1/workspace.root
combineTool.py -M Impacts -m 300 --allPars --robustFit 1 --doFits  --rMin -5 --rMax 5 --expectSignal=1 -d $1/workspace.root
combineTool.py -M Impacts -m 300 --allPars -o impacts.json -d $1/workspace.root
# plotting impacts
plotImpacts.py -i impacts.json -o impacts
