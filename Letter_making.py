import json
from pathlib import Path
from enum import Enum


ConPlaceList = ['NA', 'BILABIAL', 'LABIODENTAL', 'DENTAL', 'ALVEOLAR',
 'POSTALVEOLAR', 'RETROFLEX', 'PALATAL', 'VELAR', 'UVULAR', 'PHARYNGEAL', 'GLOTTAL']
ConPlace = Enum('ConPlace', [(ConPlaceList[i], i) for i in range(len(ConPlaceList))])

ConArtList = ['NA', 'PLOSIVE', 'NASAL', 'TRILL', 'TAP', 'FRICATIVE', 'LATERALFRICATIVE', 'APPROXIMANT', 'CLICK']
ConArt = Enum('ConArt', [(ConArtList[j], j) for j in range(len(ConArtList))])

VowelPlaceList = ['NA', 'FRONT', 'MID', 'LOW']
VowelPlace = Enum('VowelPlace', [(VowelPlaceList[i], i) for i in range(len(VowelPlaceList))])

VowelArtList = ['NA', 'TOP', 'HI', 'LO', 'BOT']
VowelArt = Enum('VowelArt', [(VowelArtList[i], i) for i in range(len(VowelArtList))])

RoundednessList = ['NA', 'ROUND', 'UNROUNDED']
Roundedness = Enum('Roundedness', [(RoundednessList[r], r) for r in range(len(RoundednessList))])

Voice = Enum('Voice', [('UNVOICED', 0),('VOICED',1), ('OTHER', 2)])

class Letter(letter_dict):
    def __init__(self, letter_dict):
        self.name = letter_dict['name']
        self.ascii = letter_dict['ascii']
        self.type = letter_dict['type'] #make this an enum: Vowel, consonant, other
        self.imagePath = letter_dict['imagepath']
        self.audioPath = letter_dict['audioPath']
        self.voice = Voice(letter_dict['voice'])
        self.cPlace = ConPlace(letter_dict['cplace'])
        self.cArt = ConArt(letter_dict['cart'])
        self.vPlace = VowelPlace(letter_dict['vplace'])
        self.vArt = VowelArt(letter_dict['vart'])
        self.round = Roundedness(letter_dict['round'])
        

def Letter_from_line(info_string):

    keysList = ['name', 'ascii', 'type', 'voice', 'cplace', 'cart', 'vplace', 'vart', 'round', 'imagepath', 'audiopath']
    info_split = info_string.split()
    let_dic = {keysList[i]:info_split[i] for i in range(len(info_split))}
    # for i in range(len(info_split)):
    return Letter(let_dic)

def Consonant_Maker():
    numPlace = len(ConPlaceList)
    numArt = len(ConArtList)
    collected_letters = []
    for i in range(0, numPlace):
        for j in range(0, numArt):
            for k in range(len(Voice)):
            #ask for input on whether there's a letter here and if so, what's its name, ascii, and paths
            print(f"Is there a letter that is a(n) {Voice(k)} {ConPlace(i)} {ConArt(j)}?")
            let_dic = {}
            name = input("If so, tell me its name or leave blank to skip")
            if name == '':
                continue
            else:
                let_dic.update({'name': name})
                let_dic.update({'ascii':input("thank you, what is this letter's ascii representation?"),
                'imagepath': input("Provide the path to the image location if applicable."),
                'audiopath': input("Provide the path to the audio file if applicable")})
                collected_letters.append(Letter(let_dic))
    return collected_letters
                

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