import VNA_sweeps as sweeps

AVERAGES = 1
POWER = -30 #dB
EDELAY = 40.04 #ns
IFBAND = 5 #kHz
CENTERF = 7.030574 #GHz
SPAN = 1 #MHz
POINTS = 1001
OUTPUTFILE = "Nb_R4_baseline.csv"
TEMP = 2000 #mK

#sweeps.getdata(CENTERF, SPAN, TEMP, AVERAGES, POWER, EDELAY, IFBAND, POINTS, OUTPUTFILE)
STARTPOWER = 0
ENDPOWER = -50
NUMSWEEPS = 6
sweeps.powersweep(STARTPOWER, ENDPOWER, NUMSWEEPS, CENTERF, SPAN, TEMP, AVERAGES, EDELAY, IFBAND, POINTS, OUTPUTFILE)
