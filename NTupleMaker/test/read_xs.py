import sys


with open('xx') as inf:
    for line in inf:
        parts = line.split() # split line into parts
        if len(parts) > 1:   # if at least 2 parts/columns
		
		sp = int(parts[0])
 		for lsp in range(0,sp-25,50):
			if lsp == 0:
				lsp = 1
			print ' C1C1_'+parts[0]+'_LSP'+str(lsp), '\t',float(parts[1])*0.001
		#print 'C1N2_'+parts[0]   # print column 2
