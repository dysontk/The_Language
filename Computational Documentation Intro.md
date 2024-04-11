The building blocks are the symbols of the phonetic system. Each of these are represented here as a python dictionary with the following keys:
### Keys:
1) "name" 
	1) The name of the symbol using the [[Standard Phonetic Typography]] 
	2) Expects: string
3) "type"
	1) Whether it is a consonant (True) or a vowel (False)
	2) Expects: bool
4) "voice"
	1) Whether the sound is voiced (True) or not (False)
	2) Expects bool
#### Consonant keys:
The following keys should be null if it is a vowel.
5) "CPlacement"
	1) Denotes the placement of articulation
	2) Expects: int (0-11)
	3) Options Table:

| 0  | Bilabial       |
|----|----------------|
| 1  | Labiodental    |
| 2  | Dental         |
| 3  | Alveolar       |
| 4  | Post alveolar  |
| 5  | Retroflex      |
| 6  | Palatal        |
| 7  | Velar          |
| 8  | Uvular         |
| 9  | Pharyngeal     |
| 10 | Glottal        |
| 11 | Not Applicable |

               

         
6) "CArticulation"
	1) Denotes the Method of Articulation 
	2) Expects: int (0-8)
	3)  Options Table:

| 0 | Plosive             |
|---|---------------------|
| 1 | Nasal               |
| 2 | Trill               |
| 3 | Tap                 |
| 4 | Fricative           |
| 5 | Lateral Fricative   |
| 6 | Approximant         |
| 7 | Lateral Approximant |
| 8 | Click               |
#### Vowel Keys:
The following are for vowels. They should be null for consonants:
8) "VHeight"
	1) Denotes the height of articulation of the vowel in other words the open or closeness of the vowels 
	2) Expects: int (0-3)
	3)  Options Table:

| 0 | Close/Near-Close   |
|---|--------------------|
| 1 | Close-Mid/Mid      |
| 2 | Open-Mid/Near-Open |
| 3 | Open               |
	NOTE: I NEED TO ADJUST THE PYTHON CODE NOW THAT MY VOWELS SEEM SET
9) "VPlacement"
	1) Denotes the later
10) : null, "Open_Close": null, "ImagePath": null}