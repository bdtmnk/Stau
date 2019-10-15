combine -M MaxLikelihoodFit --rMin -2 --rMax 2 $1  -v2 -t $2 --expectSignal $3
#1 combine -M MaxLikelihoodFit --rMin -2 --rMax 2 $1 --cminFallbackAlgo "Minuit2,Minimize,0:0.05" --cminOldRobustMinimize 0 -v2 -t $2 --expectSignal $3

