import VNA_sweeps as sweeps

# VNA parameters
AVERAGES = 1
POWER = -30 #dB
EDELAY = 55.005 #ns
IFBAND = 5 #kHz
CENTERF = [6.951535,6.962962,6.9899725,7.0305278,7.0495508] #GHz
SPAN = [0.8,0.6,0.8,0.4,0.5] #MHz
POINTS = 501
TEMP = 13.2 #mK

# Sample parameters
SAMPLEID = "A01_01" #project ID followed by sample number and die number


OUTPUTFILE = "Nb_reflection_test.csv"

#sweeps.getdata(CENTERF, SPAN, TEMP, AVERAGES, POWER, EDELAY, IFBAND, POINTS, OUTPUTFILE)
STARTPOWER = 0
ENDPOWER = -90
NUMSWEEPS = 10
count = 0
#sweeps.powersweep(STARTPOWER, ENDPOWER, NUMSWEEPS, CENTERF[0], SPAN[0], TEMP, AVERAGES, EDELAY, IFBAND, POINTS, OUTPUTFILE)
for i in CENTERF:
    sweeps.powersweep(STARTPOWER, ENDPOWER, NUMSWEEPS, i, SPAN[count], TEMP, AVERAGES, EDELAY, IFBAND, POINTS, OUTPUTFILE)
    count = count+1
    