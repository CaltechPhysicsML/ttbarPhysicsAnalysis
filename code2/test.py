import ROOT as rt

f = rt.TFile.Open("wjethists")
h = f.Get("numJets")
c = rt.TCanvas("c","c",800,600)
h.Draw()
c.Print("test.pdf")
