using namespace std;
void basic(){
///////////////// Text files follow this convention (output from nll-fast 
//# ms[GeV]  LO[pb]     NLO[pb]    NLL+NLO[pb]  d_mu+ [pb] d_mu-[pb]   d_pdf+[%]  d_pdf-[%]  d_as+[%] d_as-[%]  K_NLO   K_NLL
///////////////////////////////////////////

  vector <string> cut1;
  vector <float> cut2;
  vector <float> cut3;
  vector <float> cut4;
  vector <float> cut5;
  vector <float> cut6;
  vector <float> cut7;
  vector <float> cut8;
  vector <float> cut9;
  vector <float> cut10;
  vector <float> cut11;
  vector <float> cut12;
  vector <float> cut13;
  vector <float> cut14;
  vector <float> cut15;
  vector <float> cut16;
  vector <float> cut17;
  vector <float> cut18;
  vector <float> cut19;
  vector <float> cut20;
  

   Int_t nlines = 0;

Float_t c2,c3;
string c1;
char ch;
ch="&";
   ifstream in,mstw;
   in.open("cutflow_SingleMuon_InvMuIso.root.txt");
/*
   ifstream data,mstw;
   data.open("cutflow_SingleMuon_InvMuIso.root.txt");
   while (1) {
   getline(data,c1, '&');
      data >> c1 >>c2 ;

	cut1.push_back(c1);
	cut2.push_back(c2);

      if (!data.good()) break;

}
*/
while(true) {
    std::string line;
    std::getline( in, line );
    if( !in ) break;
    std::istringstream iline( line );
    while(true) {
        std::string str;
        std::getline( iline, str, '&' );
      in >> c1 >>c2 ;
	cout<<in<<endl;
	cut1.push_back(c1);
	cut2.push_back(c2);
        if( !iline ) break;
        // you get string by string in str here
    }
}




for (int i =0;i<cut1.size();i++)

{


cout<<cut1[i]<<"  "<<cut2[i]<<"  "<<endl;

}
}
