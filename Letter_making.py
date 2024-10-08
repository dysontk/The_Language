def make_letter_auto(nomen, typ, voi, cplace=None, cmoa=None, vHite=None, vplace=None, opcl=None, img=None):
    # typword = 'Consonant' if typ else 'Vowel'
    # voiceword = 'Voiced' if voi else 'Unvoiced'

    letDict = {
            'name': nomen,
            'type': typ,
            # 'typeword':typword,
            'voice': voi,
            # 'voiceword': voiceword,
            'CPlacement':cplace,
            'CArticulation': cmoa,
            'VHeight':vHite,
            'VPlacement':vplace,
            'Open_Close':opcl,
            'ImagePath':img            
            }
    return letDict

def showAttributes(letter):
    TitleList = ['Name', 'Type', 'Voicing Status', 'Consonant Placement', 'Method of Articulation',
        'Vowel Height', 'Vowel Placement', 'Vowel Open/Close', 'Path to Image']
    
    valList = list(letter.values())
    for i in range(len(valList)):
        print(TitleList[i], ' : ', valList[i])
    
    return 0

def showAttributesWords(letter):
    articulationOpts = ['Plosive', 'Nasal', 'Trill', 'Tap', 'Fricative',
         'Lateral Fricative', 'Approximant', 'Lateral Approximant', 'Click']
    placementOpts = ['Bilabial', 'Labioental', 'Dental',
                'Alveolar',	'Post alveolar', 'Retroflex', 'Palatal', 
                'Velar', 'Uvular',	'Pharyngeal', 'Glottal', 'Not applicable']
    Heights = ['Bottom', 'Low', 'High', 'Top']
    VPlacements = ['Front', 'Mid', 'Back']
    
    TitleList = ['Name', 'Type', 'Voicing Status', 'Consonant Placement', 'Method of Articulation',
        'Vowel Height', 'Vowel Placement', 'Vowel Open/Close', 'Path to Image']
    outList = [letter['name']]
    if letter['type']: # equiv. to 'isCons'
        outList.append('Consonant')
        outList.append('Voiced' if letter['voice'] else 'Unvoiced')
        outList.append(placementOpts[letter['CPlacement']])
        outList.append(articulationOpts[letter['CArticulation']])
        for i in range(3):
            outList.append(None)

    else:
        outList.append('Vowel')
        outList.append('Voiced' if letter['voice'] else 'Unvoiced')
        for i in range(2):
            outList.append(None)
        outList.append(Heights[letter['VHeight']])
        outList.append(VPlacements[letter['VPlacement']])
    
    outList.append(letter['ImagePath'])
    # print(outList)
    for j in range(len(outList)):
        print(TitleList[j], ": ", outList[j])
    
    return 

def make_letter(nom, isCons):
    articulationOpts = ['Plosive', 'Nasal', 'Trill', 'Tap', 'Fricative',
         'Lateral Fricative', 'Approximant', 'Lateral Approximant', 'Click']
    placementOpts = ['Bilabial', 'Labiodental', 'Dental',
                'Alveolar',	'Post alveolar', 'Retroflex', 'Palatal', 
                'Velar', 'Uvular',	'Pharyngeal', 'Glottal', 'Not applicable']
    if isCons:
        print('Options for Placement: ')
        for i in range(len(placementOpts)):
            print(i, ' -- ', placementOpts[i])
        print('')
        
        cPlacement = int(input('Using the key above, tell me the number corresponding to the proper placement. '))
        print('Options for Method of Articulation: ')
        for i in range(len(articulationOpts)):
            print(i, ' -- ', articulationOpts[i])
        print('')
        cMoA = int(input('Using the key above, tell me the number corresponding to the proper method of Articulation. '))

        voice = bool(input('Is this phoneme voiced? (1 -- yes, 0 -- no) '))
        return make_letter_auto(nom, isCons, voice, cplace=cPlacement, cmoa=cMoA)


    else:
        vHeight = int(input('Height of vowel (0[lowest], 1, 2, 3[highest]): '))
        vPlacement = int(input('Placement of vowel (0[fwd], 1, 2[back]) : '))
        vOpCl = int(input('Is the vowel Open(0) or Closed(1)? '))

        return make_letter_auto(nom, isCons, 1, vHite=vHeight, vplace=vPlacement, opcl=vOpCl)
    

def main():
    import json
    contin = True

    listOletters = []
    while contin:
        fromUser = input("Would you like to create another letter? (y/n)")
        
        if fromUser.lower() == 'n' or fromUser == '':
            print("Okay, it has been fun, I guess.")
            contin = False
            continue
        else:
            nomen = input("Please enter the name of the letter: ")
            isC = bool(input("Is this letter a consonant? (0=no, 1=yes) "))

            thisLetter = make_letter(nomen, isC)
            listOletters.append(thisLetter)
    
    for let in listOletters:
        showAttributesWords(let)
    
    with open("LetterLib.json", "w") as outfile:
        for let in listOletters:
            print("Printing ", let['name'])
            json.dump(let, outfile)
    

if __name__ == '__main__':
    main()