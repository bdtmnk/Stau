from scipy.optimize import curve_fit
import numpy as np
import sys
import xsecs
import xsecsNNLL
import time
import ROOT
from array import array
from ROOT import TFile, TTree, TCanvas, TGraph, TMultiGraph, TGraphErrors, TLegend
import CMS_lumi_combined as CMS_lumi, tdrstyle
import subprocess # to execute shell command
ROOT.gROOT.SetBatch(ROOT.kTRUE)
 
def smooth(x,a,b,c):
#  print(x.shape,np.log(x).shape)
  return np.exp(a+(b*x+c*np.log(x)))

# CMS style
CMS_lumi.cmsText = "CMS"
CMS_lumi.extraText = ""
CMS_lumi.cmsTextSize = 0.65
CMS_lumi.outOfFrame = True
tdrstyle.setTDRStyle()
 
 
# CREATE datacards

# EXECUTE datacards
def executeDataCards(files,labels):

    for file_name, label in zip(files,labels):
	print 'Executing datacard for datacards %s* and appending label %s' % (file_name,label)
	#combine_command_0 = 'rm datacard_%s.card' % (label)
        #p = subprocess.Popen(combine_command_0, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	#combine_command_1 = "combineCards.py %s* >> datacard_%s.card" % (file_name, label)
	combine_command_1 = "cp %s*  datacard_%s.card" % (file_name, label)

	print combine_command_1
        p = subprocess.Popen(combine_command_1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	(output, err) = p.communicate()  

	#This makes the wait possible
	p_status = p.wait()
        print ""
        print ">>> " + combine_command_1
        combine_command_2 = "combine -M AsymptoticLimits -m 120 -n %s datacard_%s.card" % (label,label)
        print ""
        print ">>> " + combine_command_2
        p = subprocess.Popen(combine_command_2, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print line.rstrip("\n")
        print ">>>   higgsCombine"+label+".Asymptotic.mH120.root created"
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
def plotUpperLimits(labels,values,outplot,handedness,mStau):
    # see CMS plot guidelines: https://ghm.web.cern.ch/ghm/plots/
 
    N = len(labels)
    yellow = TGraph(2*N)    # yellow band
    green = TGraph(2*N)     # green band
    median = TGraph(N)      # median line
    obs    = TGraph(N)      # obs
    #thr    = TGraph(N)      # obs

    up2s = [ ]
    masses_x, med_prefit, theory = [], [], []
    if(handedness=="degenerate") : selxsecs = xsecsNNLL.xsecs_degenerate
    elif(handedness=="left") : selxsecs = xsecsNNLL.xsecs_left
    else : selxsecs = xsecsNNLL.xsecs_right
    #sorted_keys=['50','100','150','200','250','300','350','400','450','500']
    
    sorted_keys=['50','100','120','140','160','180','200','220','240','260','280','300']

    print(selxsecs)
    masses,theory = np.array([float(key) for key in sorted_keys]),np.array([ selxsecs[key] for key in sorted_keys])
    print(masses)
    print(theory)
    print("FITTING THEORY XSEC")
#    popt, pcov = curve_fit(smooth, masses, theory, maxfev=2000)
    popt, pcov = curve_fit(smooth, masses, theory, (10,0,0),maxfev=10000)
    print(popt)

    thr     = TGraph(201-90)      # obs
    #thr2 = TGraph(201-90)
    thr0 = TGraph(2*(201-90))
    
    # output root file
    
    
    RootName = str(outplot) + ".root"
    
    f2 = TFile(RootName,"recreate")
    t = TTree( 't1', 'tree with histos' )
    #f3 = float(0.)
    
    #t.Branch('f3',f3,'f3[0]/F')
    p2sigma = array( 'f', [ 0. ] )
    p1sigma = array( 'f', [ 0. ] )
    m1sigma = array( 'f', [ 0. ] )
    m2sigma = array( 'f', [ 0. ] )    
    medianF = array( 'f', [ 0. ] )
    xsecF = array( 'f', [ 0. ] )
    obsF = array( 'f', [ 0. ] )
    massF = array( 'f', [ 0. ] )

    
    t.Branch( 'p2sigmaB', p2sigma, 'p2sigmaB/F' )
    t.Branch( 'p1sigmaB', p1sigma, 'p1sigmaB/F' )
    t.Branch( 'm1sigmaB', m1sigma, 'm1sigmaB/F' )
    t.Branch( 'm2sigmaB', m2sigma, 'm2sigmaB/F' )
    t.Branch( 'medianFB', medianF, 'medianFB/F' )
    t.Branch( 'xsecFB', xsecF, 'xsecFB/F' )
    t.Branch( 'obsFB', obsF, 'obsFB/F' )
    t.Branch( 'massFB', massF, 'massFB/F' )
    
    for iT,i in enumerate(range(90,226)):
      x=smooth(np.array([i]),*popt)
      thr.SetPoint(iT, i, x)
      #thr2.SetPoint(iT, i, x*1.05)
      thr0.SetPoint(iT, i, x*.95)
      thr0.SetPoint(2*(226-90)-1-iT, i, x*1.05)
      

    

    for i in range(N):
        xsec = smooth(np.array(float(labels[i].split('_')[0])),*popt)
        if (labels[i].split('_')[0] == "225") : xsec = smooth(np.array(200),*popt)
        file_name = "higgsCombine"+labels[i]+".AsymptoticLimits.mH120.root"
        limit = getLimits(file_name)
        up2s.append(limit[4]*xsec)
        yellow.SetPoint(    i,    values[i], limit[4]*xsec ) # + 2 sigma
        green.SetPoint(     i,    values[i], limit[3]*xsec ) # + 1 sigma
        median.SetPoint(    i,    values[i], limit[2]*xsec ) # median
        green.SetPoint(  2*N-1-i, values[i], limit[1]*xsec ) # - 1 sigma
        yellow.SetPoint( 2*N-1-i, values[i], limit[0]*xsec ) # - 2 sigma
        obs.SetPoint(    i,    values[i], limit[-1]*xsec ) # obs
        p2sigma[0] = limit[4]*xsec
        p1sigma[0] = limit[3]*xsec
        medianF[0] = limit[2]*xsec 
        m1sigma[0] = limit[1]*xsec 
        m2sigma[0] = limit[0]*xsec     
        xsecF[0] = xsec
        obsF[0] = limit[-1]*xsec
        massF[0] = values[i]
        print medianF[0]
        print xsecF[0]        
        t.Fill()
        
        




    f2.Write()
    f2.Close()
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
    frame.GetYaxis().SetTitle("95% CL upper limit on #sigma [fb]")
#    frame.GetYaxis().SetTitle("95% upper limit on #sigma #times BR / (#sigma #times BR)_{SM}")
    frame.GetXaxis().SetTitle("m(#tilde{#tau}) [GeV]")
    frame.SetMinimum(7.5)
    frame.SetMaximum(1100)
    frame.GetXaxis().SetLimits(min(values),max(values))
    #frame.GetYaxis().SetMaximum(1000)
    #yellow.SetMaximum(2000)
 
 
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


    thr0.SetFillColorAlpha(ROOT.kRed+2,0.5)
    thr0.SetLineWidth(0)
    thr0.SetLineColor(ROOT.kRed+2)
    thr0.SetFillStyle(1001)
    thr0.Draw('Fsame')

    thr.SetLineWidth(2)
    thr.SetLineColor(ROOT.kRed)
    thr.Draw('Lsame')

    
    #thr2.SetLineWidth(2)
    #thr2.SetLineColor(ROOT.kPink)
    #thr2.SetLineStyle(8)
    #thr2.Draw('Lsame')
    
    
    CMS_lumi.CMS_lumi(c,13,11)
    ROOT.gPad.SetTicks(1,1)
    frame.Draw('sameaxis')

    x1 = 0.55
    x2 = x1 + 0.24
    y1 = 0.6
    y2 = y1+.26

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
    legend.AddEntry(thr0, "#sigma_{NLO+NLL} uncertainty",'f')#Asymptotic CL_{s} #pm 2 std. deviation",'f')

    legend.Draw()
#    c.SetLogy() 
    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextAngle(0)
    latex.SetTextColor(ROOT.kBlack)
    if(handedness=="left") : latex.DrawLatex(0.15, 0.19, "pp #rightarrow #tilde{#tau}_{L} #tilde{#tau}_{L}, #tilde{#tau}_{L} #rightarrow  #tau #tilde{#chi}_{1}^{0}, m(#tilde{#chi}_{1}^{0}) = "+mStau+" GeV")#extraText)
    if(handedness=="degenerate") : latex.DrawLatex(0.15, 0.19, "pp #rightarrow #tilde{#tau}_{L,R} #tilde{#tau}_{L,R}, #tilde{#tau}_{L,R} #rightarrow  #tau #tilde{#chi}_{1}^{0}, m(#tilde{#chi}_{1}^{0}) = "+mStau+" GeV")#extraText)
    if(handedness=="right") : latex.DrawLatex(0.15, 0.19, "pp #rightarrow #tilde{#tau}_{R} #tilde{#tau}_{R}, #tilde{#tau}_{R} #rightarrow  #tau #tilde{#chi}_{1}^{0}, m(#tilde{#chi}_{1}^{0}) = "+mStau+" GeV")#extraText)
 
 
    latex.SetTextSize(0.0405)
    if(handedness=="degenerate") : latex.DrawLatex(0.15, 0.24, "Degenerate scenario")
    if(handedness=="left") : latex.DrawLatex(0.15, 0.24, "Left-handed scenario")
    if(handedness=="right") : latex.DrawLatex(0.15, 0.24, "Right-handed scenario")

   
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
 
    assert(len(sys.argv) == 4)
    mLSP 	= sys.argv[3]
    srs 	= ['HighSumMT_NJEQ0', 'HighSumMT_NJGEQ1', 'MediumSumMT_NJEQ0', 'MediumSumMT_NJGEQ1', 'LowSumMT_NJEQ0', 'LowSumMT_NJGEQ1']
    stauMasses  = [90, 100,125,150,175,200]
    if(mLSP=="20") :  stauMasses  = [100,125,150,175,200]

    #stauMasses  = [200,225]


    prefix   = ['/nfs/dust/cms/user/bobovnii/MVAstau/CMSSW_8_1_0/src/Limits/STau/%s/Stau_%s_LSP%s_' % (sys.argv[1], mStau, mLSP) for mStau in stauMasses]

    labels          = [str(mStau) +'_'+mLSP+'_'+sys.argv[2] for mStau in stauMasses]

    name	= 'Limit' + '_'+mLSP+'_'+sys.argv[2]
    #executeDataCards(prefix,labels)
    assert( sys.argv[2]=="degenerate" or sys.argv[2]=="left" or sys.argv[2]=="right")
    plotUpperLimits(labels,stauMasses, name, sys.argv[2],mLSP)
 
if __name__ == '__main__':
    main()
 
