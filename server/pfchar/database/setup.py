from pfchar.database.connection import r_exists, r_set


miscelanious = {
    'bonus_spells': [[0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0, 0], [2, 1, 1, 1, 1, 0, 0, 0, 0], [2, 2, 1, 1, 1, 1, 0, 0, 0], [2, 2, 2, 1, 1, 1, 1, 0, 0], [2, 2, 2, 2, 1, 1, 1, 1, 0], [3, 2, 2, 2, 2, 1, 1, 1, 1], [3, 3, 2, 2, 2, 2, 1, 1, 1], [3, 3, 3, 2, 2, 2, 2, 1, 1], [3, 3, 3, 3, 2, 2, 2, 2, 1], [4, 3, 3, 3, 3, 2, 2, 2, 2], [4, 4, 3, 3, 3, 3, 2, 2, 2], [4, 4, 4, 3, 3, 3, 3, 2, 2], [4, 4, 4, 4, 3, 3, 3, 3, 2], [5, 4, 4, 4, 4, 3, 3, 3, 3]],
    'feats': [{
        'name': 'Aberrant Tumor',
        'prereq': {
            'bloodline': 'aberrant'
        },
        'description': 'Gain a tumor familiar',
        'nethys_link': 'https://aonprd.com/FeatDisplay.aspx?ItemName=Aberrant%20Tumor'
    }, {
        'name': 'Aberration-Bane Caster',
        'prereq': {
            'level': 4,
            'race': 'gillman'
        }
    }]
}


classes = {
    'alchemist': {
        # 'name': 'Alchemist',
        # 'hitdie': 'd8',
        # 'alignment': 'any',
        # 'wealth': '3d6x10',
        # 'skill_points': 4,
        # 'class_skills': ['appraise', 'craft', 'disable_device', 'fly', 'heal', 'knowledge_arcana', 'knowledge_nature', 'perception', 'profession', 'sleight_of_hand', 'spellcraft', 'survival', 'use_magic_device'],
        # 'bab': [(0), (1), (2), (3), (3), (4), (5), (6, 1), (6, 1), (7, 2), (8, 3), (9, 4), (9, 4), (10, 5), (11, 6, 1), (12, 7, 2), (12, 7, 2), (13, 8, 3), (14, 9, 4), (15, 10, 5)],
        # 'saves': {
        #     'fortitude': [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        #     'reflex': [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        #     'will': [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]
        # },
        # 'spells': {
        #     'daily_allotment': [[1, 0, 0, 0, 0, 0], [2, 0, 0, 0, 0, 0], [3, 0, 0, 0, 0, 0], [3, 1, 0, 0, 0, 0], [4, 2, 0, 0, 0, 0], [4, 3, 0, 0, 0, 0], [4, 3, 1, 0, 0, 0], [4, 4, 2, 0, 0, 0], [5, 4, 3, 0, 0, 0], [5, 4, 3, 1, 0, 0], [5, 4, 4, 2, 0, 0], [5, 5, 4, 3, 0, 0], [5, 5, 4, 3, 1, 0], [5, 5, 4, 4, 2, 0], [5, 5, 5, 4, 3, 0], [5, 5, 5, 4, 3, 1], [5, 5, 5, 4, 4, 2], [5, 5, 5, 5, 4, 3], [5, 5, 5, 5, 5, 4], [5, 5, 5, 5, 5, 5]]
        # },
        # 'special': {
        #
        # },
        # 'nethys_link': 'https://aonprd.com/ClassDisplay.aspx?ItemName=Alchemist'
    },
    'antipaladin': {
        # 'name': 'Antipaladin',
        # 'hitdie': 'd10',
        # 'parent_class': 'Paladin',
        # 'alignment': 'chaotic_evil',
        # 'wealth': '5d6x10',
        # 'skill_points': 2,
        # 'class_skills': ['bluff', 'craft', 'disguise', 'handle_animal', 'intimidate', 'knowledge_religion', 'profession', 'ride', 'sense_motive', 'spellcraft', 'stealth'],
        # 'bab': [(1), (2), (3), (4), (5), (6,1), (7,2), (8,3), (9,4), (10,5), (11,6,1), (12,7,2), (13,8,3), (14,9,4), (15,10,5), (16,11,6,1), (17,12,7,2), (18,13,8,3), (19,14,9,4), (20,15,10,5)],
        # 'saves': {
        #     'fortitude': [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
        #     'refles': [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        #     'will': [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        # },
        # 'daily_spells': [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0], [2, 1, 0, 0], [2, 1, 0, 0], [2, 1, 1, 0], [2, 2, 1, 0], [3, 2, 1, 0], [3, 2, 1, 1], [3, 2, 2, 1], [3, 3, 2, 1], [4, 3, 2, 1], [4, 3, 2, 2], [4, 3, 3, 2], [4, 4, 3, 3]],
        # 'nethys_link': 'https://aonprd.com/ClassDisplay.aspx?ItemName=Antipaladin'
    },
    'arcanist': {
        # 'name': 'Arcanist',
        # 'hitdie': 'd6',
        # 'parent': 'Sorcerer and Wizard',
        # 'wealth': '2d6x10',
        # 'skill_points': 2,
        # 'class_skills': ['appraise', 'craft', 'fly', 'knowledge', 'linguistics', 'profession', 'spellcraft', 'use_magic_device'],
        # 'bab': [(0), (1), (1), (2), (2), (3), (3), (4), (4), (5), (5), (6, 1), (6, 1), (7, 2), (7, 2), (8, 3), (8, 3), (9, 4), (9, 4), (10, 5)],
        # 'saves': {
        #     'fortitude': [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        #     'reflex': [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
        #     'will': [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        # },
        # 'spells': {
        #     'daily_allotment': [[-1, 2, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 3, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 4, 0, 0, 0, 0, 0, 0, 0, 0], [-1, 4, 2, 0, 0, 0, 0, 0, 0, 0], [-1, 4, 3, 0, 0, 0, 0, 0, 0, 0], [-1, 4, 4, 2, 0, 0, 0, 0, 0, 0], [-1, 4, 4, 3, 0, 0, 0, 0, 0, 0], [-1, 4, 4, 4, 2, 0, 0, 0, 0, 0], [-1, 4, 4, 4, 3, 0, 0, 0, 0, 0], [-1, 4, 4, 4, 4, 2, 0, 0, 0, 0], [-1, 4, 4, 4, 4, 3, 0, 0, 0, 0], [-1, 4, 4, 4, 4, 4, 2, 0, 0, 0], [-1, 4, 4, 4, 4, 4, 3, 0, 0, 0], [-1, 4, 4, 4, 4, 4, 4, 2, 0, 0], [-1, 4, 4, 4, 4, 4, 4, 3, 0, 0], [-1, 4, 4, 4, 4, 4, 4, 4, 2, 0], [-1, 4, 4, 4, 4, 4, 4, 4, 3, 0], [-1, 4,  4, 4, 4, 4, 4, 4, 2], [-1, 4, 4, 4, 4, 4, 4, 4, 4, 3], [-1, 4, 4, 4, 4, 4, 4, 4, 4, 4]],
        #     'daily_prepared': [[4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [6, 4, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [7, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [7, 5, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [8, 5, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [8, 5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0], [9, 5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0], [9, 5, 5, 4, 3, 2, 0, 0, 0, 0, 0, 0, 0, 0], [9, 5, 5, 4,  2, 1, 0, 0, 0, 2, 0, 0, 0], [9, 5, 5, 4, 4, 3, 2, 0, 0, 0, 3, 0, 0, 0], [9, 5, 5, 4, 4, 3, 2, 1, 0, 0, 4, 2, 0, 0], [9, 5, 5, 4, 4, 4, 3, 2, 0, 0, 4, 3, 0, 0], [9, 5, 5, 4, 4, 4, 3, 2, 1, 0, 4, 4, 2, 0], [9, 5, 5, 4, 4, 4, 3, 3, 2, 0, 4, 4, 3, 0], [9, 5, 5, 4, 4, 4, 3, 3, 2, 1, 4, 4, 4, 2], [9, 5, 5, 4, 4, 4, 3, 3, 3, 2, 4, 4, 4, 3], [9, 5, 5, 4, 4, 4, 3, 3, 3, 3, 4, 4, 4, 4]],
        # },
        # 'nethys_link': 'https://www.aonprd.com/ClassDisplay.aspx?ItemName=Arcanist'
    },
    'barbarian': {},
    'bard': {},
    'bloodrager': {},
    'brawler': {},
    'cavalier': {},
    'cleric': {},
    'druid': {},
    'fighter': {},
    'gunslinger': {},
    'hunter': {},
    'inquisitor': {},
    'investigator': {},
    'kineticist': {},
    'magus': {},
    'medium': {},
    'mesmerist': {},
    'monk': {},
    'ninja': {},
    'occultist': {
        'name': 'Occultist',
        'hitdie': 'd8',
        'alignment': 'any',
        'wealth': '4d6x10',
        'skills_growth': 4,
        'class_skills': ['appraise', 'craft', 'diplomacy', 'disable_device', 'disguise', 'fly', 'knowledge_arcana', 'knowledge_engineering', 'knowledge_history', 'knowledge_planes', 'knowledge_religion', 'linguistics', 'perception', 'profession', 'sense_motive', 'sleight_of_hand', 'spellcraft', 'use_magic_device'],
        'bab': [(0), (1), (2), (3), (3), (4), (5), (6,1), (6,1), (7,2), (8,3), (9,4), (9,4), (10,5), (11,6,1), (12,7,2), (12,7,2), (13,8,3), (14,9,4), (15,10,5)],
        'saves': {
            'fortitude': [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12],
            'reflex': [0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6],
            'will': [2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12]
        },
        'spells': {
            'levels': 6,
            'daily_allotment': [[1], [2], [3], [3, 1], [4, 2], [4, 3], [4, 3, 1], [4, 4, 2], [5, 4, 3], [5, 4, 3, 1], [5, 4, 4, 2], [5, 5, 4, 3], [5, 5, 4, 3, 1], [5, 5, 4, 4, 2], [5, 5, 5, 4, 3], [5, 5, 5, 4, 3, 1], [5, 5, 5, 4, 4, 2], [5, 5, 5, 5, 4, 3], [5, 5, 5, 5, 5, 4], [5, 5, 5, 5, 5, 5]],
            'spell_list': [{
                'Abjuration': ['Resistance'],
                'Conjuration': ['Create Water', 'Stabilize'],
                'Divination': ['Detect Magic', 'Detect Poison', 'Detect Psychic Significance', 'Guidance', 'Know Direction', 'Read Magic', 'Sift'],
                'Enchantment': ['Daze'],
                'Evocation': ['Dancing Lights', 'Flare', 'Light', 'Spark', 'Telekinetic Projectile'],
                'Illusion': ['Ghost Sound'],
                'Necromancy': ['Bleed', 'Grave Words', 'Touch of Fatigue'],
                'Transmutation': ['Mage Hand', 'Mending', 'Message', 'Open/Close', 'Purify Food and Drink']
            }, {
                'Abjuration': ["Abjuring Step", "Alarm", "Fastidiousness", "Hex Ward", "Hold Portal", "Peacebond", "Shield", "Shock Shield", "Warding Weapon"],
                'Conjuration': ["Barbed Chains", "Cure Light Wounds", "Desperate Weapon", "Guardian Armor", "Icicle Dagger", "Instant Portrait", "Mage Armor", "Mount", "Returning Weapon", "Unseen Servant"],
                'Divination': ["Anticipate Peril", "Comprehend Languages", "Cultural Adaptation", "Detect Charm", "Detect Secret Doors", "Detect Snares and Pits", "Diagnose Disease", "Discern Next of Kin", "Heightened Awareness", "Identif", "Linked Legac", "Mindlink", "Object Reading", "Psychic Reading", "Rune Trace", "Skim", "Speechreader's Sight", "True Appraisal"],
                'Enchantment': ["Charm Person", "Command", "Forbid Action", "Hypnotism", "Memorize Page", "Memory Lapse", "Murderous Command", "Sleep"],
                'Evocation': ["Bestow Planar Infusion I", "Burning Hands", "Floating Disk", "Shocking Grasp"],
                'Illusion': ["Alter Musical Instrument", "Auditory Hallucination", "Blurred Movement", "Decrepit Disguise", "Disguise Self", "Disguise Weapon", "Echo", "Hide Bruises", "Illusion of Calm", "Magic Aura", "Mask Dweomer", "Mirror Mantis", "Quintessence", "Shadow Trap", "Shadow Weapon", "Silent Image", "Vanish"],
                'Necromancy': ["Cause Fear", "Decompose Corpse", "Grasping Corpse", "Inflict Light Wounds", "Itching Curse", "Preserve", "Restore Corpse", "Sculpt Corpse", "Skin Tag"],
                'Transmutation': ["Alter Winds", "Ant Haul", "Break", "Charge Object", "Crafter's Curse", "Crafter's Fortune", "Enlarge Person", "Erase", "Expeditious Retreat", "Feather Fall", "Funereal Weapon", "Grappling Scarf", "Gravity Bow", "Jury-Rig", "Keen Senses", "Lead Blades", "Liberating Command", "Longshot", "Magic Weapon", "Mirror Polish", "Negate Aroma", "Pass without Trace", "Reduce Person", "Refine Improvised Weapon", "Reinforce Armaments", "Sculpted Cape", "Spirit Share", "Sundering Shards", "Tears to Wine", "Vocal Alteration", "Wizened Appearance", "Youthful Appearance"]
            }, {
                'Abjuration': ["Allied Cloak", "Arcane Lock", "Bullet Shield", "Conditional Favor", "Crimson Confession", "Escape Alarm", "Node of Blasting", "Obscure Object", "Resist Energy", "With the Wind"],
                'Conjuration': ["Ablative Barrier", "Apport Object", "Cure Moderate Wounds", "Delay Poison", "Glitterdust", "Mount, Communal", "Restful Cloak", "Returning Weapon, Communal", "Wicker Horse"],
                'Divination': ["Analyze Aura", "Augury", "Blood Biography", "Create Treasure Map", "Detect Magic, Greater", "Enchantment Sight", "Find Traps", "Know Peerage", "Locate Object", "Mindshock", "Residual Tracking", "See Invisibility", "Seed Spies", "Sense Fear", "Sense Madness", "Share Language", "Share Memory", "Status", "Voluminous Vocabulary"],
                'Enchantment': ["Aversion", "Bestow Weapon Proficiency", "Calm Emotions", "Daze Monster", "Demand Offering", "Hoodwink", "Inflict Pain", "Investigative Mind", "Tactical Acumen"],
                'Evocation': ["Beacon of Guilt", "Burning Gaze", "Campfire Wall", "Contact Entity I", "Continual Flame", "Darkness", "Defensive Shock", "Extreme Buoyancy", "Flaming Sphere", "Flickering Lights", "Force Sword", "Frost Fall", "Ghost Whip", "Gust of Wind", "Lead Anchor", "Neutral Buoyancy", "Pilfering Hand", "Protective Penumbra", "Shatter", "Sound Burst"],
                'Illusion': ["Assumed Likeness", "Blur", "Disguise Other", "Ghostly Disguise", "Implant False Reading", "Instigate Psychic Duel", "Invisibility", "Invisibility Bubble", "Magic Mouth", "Mask Dweomer, Communal", "Minor Image", "Mirror Image", "Misdirection", "Obscured Script", "Phantom Trap", "Shifted Steps", "Symbol of Mirroring", "Sympathetic Aura"],
                'Necromancy': ["Animate Dead, Lesser", "Brow Gasher", "Crafter's Nightmare", "False Life", "Inflict Moderate Wounds", "Object Possession, Lesser", "Pernicious Poison", "Purge Spirit", "Scare", "Skinsend", "Spectral Hand", "Symbol of Exsanguination", "Unsettling Presence"],
                'Transmutation': ["Accelerate Poison", "Air Step", "Ant Haul, Communal", "Badger's Ferocity", "Billowing Skirt", "Bowstaff", "Certain Grip", "Chill Metal", "Codespeak", "Darkvision", "Disfiguring Touch", "Effortless Armor", "Enter Image", "Fear the Sun", "Feast of Ashes", "Fool's Gold (AA)", "Ghostbane Dirge", "Glide", "Grasping Vine", "Heat Metal", "Hidden Knowledge", "Huntmaster's Spear", "Kalistocrat's Nightmare", "Knock", "Levitate", "Magic Siege Engine", "Make Whole", "Masterwork Transformation", "Mirror Hideaway", "Perceive Cues", "Quick Change", "Reinforce Armaments, Communal", "Rope Trick", "Ropeweave", "Rotgut", "Rune of Rule", "Silk To Steel", "Spider Climb", "Splinter Spell Resistance", "Surefoot Boots", "Telekinetic Assembly", "Unerring Weapon", "Versatile Weapon", "Violent Accident", "Warp Wood", "Weapon of Awe", "Winged Sword", "Wood Shape"]
            }, {
                'Abjuration': ["Cloak of Winds", "Dispel Magic", "Erase Impressions", "Explosive Runes", "Free Swim", "Guardian Monument, Lesser", "Guarding Knowledge", "Magic Circle against Chaos", "Magic Circle against Evil", "Magic Circle against Good", "Magic Circle against Law", "Nondetection", "Protection from Energy", "Quell Energy", "Resist Energy, Communal", "Scales of Deflection", "Selective Alarm", "Thaumaturgic Circle", "Vigilant Rest"],
                'Conjuration': ["Create Drug", "Create Food and Water", "Cure Serious Wounds", "Draconic Ally", "Minor Creation", "Penumbral Disguise", "Pernicious Pranksters", "Phantom Driver", "Phantom Steed", "Pocketful of Vipers", "Sepia Snake Sigil", "Summon Ship", "Symbol of Healing", "Urban Step"],
                'Divination': ["Akashic Communion", "Arcane Sight", "Clairaudience/Clairvoyance", "Follow Aura", "Locate Weakness", "Meticulous Match", "Mnemonic Siphon", "Pierce Disguise", "Replay Tracks", "Retrocognition", "Seek Thoughts", "Share Language, Communal", "Symbol of Revelation", "Threefold Sight", "Witness"],
                'Enchantment': ["Control Summoned Creature", "Deep Slumber", "Hold Person", "Suggestion", "Symbol of Laughter"],
                'Evocation': ["Agonize", "Call Lightning", "Contact Entity II", "Daybreak Arrow", "Daylight", "Deeper Darkness", "Fireball", "Invisibility Purge", "Lightning Bolt", "Moonrise Arrow", "Motes of Dusk and Dawn", "Spotlight", "Talismanic Implement", "Tiny Hut", "Twilight Knife", "Unflappable Mien", "Wall of Split Illumination", "Wind Wall"],
                'Illusion': ["Adjustable Disguise", "Audiovisual Hallucination", "Aura Alteration", "Displacement", "Geomessage", "Illusory Script", "Instant Fake", "Invisibility Bubble, Giant", "Invisibility Sphere", "Magic Aura, Greater", "Major Image", "Mirage", "Shadowmind", "Undetectable Trap", "Vision of Hell"],
                'Necromancy': ["Animate DeadM", "Bestow Curse", "Create Soul Gem", "Flesh Puppet", "Gentle Repose", "Healing Thief", "Inflict Serious Wounds", "Retributive Reparations", "Riding Possession", "Sands of Time", "Sessile Spirit", "Toxic Gift"],
                'Transmutation': ["Age Resistance, Lesser", "Assume Appearance", "Bloodhound", "Borrow Corruption", "Countless Eyes", "Cup of Dust", "Daggermark's Exchange", "Darkvision, Communal", "Deft Digits", "Dongun Shaper's Touch", "Flame Arrow", "Fly", "Forced Mutation", "Full Pouch", "Gaseous Form", "Ghost Brand", "Haste", "Heart of the Metal", "Hostile Levitation", "Irregular Size", "Keen Edge", "Magic Vestment", "Magic Weapon, Greater", "Mark of Buoyancy", "Rags to Riches", "Secret Page", "Shrink Item", "Slow", "Spider Climb, Communal", "Stone Shape", "Symbol of Slowing", "Tail Current", "Tailwind", "Temporary Graft"]
            }, {
                'Abjuration': ["Absorb Rune I", "Ban Corruption", "Break Enchantment", "Conjuration Foil", "Curse of Magic Negation", "Dimensional Anchor", "Dismissal", "Enchantment Foil", "Fire Trap", "Freedom of Movement", "Globe of Invulnerability, Lesser", "Life Bubble", "Nondetection, Communal", "Peacebond, Greater", "Planar Aegis", "Soothe Construct", "Spell Immunity", "StoneskinM", "Symbol of Sealing", "True Form", "Unbreakable Construct", "Wreath of Blades"],
                'Conjuration': ["Cure Critical Wounds", "Dimension Door", "Flash Forward", "Major Creation", "Phantom Chariot", "Phantom Steed, Communal", "Poisonous Balm", "Rising Water", "Straitjacket", "Surface Excursion"],
                'Divination': ["Arcane Eye", "Commune with Texts", "Contact Other Plane", "Detect Scrying", "Glimpse of Truth", "Locate Creature", "Mind Probe", "Reveal Emotions", "Scrying", "Symbol of Scrying", "Unerring Tracker", "Vicarious View"],
                'Enchantment': ["Charm Monster", "Charm Person, Mass", "Confusion", "Curse of Disgust", "Daze, Mass", "Demanding Message", "Hold Monster", "Hypnotism, Greater", "Mad Sultan's Melody", "Mind Swap", "Mindwipe", "Planeslayer's Call", "Symbol of Distraction", "Symbol of Persuasion", "Symbol of Sleep"],
                'Evocation': ["Ball Lightning", "Bestow Planar Infusion II", "Brightest Light", "Contact Entity III", "Contingent Scroll", "Controlled Fireball", "Etheric Shards", "Fire Shield", "Flaming Sphere, Greater", "Ice Storm", "Pyrotechnic Eruption", "Resilient Sphere", "River of Wind", "Rope Tornado", "Sending", "Shout", "Spirit-Bound Blade", "Unbearable Brightness", "Wall of Fire", "Wall of Ice"],
                'Illusion': ["Complex Hallucination", "Illusion of Treachery", "Illusory Wall", "Impossible Angles", "Invisibility, Greater", "Quieting Weapons", "Shocking Image", "Symbol of Striking", "Telepathic Silence", "Wandering Star Motes"],
                'Necromancy': ["Conditional Curse", "Death Ward", "False Life, Greater", "Fear", "Flesh Puppet Horde", "Inflict Critical Wounds", "Masochistic Shadow", "Object Possession", "Poison", "Possession", "Red Hand of the Killer", "Spellcurse", "Summoner Conduit", "Symbol of Fear", "Symbol of Pain", "Torpid Reanimation", "Umbral Infusion"],
                'Transmutation': ["Age Resistance", "Air Walk", "Aroden's Spellsword", "Assume Appearance, Greater", "Darkvision, Greater", "Echolocation", "Magic Siege Engine, Greater", "Majestic Image", "Malfunction", "Mirror Transport", "Parchment Swarm", "Planar Adaptation", "Rapid Repair", "Revenant Armor", "Rigor Mortis", "Rusting Grasp", "Slough", "Treasure Stitching", "Warp Metal"]
            }, {
                'Abjuration': ["Bloodstone Mirror", "Dispel Magic, Greater", "Guardian Monument, Greater", "Nex's Secret Workshop", "Spell Immunity, Communal", "Spell Resistance", "Stoneskin, Communal", "Talisman of Reprieve"],
                'Conjuration': ["Bind Sage", "Cold Iron Fetters", "Create Demiplane, Lesser", "Cure Light Wounds, Mass", "Planar Binding, Lesser", "Secret Chest", "Teleport", "Wall of Stone"],
                'Divination': ["Battlemind Link", "Commune", "Find Quarry", "Foretell Failure", "Locate Gate", "Prying Eyes", "Remote Viewing", "True Seeing"],
                'Enchantment': ["Command, Greater", "Contagious Suggestion", "Dahak's Release", "Dominate Person", "Forbid Action, Greater", "Inflict Pain, Mass", "Mind Fog", "Suggestion, Mass", "Symbol of Stunning"],
                'Evocation': ["Alaznist's Jinx", "Call Lightning Storm", "Cone of Cold", "Ectoplasmic Hand", "Fire Snake", "Interposing Hand", "Wall of Force"],
                'Illusion': ["Dream Reality", "False Vision", "Illusion of Treachery, Greater", "Mislead", "Persistent Image", "Scripted Hallucination", "Seeming"],
                'Necromancy': ["Curse, Major", "Entrap Spirit", "Inflict Light Wounds, Mass", "Object Possession, Greater", "Suffocation", "Symbol of Weakness", "Unwilling Shield"],
                'Transmutation': ["Age Resistance, Greater", "Air Walk, Communal", "Awaken Construct", "Control Winds", "Energy Siege Shot", "Fabricate", "Ghostbane Dirge, Mass", "Overland Flight", "Particulate Form", "Telekinesis", "Transmute Mud to Rock", "Transmute Rock to Mud", "Waft"]
            }, {
                'Abjuration': ["Absorb Rune II", "Alleviate Corruption", "Antimagic Field", "Forbiddance", "Globe of Invulnerability", "Repulsion", "Symbol of Vulnerability"],
                'Conjuration': ["Balance of Suffering", "Call Construct", "Create Demiplane", "Cure Moderate Wounds, Mass", "Getaway", "Heal", "Planar Binding", "Roaming Pit", "Treacherous Teleport", "Wall of Iron"],
                'Divination': ["Analyze Dweomer", "Find the Path", "Legend Lore", "Prediction of Failure", "Scrying, Greater", "Soulseeker"],
                'Enchantment': ["Antipathy", "Charm Monster, Mass", "Cloak of Dreams", "Demanding Message, Mass", "Lost Legacy", "Symbol of Insanity", "Symbol of Strife", "Sympathy"],
                'Evocation': ["Betraying Sting", "Blade Barrier", "Chain Lightning", "Cold Ice Strike", "Contact Entity IV", "Contagious Flame", "Contingency", "Forceful Hand", "Freezing Sphere", "Last Azlanti's Defending Sword", "Sirocco"],
                'Illusion': ["Permanent Image", "Project Image", "Triggered Hallucination"],
                'Necromancy': ["Harm", "Inflict Moderate Wounds, Mass", "Plundered Power", "Possession, Greater", "Rotting Alliance", "Symbol of Death", "Temporary Resurrection", "Umbral Strike"],
                'Transmutation': ["Animate Objects", "Artificer's Curse", "Break, Greater", "Control Construct", "Disintegrate", "Enemy Hammer", "Energy Siege Shot, Greater", "Invoke Deity", "Ironwood", "Knock, Mass", "Planar Adaptation, Mass", "Scribe's Binding", "Statue", "Transfiguring Touch", "Transformation"]
            }]
        },
        'specials': ['Focus powers, implements 2, knacks, mental focus', 'Implements 3, magic item skill, object reading', 'Focus power', 'Shift focus', 'Aura sight, focus power', 'Implements 4', 'Focus power', 'Magic circles, outside contact 1', 'Focus power', 'Implements 5', 'Focus power', 'Binding circles, outside contact 2', 'Focus power', 'Implements 6', 'Focus power', 'Fast circles, outside contact 3', 'Focus power', 'Implements 7', 'Focus power', 'Implement mastery, outside contact 4'],
        'nethys_link': 'https://www.aonprd.com/ClassDisplay.aspx?ItemName=Occultist',
        'class_features': {
            'implements': {
                'Abjuration': {
                    'resonant_power': 'Warding Talisman',
                    'base_focus_power': 'Mind Barrier',
                    'focus_powers': ['Aegis', 'Energy Shield', 'Globe of Negation', 'Loci Sentry', 'Planar Ward', 'Unraveling'],
                    'nethys_link': 'https://www.aonprd.com/OccultistImplementsDisplay.aspx?ItemName=Abjuration'
                },
                'Conjuration': {
                    'resonant_power': '',
                    'base_focus_power': '',
                    'focus_powers': [],
                    'nethys_link': ''
                },
                'Divination': {
                    'resonant_power': '',
                    'base_focus_power': '',
                    'focus_powers': [],
                    'nethys_link': ''
                },
                'Enchantment': {
                    'resonant_power': '',
                    'base_focus_power': '',
                    'focus_powers': [],
                    'nethys_link': ''
                },
                'Evocation': {
                    'resonant_power': '',
                    'base_focus_power': '',
                    'focus_powers': [],
                    'nethys_link': ''
                },
                'Illusion': {
                    'resonant_power': '',
                    'base_focus_power': '',
                    'focus_powers': [],
                    'nethys_link': ''
                },
                'Necromancy': {
                    'resonant_power': '',
                    'base_focus_power': '',
                    'focus_powers': [],
                    'nethys_link': ''
                },
                'Transmutation': {
                    'resonant_power': '',
                    'base_focus_power': '',
                    'focus_powers': [],
                    'nethys_link': ''
                }
            }
        }
    },
    'oracle': {},
    'paladin': {},
    'psychic': {},
    'ranger': {},
    'rogue': {},
    'samurai': {},
    'shaman': {},
    'shifter': {},
    'skald': {},
    'slayer': {},
    'sorcerer': {},
    'spiritualist': {},
    'summoner': {},
    'swashbuckler': {},
    'vigilante': {},
    'warpriest': {},
    'witch': {},
    'wizard': {}
}


if not r_exists('users'):
    r_set('users', '.', json.dumps({}))
if not r_exists('characters'):
    r_set('characters', '.', json.dumps({}))
if not r_exists('classes'):
    r_set('classes', '.', json.dumps({}))
