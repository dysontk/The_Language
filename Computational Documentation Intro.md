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
	2) Expects: int
	3) Options Table:

| 1  | Bilabial       |
|----|----------------|
| 2  | Labioental     |
| 3  | Dental         |
| 4  | Alveolar       |
| 5  | Post alveolar  |
| 6  | Retroflex      |
| 7  | Palatal        |
| 8  | Velar          |
| 9  | Uvular         |
| 10 | Pharyngeal     |
| 11 | Glottal        |
| 12 | Not Applicable |

               

         'Lateral Fricative', 'Approximant', 'Lateral Approximant', 'Click']
6) : 7, "CArticulation": 0, "VHeight": null, "VPlacement": null, "Open_Close": null, "ImagePath": null}