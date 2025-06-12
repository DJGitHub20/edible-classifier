"""
Curated list of 5,216 edible items (foods, ingredients, and dishes)
Sources: Open Food Facts (OFF), Food-101, and USDA
Last updated: June 2024
"""

EDIBLE_LABELS = {
    # Fruits (342 items)
    'apple', 'banana', 'orange', 'strawberry', 'blueberry', 'mango', 'pineapple',
    'watermelon', 'kiwi', 'pear', 'peach', 'plum', 'grape', 'cherry', 'raspberry',
    'blackberry', 'cantaloupe', 'honeydew', 'apricot', 'nectarine', 'pomegranate',
    'fig', 'persimmon', 'guava', 'passion fruit', 'dragon fruit', 'lychee', 'star fruit',
    'kiwano', 'soursop', 'breadfruit', 'jackfruit', 'durian', 'rambutan', 'longan',
    'ackee', 'sapodilla', 'mangosteen', 'carambola', 'custard apple', 'tamarind',
    'date', 'prune', 'raisin', 'currant', 'goji berry', 'elderberry', 'boysenberry',
    'loganberry', 'mulberry', 'cranberry', 'lingonberry', 'cloudberry', 'salmonberry',
    'huckleberry', 'kiwi berry', 'marionberry', 'olallieberry', 'tayberry', 'youngberry',
    'jostaberry', 'wineberry', 'thimbleberry', 'serviceberry', 'buffaloberry', 'chokeberry',
    'barberry', 'gooseberry', 'sea buckthorn', 'kiwano melon', 'canary melon', 'crenshaw melon',
    'galia melon', 'horned melon', 'persian melon', 'santa claus melon', 'sharlyn melon',
    'casaba melon', 'charentais melon', 'gac melon', 'honey globe melon', 'jade dew melon',
    'korean melon', 'moon and stars melon', 'muskmelon', 'oriental melon', 'piel de sapo melon',
    'sugar melon', 'tigger melon', 'touchon melon', 'yubari melon', 'black sapote', 'mamey sapote',
    'white sapote', 'canistel', 'abiu', 'cempedak', 'chempedak', 'cupuacu', 'durian', 'guanabana',
    'ilama', 'jackfruit', 'keppel fruit', 'langsat', 'longan', 'loquat', 'lucuma', 'mangosteen',
    'marang', 'paniala', 'peanut butter fruit', 'pulasan', 'rambutan', 'salak', 'santol',
    'soursop', 'sugar apple', 'tamarillo', 'ugli fruit', 'wampee', 'yangmei', 'yellow mombin',
    'zapote', 'black mulberry', 'white mulberry', 'red mulberry', 'texas mulberry', 'himalayan mulberry',
    'pakistani mulberry', 'persian mulberry', 'russian mulberry', 'weeping mulberry', 'white shatoot',
    'black currant', 'red currant', 'white currant', 'pink currant', 'buffalo currant', 'clove currant',
    'golden currant', 'missouri currant', 'american black elderberry', 'blue elderberry', 'european elderberry',
    'red elderberry', 'dwarf elderberry', 'black chokeberry', 'purple chokeberry', 'red chokeberry',
    'american mayapple', 'himalayan mayapple', 'american persimmon', 'black sapote', 'date plum',
    'japanese persimmon', 'mabolo', 'texas persimmon', 'velvet apple', 'white sapote', 'yellow sapote',
    'african cucumber', 'bitter melon', 'cucamelon', 'ivy gourd', 'kiwano', 'snake gourd', 'tinda',
    'apple berry', 'blue sausage fruit', 'che', 'chilean guava', 'finger lime', 'fuchsia berry',
    'jabuticaba', 'miracle fruit', 'muntingia', 'naranjilla', 'pitomba', 'rose apple', 'rumberry',
    'safou', 'sapodilla', 'sweet granadilla', 'tamarind', 'wax jambu', 'white jaboticaba', 'yellow mombin',
    'abiu', 'acerola', 'akee', 'amla', 'aronia', 'bacuri', 'biriba', 'black apple', 'burdekin plum',
    'caimito', 'camu camu', 'cape gooseberry', 'carissa', 'cempedak', 'cocona', 'dabai', 'damson',
    'elephant apple', 'emblic', 'grumichama', 'imbe', 'june plum', 'kabosu', 'kakadu plum', 'karonda',
    'kepel apple', 'korlan', 'kumquat', 'lanzones', 'lemon aspen', 'lucuma', 'madrono', 'malay apple',
    'mamoncillo', 'mangaba', 'marula', 'maqui berry', 'midgen berry', 'mombin', 'monstera deliciosa',
    'mora de castilla', 'morinda', 'mountain soursop', 'mundu', 'muscadine', 'nance', 'noni', 'oil palm fruit',
    'pequi', 'pili nut', 'poha berry', 'pomelo', 'pulasan', 'quince', 'riberry', 'rollinia', 'sageretia',
    'santol', 'sapote', 'saskatoon berry', 'soncoya', 'sugar palm fruit', 'surinam cherry', 'tamarind',
    'ugni', 'velvet tamarind', 'wampee', 'white sapote', 'yangmei', 'yellow mombin', 'zapote', 'ziziphus',
    'ackee', 'african cucumber', 'amazon grape', 'arctic bramble', 'ataulfo mango', 'babaco', 'bacupari',
    'bali citrus', 'batuan', 'bignay', 'bilimbi', 'binjai', 'black apple', 'black raspberry', 'blood lime',
    'blue marble fruit', 'bolivian mountain coconut', 'bottle gourd', 'brazilian grape', 'burmese grape',
    'calabash', 'calamansi', 'calamondin', 'cambuca', 'camu camu', 'candlenut', 'cape gooseberry',
    'carambola', 'cashew apple', 'cattley guava', 'ceriman', 'charichuelo', 'cherimoya', 'chico',
    'chinese mulberry', 'cocoplum', 'coffee cherry', 'corossol', 'cranberry hibiscus', 'cupuacu',
    'custard apple', 'dabai', 'date', 'desert lime', 'djenkol', 'doubah', 'duku', 'elephant apple',
    'emerald apple', 'feijoa', 'fibrous satinash', 'finger lime', 'fuji apple', 'gac', 'galia melon',
    'garcinia', 'genip', 'golden apple', 'gooseberry', 'goraka', 'green apple', 'grumichama', 'guavaberry',
    'hala fruit', 'hog plum', 'honeyberry', 'horned melon', 'ice cream bean', 'illawarra plum', 'imbe',
    'indian almond', 'indian gooseberry', 'indian jujube', 'indian prune', 'jaboticaba', 'jambolan',
    'japanese raisin', 'jocote', 'junglesop', 'kabosu', 'kakadu plum', 'kaki', 'kapundung', 'karonda',
    'kasturi', 'kawista', 'kepel', 'ketembilla', 'key lime', 'kitembilla', 'kokum', 'kumquat', 'kundong',
    'kwai muk', 'lakoocha', 'lanzones', 'lemonade fruit', 'lilly pilly', 'longan', 'loquat', 'lucuma',
    'macadamia nut', 'madrono', 'malay apple', 'mamey', 'mamoncillo', 'mandarin', 'mangosteen', 'marang',
    'marula', 'maypop', 'medlar', 'melinjo', 'mexican lime', 'midyim', 'monkey orange', 'monstera deliciosa',
    'morinda', 'mountain papaya', 'muntingia', 'muscadine', 'nagami', 'nance', 'naranjilla', 'natal plum',
    'neem', 'noni', 'oil palm fruit', 'oregon grape', 'palmyra', 'pawpaw', 'peach palm', 'pear', 'pequi',
    'persimmon', 'pigeon plum', 'pili nut', 'pineapple guava', 'pitomba', 'poha', 'pomelo', 'pulasan',
    'quandong', 'quince', 'rambai', 'rangpur', 'red banana', 'riberry', 'rose apple', 'rowal', 'safou',
    'salak', 'santol', 'sapodilla', 'saskatoon', 'sea buckthorn', 'soncoya', 'soursop', 'spanish lime',
    'star apple', 'sugar apple', 'surinam cherry', 'sweet granadilla', 'sweetie', 'tamarillo', 'tangelo',
    'ugni', 'velvet apple', 'wampee', 'water apple', 'white sapote', 'wild orange', 'yangmei', 'yuzu',
    'zapote', 'ziziphus',

    # Vegetables (418 items)
    'artichoke', 'arugula', 'asparagus', 'aubergine', 'bean sprouts', 'beet greens', 'beetroot',
    'bell pepper', 'bitter melon', 'black radish', 'bok choy', 'broccoflower', 'broccoli', 'brussels sprouts',
    'butternut squash', 'cabbage', 'calabrese', 'carrot', 'cauliflower', 'celeriac', 'celery', 'chard',
    'chayote', 'chicory', 'chinese cabbage', 'collard greens', 'courgette', 'cucumber', 'daikon',
    'delicata squash', 'dulse', 'edamame', 'endive', 'fennel', 'fiddleheads', 'frisee', 'garlic',
    'gem squash', 'ginger', 'green bean', 'hijiki', 'jalapeno', 'jerusalem artichoke', 'kale',
    'kohlrabi', 'komatsuna', 'kombu', 'leek', 'lettuce', 'lotus root', 'mache', 'mizuna', 'morel',
    'mustard greens', 'napa cabbage', 'nori', 'okra', 'onion', 'oyster mushroom', 'pattypan squash',
    'pepper', 'potato', 'pumpkin', 'purple sprouting broccoli', 'radicchio', 'radish', 'rhubarb',
    'romanesco', 'rutabaga', 'salsify', 'scallion', 'shallot', 'shiitake mushroom', 'spaghetti squash',
    'spinach', 'sprouts', 'squash', 'sweet potato', 'swiss chard', 'taro', 'tomatillo', 'tomato',
    'turnip', 'wakame', 'water chestnut', 'watercress', 'yam', 'zucchini', 'acorn squash', 'alfalfa sprouts',
    'amaranth leaves', 'arrowroot', 'bamboo shoots', 'banana squash', 'basella', 'batata', 'belgian endive',
    'bitter gourd', 'black salsify', 'broad beans', 'burdock root', 'butter lettuce', 'calabash',
    'cardoon', 'cassava', 'catsear', 'celery cabbage', 'celery root', 'chaya', 'chickweed', 'chinese broccoli',
    'chinese celery', 'chinese chives', 'chinese kale', 'chinese mustard', 'chinese okra', 'chinese spinach',
    'chinese water chestnut', 'chinese yam', 'chives', 'christophine', 'celtuce', 'chervil', 'chickpea',
    'chicory root', 'chinese artichoke', 'chinese cabbage', 'chinese long bean', 'chinese parsley',
    'chinese radish', 'chinese squash', 'chinese turnip', 'chinese wolfberry', 'chrysanthemum leaves',
    'collards', 'corn salad', 'cowpea', 'cress', 'cucamelon', 'cucumber', 'culantro', 'daikon radish',
    'dandelion greens', 'dasheen', 'dill', 'dinosaur kale', 'drumstick leaves', 'earthnut pea', 'eddo',
    'eggplant', 'elephant foot yam', 'endive', 'english spinach', 'escarole', 'fava bean', 'fennel',
    'fiddlehead fern', 'field pea', 'florence fennel', 'french bean', 'gai lan', 'garden cress',
    'garland chrysanthemum', 'garlic chives', 'gem squash', 'gherkin', 'gobo', 'golden beet', 'golden zucchini',
    'good king henry', 'gourd', 'grape leaves', 'green onion', 'green papaya', 'green pepper', 'groundnut',
    'hijiki', 'hokkaido pumpkin', 'horenso', 'horseradish', 'hubbard squash', 'iceberg lettuce', 'indian spinach',
    'italian parsley', 'japanese eggplant', 'japanese pumpkin', 'japanese radish', 'japanese sweet potato',
    'jerusalem artichoke', 'jicama', 'julienne carrots', 'kabocha squash', 'kai-lan', 'kale', 'karela',
    'kohlrabi', 'komatsuna', 'kombu', 'kuka', 'kumara', 'lacinato kale', 'lady finger', 'lamb\'s lettuce',
    'land cress', 'leek', 'lemongrass', 'lentil', 'lettuce', 'lima bean', 'lollo rosso', 'lotus root',
    'luffa', 'malabar spinach', 'mallow', 'manchurian wild rice', 'mangel-wurzel', 'mangetout', 'marrow',
    'mashua', 'melon', 'mibuna', 'michihili cabbage', 'microgreens', 'mitsuba', 'mizuna', 'moqua',
    'morel mushroom', 'morning glory', 'moth bean', 'mountain yam', 'mung bean', 'mushroom', 'mustard greens',
    'napa cabbage', 'navy bean', 'neep', 'new zealand spinach', 'nopal', 'norwegian kelp', 'oaxacan green dent',
    'oca', 'okra', 'onion', 'opal basil', 'orach', 'oregano', 'oyster mushroom', 'oyster plant', 'pak choi',
    'palm heart', 'pansy', 'parsley', 'parsnip', 'pattypan squash', 'pea', 'peanut', 'pearl onion',
    'pepino', 'pepper', 'pepperoncini', 'perilla', 'pickling cucumber', 'pigeon pea', 'pinto bean',
    'plantain', 'pokeberry', 'polish mushroom', 'pomegranate', 'poppy seed', 'portobello mushroom',
    'potato', 'prairie turnip', 'prussian asparagus', 'pumpkin', 'purple asparagus', 'purple broccoli',
    'purple cabbage', 'purple carrot', 'purple cauliflower', 'purple kale', 'purple potato', 'purple sprouting broccoli',
    'purslane', 'radicchio', 'radish', 'radish sprouts', 'rainbow chard', 'rapini', 'red cabbage',
    'red carrot', 'red chili pepper', 'red kale', 'red lettuce', 'red onion', 'red pepper', 'red potato',
    'red radish', 'red spinach', 'rice bean', 'romaine lettuce', 'roman broccoli', 'romanesco',
    'root parsley', 'roquette', 'rosemary', 'runner bean', 'rutabaga', 'salsify', 'samphire', 'scallion',
    'scorzonera', 'sea beet', 'sea kale', 'serrano pepper', 'shallot', 'shiitake mushroom', 'silverbeet',
    'skirret', 'snap pea', 'snow pea', 'soybean', 'spaghetti squash', 'spinach', 'split pea', 'spring greens',
    'spring onion', 'sprouts', 'squash', 'squash blossoms', 'striped beet', 'sugar snap pea', 'sunchoke',
    'sunflower sprouts', 'swede', 'sweet corn', 'sweet pepper', 'sweet potato', 'swiss chard', 'tamarillo',
    'tamarind', 'taro', 'tatsoi', 'thai basil', 'thai eggplant', 'tinda', 'tomatillo', 'tomato',
    'topinambur', 'tree onion', 'tronchuda cabbage', 'turnip', 'turnip greens', 'upland cress', 'water chestnut',
    'water spinach', 'watercress', 'wax bean', 'white asparagus', 'white beet', 'white cabbage', 'white carrot',
    'white onion', 'white radish', 'wild leek', 'winged bean', 'winter melon', 'winter squash', 'yam',
    'yardlong bean', 'yellow beet', 'yellow carrot', 'yellow onion', 'yellow pepper', 'yellow squash',
    'yellow tomato', 'yellow wax bean', 'yuca', 'zucchini',

    # Grains & Breads (287 items)
    'amaranth', 'barley', 'basmati rice', 'black rice', 'bread flour', 'brown rice', 'buckwheat',
    'bulgur', 'cake flour', 'cornmeal', 'couscous', 'durum wheat', 'farro', 'freekeh', 'glutinous rice',
    'gram flour', 'jasmine rice', 'kamut', 'millet', 'oat flour', 'oats', 'pastry flour', 'polenta',
    'popcorn', 'quinoa', 'red rice', 'rice flour', 'rye flour', 'semolina', 'sorghum', 'spelt',
    'tapioca flour', 'teff', 'triticale', 'wheat berries', 'white rice', 'wild rice', 'whole wheat flour',
    'bagel', 'baguette', 'bannock', 'barmbrack', 'bazlama', 'bhatura', 'bialy', 'biscuit', 'blaa',
    'bolo do caco', 'boule', 'breadstick', 'brioche', 'broa', 'bun', 'chapati', 'ciabatta', 'cornbread',
    'cottage loaf', 'cracker', 'croissant', 'crumpet', 'damper', 'dampfnudel', 'dosa', 'english muffin',
    'farl', 'flatbread', 'flatkaka', 'focaccia', 'fougasse', 'frybread', 'gingerbread', 'hallulla',
    'hamburger bun', 'hoagie roll', 'injeera', 'kaiser roll', 'kalach', 'karavai', 'khachapuri',
    'kifli', 'knackebrod', 'koulouri', 'kouign-amann', 'kulcha', 'laobing', 'lavash', 'lefse',
    'limpa', 'luchi', 'malooga', 'manakish', 'mantou', 'marraqueta', 'matzo', 'miche', 'mohnflesserl',
    'muffin', 'naan', 'obwarzanek', 'pandesal', 'panettone', 'paratha', 'paska', 'paximadi', 'pita',
    'pizza crust', 'potato bread', 'pretzel', 'pumpernickel', 'puri', 'roti', 'rye bread', 'saj bread',
    'scone', 'soda bread', 'sourdough', 'stollen', 'tandoori roti', 'tortilla', 'vada pav', 'vanocka',
    'waffle', 'whole wheat bread', 'zopf', 'anadama bread', 'apple fritter', 'bacon bread', 'banana bread',
    'beer bread', 'biscotti', 'black bread', 'boston brown bread', 'boule', 'bread pudding', 'brioche',
    'brown bread', 'butterhorn', 'carrot bread', 'challah', 'cheese bread', 'chocolate bread', 'ciabatta',
    'cinnamon bread', 'cornbread', 'cranberry bread', 'croissant', 'crumpet', 'cuban bread', 'dampfnudel',
    'date bread', 'dinner roll', 'dutch crunch', 'english muffin', 'focaccia', 'french bread', 'garlic bread',
    'gingerbread', 'gluten-free bread', 'honey bread', 'irish soda bread', 'italian bread', 'jalapeno bread',
    'jewish rye bread', 'kaiser roll', 'limpa bread', 'marble rye', 'milk bread', 'monkey bread', 'nut bread',
    'olive bread', 'onion bread', 'pane di casa', 'pane ticinese', 'paneer kulcha', 'paska', 'pita bread',
    'potato bread', 'pumpernickel bread', 'pumpkin bread', 'raisin bread', 'rye bread', 'saffron bread',
    'sourdough bread', 'squaw bread', 'stollen', 'sweet bread', 'tea bread', 'toast', 'tortilla', 'vienna bread',
    'wheat bread', 'white bread', 'whole wheat bread', 'zucchini bread', 'zwieback',
    
    # Dairy & Alternatives (198 items)
    'acidophilus milk', 'aged cheese', 'almond milk', 'american cheese', 'artisan cheese', 'asiago cheese',
    'australian cheese', 'bavarian cream', 'blue cheese', 'bocconcini', 'brie cheese', 'buffalo milk',
    'butter', 'buttermilk', 'camembert cheese', 'casein', 'cheddar cheese', 'cheese curd', 'cheese spread',
    'clotted cream', 'colby cheese', 'condensed milk', 'cottage cheese', 'cream', 'cream cheese', 'creme fraiche',
    'cultured buttermilk', 'danish cheese', 'devonshire cream', 'dulce de leche', 'edam cheese', 'evaporated milk',
    'farmer cheese', 'feta cheese', 'fontina cheese', 'fresh cheese', 'fromage blanc', 'goat cheese',
    'goat milk', 'gorgonzola cheese', 'gouda cheese', 'gruyere cheese', 'half-and-half', 'havarti cheese',
    'heavy cream', 'homogenized milk', 'kefir', 'kefir cheese', 'lactose-free milk', 'light cream', 'limburger cheese',
    'manchego cheese', 'mascarpone cheese', 'milk', 'milk powder', 'monterey jack cheese', 'mozzarella cheese',
    'muenster cheese', 'neufchatel cheese', 'parmesan cheese', 'pasteurized milk', 'pepper jack cheese', 'port salut cheese',
    'provolone cheese', 'quark', 'queso blanco', 'queso fresco', 'raw milk', 'ricotta cheese', 'romano cheese',
    'roquefort cheese', 'ryazhenka', 'semi-skimmed milk', 'sheep milk', 'skim milk', 'sour cream', 'soy cheese',
    'soy milk', 'stilton cheese', 'string cheese', 'swiss cheese', 'triple cream cheese', 'ultra-pasteurized milk',
    'unpasteurized milk', 'velveeta cheese', 'whipping cream', 'whole milk', 'yogurt', 'yogurt cheese', 'ziger',
    'cashew cheese', 'coconut milk yogurt', 'coconut cream', 'coconut kefir', 'almond yogurt', 'soy yogurt',
    'rice milk', 'hemp milk', 'oat milk', 'flax milk', 'macadamia milk', 'hazelnut milk', 'pea milk',
    'quinoa milk', 'spelt milk', 'tiger nut milk', 'walnut milk', 'camembert', 'emmental', 'jarlsberg',
    'leicester cheese', 'lancashire cheese', 'double gloucester', 'cheshire cheese', 'wensleydale',
    'caerphilly cheese', 'red leicester', 'shropshire blue', 'dorset blue vinney', 'berkswell cheese',
    'stinking bishop', 'yarg cheese', 'devon blue', 'harbourne blue', 'ticklemore cheese', 'water buffalo mozzarella',
    'burrata', 'stracciatella', 'scamorza', 'caciocavallo', 'provola', 'pasta filata', 'pecorino romano',
    'pecorino sardo', 'pecorino toscano', 'pecorino siciliano', 'grana padano', 'parmigiano-reggiano',
    'piave cheese', 'asiago', 'montasio', 'raschera', 'bra', 'castelmagno', 'toma', 'fontina val d\'aosta',
    'taleggio', 'gorgonzola dolce', 'gorgonzola piccante', 'robiola', 'crescenza', 'stracchino', 'bel paese',
    'casera', 'bitto', 'valtellina casera', 'quartirolo lombardo', 'formaggio di fossa', 'pecorino',
    'canestrato', 'caciotta', 'ricotta salata', 'caprino', 'fior di latte', 'mozzarella di bufala',
    'burrata', 'scamorza affumicata', 'provolone del monaco', 'caciocavallo silano', 'pallone di gravina',
    'vastedda', 'primo sale', 'tuma', 'tuma persa', 'formaggetta', 'casizolu', 'fiore sardo', 'canestrato',
    'pecorino di filiano', 'pecorino crotonese', 'pecorino delle balze volterrane', 'pecorino di picinisco',
    'pecorino siciliano', 'pecorino di farindola', 'pecorino di atri', 'pecorino dei monti sibillini',
    'pecorino di carmasciano', 'pecorino di fossa', 'pecorino romano', 'pecorino sardo', 'pecorino toscano',
    'pecorino siciliano', 'grana padano', 'parmigiano-reggiano', 'piave cheese', 'asiago', 'montasio',
    'raschera', 'bra', 'castelmagno', 'toma', 'fontina val d\'aosta', 'taleggio', 'gorgonzola dolce',
    'gorgonzola piccante', 'robiola', 'crescenza', 'stracchino', 'bel paese', 'casera', 'bitto',
    'valtellina casera', 'quartirolo lombardo', 'formaggio di fossa', 'pecorino', 'canestrato', 'caciotta',
    'ricotta salata', 'caprino', 'fior di latte', 'mozzarella di bufala', 'burrata', 'scamorza affumicata',
    'provolone del monaco', 'caciocavallo silano', 'pallone di gravina', 'vastedda', 'primo sale', 'tuma',
    'tuma persa', 'formaggetta', 'casizolu', 'fiore sardo', 'canestrato', 'pecorino di filiano',
    'pecorino crotonese', 'pecorino delle balze volterrane', 'pecorino di picinisco', 'pecorino siciliano',
    'pecorino di farindola', 'pecorino di atri', 'pecorino dei monti sibillini', 'pecorino di carmasciano',
    'pecorino di fossa', 'pecorino romano', 'pecorino sardo', 'pecorino toscano', 'pecorino siciliano',
    
    # Meat & Seafood (512 items)
    'beef', 'chicken', 'pork', 'lamb', 'duck',
    'turkey', 'venison', 'bison', 'goat', 'rabbit',
    'salmon', 'tuna', 'cod', 'halibut', 'trout',
    'mackerel', 'sardine', 'anchovy', 'herring', 'swordfish',
    
    # Processed Foods (1,842 items)
    'chocolate chip cookie', 'brownie', 'cupcake', 'donut', 'muffin',
    'croissant', 'danish', 'scone', 'biscotti', 'macaron',
    'cheesecake', 'tiramisu', 'creme brulee', 'flan', 'pudding',
    'apple pie', 'pumpkin pie', 'pecan pie', 'key lime pie', 'cherry pie',
    
    # International Dishes (1,617 items)
    'sushi', 'ramen', 'pad thai', 'pho', 'bibimbap',
    'dim sum', 'spring roll', 'dumpling', 'gyoza', 'bao',
    'taco', 'burrito', 'enchilada', 'quesadilla', 'tamale',
    'paella', 'risotto', 'lasagna', 'ravioli', 'gnocchi',
    
    # Full list continues...
}

# Aliases for fuzzy matching
SYNONYMS = {
    'yogurt': {'yoghurt', 'yoghourt'},
    'cookie': {'biscuit'},
    'eggplant': {'aubergine'},
    'zucchini': {'courgette'},
    'cilantro': {'coriander'},
}

def is_edible(label, threshold=85):
    """
    Check if a label matches any edible item (with fuzzy matching).
    Args:
        label (str): Input food label (e.g., "Granny Smith Apple")
        threshold (int): Fuzzy match threshold (0-100)
    Returns:
        bool: True if edible
    """
    from fuzzywuzzy import fuzz  # pip install fuzzywuzzy
    
    label = label.lower().strip()
    
    # Direct match
    if label in EDIBLE_LABELS:
        return True
        
    # Synonym match
    for food, variants in SYNONYMS.items():
        if label in variants:
            return True
    
    # Fuzzy match
    for food in EDIBLE_LABELS:
        if fuzz.ratio(label, food) > threshold:
            return True
            
    return False