import numpy as np

words = ['absolute', 'academic', 'accident', 'activity', 'addition', 'youthful', 'wrinkles', 'wrestler', 'vitamins',
         'virulent', 'verbatim', 'unwanted', 'umbrella', 'untitled', 'twitters', 'twilight', 'backbite', 'backyard',
         'balloons', 'bedrooms', 'bereaved', 'tutorial', 'bathroom', 'becoming', 'benjamin', 'birthday', 'boundary',
         'breaking', 'breeding', 'building', 'bulletin', 'business', 'calendar', 'campaign',
         'capacity', 'casualty', 'catching', 'category', 'catholic', 'cautious', 'cellular', 'ceremony', 'chairman',
         'champion', 'chemical', 'children', 'circular', 'civilian', 'clearing', 'clinical', 'clothing',
         'collapse', 'colonial', 'colorful', 'commence', 'commerce', 'complain', 'complete', 'composed', 'compound',
         'comprise', 'computer', 'conclude', 'concrete', 'conflict', 'confused', 'congress', 'consider', 'constant',
         'consumer', 'continue', 'contract', 'contrary', 'contrast', 'convince', 'corridor', 'coverage', 'covering',
         'creation', 'creative', 'criminal', 'critical', 'crossing', 'cultural', 'currency', 'customer', 'database',
         'daughter', 'daylight', 'deadline', 'deciding', 'decision', 'decrease', 'deferred', 'definite', 'delicate',
         'delivery', 'describe', 'designer', 'detailed', 'diabetes', 'dialogue', 'diameter', 'directly', 'director',
         'disabled', 'disaster', 'disclose', 'discount', 'discover', 'disorder', 'disposal', 'distance', 'distinct',
         'district', 'dividend', 'division', 'doctrine', 'document', 'domestic', 'dominant', 'dominate', 'doubtful',
         'dramatic', 'dressing', 'dropping', 'duration', 'dynamics', 'earnings', 'economic', 'educated', 'efficacy',
         'eighteen', 'election', 'electric', 'eligible', 'emerging', 'emphasis',
         'employee', 'endeavor', 'engaging', 'engineer', 'enormous', 'entirely', 'entrance', 'envelope', 'equality',
         'equation', 'estimate', 'evaluate', 'eventual', 'everyday', 'everyone', 'evidence', 'exchange', 'exciting',
         'exercise', 'explicit', 'exposure', 'extended', 'external', 'facility', 'familiar', 'featured', 'feedback',
         'festival', 'finished', 'firewall', 'flagship', 'flexible', 'floating', 'football', 'foothill', 'forecast',
         'foremost', 'formerly', 'fourteen',
         'fraction', 'franklin', 'frequent', 'friendly', 'frontier', 'function', 'generate', 'generous', 'goodwill',
         'governor', 'graduate', 'graphics',
         'grateful', 'guardian', 'guidance', 'handling', 'hardware', 'heritage', 'highland', 'historic', 'homeless',
         'homepage',
         'hospital', 'humanity', 'identify', 'identity', 'ideology', 'imperial', 'incident', 'included', 'increase',
         'indicate', 'indirect', 'industry', 'informal', 'informed', 'inherent', 'initiate', 'innocent', 'inspired',
         'instance', 'integral', 'intended', 'interact',
         'interest', 'interior', 'internal', 'interval', 'intimate', 'intranet', 'invasion', 'involved', 'isolated',
         'judgment', 'judicial', 'junction', 'keyboard', 'landlord', 'language', 'laughter', 'learning', 'leverage',
         'lifetime', 'lighting', 'likewise', 'limiting', 'literary', 'location',
         'magazine', 'magnetic', 'maintain', 'majority', 'marginal', 'marriage', 'material', 'maximize', 'meantime',
         'measured', 'medicine', 'medieval', 'memorial', 'merchant', 'midnight', 'military', 'minimize', 'minister',
         'ministry', 'minority', 'mobility', 'modeling', 'moderate', 'momentum', 'monetary', 'moreover', 'mortgage',
         'mountain', 'mounting', 'movement', 'multiple', 'national', 'negative', 'nineteen', 'northern', 'notebook',
         'numerous', 'observer', 'occasion', 'offering', 'official',
         'offshore', 'operator', 'opponent', 'opposite', 'optimism', 'optional', 'ordinary', 'organize', 'original',
         'overcome', 'overhead', 'overseas', 'overview', 'painting', 'parallel', 'parental', 'patented', 'patience',
         'peaceful', 'periodic', 'personal', 'persuade', 'petition', 'physical', 'pipeline', 'platform', 'pleasant',
         'pleasure',
         'politics', 'portable', 'portrait', 'position', 'positive', 'possible', 'powerful', 'practice', 'precious',
         'pregnant', 'presence', 'preserve', 'pressing', 'pressure', 'previous', 'princess', 'printing', 'priority',
         'probable', 'probably', 'producer', 'profound', 'progress', 'property', 'proposal', 'prospect', 'protocol',
         'provided',
         'provider', 'province', 'publicly', 'purchase', 'pursuant', 'quantity', 'question', 'rational', 'reaction',
         'received', 'receiver', 'recovery', 'regional', 'register', 'relation', 'relative', 'relevant', 'reliable',
         'reliance', 'religion', 'remember', 'renowned', 'repeated', 'reporter',
         'republic', 'required', 'research', 'reserved', 'resident', 'resigned', 'resource', 'response',
         'restrict', 'revision', 'rigorous', 'romantic', 'sampling', 'scenario', 'schedule', 'scrutiny', 'seasonal',
         'secondly', 'security', 'sensible', 'sentence', 'separate', 'sequence',
         'sergeant', 'shipping', 'shortage', 'shoulder', 'simplify', 'situated',
         'slightly', 'software', 'solution', 'somebody', 'somewhat', 'southern',
         'speaking', 'specific', 'spectrum', 'sporting', 'standard', 'standing',
         'standout', 'sterling', 'straight', 'strategy', 'strength', 'striking',
         'struggle', 'stunning', 'suburban', 'suitable', 'superior', 'supposed',
         'surgical', 'surprise', 'survival', 'sweeping', 'swimming',
         'symbolic', 'sympathy', 'syndrome', 'tactical', 'tailored', 'takeover', 'tangible', 'taxation',
         'taxpayer', 'teaching', 'tendency',
         'terminal', 'terrible', 'thinking', 'thirteen', 'thorough', 'thousand', 'together', 'tomorrow', 'touching',
         'tracking', 'training', 'transfer', 'traveled', 'treasury',
         'triangle', 'tropical', 'turnover', 'ultimate', 'umbrella', 'universe', 'unlawful', 'unlikely', 'valuable',
         'variable', 'vertical', 'victoria',
         'violence', 'volatile', 'warranty', 'weakness', 'weighted', 'whatever', 'whenever', 'wherever',
         'wildlife', 'wireless', 'withdraw', 'woodland', 'workshop', 'yourself']


def generate_word(words):
    random_word_index = np.random.randint(0, len(words) - 1)
    print("Your letter has ", len(words[random_word_index]), " letters")
    return words[random_word_index]


def find_letter(character, word, guessing):
    for i in range(len(word)):
        if word[i] == character:
            guessing[i] = 1
    return guessing


def current_status(word, guessing):
    for i in range(len(word)):
        if guessing[i] == 0:
            print("_", end="")
        elif guessing[i] == 1:
            print(word[i], end="")
    print("\n")


def game_loop(random_word, guessed):
    chance = 6
    print("You have ", chance, " chances")
    while sum(guessed) != len(random_word):
        letter = input("Enter your letter: ")
        if random_word.find(letter) == -1:
            print("You lost one chance!")
            chance -= 1
        else:
            print("You got it correct!")
            guessed = find_letter(letter, random_word, guessed)
        if chance == 0:
            print("You Lost!")
            print("The Word was: ", random_word)
            break
        elif sum(guessed) == len(random_word):
            print("After this guess: ")
            current_status(random_word, guessed)
            print("Hurrah! You Won!")
        else:
            print("After this guess: ")
            current_status(random_word, guessed)
            print("Remaining Chances: ", chance)


random_word = generate_word(words)
guessed = np.zeros(len(random_word))
game_loop(random_word, guessed)
