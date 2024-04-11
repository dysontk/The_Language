import json
from pathlib import Path

def make_letter_auto(nomen, typ, voi, cplace=None, cmoa=None, vHite=None, vplace=None, round=None, img=None):
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
            'unrounded':opcl,
            'ImagePath':img            
            }
    return letDict

def showAttributes(letter):
    TitleList = ['Name', 'Type', 'Voicing Status', 'Consonant Placement', 'Method of Articulation',
        'Vowel Openness', 'Vowel Placement', 'Roundedness', 'Path to Image']
    
    valList = list(letter.values())
    for i in range(len(valList)):
        print(TitleList[i], ' : ', valList[i])
    
    return 0

def showAttributesWords(letter):
    articulationOpts = ['Plosive', 'Nasal', 'Trill', 'Tap', 'Fricative',
         'Lateral Fricative', 'Approximant', 'Lateral Approximant', 'Click']
    placementOpts = ['Bilabial', 'Labiodental', 'Dental',
                'Alveolar',	'Post alveolar', 'Retroflex', 'Palatal', 
                'Velar', 'Uvular',	'Pharyngeal', 'Glottal', 'Not applicable']
    Openness = ['Closed', 'Near-closed', 'Close-mid', 'Mid', 'Open-mid', 'Near-open', 'Open']
    VPlacements = ['Front', 'Central', 'Back']
    
    TitleList = ['Name', 'Type', 'Voicing Status', 'Consonant Placement', 'Method of Articulation',
        'Vowel Height', 'Vowel Placement', 'Roundedness', 'Path to Image']
    Rounds = ['Unrounded', 'Rounded']
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
        outList.append(Rounds[letter['unrounded']])
    
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
    
def write_json(new_data, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        print(type(file_data))

def main():

    # write_json("hi", 'LetterLib.json')
    # This portion  is to make one letter at a time
    # return 0
    # contin = True

    listOletters = []
    # while contin:
    #     fromUser = input("Would you like to create another letter? (y/n)")
        
    #     if fromUser.lower() == 'n' or fromUser == '':
    #         print("Okay, it has been fun, I guess.")
    #         contin = False
    #         continue
    #     else:
    #         nomen = input("Please enter the name of the letter: ")
    #         isC = bool(input("Is this letter a consonant? (0=no, 1=yes) "))

    #         thisLetter = make_letter(nomen, isC)
    #         listOletters.append(thisLetter)

    wantConsonants = True if input('Do you want to make Consonants? (y/n) ')=='y' else False
    wantVowels = True if input('Now how `bout some Vowels sugartits? (y/n) ')=='y' else False

    
    # This portion will ask us what letters exist:
    articulationOpts = ['Plosive', 'Nasal', 'Trill', 'Tap', 'Fricative',
                         'Approximant', 'Lateral Approximant', 'Click']
    placementOpts = ['Bilabial', 'Labiodental', 'Dental',
                'Alveolar',	'Post alveolar', 'Retroflex', 'Palatal', 
                'Velar', 'Glottal']
    if wantConsonants:
        #  make_letter_auto(nomen, typ, voi, cplace=None, cmoa=None, vHite=None, vplace=None, opcl=None, img=None):
        labDent=[]
        for art in articulationOpts:
            for place in placementOpts:
                for voice in ['unvoiced', 'voiced']:
                    bools = [(art=='Nasal' and voice=='unvoiced'), (place == 'Labiodental' and art !='Fricative'), 
                            (place == 'Labiodental' and art !='Fricative'), (art=='Nasal' and place not in ['Bilabial', 'Alveolar', 'Retroflex']),
                            (art=='Trill' and place not in ['Bilabial', 'Alveolar']), (art=='Approximant' and place!='Alveolar'),
                            (art=='Lateral Approximant' and place != 'Alveolar')]
                    ShouldCont = False
                    for b in bool:
                        if b:
                            ShouldCont=True
                            break
                    if ShouldCont:
                        continue
                    fromUser = input(f'What is the name of the {voice} {place} {art}? (0 for N/A) ')
                    if fromUser!= '0':
                        listOletters.append(make_letter_auto(fromUser, 'Consonant', voice, cplace=place, cmoa=art))
    if wantVowels:
        # 'VHeight':vHite,
        #         'VPlacement':vplace,
        #         'Open_Close':opcl,
        VHeights = []
        VPlaces = []
        OpCls = ['open', 'closed']

        for vh in VHeights:
            for vp in VPlaces:
                for i in range(len(OpCls)):
                fromUser = input(f'What is the name of the {vh} {vh} {OpCls[i]} vowel')
                if fromUser!= '0':
                    listOletters.append(make_letter_auto(fromUser, 'Vowel', 1, vHite=vh, vplace=vp, opcl=i))


    print("You have made the following letters")
    for let in listOletters:
        print(type(let))
        showAttributesWords(let)
        print('')
    
    thisPath = Path('LetterLib.json')

    if thisPath.is_file():
        print("This file already exists. I will make sure to keep that information")
        
        with open('LetterLib.json', 'r+') as file:
            file_data = json.load(file)
            print(file_data)
            # print(file_data.appen(list))
            listOletters = file_data + listOletters 


    with open("LetterLib.json", "w") as outfile:
        json.dump(listOletters, outfile)
        # for let in listOletters:
        #     print("Printing ", let['name'])
        #     json.dump(let, outfile)
        #     json
    

if __name__ == '__main__':
    main()