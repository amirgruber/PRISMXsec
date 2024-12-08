## imports
from bisect import bisect as bisect
import numpy as np
from csv import reader
import numpy.random as rnd
import ROOT
import os
import sys
import time

toy = sys.argv[1]

files = ["/eos/home-a/amgruber/SWAN_projects/XSec_ROOT/TTreeMerges/proj"+str(i+1)+"_merged.root" for i in range(58)]

centers = []

pwd = '/eos/user/a/amgruber/SWAN_projects/FluxTest/NewToys/'
with open(pwd+'BinCenters.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        centers.append(1000*np.array(row).astype(float)[1:])
centers = centers[1:-1]

widths = []

with open(pwd+'BinWidths.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        widths.append(1000*np.array(row).astype(float)[1:])
widths = [np.array(widths[i])/2 for i in range(len(widths))][1:-1]
##

## read weights
def floatize(string,oa_bin,energy_bin):
    k = -2 if energy_bin == len(weights_string)-1 else -1
    return float(string[2:k])

toy_weights = []
with open(pwd+'NewToyWeights/toy'+str(toy)+'weights.txt', 'r') as fp:
    for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        toy_weights.append(x)
weights = []
for oa_bin in range(len(toy_weights)):
    weights_string = toy_weights[oa_bin].split(',')
    check = []
    for i in range(len(weights_string)):
        check.append(floatize(weights_string[i],0,i))
    weights.append(check)
##

## read event by event bins (jagged_bins)
EbE_bins = np.load(pwd+'EbE_bins.npy')

## q3_cut?
q3_cut = False

## loop
folder = "BaseResults/"
ofile_path = pwd+folder+"ToyEventRatesFixedToy"+str(toy)+".root"
#####
file = ROOT.TFile.Open(ofile_path,"recreate")
for oa_bin in range(58):
    file.Close()
    print("oa_bin: "+str(oa_bin))
    Enu_true_hist = ROOT.TH1D("Enu_trueHistToy"+str(toy)+"OAB"+str(oa_bin+1),"Enu_trueHistOAB"+str(oa_bin+1),8000,0,8000)
    OmegaReco_hist = ROOT.TH1D("OmegaRecoHistToy"+str(toy)+"OAB"+str(oa_bin+1),"OmegaRecoHistOAB"+str(oa_bin+1),16000,-8000,8000)
    OmegaTrue_hist = ROOT.TH1D("OmegaTrueHistToy"+str(toy)+"OAB"+str(oa_bin+1),"OmegaTrueHistOAB"+str(oa_bin+1),8000,0,8000)
    ELep_hist = ROOT.TH1D("ELepHistToy"+str(toy)+"OAB"+str(oa_bin+1),"ELepHistOAB"+str(oa_bin+1),8000,0,8000)
    ELep4000_hist = ROOT.TH1D("ELep4000HistToy"+str(toy)+"OAB"+str(oa_bin+1),"ELepHistOAB"+str(oa_bin+1),8000,0,8000)
    oa_file = ROOT.TFile(files[oa_bin],"READ")
    t = oa_file.Get("FlatTree_VARS")
    cnt = 0
    for event in t:
        jagged_bin = EbE_bins[oa_bin][cnt]
        enu_bin = bisect(centers[jagged_bin]-widths[jagged_bin],event.Enu_true)
        w = weights[jagged_bin][enu_bin]
        if event.ELep + event.Erecoil_minerva < 4000:
                ELep4000_hist.Fill(event.ELep,w)
        Enu_true_hist.Fill(event.Enu_true,w)
        OmegaReco_hist.Fill(-event.ELep,w)
        OmegaTrue_hist.Fill(event.Enu_true-event.ELep,w)
	ELep_hist.Fill(event.ELep,w)
        cnt += 1
    oa_file.Close()
    file = ROOT.TFile.Open(ofile_path,"update")
    Enu_true_hist.Write()
    OmegaReco_hist.Write()
    OmegaTrue_hist.Write()
    ELep_hist.Write()
    ELep4000_hist.Write()

file.Close()
print("done")
