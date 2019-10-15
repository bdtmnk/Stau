void Value(float base, 
	   float mean,
	   float err) {

  float x = TMath::Power(base,mean);
  float xu = TMath::Power(base,mean+err);
  float xd = TMath::Power(base,mean-err);

  float u = xu - x;
  float d = x - xd;

  std::cout << " tauId = " << x << " + " << u << " - " << d << std::endl;

}
