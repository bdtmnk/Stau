from glob import glob
import sys,os
from array import array
import ROOT as r
import plottery_utils as u
import plottery as ply
import numpy as np

colorvv  =r.TColor.GetColor("#8646ba");
colortt  =r.TColor.GetColor("#9999cc");
colorttx =r.TColor.GetColor("#33CCFF");
colorwjet=r.TColor.GetColor("#de5a6a");
colordyj =r.TColor.GetColor("#ffcc66");
colorztt =r.TColor.GetColor("#58d885");
colorst  =r.TColor.GetColor("#b6d0ea");
colorww  =r.TColor.GetColor("#C390D4");
colorfakes=r.TColor.GetColor("#ffccff");

for file in glob("*.root"):
#file ="Var_BDTmutau_Stau100_16_35invfb_mt_SR.root"
	f1   =r.TFile(file)
	tag=file.split('_35')[0].split('Var_')[1]+";1"
	print(tag)
	data_obs=f1.Get("data_obs_"+tag)
	tt=f1.Get("tt_"+tag)
	wj=f1.Get("wj_"+tag)
	dyj=f1.Get("dyj_"+tag)
	ztt=f1.Get("ztt_"+tag)
	dib=f1.Get("dib_"+tag)
	sT=f1.Get("sT_"+tag)
	ww=f1.Get("ww_"+tag)
	ttx             =f1.Get("ttx_"+tag)
	fakes=f1.Get("fakes_"+tag)
	rest=f1.Get("rest_"+tag)

	allBkg =f1.Get("allbkg_"+tag)

	hS1=f1.Get("Stau100_LSP1_left_B_"+tag)
	#hS2=f1.Get("Stau150_LSP1_left_B_"+tag)
	hS2=f1.Get("Stau125_LSP1_left_B_"+tag)
	hS3=f1.Get("Stau200_LSP1_left_B_"+tag)
	print(data_obs.Integral(),tt.Integral(),wj.Integral(),dyj.Integral(),ztt.Integral(),dib.Integral(),sT.Integral(),ww.Integral(),ttx.Integral())



	rest.Add(dib)
	rest.Add(wj)
	rest.Add(ww)

	print rest.GetBinContent(26)


	tt.Add(sT)
	tt.Add(ttx)


	dyj.Add(ztt)



	colorFakes = r.TColor.GetColor("#33ccff")
	colorOther = r.TColor.GetColor("#c390d4")
	colorTop = r.TColor.GetColor("#de5a6a")
	colorDY = r.TColor.GetColor("#ffcc66")
	colors = [colorDY, colorFakes, colorTop, colorOther][::-1]
	bgs = [dyj,fakes,tt,rest][::-1]
	leg_labels = ["DY+jets","Jet#rightarrow #tau_{h}", "Top quark", "Other SM"][::-1]


	#nB= 27;
	#binsBDT=array("d",[0.0, 0.4,0.41,0.42,0.43,0.44,0.45,0.46,0.47,0.48,0.49,0.5,0.51,0.52,0.53,0.54,0.55,0.56,0.57,0.58,0.59,0.6,0.61,0.62,0.63,0.64,0.655,1.0])
	binsBDT=array("d", dyj.GetXaxis().GetXbins())
	xaxis = 'BDT(100) Discriminant'
	yaxis = 'Events / Bin'
	x = 0
	y = data_obs.GetNbinsX()

	if('el' in tag) : obj='e'
	else : obj='#mu'
	if('METFB' in tag) : 
	  binsBDT=array("d",np.linspace(0,250,25))
	  xaxis = 'p_{T}^{miss} [GeV]'
	  yaxis = 'Events / 10 GeV'
	  y=30
        elif('hInv' in tag) : 
	  binsBDT=array("d",np.linspace(50,400,35))
	  #xaxis = 'Visible Mass [GeV]'
          xaxis = 'm(%s#tau_{h}) [GeV]' % obj
          yaxis = 'Events / 10 GeV'
	  x=5
	  y=35
	elif('MTtot' in tag) :
	  binsBDT=array("d",np.linspace(50,400,35))
	  xaxis = 'm_{T}^{tot} [GeV]'
	  yaxis = 'Events / 10 GeV'
	  x=5
	  y=35
	if('16' in file): lumi='2016, 35.9'
	elif ('17' in file) : lumi='2017, 41.3'
	else : lumi=77.2
	if(file == 'Var_METFB_16_35invfb_mt_SR.root' or file == 'Var_hInvMassMuTau_16_35invfb_mt_SR.root' or file == 'Var_MTtot_16_35invfb_mt_SR.root') : lumi='77.2' 
	if('2017' in file) : lumi='2017, 41.3'
	#print(len(binsBDT))
	print(binsBDT)
        nB = len(binsBDT)-1;
	b1 = r.TH1D("","",nB,binsBDT);
	b2 = r.TH1D("","",nB,binsBDT);
	b3 = r.TH1D("","",nB,binsBDT);
	b4 = r.TH1D("","",nB,binsBDT);
	b5 = r.TH1D("","",nB,binsBDT);
	b6 = r.TH1D("","",nB,binsBDT);
	b7 = r.TH1D("","",nB,binsBDT);
	b8 = r.TH1D("","",nB,binsBDT);
	b9 = r.TH1D("","",nB,binsBDT);

	for bin_ in range(1,y+1):#+data_obs.GetNbinsX()+1):
	  b1.SetBinContent(bin_, dyj.GetBinContent(bin_+x))
	  b2.SetBinContent(bin_, fakes.GetBinContent(bin_+x))
	  b3.SetBinContent(bin_, tt.GetBinContent(bin_+x))
	  b4.SetBinContent(bin_, rest.GetBinContent(bin_+x))
	  b5.SetBinContent(bin_, np.sqrt(allBkg.GetBinError(bin_+x)*allBkg.GetBinError(bin_+x)+allBkg.GetBinContent(bin_+x)*.15*allBkg.GetBinContent(bin_+x)*.15))
	  b6.SetBinContent(bin_, data_obs.GetBinContent(bin_+x))
	  b7.SetBinContent(bin_, hS1.GetBinContent(bin_+x))
	  b8.SetBinContent(bin_, hS2.GetBinContent(bin_+x))
	  b9.SetBinContent(bin_, hS3.GetBinContent(bin_+x))
	  b7.SetBinError(bin_, hS1.GetBinError(bin_+x))
	  b8.SetBinError(bin_, hS2.GetBinError(bin_+x))
	  b9.SetBinError(bin_, hS3.GetBinError(bin_+x))
        y-=1
        for bin_ in range(y+1,+data_obs.GetNbinsX()+1):
	  print(bin_, b2.GetBinContent(y)+fakes.GetBinContent(bin_+x))
          b1.SetBinContent(y, b1.GetBinContent(y)+dyj.GetBinContent(bin_+x))
          b2.SetBinContent(y, b2.GetBinContent(y)+fakes.GetBinContent(bin_+x))
          b3.SetBinContent(y, b3.GetBinContent(y)+tt.GetBinContent(bin_+x))
          b4.SetBinContent(y, b4.GetBinContent(y)+rest.GetBinContent(bin_+x))
          b5.SetBinContent(y, np.sqrt(b5.GetBinContent(y) * b5.GetBinContent(y) + allBkg.GetBinError(bin_+x)*allBkg.GetBinError(bin_+x)+allBkg.GetBinContent(bin_+x)*.15*allBkg.GetBinContent(bin_+x)*.15))
          b6.SetBinContent(y, b6.GetBinContent(y)+data_obs.GetBinContent(bin_+x))
          b7.SetBinContent(y, b7.GetBinContent(y)+hS1.GetBinContent(bin_+x))
          b8.SetBinContent(y, b8.GetBinContent(y)+hS2.GetBinContent(bin_+x))
          b9.SetBinContent(y, b9.GetBinContent(y)+hS3.GetBinContent(bin_+x))
          b7.SetBinError(y, np.sqrt(b7.GetBinError(y) * b7.GetBinError(y) + hS1.GetBinError(bin_+x)*hS1.GetBinError(bin_+x)))
          b8.SetBinError(y, hS2.GetBinError(bin_+x))
          b9.SetBinError(y, hS3.GetBinError(bin_+x))


	ply.plot_hist(
	bgs=[b1,b2,b3,b4][::-1],
	syst = b5,
	data = b6,
#	sigs = [b7,b8,b9],
#	sig_labels = ['#tilde{#tau}_{L}(100), #tilde{#chi}_{1}^{0}(1)','#tilde{#tau}_{L}(150), #tilde{#chi}_{1}^{0}(1)','#tilde{#tau}_{L}(200), #tilde{#chi}_{1}^{0}(1)'],
	colors = colors,
	legend_labels = leg_labels,
	options = {
                       "legend_coordinates" : [.65,.65,.95,.93],
                    "show_bkg_errors" :False,
                    "legend_scalex": 1.,
                    "legend_scaley": 1,

                        "extra_text" : [obj+"#tau_{h}"],
                        "extra_text_size" : .075,
                        "extra_text_xpos" : .8 ,
                        "extra_text_ypos" : .525,
	    "show_bkg_errors" :False,
	    "yaxis_range" : [.5,20000],
	    "ratio_range":[.4,2.5],
	    "hist_disable_xerrors": True,
	    "output_name": "plots2/"+file.replace(".root",""),
	    "legend_percentageinbox": False,
	    "cms_label": "Preliminary",
	    "lumi_value": lumi,
	    "output_ic": True,
	    "us_flag": False,
	    "xaxis_label" : xaxis, #'BDT (100) Discriminate',
	    "yaxis_label" : yaxis, #'Events / Bin',
	    "hist_disable_xerrors": False,
	    "bkg_sort_method" : "unsorted",
            "yaxis_log" : True,
	    "yaxis_moreloglabels" : False,
            "hist_line_black" : True,
            "bkg_err_fill_color" : r.kBlue,
            "bkg_err_fill_style" : 1001,
            "canvas_ratio_bottommargin" : 0.05,
            "ratio_name" : "Obs. / Pred.",
            "legend_opacity" : 1
	    }
	)

