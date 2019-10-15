#combine -M MaxLikelihoodFit --plots --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL --rMin=-4 --rMax=4 -m 125  $1  -t -1 --expectSignal=1 -v3
#combine -M MaxLikelihoodFit --plots --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL --rMin=-4 --rMax=4 -m 125  $1  -t -1 --expectSignal=1 -v3 --numToysForShapes 1000 
combine -M MaxLikelihoodFit --plots --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL --robustFit=1 $1  -v2  --rMin=-4 --rMax=4
