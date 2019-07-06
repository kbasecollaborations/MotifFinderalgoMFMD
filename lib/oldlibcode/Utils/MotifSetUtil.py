

#TODO: extract sequence from output files, add to motif object
def ConvertMotif(motif,MotifSet):
    newMotif = {}
    newMotif['Motif_Locations'] = []
    for loc in motif['Locations']:
        new_loc = {}
        new_loc['Feature_id'] = loc[0]
        new_loc['start'] = int(loc[1])
        new_loc['end'] = int(loc[2])
        new_loc['orientation'] = loc[3]
        new_loc['sequence']= 'SEQUENCE'
        newMotif['Motif_Locations'].append(new_loc.copy())
    newMotif['Iupac_sequence'] = motif['Iupac_signature']
    newMotif['PWM'] = {}
    newMotif['PFM'] = {}
    for letter in MotifSet['Alphabet']:
        newMotif['PWM'][letter] = []
        newMotif['PFM'][letter] = []
    for row in motif['pwm']:
        for pair in row:
            newMotif['PWM'][pair[0]].append(pair[1])
    return newMotif

def parseMotifList(MotifList, MotifSet):
    for motif in MotifList:
        MotifSet['Motifs'].append(ConvertMotif(motif,MotifSet))
