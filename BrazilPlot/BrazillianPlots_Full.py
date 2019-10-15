import sys
import xsecs
import time
import ROOT
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend
import CMS_lumi_combined as CMS_lumi, tdrstyle
import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
 
# CMS style
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = "Preliminary"
CMS_lumi.cmsTextSize = 0.65
CMS_lumi.outOfFrame = True
tdrstyle.setTDRStyle()
 
 
# CREATE datacards

# EXECUTE datacards
def executeDataCards(files,labels):

    for file_name, label in zip(files,labels):
	print 'Executing datacard for datacards %s* and appending label %s' % (file_name,label)
##	combine_command_0 = 'rm datacard_%s.card' % (label)
 #       p = subprocess.Popen(combine_command_0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	combine_command_1 = "combineCards.py %s* >> datacard_%s.card" % (file_name, label)
	print combine_command_1
        p = subprocess.Popen(combine_command_1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	(output, err) = p.communicate()  

	#This makes the wait possible
	p_status = p.wait()
        print ""
        print ">>> " + combine_command_1
        combine_command_2 = "combine -M AsymptoticLimits -m 125 -n %s datacard_%s.card" % (label,label)
        print ""
        print ">>> " + combine_command_2
        p = subprocess.Popen(combine_command_2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line.rstrip("\n")
        print ">>>   higgsCombine"+label+".Asymptotic.mH125.root created"
        retval = p.wait()
        combine_command_0 = 'rm datacard_%s.card' % (label)
        p = subprocess.Popen(combine_command_0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

 
# GET limits from root file
def getLimits(file_name):
 
    file = TFile(file_name)
    tree = file.Get("limit")
 
    limits = [ ]
    for quantile in tree:
        limits.append(tree.limit)
        print ">>>   %.2f" % limits[-1]
 
    return limits[:6]
 
 
# PLOT upper limits
def plotUpperLimits(labels,values,outplot):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
 
    N = len(labels)
    yellow = TGraph(2*N)    # yellow band
    green = TGraph(2*N)     # green band
    median = TGraph(N)      # median line
    obs    = TGraph(N)      # obs
    thr    = TGraph(N)      # obs

    up2s = [ ]

    for i in range(N):
        xsec = xsecs.xsecs[labels[i].split('_')[0]]
        file_name = "higgsCombine"+labels[i]+".AsymptoticLimits.mH125.root"
	print(file_name)
        limit = getLimits(file_name)
	print limit[4]*xsec
        up2s.append(limit[4]*xsec)
        yellow.SetPoint(    i,    values[i], limit[4]*xsec ) # + 2 sigma
        green.SetPoint(     i,    values[i], limit[3]*xsec ) # + 1 sigma
        median.SetPoint(    i,    values[i], limit[2]*xsec ) # median
        green.SetPoint(  2*N-1-i, values[i], limit[1]*xsec ) # - 1 sigma
        yellow.SetPoint( 2*N-1-i, values[i], limit[0]*xsec ) # - 2 sigma
        obs.SetPoint(    i,    values[i], limit[-1]*xsec ) # obs
        thr.SetPoint(    i,    values[i], xsec ) # obs

    W = 800
    H  = 600
    T = 0.08*H
    B = 0.12*H
    L = 0.12*W
    R = 0.04*W
    c = TCanvas("c","c",100,100,W,H)
    c.SetFillColor(0)
    c.SetBorderMode(0)
    c.SetFrameFillStyle(0)
    c.SetFrameBorderMode(0)
    c.SetLeftMargin( L/W )
    c.SetRightMargin( R/W )
    c.SetTopMargin( T/H )
    c.SetBottomMargin( B/H )
    c.SetTickx(0)
    c.SetTicky(0)
    c.SetGrid()
    c.SetLogy()
    c.cd()
    frame = c.DrawFrame(1.4,0.001, 4.1, 10)
    frame.GetYaxis().CenterTitle()
    frame.GetYaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetTitleSize(0.05)
    frame.GetXaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetLabelSize(0.04)
    frame.GetYaxis().SetTitleOffset(0.9)
    frame.GetXaxis().SetNdivisions(508)
    frame.GetYaxis().CenterTitle(True)
    frame.GetYaxis().SetTitle("95% upper limit on #sigma[fb]")
#    frame.GetYaxis().SetTitle("95% upper limit on #sigma #times BR / (#sigma #times BR)_{SM}")
    frame.GetXaxis().SetTitle("M_{#tilde{#tau}} [GeV]")
    frame.SetMinimum(9)
    frame.SetMaximum(max(up2s)*1.05)
    frame.GetXaxis().SetLimits(min(values),max(values))
 
    yellow.SetFillColor(ROOT.kOrange)
    yellow.SetLineColor(ROOT.kOrange)
    yellow.SetFillStyle(1001)
    yellow.Draw('F')
 
    green.SetFillColor(ROOT.kGreen+1)
    green.SetLineColor(ROOT.kGreen+1)
    green.SetFillStyle(1001)
    green.Draw('Fsame')
 
    median.SetLineColor(1)
    median.SetLineWidth(3)
    median.SetLineStyle(2)
    median.Draw('Lsame')

    obs.SetLineWidth(4)
    obs.Draw('Lsame')

    thr.SetLineWidth(4)
    thr.SetLineColor(ROOT.kRed)
    thr.Draw('Lsame')

    CMS_lumi.CMS_lumi(c,13,11)
    ROOT.gPad.SetTicks(1,1)
    frame.Draw('sameaxis')

    x1 = 0.55
    x2 = x1 + 0.24
    y1 = 0.7
    y2 = y1+.16

    legend = TLegend(x1,y1,x2,y2)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    legend.SetTextSize(0.041)
    legend.SetTextFont(42)
    legend.AddEntry(median, "Asymptotic CL_{s} expected",'L')
    legend.AddEntry(green, "#pm 1 std. deviation",'f')
#    legend.AddEntry(green, "Asymptotic CL_{s} #pm 1 std. deviation",'f')
    legend.AddEntry(yellow,"#pm 2 std. deviation",'f')
    legend.AddEntry(obs, "Observed",'L')#Asymptotic CL_{s} #pm 2 std. deviation",'f')
    legend.AddEntry(thr, "#sigma_{NLO+NLL}",'L')#Asymptotic CL_{s} #pm 2 std. deviation",'f')
    legend.Draw()
#    c.SetLogy() 
    print " "
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)
    latex.DrawLatex(0.15, 0.2, "pp #rightarrow #tilde{#tau} #tilde{#tau}, #tilde{#tau} #rightarrow  #tau #tilde{#chi}_{1}^{0}, m(#tilde{#chi}_{1}^{0}) = 0 GeV")#extraText)
    latex.SetTextSize(0.0275)
    latex.DrawLatex(0.15, 0.15, "Degenerate scenario")
    c.SaveAs(outplot+".pdf")#"UpperLimit.png")
    c.SaveAs(outplot+".png")
    c.Close()
 
 
# RANGE of floats
def frange(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step
 
 
# MAIN
def main():
 
    mLSP 	= '10'
    srs 	= ['HighSumMT_NJEQ0', 'HighSumMT_NJGEQ1', 'MediumSumMT_NJEQ0', 'MediumSumMT_NJGEQ1', 'LowSumMT_NJEQ0', 'LowSumMT_NJGEQ1']
    stauMasses  = [100,125,150,175,200]



    prefix   = ['%s/signalcards2016/mStau_%s_mLSP_%s_' % (sys.argv[1], mStau, mLSP) for mStau in stauMasses]

    labels          = [str(mStau) +'_'+mLSP for mStau in stauMasses]

    executeDataCards(prefix,labels)
    if (len(sys.argv) == 1): plotUpperLimits(labels,stauMasses,'default')
    else : plotUpperLimits(labels,stauMasses,sys.argv[1])
 
 
if __name__ == '__main__':
    main()
 
