import json
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pyseqlogo.pyseqlogo import draw_logo, setup_axis

def buildReportFromMotifSet(MotifSet,htmlDir,imgStr):
    htmlReport = '<html><body>'
    htmlReport += '<table style="width:100%" border=1>\n' + '<tr>\n'
    #htmlReport += '<th> Sequence </th>\n' + '<th> Logo </th>\n' + '<th> Ratio </th>\n + </tr>\n'
    htmlReport += '<th> Sequence </th>\n' + '<th> Logo </th>\n' + '<th> Locations </th>\n + </tr>\n'
    #numFeat = int(sys.argv[3])
    #numFeat = int(sys.argv[3])

    #for each motif
    #get the iupac
    #get the locations
    #all we need
    #argvs - 1: jsonpath , 2: outhtmlpath, 3:num seqs
    for motif in MotifSet['Motifs']:
        htmlReport += '<tr>\n <td> ' + motif['Iupac_sequence'] + ' </td>\n'
        #plt.rcParams['figure.dpi'] = 300
        #this might not work...
        PSLPWM = []
        for base in motif['PWM'].keys():
            for i,w in enumerate(motif['PWM'][base]):
                if len(PSLPWM) == i:
                    PSLPWM.append([])
                PSLPWM[i].append((base,w))
        #fig, axarr = draw_logo(motif['pwm'])
        fig, axarr = draw_logo(PSLPWM)
        fig.tight_layout()
        imgName = imgStr + '_' + motif['Iupac_sequence']

        #imgName = motif['Iupac_sequence'] + sys.argv[2].split('/')[len(sys.argv[2].split('/'))-1].replace('.html','') + '.png'

        #saveTo = htmlDir + '/' + imgName
        #saveTo = '/' + '/'.join(sys.argv[2].split('/')[:-1]) + '/'  + imgName
        saveTo = htmlDir + '/' + imgName
        htmlReport += '<td> <img src="' + imgName + '.png'+ '" height=25%> </td>\n'
        seqDict = {}
        #for l in motif['Locations']:
        #    seqDict[l[0]] = 1
        #ratio = float(len(seqDict))/float(numFeat)

        locationString = ''
        for loc in motif['Motif_Locations']:
            locationList = [loc['sequence_id'],str(loc['start']),str(loc['end']),loc['orientation']]
            locationString += ' '.join(locationList) + '<br />'

        htmlReport += '<td> '  + locationString + ' </td>\n'
        #htmlReport += '<td> '  + str(ratio) + ' </td>\n'

        htmlReport += '</tr>\n'
        plt.savefig(saveTo)
        plt.close()
    htmlReport += '</table>\n'
    htmlReport += '</body></html>'
    #htmlPath = htmlDir + '/' + sys.argv[2]
    htmlFileName = htmlDir+ '/' + imgStr + '.html'
    with open(htmlFileName,'w') as html_handle:
        html_handle.write(str(htmlReport))
