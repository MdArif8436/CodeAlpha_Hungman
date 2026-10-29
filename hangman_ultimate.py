

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Optional


# Each entry is (secret_word, hint). Words use English letters only so that
# guesses can be validated simply and consistently.
WORD_BANK: dict[str, list[tuple[str, str]]] = {
    "Animals": [
        ("elephant", "A very large land mammal with a trunk."),
        ("giraffe", "The tallest living land animal."),
        ("penguin", "A flightless bird that is an excellent swimmer."),
        ("dolphin", "An intelligent marine mammal known for its clicks."),
        ("kangaroo", "An Australian animal that hops and has a pouch."),
        ("crocodile", "A large reptile with powerful jaws."),
        ("butterfly", "An insect that begins life as a caterpillar."),
        ("octopus", "A sea animal with eight arms."),
        ("leopard", "A spotted big cat known for climbing."),
        ("hamster", "A small pet rodent that stores food in its cheeks."),
        ("flamingo", "A long-legged bird often known for its pink colour."),
        ("squirrel", "A bushy-tailed animal that often collects nuts."),
        ("rhinoceros", "A large animal with one or two horns on its snout."),
        ("cheetah", "The fastest land animal over short distances."),
        ("hedgehog", "A small mammal covered in protective spines."),
        ("tortoise", "A slow-moving reptile with a protective shell."),
        ("gorilla", "A powerful great ape native to African forests."),
        ("peacock", "A bird famous for the male's colourful tail display."),
        ("whale", "A huge marine mammal that breathes air."),
        ("wolf", "A wild canine that often lives and hunts in a pack."),
    ],
    "Food": [
        ("pineapple", "A tropical fruit with a spiky outer skin."),
        ("watermelon", "A large fruit with a green rind and watery red flesh."),
        ("strawberry", "A red fruit with tiny seeds on its outside."),
        ("sandwich", "Food made by placing a filling between pieces of bread."),
        ("pancake", "A flat breakfast food cooked in a pan."),
        ("chocolate", "A sweet food made from cocoa."),
        ("noodles", "Long strands of food often served in soup or sauce."),
        ("dumpling", "A small piece of dough that may contain a filling."),
        ("potato", "A starchy vegetable often used to make fries."),
        ("carrot", "An orange root vegetable often associated with rabbits."),
        ("broccoli", "A green vegetable with a tree-like shape."),
        ("omelette", "A dish made by cooking beaten eggs in a pan."),
        ("biscuit", "A small baked snack; the meaning varies by country."),
        ("yogurt", "A creamy food made by fermenting milk."),
        ("cheese", "A dairy food made from curdled milk."),
        ("popcorn", "A snack made from heated corn kernels."),
        ("burger", "A sandwich often made with a round bun and a patty."),
        ("mango", "A sweet tropical fruit with a large flat seed."),
        ("papaya", "A tropical fruit with orange flesh and black seeds."),
        ("coconut", "A tropical fruit with a hard shell and white flesh."),
    ],
    "Nature": [
        ("mountain", "A very high natural elevation of land."),
        ("waterfall", "Water that drops vertically over a cliff or ledge."),
        ("forest", "A large area covered mainly with trees."),
        ("desert", "A very dry region that receives little precipitation."),
        ("volcano", "An opening in Earth's crust that can release lava."),
        ("rainbow", "A colourful arc that can appear after rain."),
        ("thunder", "The sound caused by lightning."),
        ("lightning", "A bright electrical discharge in the atmosphere."),
        ("glacier", "A large, slowly moving mass of ice."),
        ("island", "Land completely surrounded by water."),
        ("ocean", "A vast body of salt water."),
        ("river", "A natural stream of flowing water."),
        ("meadow", "An open field of grass and wildflowers."),
        ("canyon", "A deep valley with steep sides."),
        ("rainforest", "A dense forest that receives abundant rainfall."),
        ("earthquake", "Sudden shaking of the ground."),
        ("breeze", "A light, gentle wind."),
        ("tornado", "A violently rotating column of air."),
        ("sunlight", "Light that comes from the Sun."),
        ("starlight", "Light that reaches us from stars."),
    ],
    "Technology": [
        ("computer", "An electronic machine that processes information."),
        ("keyboard", "A device used to type letters and commands."),
        ("monitor", "A screen used to display computer output."),
        ("internet", "A worldwide network connecting computers."),
        ("software", "Programs and instructions used by a computer."),
        ("hardware", "The physical parts of a computer system."),
        ("firewall", "A security system that filters unwanted network traffic."),
        ("smartphone", "A mobile phone with advanced computing features."),
        ("bluetooth", "A short-range wireless communication technology."),
        ("robot", "A machine that can perform tasks automatically."),
        ("satellite", "An object that orbits a planet or another body."),
        ("touchpad", "A touch-sensitive surface used to control a computer pointer."),
        ("password", "A secret string used to verify access."),
        ("download", "To receive a file from another system."),
        ("website", "A collection of related pages on the internet."),
        ("browser", "An application used to view websites."),
        ("wireless", "Communicating without a physical cable."),
        ("microchip", "A tiny electronic circuit built on a small piece of material."),
        ("processor", "The computer component that executes instructions."),
        ("encryption", "The process of turning data into coded information."),
    ],
    "Programming": [
        ("python", "A popular programming language named after a comedy group."),
        ("variable", "A named place used to store a value in a program."),
        ("function", "A reusable block of code that performs a task."),
        ("algorithm", "A step-by-step method for solving a problem."),
        ("compiler", "A tool that translates source code into another form."),
        ("debugging", "Finding and fixing errors in a program."),
        ("iteration", "Repeating a set of instructions."),
        ("recursion", "A technique where a function calls itself."),
        ("integer", "A whole number that has no fractional part."),
        ("boolean", "A data type with true and false values."),
        
        ("debugger", "A tool used to inspect code and find software errors."),
        ("functionality", "The set of actions or features something provides."),
        ("javascript", "A programming language widely used for web development."),
        ("typescript", "A typed programming language built on JavaScript."),
        ("repository", "A place where project files and version history are stored."),
        ("terminal", "A text-based interface for entering commands."),
        ("framework", "A reusable foundation for building software."),
        ("exception", "An event that interrupts normal program execution."),
        ("parameter", "An input named in a function definition."),
        ("syntax", "The rules that define valid code structure."),
    ],
    "Space": [
        ("astronaut", "A person trained to travel and work in space."),
        ("quasar", "An extremely bright distant object powered by material around a black hole."),
        ("galaxy", "A huge system of stars, gas, and dust."),
        ("planet", "A large body that orbits a star."),
        ("asteroid", "A small rocky body orbiting the Sun."),
        ("comet", "An icy object that can develop a glowing tail near the Sun."),
        ("meteor", "A streak of light produced as space material enters an atmosphere."),
        ("nebula", "A large cloud of gas and dust in space."),
        ("gravity", "The attraction between objects that have mass."),
        ("universe", "All of space, time, matter, and energy."),
        ("orbit", "The path one object takes around another."),
        ("eclipse", "An event where one celestial body blocks another."),
        ("moonlight", "Sunlight reflected from the Moon."),
        ("cosmos", "Another word for the universe."),
        ("spaceship", "A vehicle designed for travel beyond Earth."),
    ],
    "Countries": [
        ("india", "A country in South Asia."),
        ("canada", "A large country in North America."),
        ("brazil", "The largest country in South America."),
        ("japan", "An island country in East Asia."),
        ("australia", "A country and continent in the Southern Hemisphere."),
        ("nepal", "A Himalayan country north of India."),
        ("bhutan", "A Himalayan kingdom known for its mountains."),
        ("france", "A European country whose capital is Paris."),
        ("germany", "A European country whose capital is Berlin."),
        ("italy", "A European country shaped like a boot on the map."),
        ("kenya", "An East African country known for wildlife and savannas."),
        ("egypt", "A North African country famous for ancient pyramids."),
        ("mexico", "A country south of the United States."),
        ("thailand", "A Southeast Asian country formerly known as Siam."),
        ("singapore", "A city-state in Southeast Asia."),
        ("pakistan", "A country in South Asia."),
        ("maldives", "An island country in the Indian Ocean."),
        ("argentina", "A South American country famous for tango and football."),
        ("norway", "A Nordic country known for fjords."),
        ("spain", "A European country on the Iberian Peninsula."),
    ],
    "Sports": [
        ("football", "A team sport played with a ball and goals."),
        ("cricket", "A bat-and-ball sport popular in India."),
        ("badminton", "A racket sport played with a shuttlecock."),
        ("basketball", "A sport where players try to score through a high hoop."),
        ("volleyball", "A team sport where players hit a ball over a net."),
        ("swimming", "Moving through water using the body."),
        ("athletics", "Track and field events such as running and jumping."),
        ("gymnastics", "A sport involving strength, balance, and flexibility."),
        ("wrestling", "A combat sport involving grappling techniques."),
        ("hockey", "A team sport played with sticks and a ball or puck."),
        ("tennis", "A racket sport played across a net."),
        ("cycling", "Riding a bicycle, often as a sport."),
        ("archery", "A sport that involves shooting arrows at a target."),
        ("marathon", "A long-distance running race of about 42 kilometres."),
        ("skating", "Gliding on skates over a surface or ice."),
    ],
    "Everyday": [
        ("backpack", "A bag carried on your back with shoulder straps."),
        ("umbrella", "An object used to shield you from rain or sun."),
        ("calendar", "A chart or system that organises days and months."),
        ("bedroom", "A room used mainly for sleeping."),
        ("window", "An opening in a wall that often lets in light."),
        ("doorbell", "A device that alerts someone when a visitor arrives."),
        ("notebook", "A book of blank or lined pages for writing."),
        ("scissors", "A tool with two blades used for cutting."),
        ("bicycle", "A two-wheeled vehicle powered by pedalling."),
        ("bottle", "A container commonly used to hold liquids."),
        ("pillow", "A soft cushion used to support your head."),
        ("blanket", "A warm covering used on a bed."),
        ("kitchen", "A room where meals are prepared."),
        ("mirror", "A surface that reflects an image."),
        ("wallet", "A small item used to carry money and cards."),
        ("keychain", "An item that keeps keys together."),
        ("toothbrush", "A tool used to clean your teeth."),
        ("refrigerator", "An appliance that keeps food cold."),
        ("headphones", "A device worn over or in the ears to hear audio."),
        ("flashlight", "A portable light powered by batteries or a rechargeable cell."),
    ],
    "Science": [
        ("molecule", "Two or more atoms chemically bonded together."),
        ("oxygen", "A gas needed by most humans for respiration."),
        ("hydrogen", "The lightest chemical element."),
        ("supernova", "A powerful explosion that marks the end of certain stars."),
        ("photosynthesis", "The process plants use to convert light into chemical energy."),
        ("electricity", "A form of energy associated with electric charge."),
        ("magnetism", "A physical phenomenon involving magnetic fields."),
        ("bacteria", "Microscopic single-celled organisms."),
        ("inertia", "The tendency of an object to resist a change in its motion."),
        ("microscope", "An instrument used to view very small objects."),
        ("ecosystem", "Living things interacting with each other and their environment."),
        ("voltage", "The electrical potential difference between two points."),
        ("friction", "A force that resists motion between surfaces."),
        ("evaporation", "The change from a liquid into a gas."),
        ("condensation", "The change from a gas into a liquid."),
        ("atom", "The basic unit of a chemical element."),
        ("neutron", "A subatomic particle with no electric charge."),
        ("evolution", "The change in inherited traits in populations over generations."),
        ("habitat", "The natural home of an organism."),
        ("mineral", "A naturally occurring inorganic solid."),
    ],
    "Music": [
        ("guitar", "A string instrument often played by strumming or plucking."),
        ("piano", "A keyboard instrument with strings struck by hammers."),
        ("violin", "A small, high-pitched string instrument played with a bow."),
        ("rhythm", "The pattern of beats in music."),
        ("melody", "A sequence of musical notes that forms a tune."),
        ("concert", "A live performance of music for an audience."),
        ("drummer", "A musician who plays percussion instruments."),
        ("trumpet", "A brass instrument with a bright sound."),
        ("flute", "A wind instrument played by blowing across an opening."),
        ("singer", "A person who performs with their voice."),
        ("harmony", "Different musical notes played or sung together."),
        ("playlist", "A list of songs selected for playback."),
    ],
    "Transport": [
        ("airplane", "A powered aircraft with fixed wings."),
        ("helicopter", "An aircraft that uses rotating blades to fly."),
        ("submarine", "A vessel designed to travel underwater."),
        ("motorcycle", "A two-wheeled motor vehicle."),
        ("ambulance", "A vehicle used to transport people needing medical care."),
        ("locomotive", "A railway vehicle that pulls or pushes a train."),
        ("scooter", "A small two-wheeled vehicle, powered or unpowered."),
        ("sailboat", "A boat propelled mainly by wind in its sails."),
        ("highway", "A major public road for vehicles."),
        ("traffic", "Vehicles and movement on roads."),
        ("airport", "A place where aircraft take off and land."),
        ("railway", "A transport system using trains on tracks."),
        ("rickshaw", "A small passenger vehicle common in parts of Asia."),
        ("tramway", "A track-based urban transport system used by trams."),
    ],
}


# Supplemental word bank. Words are stored as plain lowercase strings here;
# build_word_bank() adds them to the original entries and supplies a useful
# category/first-letter/length hint for each extra word.
EXTRA_WORDS: dict[str, list[str]] = {
    "Animals": "badger beaver buffalo camel chimpanzee cougar falcon ferret gazelle hyena iguana jaguar koala lemur moose otter panther pelican porcupine raccoon sloth walrus wombat yak zebra".split(),
    "Food": "avocado blueberry cauliflower celery cinnamon croissant cucumber cupcake curry garlic ginger lasagna lentil lettuce macaroni marshmallow olive onion orange pretzel pumpkin radish raspberry spinach taco tofu vanilla walnut zucchini apricot plum raisin".split(),
    "Nature": "cliff coastline delta dune fern field flower foothill geyser hillside lagoon marsh oasis pebble plateau pond prairie reef ridge rock shore stream swamp valley vegetation".split(),
    "Technology": "adapter antenna application bandwidth battery chatbot database desktop device display encryption gadget graphics laptop modem motherboard network pixel platform router server spreadsheet touchscreen update username webpage processor".split(),
    "Programming": "array argument assignment attribute backend breakpoint callback class coding constant dictionary library module operator package recursion statement string syntax testing tuple debugging deployment variable boolean inheritance polymorphism exception".split(),
    "Space": "blackhole constellation crater extraterrestrial launchpad lunar mars rover planetarium pulsar rocket solar telescope astronaut cosmology asteroid meteoroid exoplanet stardust spacecraft supernova wormhole".split(),
    "Countries": "afghanistan algeria austria bangladesh belgium cambodia chile colombia croatia denmark ethiopia finland ghana greece indonesia ireland jamaica malaysia mongolia morocco myanmar nigeria portugal sweden switzerland vietnam".split(),
    "Sports": "baseball bowling boxing canoeing fencing handball hurdles javelin kayaking karate lacrosse rugby sprint surfing taekwondo triathlon umpire skiing snowboarding rowing diving polo".split(),
    "Everyday": "alarmclock armchair bathtub bookmark calendar candle charger clipboard curtain doormat drawer envelope eyeglasses faucet doorknob hammock ladder mailbox napkin stapler suitcase teapot tissue toothpaste vacuum zipper".split(),
    "Science": "acid alloy astronomy catalyst chromosome compound crystal density isotope laboratory laser microbe nucleus organism particle polymer protein radiation solvent spectrum isotope enzyme plasma sediment symbiosis telescope".split(),
    "Music": "accordion banjo cello clarinet cymbal harmony harmonica lyric orchestra percussion saxophone symphony tempo tenor ukulele vocalist xylophone chorus opera sonata bassoon mandolin metronome".split(),
    "Transport": "convertible ferry gondola minibus monorail paraglider pedestrian pickup quadcopter scooter sedan skateboard spacecraft tanker taxi tractor trolley van wagon yacht cablecar hovercraft".split(),
    "Weather": "blizzard cloud drizzle drought forecast hail humidity hurricane monsoon overcast rainfall sleet snowfall snowstorm sunshine temperature thunderstorm typhoon weather wind chill mist cyclone".split(),
    "Plants": "acorn bamboo blossom branch cactus clover daisy evergreen fern garden ivy jasmine lavender lotus maple orchid palm petal pine rose sequoia sunflower tulip willow".split(),
    "Insects": "ant aphid bee beetle cicada cockroach dragonfly firefly flea grasshopper hornet ladybug mosquito moth termite wasp weevil mantis caterpillar cricket mayfly".split(),
    "Clothing": "apron blazer blouse boots cardigan coat costume denim dress hoodie jacket jeans leggings overalls pajamas poncho scarf shirt shorts sweater tunic uniform vest".split(),
    "Careers": "architect artist baker carpenter cashier chef chemist dentist designer doctor electrician farmer firefighter florist journalist mechanic nurse painter pharmacist photographer pilot plumber scientist tailor teacher veterinarian".split(),
    "Buildings": "apartment barn cabin castle cathedral cottage courthouse factory farmhouse lighthouse mansion museum palace pavilion prison pyramid skyscraper stadium synagogue temple theater warehouse workshop".split(),
    "Geography": "archipelago bay basin border capital continent country equator estuary gulf hemisphere latitude longitude peninsula province region strait territory tropics tundra watershed coastline plateau".split(),
    "Emotions": "admiration amusement anger anxiety awe boredom calm confidence confusion delight disappointment embarrassment excitement fear gratitude grief hope jealousy joy loneliness pride relief sadness surprise wonder".split(),
    "Mathematics": "addition algebra angle arithmetic average calculus decimal denominator equation fraction geometry graph integer measure numerator percentage quotient radius subtraction theorem variable".split(),
    "Arts": "animation canvas carving collage comedy drawing gallery illustration portrait pottery sculpture sketch theatre watercolor charcoal mosaic mural printmaking portraiture".split(),
    "School": "alphabet backpack blackboard classroom classroom chalk classroom desk textbook homework lesson library notebook principal recess semester subject timetable worksheet syllabus diploma campus lecture".split(),
    "Travel": "adventure baggage boarding brochure campground destination excursion guidebook itinerary journey landmark luggage passport reservation resort souvenir suitcase tourism traveler vacation voyage".split(),
    "Ocean": "anchovy barnacle coral current eel kelp krill lobster manatee mussel narwhal plankton seahorse shrimp starfish stingray swordfish tuna urchin jellyfish seagrass anemone".split(),
    "Body": "ankle artery beard brain cheek chin elbow eyebrow eyelash forehead heel intestine kidney knee liver muscle nostril pancreas rib shoulder skeleton stomach tendon wrist".split(),
    "Mythology": "apollo artemis athena atlas cerberus centaur cyclops demeter hades hercules hermes medusa minerva minotaur odyssey olympus pegasus poseidon siren zeus phoenix".split(),
    "History": "ancient artifact dynasty empire explorer fortress invention kingdom monument pioneer revolution treaty civilization emperor historian medieval parliament republic renaissance".split(),
    "Fantasy": "alchemy amulet barbarian cauldron dragon elf enchantment fairy goblin griffin guardian wizard knight magic mermaid oracle phoenix potion spell unicorn vampire sorcerer".split(),
    "Kitchen": "blender colander cooker crockery grater kettle ladle microwave mixer oven peeler platter saucepan spatula stove strainer toaster tongs whisk wok saucepan".split(),
    "Furniture": "bookcase cabinet chair cupboard desk dresser futon headboard ottoman recliner rockingchair shelf sideboard sofa stool table wardrobe workbench bench".split(),
    "Colors": "amber beige crimson cyan emerald indigo ivory lavender magenta maroon navy ochre olive orange peach pink purple scarlet silver turquoise violet yellow".split(),
    "Tools": "anvil axe chisel clamp drill file hammer level mallet pliers rake saw screwdriver shovel spanner trowel wrench crowbar hacksaw sander tape measure".split(),
    "Literature": "allegory anthology author biography chapter character fiction folklore fable genre haiku legend novel narrator poetry prose quotation romance satire sonnet thriller tragedy".split(),
    "Games": "arcade checkers chess controller dominoes dungeon esports joystick mahjong maze monopoly multiplayer puzzle quest riddle solitaire strategy sudoku tabletop tournament trivia".split(),
    "Vehicles": "sedan hatchback limousine roadster buggy carriage chariot forklift go-kart hearse jetliner moped scooter tram truck unicycle wagon snowmobile hovercraft".split(),
}


MEGA_WORDS: dict[str, list[str]] = {
    "Animals": """
    alligator alpaca anaconda antelope baboon barracuda bat bear blackbird boar bobcat budgie buffalo cardinal carp catfish chameleon cobra coyote crane crow deer dingo eagle eel egret emu gecko gerbil gibbon goldfish goose grouse guppy hawk ibis jackal lion lizard llama macaw magpie meerkat mink mole mongoose monkey newt orca ostrich ox parrot partridge piranha platypus possum puma quail rabbit ram raven reindeer robin salamander salmon seal shark sheep skunk sparrow spider squid stork swan thrush turkey viper vulture weasel wildcat wolverine woodpecker orangutan chimpanzee baboon
    """.split(),
    "Food": """
    almond apple barley basil beef beetroot bread brownie cabbage cake caper cashew cereal cherry chickpea chilli chips chutney cocoa cookie corn couscous cracker cranberry cream date doughnut eggplant fig fish flour guava honey hummus icecream jam juice kiwi lemon lime lychee millet muesli mushroom mustard parsley pasta pear peanut pecan pepper pickle pie pizza pomegranate porridge prawn pudding quinoa rice rosemary salt sausage sesame soup soy spice squash sugar syrup tea toast tomato turmeric turnip vinegar waffle wheat yam aubergine bagel burrito falafel goulash granola kebab kimchi pancake ravioli risotto sorbet sushi taco tortilla
    """.split(),
    "Nature": """
    avalanche badlands bayou bluff bog boulder branch brook brush canopy cave cavern cliff clover creek crevice crystal current delta driftwood dune farmland fissure fjord floodplain foothill fossil geyser gorge grove harbor heath iceberg inlet jungle knoll lagoon landslide ledge lowland mangrove mesa moor mudslide oasis outcrop pasture peak peninsula prairie ravine reservoir ridge riverbank rockslide savanna shoal sinkhole slope springstone summit thicket tidepool timberland treeline tributary undergrowth upland watershed wetland woodland
    """.split(),
    "Technology": """
    actuator algorithmic android antivirus appliance automation avatar backup barcode biometrics bitbucket blockchain bookmark camera capacitor cellphone chipset circuit clipboard cloud computing codec cursor cybercrime cyberspace dashboard dataport device driver digitizer dongle email emulator ethernet firmware font scanner hotspot hyperlink icon input interface intranet joystick kiosk motherboard mousepad nanobot notebook operating operating system optical keypad peripheral phishing podcast protocol quantum computing scanner screenshot searchengine sensor simulator smartwatch socialmedia socket serverless smartwatch touchscreen trackpad transistor upload userinterface virtual reality webcam widget wifi workstation wearable
    """.split(),
    "Programming": """
    abstraction agile argument arithmetic assertion asynchronous bitwise branch bytecode casing closure commit condition container coroutine database dependency deployment deque destructor encapsulation endpoint enumeration event expression iterator flag frontend generator git graph handler hashmap heap integration keyword lambda linkedlist linting loop metaclass middleware namespace object operand optimization output override parser pipeline pointer procedure property queue recursion refactor regression release runtime sandbox schema script semaphore serializer shell singleton stack syntaxerror testcase token transpiler unit test validation value variable vector versioning virtualenv webhook
    """.split(),
    "Space": """
    aphelion astronomy astronautical barycenter celestial chromosphere cosmonaut cratered darkmatter docking dwarfstar exoplanet galactic heliosphere interstellar ionosphere launch lunar lunation magnetosphere microgravity multiverse observatory occultation planetarium planetary probe radiationbelt redshift retrograde satellite solarflare solstice spacewalk spacetime starcluster starship stratosphere terminator thermosphere ultraviolet vacuum vaporwave vernal vortex zenith zodiacal astrometry blackhole eventhorizon lightyear moonbase moonstone moonwalker orbiting perihelion photosphere quasarion radiometer rocketship spacelab spaceport starfield supercluster telescope transit universe
    """.split(),
    "Countries": """
    angola armenia bahamas barbados belarus belize benin bolivia botswana bulgaria burundi cameroon chad comoros congo cuba cyprus djibouti dominica ecuador eritrea estonia fiji gabon gambia georgia grenada guatemala guinea guyana haiti honduras hungary iceland iran iraq israel ivorycoast jordan kazakhstan kuwait kyrgyzstan laos latvia lebanon lesotho liberia libya lithuania luxembourg madagascar malawi mali malta mauritania mauritius moldova monaco montenegro mozambique namibia nicaragua niger oman panama paraguay peru philippines poland qatar romania rwanda samoa senegal serbia seychelles slovakia slovenia somalia suriname syria taiwan tajikistan tanzania togo tonga tunisia turkey turkmenistan uganda ukraine uruguay uzbekistan vanuatu venezuela yemen zambia zimbabwe
    """.split(),
    "Sports": """
    aerobics backstroke biathlon billiards bodybuilding bobsled bodybuilding breakdance broomball climbing croquet curling decathlon discus duathlon endurance equestrian esports eventing fieldhockey figure skating freestyle futsal goalkeeping hammerthrow highjump horseback icehockey inline skating judo kickboxing longjump pentathlon pickleball powerlifting racquetball relay running shotput skateboard slalom softball speedskating steeplechase sumo tabletennis teamhandball waterskiing weightlifting windsurfing zorbing mountaineering parkour pilates powerboat racing racewalking rowing rugby league sailing scuba diving shooting shuffleboard snooker squash strongman synchronized swimming trampoline ultimate frisbee waterpolo weightlifting
    """.split(),
    "Everyday": """
    address adhesive airtag album ashtray awning badge basket battery belt bin blanketbox boardgame bolt bowl broom bucket button calculator canister carpet cellphone chain chalk clock coaster comb compass container cork cushion detergent diary dishcloth doormat dustpan earbud eraser extension cord fan folder frame funnel gloves grocery hamper hanger handkerchief jar jug lantern lock lunchbox magnet marker matchbox measuringtape memo mug package padlock pan paperclip parcel pen pencil picture pin plug postcard purse razor remote remotecontrol ribbon ring ruler scarf sealant soap sponge spoon string sunglasses switch tablet tag towel tray tripod tumbler tissuebox toolbox timer tissuepaper wallet watch whistle
    """.split(),
    "Science": """
    acceleration antibody astronomy atomizer biochemistry buoyancy calorimeter capillary carbon catalyst centrifuge chemical chromatography cytoplasm decibel diffraction dissection distillation ecology electron electromagnet endocrinology energy entropy enzyme equilibrium fermentation filtration fluorescence force frequency genetics geology germination greenhouse gas hypothesis immunology indicator infrared ion kinetic isotope kinetics magnet meteorology microbiology neutron optics osmosis oxidation pathology pendulum periodicity petri quantum quark radiation reaction refraction relativity resistance resonance respiration seismology spectroscopy stimulus synthesis thermodynamics ultrasound valence viscosity wavelength
    """.split(),
    "Music": """
    alto arpeggio autoharp baritone beatbox blues brass cadence clarinetist composition concerto contralto counterpoint didgeridoo dynamics electricguitar encore falsetto fiddle finale folk song glockenspiel groove harpsichord hymn improvisation instrument jazz jingle kazoo keyboardist libretto lyricist mallet maraca medley mezzo soprano musicbox notation octave overture percussionist phonograph piccolo pitch polka prelude quartet recorder refrain reggae requiem riff rockabilly rondo scale serenade sitar solo soprano soundcheck soundtrack tambourine tuning ukulele virtuoso woodwind
    """.split(),
    "Transport": """
    airliner amphibian autorickshaw automobile barge biplane blimp boat bus cab caboose camelcart cargo catamaran coach container ship cruiser dinghy dragster droshky dumper ferryboat fireengine freight glider gondola handcar hovercraft hydrofoil jet ski jumbojet kayak limousine lifeboat longboat moped passenger ship patrolboat pedicab punt raft roadster sailplane schooner seaplane sedan ship steamboat streetcar tanker towtruck trawler trolleybus tugboat turboprop vanpool wagonette watercraft yacht zeppelin
    """.split(),
    "Weather": """
    anemometer anticyclone atmospheric barometer breezelet cloudburst cloudless coldfront dewpoint downpour duststorm easterly flurry fogbank freeze frostbite frostline gust heatwave icepellet jetstream lightningstorm lowpressure microburst misty northerly precipitation pressure cyclone raincloud raindrop rainstorm sandstorm sea breeze snowflake squall storm surge sultriness temperature inversion tradewind updraft vapor visibility warmfront waterspout west wind windstorm windward windchill windspeed
    """.split(),
    "Plants": """
    aloe amaranth anemone applewood arbor azalea beech begonia bindweed birch bluebell bonsai bramble briar bromeliad buttercup camellia carnation cassava cedar chicory chrysanthemum citron citronella conifer coriander cottonwood crocus currant dahlia dandelion dogwood elderberry eucalyptus fennel figtree freesia geranium ginkgo gladiolus honeysuckle hyacinth hydrangea juniper kapok larch lilac magnolia marigold mimosa mulberry narcissus nettle nutmeg oregano papyrus periwinkle poppy privet quince redwood rhododendron saffron sage sandalwood snapdragon sorghum spearmint spruce tamarind thyme hemlock yew
    """.split(),
    "Insects": """
    antlion armyworm bedbug beeetle bollworm butterflyfish booklouse botfly bristletail bumblebee butterfly beetlebug clickbeetle caddisfly dobsonfly earwig emeraldashborer ensignwasp fruitfly gallwasp glowworm gnat grig katydid lacewing leafhopper locust longhorn mantid mealworm mealybug mayfly molecricket muddauber paperwasp planthopper robberfly sawfly scaleinsect silverfish skimmer stickinsect stonefly swallowtail tsetsefly walkingstick waterbug waterstrider whitefly woollybear yellowjacket
    """.split(),
    "Clothing": """
    anklet ascot balaclava bandana bathing suit bathrobe beanie belt buckle beret bikini camisole cap cape cloak clogs coveralls cravat crinoline culottes cummerbund dressshirt earmuffs espadrilles gaiters galoshes garter gilet gown headband headscarf kimono kilt loincloth mittens moccasins necktie nightgown overcoat petticoat polo shirt pullover raincoat romper sandals sash shawl sneakers swimsuit tights topcoat tracksuit trunks turban turtleneck windbreaker
    """.split(),
    "Careers": """
    accountant actor actuary animator archaeologist astronaut auditor beekeeper biologist bookkeeper botanist brewer broadcaster cardiologist caregiver coach curator dataanalyst economist editor engineer epidemiologist geographer geologist illustrator interpreter investigator investor librarian lifeguard linguist locksmith magistrate mathematician meteorologist midwife model monk navigator negotiator optician paramedic pastrychef playwright podcaster poet politician professor psychologist radiologist researcher sailor sculptor statistician surgeon translator usher undertaker urbanplanner webdeveloper welder zoologist
    """.split(),
    "Buildings": """
    abbey arcade armory barracks basilica bathhouse bell tower boathouse bodega brewery bungalow casino citadel clubhouse conservatory dormitory embassy observatory orphanage outbuilding pagoda parsonage penitentiary planetarium playhouse rectory refinery retreat sanatorium sanctuary schoolhouse seminary shelter shipyard shrine silo smithy spa storehouse substation townhouse towerhouse trellis villa windmill winery ziggurat amphitheater arena courthouse depot greenhouse inn manor monastery mosque motel office orphanage outpost powerhouse stable synagogue
    """.split(),
    "Geography": """
    altitude archway atoll badland basin bedrock canyonland catchment channel cliffside confluence cordillera escarpment floodplain foothill headland hinterland highland lowland meander mountainrange plain promontory shoreline watershed isthmus landform seaboard seamount seaway seiche saltflat sandbar seashore snowfield steppe subcontinent subduction trench topography valleyfloor volcanic arc volcano vent watercourse waterway islandchain islandarc riverdelta riverbed ridgeback riftvalley mountainpass coastline plainland
    """.split(),
    "Emotions": """
    acceptance affection agitation alienation anticipation apathy appreciation assertiveness contentment courage curiosity despair determination disappointment dismay distrust eagerness ecstasy elation empathy envy exasperation exhilaration frustration fulfillment fury generosity gloom guilt happiness hostility humiliation impatience insecurity inspiration irritation kindness longing melancholy nostalgia optimism passion perplexity pessimism serenity shame sympathy tenderness tolerance trust uncertainty enthusiasm
    """.split(),
    "Mathematics": """
    abacus absolute algebraic amplitude asymptote axiom binomial coefficient commutative composite congruence coordinate corollary cylinder divisor dividend exponent exponential factorial functionary polynomial hypotenuse inequality logarithm matrix median modulus multiple multiplicand multiplier parabola parallel permutation pi plane polygon prime probability proportion pyramid quadrilateral quotient random radius ratio remainder rhombus sequence series sine sphere square root statistics tangent trigonometry theorem variable vector vertex volume
    """.split(),
    "Arts": """
    abstract acrylic airbrush assemblage ballet calligraphy caricature ceramics choreography cinematography claycraft colorist concept art contemporary craft dance decoupage design diorama engraving expressionism filmography fresco graffiti graphic art impressionism installation landscape lithography realism manuscript miniature modernism monotype oil painting origami pastel performance photogram photography pixelart popart realism relief art renaissance rendering screenprint stilllife storyboard surrealism tapestry tattooing typography woodcut
    """.split(),
    "School": """
    academy attendance auditorium blackboard bookmark calculator campus certificate chemistry classmate college commencement composition dean degree detention dictionary elective examination faculty flashcard grade graduation handbook headmaster highlighter instructor journal kindergarten laboratory mathematics mentor module pedagogy pedagogue playground professor pupil registrar reportcard scholarship schoolbag schoolmate science fair seating seminar stationery student studygroup teacher trainee transcript tuition university valedictorian vocabulary
    """.split(),
    "Travel": """
    airfare backpacker backpacking berth booking cabincrew carryon checkin commute customs daytrip departure excursionist expedition fare ferrying flight itinerary jetlag layover mapmaker motorway navigation overnight packing package tour pilgrimage platform porter railwaypass roadtrip roundtrip route sightseeing sleepercar stopover terminal ticketing timetable tourguide transfer transit travelogue trek trekking tripper tourist visa waiver wanderer wayfarer weekend getaway
    """.split(),
    "Ocean": """
    albatross algae amphipod anglerfish barracuda basketstar beachcomber bluewhale bottlenose brine bryozoan bycatch cuttlefish damselfish dugong fanworm fishery flatfish flyingfish haddock hagfish hammerhead harborseal hermitcrab horseshoe crab hydrothermal jellyfish kingcrab lanternfish limpet manta marlin monkfish moray narwhal nudibranch oyster pelagic penguinfish porpoise pufferfish remora rockfish sailfish scallop sea cucumber sea dragon sea lion sea otter sea turtle seaweed sponge squidfish triggerfish walrus warthog whale shark wrasse
    """.split(),
    "Body": """
    abdomen adductor adrenal alveoli bicep bladder blood cell bone marrow cartilage cerebellum cerebrum clavicle cochlea colon cornea diaphragm eardrum femur fibula gallbladder gland gluteus hamstring hippocampus humerus hypothalamus iris jaw joint larynx ligament lymph mandible medulla metatarsal molar pancreas patella pelvis phalanx pharynx retina scapula sinus sternum thyroid tibia trachea ulna ureter urethra vertebra villi vocalcord
    """.split(),
    "Mythology": """
    achilles aegis aeolus aphrodite ares argonaut argus asgard banshee basilisk bragi calypso chimera clio dionysus dryad echo fenrir freya furies gaia gorgon griffin hel helen hephaestus hera hypnos janus jormungandr kraken lorelei loki lycaon morpheus muses nemesis nereid nymph odin osiris pandora persephone perseus prometheus ragnarok rhea satyr selene thor titan valkyrie vesta vulcan
    """.split(),
    "History": """
    abolitionist alliance armistice aristocracy archive armada baroque blockade bourgeoisie campaign colonist confederacy congress constitution coup crusader decolonization democracy diplomacy disarmament discovery document duchy electorate emancipation expedition feudalism founding genealogy imperialism industrialization insurgency legislature manifesto monarchy nationalism occupation parliamentarian patriotism plague plantation propaganda protectorate rebellion reconstruction referendum regime relic resistance revolutionist secession siege sovereignty suffrage uprising viceroy warlord
    """.split(),
    "Fantasy": """
    adventurer banshee battlemage beastmaster changeling conjurer cryptid darklord demonology druid dweller familiar firebird fleshgolem frostgiant gargoyle genie golem halfelf hobbit homunculus hydra illusionist imp infernal kelpie lich lorekeeper lycanthrope necromancer nightelf nightshade paladin poltergeist shapeshifter shaman shapeshifter sorcery spellbook sprite succubus sylph warlock werewolf wight wraith yeti wyrm wyvern
    """.split(),
    "Kitchen": """
    airfryer bainmarie bakingtray baster breadbox breadmaker cakepan canopener casserole cleaver coffeegrinder coffeemaker cooktop coolingrack cuttingboard dishpan dutchoven eggbeater eggcup espresso filterware foodprocessor freezer fryingpan garlicpress icebucket icecream maker juicer mandoline measuringcup measuringjug mixingbowl muffinpan nutcracker pastrybrush pieplate pizzacutter pressurecooker ricecooker rollingpin saladspinner scale skimmer slowcooker steamer stockpot thermos timer tupperware utensil vegetablepeeler waffleiron zester
    """.split(),
    "Furniture": """
    bedstead bedside cabinet benchseat buffet bunkbed credenza daybed diningtable footboard footrest fourposter futon glasscabinet hutch loveseat mattress mantel nightstand piano bench platformbed pouf ottoman rack secretary settee shoe rack sidechair sleeper sofa sofa bed standingdesk stepstool sunlounger tableleaf tea trolley trunk vanity wallunit writingdesk upholstered chaise longue barstool coatstand credence credenza credenza
    """.split(),
    "Colors": """
    aquamarine auburn azure burgundy cerulean chartreuse chocolate cobalt coral copper ecru fuchsia gold gray green heliotrope lilac lime ocher opal pewter plum russet saffron sapphire sepia sienna slate taupe vermilion wine white black bronze charcoal flax indigo jade khaki lemon lilac mauve mint ochre umber
    """.split(),
    "Tools": """
    awl barrow boltcutters brace bradawl brushcarver caulking chiselbit compasssaw countersink crowbar cutter deburrer drawknife drillbit filetool fret saw gouge hacksaw hammerhead handplane hatchet hedgecutter hexkey honingstone jackhammer jigsaw keyhole saw lathe mallet masonrybit nailgun nailset plane plumbbob prybar punch reamer riveter router scribe scraper sharpeningstone solderingiron spokeshave staplegun tap wrench threader tin snips torque wrench vise wirecutter
    """.split(),
    "Literature": """
    actant afterword aphorism audiobook autobiography ballad bibliography bildungsroman canon couplet criticism dramatic irony dramaturgy elegy epigram essay exposition fanzine flashfiction freeverse glossary libretto limerick memoir metaphor metonymy monologue mythology mythos novella ode onomatopoeia pamphlet parable parody pastiche penname personification plot point of view preface rhetoric rhyme rhyming scheme soliloquy stanza synopsis tercet thesis tone trope verse writing
    """.split(),
    "Games": """
    backgammon bagatelle boardgame capture cardgame charades co-op collectible crossword deckbuilder dodgeball escape room gamepad gamepiece gameplan gameplay geocaching hideandseek hopscotch immersive jigsaw labyrinth lanparty leaderboard levelup lootbox matchplay minigame MMORPG paintball partygame pinball platformer playthrough roleplay sandboxgame scavengerhunt speedrun tabletopgame tag team puzzle towerdefense videogame wordsearch wordplay
    """.split(),
    "Vehicles": """
    autogyro barouche beachbuggy bicyclecar boomtruck boxcar buckettruck bulldozer campervan caravel carpool carter carryall coupe crawler deliveryvan dumptruck earthmover electriccar flatbed fourwheeler hearse hotrod icebreaker interceptor jeep jitney kei car lorry mailvan motorhome offroader patrolcar roadroller snowplow sports car steamroller street sweeper towbar trailer truck tractor trailer tramway transitvan utilityvehicle wagon train wheelbarrow
    """.split(),
}

CATEGORY_HINTS: dict[str, str] = {
    "Animals": "Think of a living animal",
    "Food": "Think of something people eat or drink",
    "Nature": "Think of a feature or part of the natural world",
    "Technology": "Think of a modern device or digital technology",
    "Programming": "Think of a software development term",
    "Space": "Think of something connected with outer space",
    "Countries": "Think of a country or nation",
    "Sports": "Think of a sport or sporting term",
    "Everyday": "Think of a common item used in daily life",
    "Science": "Think of a scientific idea or object",
    "Music": "Think of a musical instrument or music term",
    "Transport": "Think of transportation or a way to travel",
    "Weather": "Think of a weather condition or atmospheric event",
    "Plants": "Think of a plant or a part of a plant",
    "Insects": "Think of a small invertebrate in the insect group",
    "Clothing": "Think of something a person might wear",
    "Careers": "Think of a job or profession",
    "Buildings": "Think of a building or built structure",
    "Geography": "Think of a geographical feature or location term",
    "Emotions": "Think of a feeling or emotional state",
    "Mathematics": "Think of a mathematical term",
    "Arts": "Think of an art form or creative technique",
    "School": "Think of something connected with education",
    "Travel": "Think of something useful for a trip or journey",
    "Ocean": "Think of marine life or an ocean-related term",
    "Body": "Think of a part or structure of the human body",
    "Mythology": "Think of a figure or concept from mythology",
    "History": "Think of a historical term or concept",
    "Fantasy": "Think of a fantasy creature or magical concept",
    "Kitchen": "Think of a tool or appliance used in a kitchen",
    "Furniture": "Think of an item of furniture",
    "Colors": "Think of a color name",
    "Tools": "Think of a tool used for making, fixing, or building things",
    "Literature": "Think of a literary form or reading-related term",
    "Games": "Think of a game or gaming term",
    "Vehicles": "Think of a type of vehicle",
}


def extend_word_bank() -> None:
    """Add supplemental words without duplicating any existing answer."""
    known = {
        word.casefold()
        for entries in WORD_BANK.values()
        for word, _hint in entries
    }
    # Add both the original supplement and the expanded word pack. The same
    # validation applies to every word so guesses and stored answers stay consistent.
    for supplemental_bank in (EXTRA_WORDS, MEGA_WORDS):
        for category, words in supplemental_bank.items():
            entries = WORD_BANK.setdefault(category, [])
            for raw_word in words:
                word = raw_word.strip().casefold()
                # Keep the word validator and answer bank consistent: A-Z only.
                if not word.isascii() or not word.isalpha() or word in known:
                    continue
                clue = CATEGORY_HINTS.get(category, f"Think of a word in {category}.")
                hint = f"{clue}. It begins with '{word[0].upper()}' and has {len(word)} letters."
                entries.append((word, hint))
                known.add(word)


extend_word_bank()

# Eight mistake stages provide a clear visual for Easy mode (8 mistakes).
HANGMAN_PICTURES = [
    r"""
  +---+
  |   |
      |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
    r"""
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
=========""",
    r"""
  +---+
  |   |
  [X] |
 /|\  |
 / \  |
      |
=========""",
]

DIFFICULTIES: dict[str, dict[str, int]] = {
    "Easy": {"max_mistakes": 8, "multiplier": 1},
    "Normal": {"max_mistakes": 6, "multiplier": 2},
    "Hard": {"max_mistakes": 4, "multiplier": 3},
}

STATS_FILE = Path(__file__).with_name("hangman_ultimate_stats.json")
DEFAULT_STATS: dict[str, int] = {
    "rounds_played": 0,
    "wins": 0,
    "losses": 0,
    "abandoned": 0,
    "total_score": 0,
    "current_streak": 0,
    "best_streak": 0,
    "valid_guesses": 0,
    "correct_guesses": 0,
}


def load_stats() -> dict[str, int]:
    """Load saved statistics, falling back safely if the file is missing or invalid."""
    try:
        saved = json.loads(STATS_FILE.read_text(encoding="utf-8"))
        if not isinstance(saved, dict):
            raise ValueError("Statistics file must contain a JSON object.")
        stats = DEFAULT_STATS.copy()
        for key in stats:
            value = saved.get(key, 0)
            # Avoid invalid types and negative counters from a damaged/manual file.
            stats[key] = max(0, int(value))
        return stats
    except FileNotFoundError:
        return DEFAULT_STATS.copy()
    except (OSError, json.JSONDecodeError, TypeError, ValueError):
        print("Note: saved statistics could not be read; starting with fresh stats.")
        return DEFAULT_STATS.copy()


def save_stats(stats: dict[str, int]) -> None:
    """Persist statistics without crashing the game if writing is unavailable."""
    try:
        STATS_FILE.write_text(
            json.dumps(stats, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except OSError:
        print("Note: statistics could not be saved (folder may be read-only).")


def show_statistics(stats: dict[str, int]) -> None:
    """Display cumulative statistics for this installation of the game."""
    guesses = stats["valid_guesses"]
    accuracy = (stats["correct_guesses"] / guesses * 100) if guesses else 0.0
    print("\n" + "=" * 42)
    print("                YOUR STATS")
    print("=" * 42)
    print(f"Rounds played : {stats['rounds_played']}")
    print(f"Wins          : {stats['wins']}")
    print(f"Losses        : {stats['losses']}")
    print(f"Abandoned     : {stats['abandoned']}")
    print(f"Total score   : {stats['total_score']}")
    print(f"Current streak: {stats['current_streak']}")
    print(f"Best streak   : {stats['best_streak']}")
    print(f"Guess accuracy: {accuracy:.1f}%")
    print("=" * 42)


def choose_category() -> Optional[str]:
    """Ask the player for a word category; return None to quit."""
    categories = sorted(WORD_BANK)
    category_lookup = {name.casefold(): name for name in categories}

    print("\nChoose a category:")
    print("  0. Random category")
    for number, category in enumerate(categories, start=1):
        print(f"  {number}. {category}")
    print("  Q. Quit")

    while True:
        choice = input("Category number or name: ").strip().casefold()
        if choice in {"q", "quit", "exit"}:
            return None
        if choice == "0" or choice == "random":
            return "Random"
        if choice in category_lookup:
            return category_lookup[choice]
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            return categories[int(choice) - 1]
        print("Invalid choice. Enter a listed number, a category name, or Q.")


def choose_difficulty() -> Optional[str]:
    """Ask for a difficulty mode; return None to quit."""
    print("\nChoose difficulty:")
    print("  1. Easy   - 8 mistakes allowed, score x1")
    print("  2. Normal - 6 mistakes allowed, score x2")
    print("  3. Hard   - 4 mistakes allowed, score x3")
    print("  Q. Quit")

    choices = {"1": "Easy", "2": "Normal", "3": "Hard"}
    while True:
        choice = input("Difficulty: ").strip().casefold()
        if choice in {"q", "quit", "exit"}:
            return None
        if choice in choices:
            return choices[choice]
        if choice.title() in DIFFICULTIES:
            return choice.title()
        print("Invalid choice. Enter 1, 2, 3, Easy, Normal, Hard, or Q.")


def display_word(secret_word: str, guessed_letters: set[str]) -> str:
    """Return the word with unguessed letters replaced by underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)


def get_hangman_stage(incorrect_guesses: int, max_mistakes: int) -> int:
    """Map the selected difficulty's mistakes onto the available drawing stages."""
    last_stage = len(HANGMAN_PICTURES) - 1
    if incorrect_guesses <= 0:
        return 0
    return min(last_stage, (incorrect_guesses * last_stage + max_mistakes - 1) // max_mistakes)


def play_round(category_choice: str, difficulty: str, stats: dict[str, int]) -> str:
    """Play one round. Return 'finished' or 'quit'."""
    actual_category = (
        random.choice(list(WORD_BANK)) if category_choice == "Random" else category_choice
    )
    secret_word, hint_text = random.choice(WORD_BANK[actual_category])
    config = DIFFICULTIES[difficulty]
    max_mistakes = config["max_mistakes"]
    multiplier = config["multiplier"]

    guessed_letters: set[str] = set()
    guessed_words: set[str] = set()
    incorrect_guesses = 0
    hint_used = False
    stats["rounds_played"] += 1

    print("\n" + "=" * 48)
    print("                 HANGMAN ULTIMATE")
    print("=" * 48)
    print(f"Category: {actual_category}  |  Difficulty: {difficulty}")
    print(f"The word contains {len(secret_word)} letters.")
    print("Commands: type a letter, a full word, HINT (or ?), or QUIT.")
    print("A hint costs one life and can be used once per round.")

    while True:
        stage = get_hangman_stage(incorrect_guesses, max_mistakes)
        print(HANGMAN_PICTURES[stage])
        print("\nWord:       ", display_word(secret_word, guessed_letters))
        print(f"Mistakes:    {incorrect_guesses}/{max_mistakes}")
        print(f"Lives left:  {max_mistakes - incorrect_guesses}")
        print("Letters tried:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")
        print("Words tried:  ", ", ".join(sorted(guessed_words)) if guessed_words else "None")

        if all(letter in guessed_letters for letter in secret_word):
            print("\n*** YOU WIN! You guessed the word! ***")
            print(f"The word was: {secret_word}")
            stats["wins"] += 1
            stats["current_streak"] += 1
            stats["best_streak"] = max(stats["best_streak"], stats["current_streak"])
            remaining = max_mistakes - incorrect_guesses
            hint_bonus = 0 if hint_used else 20
            points = (len(secret_word) * 10 + remaining * 5 + hint_bonus) * multiplier
            stats["total_score"] += points
            print(f"Round score: {points} points (difficulty multiplier x{multiplier}).")
            print(f"Winning streak: {stats['current_streak']}")
            return "finished"

        if incorrect_guesses >= max_mistakes:
            print("\nGAME OVER! You have used all your mistakes.")
            print(f"The correct word was: {secret_word}")
            stats["losses"] += 1
            stats["current_streak"] = 0
            return "finished"

        guess = input("\nYour guess: ").strip().casefold()

        if guess in {"quit", "exit"}:
            print(f"Round abandoned. The word was: {secret_word}")
            stats["abandoned"] += 1
            stats["current_streak"] = 0
            return "quit"

        if guess in {"hint", "?"}:
            if hint_used:
                print("You have already used your hint this round.")
            else:
                hint_used = True
                incorrect_guesses += 1
                print(f"HINT (costs one life): {hint_text}")
            continue

        if not guess:
            print("Please enter a letter, a full word, HINT, or QUIT.")
            continue

        if not guess.isalpha() or not guess.isascii():
            print("Invalid input. Use English letters A-Z only.")
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already tried that letter. No life was lost.")
                continue
            guessed_letters.add(guess)
            stats["valid_guesses"] += 1
            if guess in secret_word:
                stats["correct_guesses"] += 1
                print("Correct letter!")
            else:
                incorrect_guesses += 1
                print("Incorrect. That letter is not in the word.")
            continue

        # A longer alphabetic input is treated as a full-word guess.
        if guess in guessed_words:
            print("You already tried that word. No life was lost.")
            continue
        guessed_words.add(guess)
        stats["valid_guesses"] += 1
        if guess == secret_word:
            guessed_letters.update(secret_word)
            stats["correct_guesses"] += 1
            print("Correct! You found the whole word.")
        else:
            incorrect_guesses += 1
            print("Incorrect word. One life was lost.")


def ask_to_replay(stats: dict[str, int]) -> bool:
    """Ask whether to continue; S shows stats without ending the session."""
    while True:
        choice = input("\nPlay another round? [Y]es / [N]o / [S]tats: ").strip().casefold()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no", "q", "quit", "exit"}:
            return False
        if choice in {"s", "stats", "score"}:
            show_statistics(stats)
        else:
            print("Please enter Y, N, or S.")


def main() -> None:
    """Run the game session and save statistics when the session ends."""
    stats = load_stats()
    print("=" * 48)
    print("             HANGMAN ULTIMATE")
    print("Guess letters, solve the word, and build a streak!")
    print("=" * 48)
    print(f"Words available: {sum(len(words) for words in WORD_BANK.values())} unique words across {len(WORD_BANK)} categories")
    print("Your lifetime stats are saved locally when possible.")

    try:
        while True:
            category = choose_category()
            if category is None:
                break

            difficulty = choose_difficulty()
            if difficulty is None:
                break

            result = play_round(category, difficulty, stats)
            save_stats(stats)
            if result == "quit" or not ask_to_replay(stats):
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. Saving your stats...")
    finally:
        save_stats(stats)
        show_statistics(stats)
        print("\nThanks for playing Hangman Ultimate. Goodbye!")


if __name__ == "__main__":
    main()
