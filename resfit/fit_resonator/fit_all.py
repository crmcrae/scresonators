import numpy as np
import matplotlib.pyplot as plt
import pandas as pd #speadsheet commands
import sys #update paths
import os #import os in order to find relative path
import glob

from matplotlib.gridspec import GridSpec
from scipy.interpolate import interp1d
pathToParent = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #set a variable that equals the relative path of parent directory
sys.path.append(pathToParent)#path to Fit_Cavity
import fit_resonator.resonator as res
import fit_resonator.fit_S_data as fsd
np.set_printoptions(precision=4,suppress=True)# display numbers with 4 sig. figures (digits)

                         ## User Input ##

dir = '/Users/coreyraemcrae/OneDrive/OneDrive - UCB-O365/GoldDR_data/Nb01_01/cooldown16/6p7035214GHz_VLPsweep_202102020_17_19_34' #make sure to use / instead of \
dir_output = '/Users/coreyraemcrae/Documents/GoldDR_fits/Nb01_01/cooldown16/6p7035214GHz_VLPsweep_202102020_17_19_34/'

                         ## End User Input ##

if not os.path.exists(dir_output):
    os.makedirs(dir_output)

os.chdir(dir)
names = []
for file in glob.glob("*.csv"):
    if file != 'conditions.csv':
        names.append(file)
names.sort()

Qi_values = []
Qi_conf = []
Qc_values = []
Qc_conf = []
power_values = []

for i in names:
    filename = i
    filepath = dir+'/'+filename
    print(filename)

    currentpower = filename[:filename.index("dB")]
    currentpower = currentpower.replace('p','.')
    for i in range(1, 5, 1):
        currentpower = currentpower[currentpower.index("_"):]
        currentpower = currentpower[1:]

    power_values.append(currentpower)

    #path_to_background = dir+'/'+'Nb_R4_baseline_-50.0dBm_2000mK.csv'

    #############################################
    ## create Method

    fit_type = 'DCM'
    MC_iteration = 10
    MC_rounds = 1e3
    MC_fix = ['w1']
    #manual_init = [Qi,Qc,freq,phi]        #make your own initial guess: [Qi, Qc, freq, phi] (instead of phi used Qa for CPZM)
    manual_init = None # find initial guess by itself

    try:
        Method = res.FitMethod(fit_type, MC_iteration, MC_rounds=MC_rounds,\
                     MC_fix=MC_fix, manual_init=manual_init, MC_step_const=0.3) #mcrounds = 100,000 unless otherwise specified
    except:
        print("Failed to initialize method, please change parameters")
        quit()

    ##############################################################

    normalize = 10

    ### Fit Resonator function without background removal ###
    params,conf_array,fig1,chi1,init1 = fsd.fit_resonator(filename=filename,Method=Method,normalize=normalize,dir=dir,dir_output = dir_output)#,path_to_background)


    Qi_values.append((params[0]**-1-np.real((params[1]/np.exp(1j*params[3]))**-1))**-1)
    Qi_conf.append(conf_array[1])

    Qc_values.append(1/np.real(1/(params[1]/np.exp(1j*params[3]))))
    Qc_conf.append(conf_array[3])

    ### Fit Resonator function with background removal ###
    #path_to_background = dir+'/'+'example_background.csv'
    #params1,fig1,chi1,init1 = Fit_Resonator(filename,filepath,Method,normalize,dir,path_to_background)
    ###############################################



file = open(dir_output + "/power_sweep_params.csv","w")
count = 0
file.write('Power (dB)'+ ','+'Qi' + ',' + 'Qi_conf' + ',' + 'Qc' + ',' + 'Qc_conf[count]' + '\n')
for i in Qi_values:
    file.write(str(power_values[count]) + ',' + str(i) + ',' + str(Qi_conf[count]) + ',' + str(Qc_values[count]) + ',' + str(Qc_conf[count]) + '\n')
    count = count + 1
