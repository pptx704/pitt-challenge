sex_choice = (
    ("male", "Male"),
    ("female", "Female"),
    ("others", "Others")
)

evidence_choice = (
    ("present", "present"),
    ("absent", "absent"),
    ("unknown", "unknown")
)

boroughs = (
    ("Bronx","Bronx"),
    ("Brooklyn","Brooklyn"),
    ("Cedarhurst","Cedarhurst"),
    ("Flushing","Flushing"),
    ("Jackson Heights","Jackson Heights"),
    ("Manhattan","Manhattan"),
    ("New York","New York"),
    ("Queens","Queens"),
    ("Staten Island","Staten Island"),
)

all_tests = {
    "allergologist": ["RBC Count", "WBC Count"],
    "dermatologist": ["RBC Count", "WBC Count", "Urine Test"],
    "psychologist": [ "RBC Count", "WBC Count"],
    "gastroenterologist": ["RBC Count", "WBC Count"],
    "ophthalmologist": ["RBC Count", "WBC Count"],
    "general practitioner": ["RBC Count", "WBC Count", "BP Test"],
    "cardiologist": ["ECG", "Cardiac Output", "Stroke Volume", "Heart Rate"],
    "pulmonologist": ["Spirometry", "Pulse Oximetry"],
    "surgeon": ["Urine Test", "ECG", "WBC Count", "Glucose Test","Potassium Test"],
    "gynecologist": ["RBC Count", "WBC Count", "Urine Test"],
    "endocrinologist": ["RBC Count", "WBC Count"],
    "rheumatologist": ["Erythrocyte Sedimentation Rate (ESR)", "RBC Count", "WBC Count"],
    "urologist": ["RBC Count", "WBC Count", "Urine Test"],
    "nephrologist": ["RBC Count", "WBC Count", "Creatinine Test", "Urine Test"],
    "hematologist": ["RBC Count", "WBC Count", "Haemoglobin Count", "Platelets Count", "Hematocrit Test"],
    "oncologist": ["CBC count"],
    "diabetologist": ["BP Test", "Lipid Profile LDL", "Lipid Profile HDL", "Sugar Test"],
    "infectiologist": ["RBC Count", "WBC Count"],
    "pediatrician": ["RBC Count", "WBC Count", "Urine Test"],
    "toxicologist": ["RBC Count", "WBC Count", "Urine Test"]
}

test_values = {
    "RBC Count":{
        "max":5.72,
        "min":4.32,
        "pot_max":6.3,
        "pot_min":3.9,
        "unit":"million cells/mcL"
    },
    "WBC Count":{
        "max":10500,
        "min":3500,
        "pot_max":13000,
        "pot_min":2500,
        "unit":"cells/mcL"
    },
    "Urine Test":{
        "max":8.5,
        "min":5,
        "pot_max":10.0,
        "pot_min":3.5,
        "unit":"pH"
    },
    "BP Test":{
        "max":130,
        "min":80,
        "pot_max":160,
        "pot_min":60,
        "unit":"mm Hg P"
    },
  
    "Cardiac Output":{
        "max":8,
        "min":4,
        "pot_max":9.5,
        "pot_min":3.0,
        "unit":"L/min"
    },
    "Stroke Volume":{
        "max":100,
        "min":50,
        "pot_max":120,
        "pot_min":40,
        "unit":"mL"
    },
    "Heart Rate":{
        "max":100,
        "min":60,
        "pot_max":120,
        "pot_min":45,
        "unit":"bpm"
    },
    "Spirometry":{
        "max":120,
        "min":80,
        "pot_max":150,
        "pot_min":60,
        "unit":"%"
    },
    "Pulse Oximetry":{
        "max":100,
        "min":90,
        "pot_max":100,
        "pot_min":86,
        "unit":"bpm"
    },
    "Glucose Test":{
        "max":99,
        "min":70,
        "pot_max":120,
        "pot_min":55,
        "unit":"mg/dL"
    },
    "Potassium Test":{
        "max":5.1,
        "min":3.5,
        "pot_max":5.8,
        "pot_min":3.0,
        "unit":"mEq/L"
    },
    "Erythrocyte Sedimentation Rate (ESR)":{
        "max":22,
        "min":0,
        "pot_max":25,
        "pot_min":0,
        "unit":"mm/hr"
    },
    "Creatinine Test":{
        "max":1.3,
        "min":0.9,
        "pot_max":1.5,
        "pot_min":0.75,
        "unit":"mg/dL"
    },
    "Haemoglobin Count":{
        "max":17.5,
        "min":13.5,
        "pot_max":20.5,
        "pot_min":10.5,
        "unit":"g/dL"
    },
    "Platelets Count":{
        "max":450000,
        "min":150000,
        "pot_max":60000,
        "pot_min":12000,
        "unit":"/mcL"
    },
    "Hematocrit Test":{
        "max":50,
        "min":38.8,
        "pot_max":60.0,
        "pot_min":30.0,
        "unit":"%"
    },
    "Lipid Profile HDL":{
        "max":60,
        "min":40,
        "pot_max":70,
        "pot_min":30,
        "unit":"mg/dL"
    },
    "Lipid Profile LDL":{
        "max":160,
        "min":100,
        "pot_max":200,
        "pot_min":80,
        "unit":"mg/dL"
    },
    "Sugar Test":{
        "max":125,
        "min":0,
        "pot_max":150,
        "pot_min":50,
        "unit":"mg/dL"
    }
}

specialists = {
    "Bronx": {
        "urologist": [
            {
                "id": "8cd37936aea7522f5eebb11fdfa15297",
                "name": "Alexander Beylinson",
                "address": "-",
                "email": "alexander_beylinson_11205@gmail.com"
            },
            {
                "id": "dfdf3efc4070fa7bd7177117e313e94b",
                "name": "Richard Friedlander",
                "address": "1718 Pitkin Avenue",
                "email": "richard_friedlander_11203@gmail.com"
            },
            {
                "id": "950e994294b6ba710af6726ff44166bb",
                "name": "George Lum",
                "address": "1250 Shakespeare Avenue",
                "email": "george_lum_10457@gmail.com"
            },
            {
                "id": "49638003d98b918a8059f16e2b9130f3",
                "name": "Marc Yunis",
                "address": "1641 Bergen Street",
                "email": "marc_yunis_11234@gmail.com"
            },
            {
                "id": "cc62b689b3ed3928d40cd33d31d91444",
                "name": "Carmina Rivera",
                "address": "155 W. 19th St",
                "email": "carmina_rivera_10024@gmail.com"
            },
            {
                "id": "10a9c51ec4e357a369e863e2b189564d",
                "name": "Rohini Thodge",
                "address": "69-11B Roosevelt Ave.",
                "email": "rohini_thodge_11373@gmail.com"
            },
            {
                "id": "4a39967bd9b5bb7e70626bb29938a832",
                "name": "Rahul Solanki",
                "address": "41-50 78th St., Ground Fl.",
                "email": "rahul_solanki_11373@gmail.com"
            },
            {
                "id": "fe19eebe154d7293dd34e75d2caf28e4",
                "name": "Barry Weinberg",
                "address": "2083 East 65 Street",
                "email": "barry_weinberg_11217@gmail.com"
            },
            {
                "id": "683910cace4960d7fe7238fe70c1b22e",
                "name": "Frances Dirks",
                "address": "1421 E 2ND ST",
                "email": "frances_dirks_11219@gmail.com"
            },
            {
                "id": "8434e8ece4042b6ce7922b31ace576d8",
                "name": "Claudia Useda",
                "address": "128 Fort Washington Ave",
                "email": "claudia_useda_10031@gmail.com"
            },
            {
                "id": "988da29d490dd69c1f6235cc3e40f12e",
                "name": "Marie Garnes",
                "address": "108 E 96th St",
                "email": "marie_garnes_10021@gmail.com"
            },
            {
                "id": "f42d84ffbebdb15440e0149cbc7190a3",
                "name": "Edward A. Nichols",
                "address": "1162 Edison Ave",
                "email": "edward_a._nichols_10466@gmail.com"
            },
            {
                "id": "0f54ee2b92eedff29b53b4978b1a2851",
                "name": "Michael Sabido",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "michael_sabido_10013@gmail.com"
            },
            {
                "id": "871c08906c0f71cc1b3ea3892e3107ba",
                "name": "Jeffrey Ben-Zvi",
                "address": "716 east 32nd st",
                "email": "jeffrey_ben-zvi_11220@gmail.com"
            },
            {
                "id": "813c44c07f48db21c26fc97422d723fc",
                "name": "Wilner Bonhomme",
                "address": "833 58th Street",
                "email": "wilner_bonhomme_11224@gmail.com"
            },
            {
                "id": "c92523cb52bff699a350b60c76a9f0d9",
                "name": "Laura Bruno",
                "address": "9817 Queens Boulevard, LL2",
                "email": "laura_bruno_11368@gmail.com"
            },
            {
                "id": "4b8642233869565c1b8c5821be97d33e",
                "name": "Fernando A. Ginebra",
                "address": "1455 East 24th Street",
                "email": "fernando_a._ginebra_11211@gmail.com"
            },
            {
                "id": "151aa89fd8a934ed80b1e0387376f17e",
                "name": "Nissar Shaikh",
                "address": "87-59 171st Street",
                "email": "nissar_shaikh_11372@gmail.com"
            },
            {
                "id": "0861d985f3c440739ae78b0ec239859e",
                "name": "Frank Arbucci",
                "address": "164-08 65th Ave",
                "email": "frank_arbucci_11375@gmail.com"
            },
            {
                "id": "047992de83d7cf4b470bd9d283f70271",
                "name": "Alan Ross",
                "address": "142-20 Franklin Ave",
                "email": "alan_ross_11372@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "25f120a0dd474fbd19280ba7d6dcf165",
                "name": "Alex Bruckstein",
                "address": "90-10 Elmhurst Avenue",
                "email": "alex_bruckstein_11373@gmail.com"
            },
            {
                "id": "fd33af7386e3a4ffef8237699c6e04b8",
                "name": "Allan Detweiler",
                "address": "87-59 171st Street",
                "email": "allan_detweiler_11372@gmail.com"
            },
            {
                "id": "b0845a1397cb3a1857beadfb6627be28",
                "name": "Mariamma G. Chelagiri",
                "address": "139-16 91st Avenue",
                "email": "mariamma_g._chelagiri_10453@gmail.com"
            },
            {
                "id": "cad133b2e4670c46e0d55f659cfbfb1c",
                "name": "Priya malik",
                "address": "75-06 ELIOT AVE",
                "email": "priya_malik_11355@gmail.com"
            },
            {
                "id": "2681ad9f87c1d95cce7cc0018a646199",
                "name": "Jeffrey Goldstein",
                "address": "711 Cedar Lawn",
                "email": "jeffrey_goldstein_11418@gmail.com"
            },
            {
                "id": "bd6ef6576ec76c861587c097abecd6c5",
                "name": "Ramon Moquete",
                "address": "172-27 Highland Ave, Suite 1 B",
                "email": "ramon_moquete_11429@gmail.com"
            },
            {
                "id": "6e9c0b3b58315fea8ac0fe0eb73b9989",
                "name": "Jack Resnick",
                "address": "622 OCEAN AVENUE",
                "email": "jack_resnick_11220@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "d105d192ca4b9d45e24cd967937067d8",
                "name": "Claudia Geris",
                "address": "833 58th Street",
                "email": "claudia_geris_11224@gmail.com"
            },
            {
                "id": "59475e38ed8c7738d9a3f06eceb7f3e3",
                "name": "Gerald Roberts",
                "address": "629 West 185th Street",
                "email": "gerald_roberts_11372@gmail.com"
            },
            {
                "id": "23cc681ae32ef800fafbb10efbf62974",
                "name": "Judith Jones",
                "address": "25-92 steinway street",
                "email": "judith_jones_11374@gmail.com"
            },
            {
                "id": "321f668956b40e33bdbae5288239240c",
                "name": "Alice Riegel",
                "address": "-9613 Flatlands Avenue",
                "email": "alice_riegel_11207@gmail.com"
            },
            {
                "id": "a6d60bb7275b9287d6c3dda99a7b1aea",
                "name": "Monique Apollon",
                "address": "121-02 Hillside Avenue",
                "email": "monique_apollon_11203@gmail.com"
            },
            {
                "id": "62f866e4ec16166d58e136ed752c8608",
                "name": "Dominick Bioh",
                "address": "6805 Fort Hamilton Parkway",
                "email": "dominick_bioh_11216@gmail.com"
            },
            {
                "id": "04e9931ed12d82b957d234343aaf4e43",
                "name": "PCP TBD",
                "address": "170 W.233rd Street",
                "email": "pcp_tbd_10457@gmail.com"
            },
            {
                "id": "0f36e2857a4b27333542c67e34302efc",
                "name": "cindy chen",
                "address": "2385 Arthur Avenue, Suite 206",
                "email": "cindy_chen_10453@gmail.com"
            },
            {
                "id": "5697876e1e0cda3ad2425a537a7a7ee1",
                "name": "Ransford Newhad",
                "address": "9817 Queens Boulevard, LL2",
                "email": "ransford_newhad_11368@gmail.com"
            },
            {
                "id": "4d4f181aedc1e74524903a99b6d1fb8d",
                "name": "Ghizlane Benchekroune",
                "address": "2015 Grand Concourse",
                "email": "ghizlane_benchekroune_10467@gmail.com"
            },
            {
                "id": "cd535f6261126f5a97cda2eb549844c9",
                "name": "Carol Roye",
                "address": "4434 Amboy Road",
                "email": "carol_roye_11356@gmail.com"
            },
            {
                "id": "890ba8865aaf80d920c6b6f311affc07",
                "name": "Chaudhry Ghumman",
                "address": "707 West 171st Suite A",
                "email": "chaudhry_ghumman_10034@gmail.com"
            },
            {
                "id": "bde06da04b020f85dddb6b9e7934ba8a",
                "name": "Peter Ruzohorsky",
                "address": "8330 Vietor Avenue, Suite P-1",
                "email": "peter_ruzohorsky_11356@gmail.com"
            },
            {
                "id": "00697baf84ab4377cbf4239ff768387f",
                "name": "Ashoke Kumar Das",
                "address": "90-01 A Rosevelt Ave.",
                "email": "ashoke_kumar_das_11355@gmail.com"
            },
            {
                "id": "1b3b1e3d787e7a96aac531d409c74e61",
                "name": "Sindhu Gupta",
                "address": "139-16 91st Avenue",
                "email": "sindhu_gupta_10453@gmail.com"
            },
            {
                "id": "85da614516b8cd016bab227e2e64dc07",
                "name": "Ndeye Kone",
                "address": "432 Bedford Avenue",
                "email": "ndeye_kone_11208@gmail.com"
            },
            {
                "id": "0f5d47c147de6c13a841332a3a1609a1",
                "name": "Daniel Reich",
                "address": "445 Park Avenue",
                "email": "daniel_reich_11211@gmail.com"
            },
            {
                "id": "a8bc5226ad57cb1e3b049bc0f7f96cc8",
                "name": "Mohammad Azam",
                "address": "14 East 4th Street",
                "email": "mohammad_azam_10033@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "bc529e2df06d4e2ab0397a3887790ded",
                "name": "John Maese",
                "address": "121A West 20th Street",
                "email": "john_maese_10021@gmail.com"
            },
            {
                "id": "1ae2a1940c3bb3265e9cbedb0be11c40",
                "name": "Mohammad Bhatti",
                "address": "1216 Beach Ave #1",
                "email": "mohammad_bhatti_10453@gmail.com"
            },
            {
                "id": "cc4227a997e0e50d1ba84d86f6e3b62a",
                "name": "Richard L. Francisco",
                "address": "320 East 188th Street",
                "email": "richard_l._francisco_10468@gmail.com"
            },
            {
                "id": "636cbee2c0e0ce8a0b33ed57ffd2336c",
                "name": "Sameer K Misra",
                "address": "39 East Broadway Suite 307",
                "email": "sameer_k_misra_10016@gmail.com"
            },
            {
                "id": "63cd21914049cb467fde019154a908ba",
                "name": "Todd McNiff",
                "address": "775 57th Street",
                "email": "todd_mcniff_11219@gmail.com"
            },
            {
                "id": "ce1bcaca4254e50c5812af2c0b606e60",
                "name": "Vidya Valada",
                "address": "4543 43rd Street",
                "email": "vidya_valada_11372@gmail.com"
            },
            {
                "id": "d601cfd5854acaf5073d260bc08b45f9",
                "name": "Jill Swenson",
                "address": "83-10 Queens Blvd",
                "email": "jill_swenson_11372@gmail.com"
            },
            {
                "id": "d44dc3e999bd039454ce156c2e31a2ed",
                "name": "Aurea Quiroz",
                "address": "251 E 33RD ST LBBY 1N",
                "email": "aurea_quiroz_10003@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "fa96f05683219520088b3c2be2f996a6",
                "name": "STELLA MILOS",
                "address": "4335 Hylan Blvd",
                "email": "stella_milos_10312@gmail.com"
            },
            {
                "id": "5a074069ea0b1ac3de919e6b2d454d04",
                "name": "Joseph Frager",
                "address": "43-20A Roosevelt Avenue",
                "email": "joseph_frager_11355@gmail.com"
            },
            {
                "id": "2d5c6969abda7e9ff41b101c3363bd87",
                "name": "Yuping Chen",
                "address": "745 Nostrand Avenue",
                "email": "yuping_chen_11220@gmail.com"
            },
            {
                "id": "e4c8d14bc07f23c90108bb5d1177c188",
                "name": "Nadia Martinez de Pimentel",
                "address": "1627 Broadway",
                "email": "nadia_martinez_de_pimentel_10032@gmail.com"
            },
            {
                "id": "a0a446e90dbdcffe4462dab941a9de38",
                "name": "Modi Phiroza",
                "address": "121A West 20th Street",
                "email": "modi_phiroza_10021@gmail.com"
            },
            {
                "id": "b6a93ee20ce5aabdeaed941125a08185",
                "name": "Helen Hsieh",
                "address": "4335 Hylan Blvd",
                "email": "helen_hsieh_10312@gmail.com"
            },
            {
                "id": "e66d9b26d97cce1e83596a3ceb525dde",
                "name": "JI-QING WEI",
                "address": "113-11 Jamaica Ave,",
                "email": "ji-qing_wei_11354@gmail.com"
            },
            {
                "id": "96b987db2ab487a209f5e6d868910d8a",
                "name": "Nadge Coupet",
                "address": "131-76 Laurelton Parkway",
                "email": "nadge_coupet_11411@gmail.com"
            },
            {
                "id": "2b435a90b34f3e7e3850335b7a7034bd",
                "name": "Jessica Huang",
                "address": "136-20 38th Ave Suite 6M",
                "email": "jessica_huang_11368@gmail.com"
            },
            {
                "id": "451134ff3bf2ac33faf942ab9449ea99",
                "name": "Reucar Quijada",
                "address": "5 Avenue I",
                "email": "reucar_quijada_11211@gmail.com"
            },
            {
                "id": "f318c40e58aebe946fd99e6c426f9c00",
                "name": "Jacques Antoine",
                "address": "112-03 Queens Blvd",
                "email": "jacques_antoine_11354@gmail.com"
            },
            {
                "id": "ae3f7867d2b2e837c2ac05d75066448a",
                "name": "Alexander Merson",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "alexander_merson_10462@gmail.com"
            },
            {
                "id": "7c489bf528639f6c728ccbfa48bd95e0",
                "name": "Boris Sagalovich",
                "address": "1280 Givan Avenue",
                "email": "boris_sagalovich_10453@gmail.com"
            },
            {
                "id": "357d46e45024951dce1eeeefca85e916",
                "name": "Chaim Wanounou",
                "address": "41-61 Kissena Blvd.",
                "email": "chaim_wanounou_11355@gmail.com"
            },
            {
                "id": "60d11469d0cd45cf2ba4df298af729c8",
                "name": "Bin Yang",
                "address": "444 Willis Avenue",
                "email": "bin_yang_10468@gmail.com"
            },
            {
                "id": "f5a31d80f05dbbd430565eec888f7fe1",
                "name": "Hong Ye",
                "address": "1153 58 Street",
                "email": "hong_ye_11213@gmail.com"
            },
            {
                "id": "f522d52317105d1d8741702b99665eed",
                "name": "Mukund Mody",
                "address": "450 Clarkson Ave",
                "email": "mukund_mody_11203@gmail.com"
            },
            {
                "id": "17ffdaccce8632bed7171c4a195e151c",
                "name": "Steven Barkoff",
                "address": "1153 58 Street",
                "email": "steven_barkoff_11213@gmail.com"
            },
            {
                "id": "4a32be191aa2ea2ab9ad37279ab5df20",
                "name": "Emancia Neil",
                "address": "123 Lafayette Street, 6th floor",
                "email": "emancia_neil_10013@gmail.com"
            },
            {
                "id": "4619eedecb2a4bc74e17fc27a91f2c14",
                "name": "Joseph Mintah",
                "address": "121-02 Hillside Avenue",
                "email": "joseph_mintah_11203@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "05953d8d4ef82944f6e9721bc1db6c1c",
                "name": "Punyadechi Photangtham",
                "address": "520 Neptune avenue",
                "email": "punyadechi_photangtham_11224@gmail.com"
            },
            {
                "id": "71b8c825e1b9b56e2a4c4e14f2321f97",
                "name": "Carlos Gonzalez",
                "address": "446 Mcdonald Ave",
                "email": "carlos_gonzalez_11215@gmail.com"
            },
            {
                "id": "9df915fecda7ea9a4016e211c1834b9b",
                "name": "Juan A. Medina",
                "address": "217 Ovington Avenue",
                "email": "juan_a._medina_11210@gmail.com"
            },
            {
                "id": "d58f0be22f49bd12a95ce87ba1d6ded6",
                "name": "Caesar Preposi",
                "address": "-",
                "email": "caesar_preposi_11205@gmail.com"
            },
            {
                "id": "223178f59ab5adcb6363161bbdf10225",
                "name": "Jose Fibrellet",
                "address": "161 Madison Ave",
                "email": "jose_fibrellet_10027@gmail.com"
            },
            {
                "id": "076a15404f9b508e438a51dbab2f267f",
                "name": "Etan Kurland",
                "address": "93-20 A Roosevelt Avenue",
                "email": "etan_kurland_11103@gmail.com"
            },
            {
                "id": "0805c1342981f4f3b7ac5f94cf9ff3a5",
                "name": "Kecia Gerlach",
                "address": "121A West 20th Street",
                "email": "kecia_gerlach_10021@gmail.com"
            },
            {
                "id": "d630d55d64e4dc9a8aa45ccc685b54dd",
                "name": "Timothy Au",
                "address": "2015 Grand Concourse",
                "email": "timothy_au_10467@gmail.com"
            },
            {
                "id": "5ded6a82e74123144e99805249ba7b71",
                "name": "Oleq Davie",
                "address": "131-24 Rockaway Blvd",
                "email": "oleq_davie_11373@gmail.com"
            },
            {
                "id": "399b03cf76ee27d7e745c29a52418c46",
                "name": "Thao Ngo",
                "address": "145 Chambers St.",
                "email": "thao_ngo_10040@gmail.com"
            },
            {
                "id": "70f3c62b2b1897eea0fdb3cbbe8eee17",
                "name": "Jitendra Patel",
                "address": "42-36 82 STREET C-CF",
                "email": "jitendra_patel_11375@gmail.com"
            },
            {
                "id": "2d193a9148e82aecd40f6ed13aaacb92",
                "name": "HANI HABIB",
                "address": "64-15 Fresh Pond Rd",
                "email": "hani_habib_11418@gmail.com"
            },
            {
                "id": "2712a9eedb6609ef01e37855459d0932",
                "name": "Leticia Gonzalez .",
                "address": "131-24 Rockawaty Blvd",
                "email": "leticia_gonzalez_._11693@gmail.com"
            },
            {
                "id": "54687ab387fe80fcbf2541579ac6a637",
                "name": "Prakash Kancherla",
                "address": "391 Eastern Parkway",
                "email": "prakash_kancherla_11204@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "7a1029912d9f7e5c1e54c8279da8a33c",
                "name": "MUHAMMAD BILLAH",
                "address": "314 West 14th Street",
                "email": "muhammad_billah_11355@gmail.com"
            },
            {
                "id": "5410729edccad7eedba5d0a01f4a2a9a",
                "name": "Oluwatoyosi Dairo",
                "address": "225 east 149th street",
                "email": "oluwatoyosi_dairo_10453@gmail.com"
            },
            {
                "id": "9658fa4f6bc23316bbcf7e83a6921551",
                "name": "Eliahu Samra",
                "address": "540 East New York Avenue",
                "email": "eliahu_samra_11219@gmail.com"
            },
            {
                "id": "e8fb4bfb7eb6b2d6b471464c9f1e5aa4",
                "name": "David Winter",
                "address": "2385 Arthur Avenue, Suite 206",
                "email": "david_winter_10453@gmail.com"
            },
            {
                "id": "00635719adc5fe5b0e139b4837e96296",
                "name": "Nicolas Rossetti",
                "address": "2015 Grand Concourse",
                "email": "nicolas_rossetti_10467@gmail.com"
            },
            {
                "id": "dc60483fae6b63b659d6a612a2c774a3",
                "name": "Yuliya Giyaur",
                "address": "1565 Grand Concourse",
                "email": "yuliya_giyaur_10451@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "b92cb691c0434808b553d37a39282710",
                "name": "Jessica Borrero",
                "address": "176-60 Union Turnpike, Suite 145",
                "email": "jessica_borrero_11355@gmail.com"
            },
            {
                "id": "d2f4a14df6b761c5cc0a7b8cf7ff7dfe",
                "name": "Rita Goldvug",
                "address": "115 Central Park West",
                "email": "rita_goldvug_10011@gmail.com"
            },
            {
                "id": "71d3c5d23130adb437ce596c53673cb4",
                "name": "Xiandong Shi",
                "address": "629 W 185th St",
                "email": "xiandong_shi_10016@gmail.com"
            },
            {
                "id": "8e21990cddfb945a95da87568d2e6ddb",
                "name": "BREDY PIERRE-LOUIS MD",
                "address": "245 East 35th Street",
                "email": "bredy_pierre-louis_md_10012@gmail.com"
            },
            {
                "id": "63044396efb72f87f5c109a298ebc1de",
                "name": "Jubil Malieckal",
                "address": "139-16 91st Avenue",
                "email": "jubil_malieckal_10453@gmail.com"
            },
            {
                "id": "b94707c3e6647f5cefccff6118934c72",
                "name": "JOHN CAHILL",
                "address": "102-11 Roosevelt Avenue",
                "email": "john_cahill_10011@gmail.com"
            },
            {
                "id": "5b00d80b96052b2d320adc4c6d199ad8",
                "name": "Chrystian Belliard",
                "address": "1627 Broadway",
                "email": "chrystian_belliard_10032@gmail.com"
            },
            {
                "id": "d1d1f7d423f16dcff3fab1dc73e59361",
                "name": "Provat Das",
                "address": "25-52 STEINWAY STREET",
                "email": "provat_das_11691@gmail.com"
            },
            {
                "id": "c420cfe7b0fe39b8a0f4c84fb0d06de5",
                "name": "Jorge Cornielle",
                "address": "160 Parkside Ave, Suite 1D",
                "email": "jorge_cornielle_11220@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "b07894f8e9caac2195c0cff6f33435ea",
                "name": "Josefa Grech",
                "address": "9817 Queens Boulevard, LL2",
                "email": "josefa_grech_11368@gmail.com"
            },
            {
                "id": "b7ad71d6f96036c8b972a90b0424fe78",
                "name": "Roxanne Hobbs-Green",
                "address": "1236 FULTON STREET",
                "email": "roxanne_hobbs-green_11419@gmail.com"
            },
            {
                "id": "3ce53938fec6e3f9f5e00bac3595341d",
                "name": "Diego Ponieman",
                "address": "911 Park Ave",
                "email": "diego_ponieman_10002@gmail.com"
            },
            {
                "id": "6dc3f7ae62f29cfe6b2a6bc678b20bc1",
                "name": "Dionicio Trejo",
                "address": "1121 coney island ave",
                "email": "dionicio_trejo_11216@gmail.com"
            },
            {
                "id": "df7ef0ddae7ed72394e16405b101d2aa",
                "name": "Jennifer Figueroa",
                "address": "596 Pennsylvania Avenue",
                "email": "jennifer_figueroa_11218@gmail.com"
            },
            {
                "id": "bb1db69f05ba53489406abce6a7cd118",
                "name": "Melina Mejia",
                "address": "72-35 112th St",
                "email": "melina_mejia_11420@gmail.com"
            },
            {
                "id": "65a5d1a5d587c525d9bf6b6236d139c0",
                "name": "Christopher Phang",
                "address": "113-11 Jamaica Ave,",
                "email": "christopher_phang_11354@gmail.com"
            },
            {
                "id": "7385fc6e89ebbdd3fe250c190e4a87eb",
                "name": "Nedjie Pierre",
                "address": "102-11 Roosevelt Avenue",
                "email": "nedjie_pierre_10011@gmail.com"
            },
            {
                "id": "7891eca3d13bd121dc91041eee196172",
                "name": "Anming Luo",
                "address": "125 East 86th Street",
                "email": "anming_luo_10031@gmail.com"
            },
            {
                "id": "e739e7fc3876a72b0f7ec31623fd9c59",
                "name": "Bassam Aldaia",
                "address": "4260 Broadway",
                "email": "bassam_aldaia_10027@gmail.com"
            },
            {
                "id": "eb36d75dbea530839355d9f0d44b38c4",
                "name": "Haroutyoun Margossian",
                "address": "622 Schnedctady Avenue",
                "email": "haroutyoun_margossian_11203@gmail.com"
            },
            {
                "id": "1d95cebefa8464c6c6a5e401d4fb988c",
                "name": "Most Jahan Begum",
                "address": "2426 Eastchester Road",
                "email": "most_jahan_begum_10458@gmail.com"
            },
            {
                "id": "6e2c82e2c992d0031a19a9aad41de161",
                "name": "Rita Khanijou",
                "address": "210 W 139th St",
                "email": "rita_khanijou_10002@gmail.com"
            },
            {
                "id": "b4ad909a4eba9f48433ab8f8a207c921",
                "name": "Christine Rodler",
                "address": "4207 30th Avenue",
                "email": "christine_rodler_11435@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "ea03b2f4e6b88d052ad85fadcea20640",
                "name": "Mariela Jimenez",
                "address": "1335 Ocean Parkway",
                "email": "mariela_jimenez_11213@gmail.com"
            },
            {
                "id": "3fd32cfef7413f01aa5e622a9baa34d8",
                "name": "Shirishbhai Patel",
                "address": "12102 Hillside Avenue",
                "email": "shirishbhai_patel_11217@gmail.com"
            },
            {
                "id": "b1d2a57fe0b25dee9fc82bd435821c1f",
                "name": "Avi Bitton",
                "address": "1335 Linden Blvd, Suite 117",
                "email": "avi_bitton_11210@gmail.com"
            },
            {
                "id": "e8fda70a21a5647283a973c566585489",
                "name": "Rilee Chowlera",
                "address": "217 Ovington Avenue",
                "email": "rilee_chowlera_11210@gmail.com"
            },
            {
                "id": "43d3312a904694cbf2ae26b2e3d267d9",
                "name": "Florence Pua",
                "address": "41-60 Main Street #217",
                "email": "florence_pua_11354@gmail.com"
            },
            {
                "id": "6df53a04697bada390c2c8cc443bc039",
                "name": "Candido Norberto",
                "address": "93-20 A Roosevelt Avenue",
                "email": "candido_norberto_11103@gmail.com"
            },
            {
                "id": "84720f162cc911a3294cc534fd15e205",
                "name": "Jilan Shah",
                "address": "4260 Broadway",
                "email": "jilan_shah_10027@gmail.com"
            },
            {
                "id": "113839b06a5e39cad405f79373109a68",
                "name": "Gang Meng",
                "address": "86 East 49 st , suite G",
                "email": "gang_meng_11230@gmail.com"
            },
            {
                "id": "2994135080f953d245fb95e27910a595",
                "name": "Alcedo Cruz",
                "address": "47-17 157 STREET",
                "email": "alcedo_cruz_11373@gmail.com"
            },
            {
                "id": "957a50e3fbcf697a003e54bb68e875ef",
                "name": "David Stein",
                "address": "1545 Atlantic Avenue, Suite 108",
                "email": "david_stein_11230@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "1e19c2304e41f5a051c548765b72ff86",
                "name": "Sotirios Kassapidis",
                "address": "113-11 Jamaica Ave,",
                "email": "sotirios_kassapidis_11354@gmail.com"
            },
            {
                "id": "14fc149e292d64362c30d5dad9962f79",
                "name": "Vi Quach",
                "address": "1153 58th Street",
                "email": "vi_quach_11211@gmail.com"
            },
            {
                "id": "b48714164f7a38a3258734ad9dc60ee2",
                "name": "Jack Levine",
                "address": "581 W 161 STREET",
                "email": "jack_levine_10107@gmail.com"
            },
            {
                "id": "dd5b5deb83430dab32412255e90c6bcd",
                "name": "Mario Saint-Laurent",
                "address": "42 Broadway Ave",
                "email": "mario_saint-laurent_10028@gmail.com"
            },
            {
                "id": "a50806ac9600cbfe9088cedd3711b47c",
                "name": "Stuart Goldwasser",
                "address": "445 Park Avenue",
                "email": "stuart_goldwasser_11211@gmail.com"
            },
            {
                "id": "e2ab59b61c7f44724f892398353b94ad",
                "name": "Abdulla Alwani",
                "address": "2 West 86th Street Suite 4",
                "email": "abdulla_alwani_10013@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "3e3c96943451de8df7ae19b53e67b155",
                "name": "Camille Philippe",
                "address": "102-11 Roosevelt Avenue",
                "email": "camille_philippe_10011@gmail.com"
            },
            {
                "id": "d9921a51a87849f5eca60847a5e6bd62",
                "name": "Margaret Kearns-Stanley",
                "address": "48 Market St., Suite B",
                "email": "margaret_kearns-stanley_10003@gmail.com"
            },
            {
                "id": "40af4ca2b74a6e115d50f0a6b2dd6e68",
                "name": "Robert Romanoff",
                "address": "629 West 185th Street",
                "email": "robert_romanoff_11372@gmail.com"
            },
            {
                "id": "1e0e4db928cfcb795537d0f7a73240d8",
                "name": "Bingjing Roberts",
                "address": "410 Lakeville Road, Suite 202",
                "email": "bingjing_roberts_11377@gmail.com"
            },
            {
                "id": "593ff1208266b313090b2b2e32f4d7f1",
                "name": "Timothy Wong",
                "address": "43-70 Kissena Blvd, 1L",
                "email": "timothy_wong_11374@gmail.com"
            },
            {
                "id": "e93fdf734c0304715ddb3a35a46b16f5",
                "name": "Muhammad Haque",
                "address": "66 38 FOREST AVENUE",
                "email": "muhammad_haque_11042@gmail.com"
            },
            {
                "id": "5ee8225819f2ba5e3fdcc87bc228d99d",
                "name": "John Munoz",
                "address": "63-118 Woodhaven Blvd",
                "email": "john_munoz_11355@gmail.com"
            },
            {
                "id": "c9e3aaef3739c867a8bb9a62a778a9ac",
                "name": "Mark Joseph",
                "address": "123 Lafayette Street, 6th floor",
                "email": "mark_joseph_10013@gmail.com"
            },
            {
                "id": "9bfbb73537513bd8c746389b744cd5b1",
                "name": "Lourdes Aguayo",
                "address": "739 Knickerbocker Avenue",
                "email": "lourdes_aguayo_11203@gmail.com"
            },
            {
                "id": "03761a286e1fc0605939f3504b58653a",
                "name": "Vinay Shah",
                "address": "445 Park Avenue",
                "email": "vinay_shah_11211@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "44ef48a724e9a769093efbd9fe29257c",
                "name": "Lilliam Soto-Alcantara",
                "address": "3016 GLENWOOD RD",
                "email": "lilliam_soto-alcantara_11209@gmail.com"
            },
            {
                "id": "8bac7ddaeba5d8d68c0c08ee52b43121",
                "name": "Letha Daniel",
                "address": "520 Neptune avenue",
                "email": "letha_daniel_11224@gmail.com"
            },
            {
                "id": "5dff4a4620da36f3fea12c04da50c868",
                "name": "Bruce Chung",
                "address": "6414 Bay Park Way",
                "email": "bruce_chung_11212@gmail.com"
            },
            {
                "id": "2d40ccb031252210d8287b2c7cdacfae",
                "name": "Patrick Dalton",
                "address": "205-16 Linden blvd",
                "email": "patrick_dalton_11377@gmail.com"
            },
            {
                "id": "bbab8e13ce0664f990622698d9696605",
                "name": "Dov Grant",
                "address": "170 West 12th Street",
                "email": "dov_grant_10033@gmail.com"
            },
            {
                "id": "6437482866c80a33eaaf641897e394c2",
                "name": "Leon Scrimmager",
                "address": "3071 Perry Avenue",
                "email": "leon_scrimmager_10453@gmail.com"
            },
            {
                "id": "ee34381bc3ef4cb93bd913350d7e2c3a",
                "name": "Natalie Wilson",
                "address": "350 Ocean Ave, 1B",
                "email": "natalie_wilson_11218@gmail.com"
            },
            {
                "id": "4c62ac846d784c4c7797a0639b101616",
                "name": "Roland Nyein",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "roland_nyein_10462@gmail.com"
            },
            {
                "id": "a5a9e28da521510cd7e3af3890458295",
                "name": "Deqing Sun",
                "address": "571 Academy Street, Apt. GLE",
                "email": "deqing_sun_10016@gmail.com"
            },
            {
                "id": "c62a6d0ad75866ec80df7c9412f7066e",
                "name": "Donald Martinelli",
                "address": "159-05 92nd St.",
                "email": "donald_martinelli_11367@gmail.com"
            },
            {
                "id": "db5e8ae5a3ae44fd8eb0900d36792808",
                "name": "Leung Wing Wong",
                "address": "13338 41 ROAD, SUITE 2Q",
                "email": "leung_wing_wong_11355@gmail.com"
            },
            {
                "id": "a26dab48f6e05a46f4e75ba4715d1a0a",
                "name": "Olga Tyuleneva",
                "address": "264 1st Street",
                "email": "olga_tyuleneva_11210@gmail.com"
            },
            {
                "id": "503726e7288eb7dfe64eff136108e63c",
                "name": "Elna Tamayo-Prado",
                "address": "3071 Perry Avenue",
                "email": "elna_tamayo-prado_10453@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "35746014729179a74559343fb5af7436",
                "name": "Yehuda Bar-Zvi",
                "address": "133-36 41st Road, Suite 1",
                "email": "yehuda_bar-zvi_11372@gmail.com"
            },
            {
                "id": "c8d1f8455e17f0c30a1b4941cb895f6a",
                "name": "Angela Hon",
                "address": "1262 Boston Road",
                "email": "angela_hon_10463@gmail.com"
            },
            {
                "id": "8149d25c3e09995707209c3a38bc57d4",
                "name": "Nina Priven",
                "address": "2235 8th Avenue",
                "email": "nina_priven_10033@gmail.com"
            },
            {
                "id": "bff9f689755ad1f4d131189297662045",
                "name": "Jose Vargas",
                "address": "446 mcdonald ave",
                "email": "jose_vargas_11211@gmail.com"
            },
            {
                "id": "7e5fd5581e71c984fb189d2d8b20bff5",
                "name": "Xiaxi HU",
                "address": "43-20A Roosevelt Avenue",
                "email": "xiaxi_hu_11355@gmail.com"
            },
            {
                "id": "05443baff0c78fad1fdadd9845047581",
                "name": "Lucy Palomino",
                "address": "594 Broadway Suite 310",
                "email": "lucy_palomino_10016@gmail.com"
            },
            {
                "id": "65144aa4cfc607f7f1c625e481fdd81c",
                "name": "Stellios Trikounakis",
                "address": "155 W. 19th St 4th floor",
                "email": "stellios_trikounakis_10034@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "b1ef9be57e51b90c11d49a44745a1c16",
                "name": "Alan Katz",
                "address": "102-11 Roosevelt Avenue",
                "email": "alan_katz_10011@gmail.com"
            },
            {
                "id": "fd3b6c37c491c7319fbc61a277d7421b",
                "name": "Nick Gianoukakis",
                "address": "5722 7th ave",
                "email": "nick_gianoukakis_11238@gmail.com"
            },
            {
                "id": "f9d1ba7767738cade4a70b3e27bc2e49",
                "name": "Judah Charnoff",
                "address": "3071 Perry Avenue",
                "email": "judah_charnoff_10453@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "6c35341b898caabd2090775dfea28329",
                "name": "Alice Lau",
                "address": "212 E 70th st",
                "email": "alice_lau_10013@gmail.com"
            },
            {
                "id": "2cb049d392706988d09fe326f0a363c4",
                "name": "Patricia Leone",
                "address": "245 East 35th Street",
                "email": "patricia_leone_10012@gmail.com"
            },
            {
                "id": "c670bc34d97882cfb360f3e2f4922216",
                "name": "Arthur Manning",
                "address": "160 East 32nd St",
                "email": "arthur_manning_10010@gmail.com"
            },
            {
                "id": "2060da960cabd0f613759303f42ff540",
                "name": "Mary Noecker",
                "address": "305 Seguine Ave Ste. 1",
                "email": "mary_noecker_10305@gmail.com"
            },
            {
                "id": "69d15ecdef8d9757fc537962045e0bbf",
                "name": "David Gomez",
                "address": "450 clarkson ave",
                "email": "david_gomez_11212@gmail.com"
            },
            {
                "id": "6bb6c84d5d8a298c6e96f49515265155",
                "name": "Betty Punzalan",
                "address": "40 West 135th Street",
                "email": "betty_punzalan_10128@gmail.com"
            },
            {
                "id": "767cdfa295171fba9dcd3c335a476bdf",
                "name": "Janet Collins",
                "address": "95 University Place",
                "email": "janet_collins_10011@gmail.com"
            },
            {
                "id": "d335d8b29d8b64449c6c776953f6684c",
                "name": "GARY ABBERBOCK",
                "address": "706 Banner Ave.",
                "email": "gary_abberbock_11220@gmail.com"
            },
            {
                "id": "2ac0a89541b6d623f97baa5506cdd085",
                "name": "Edna Anne Pytlak",
                "address": "19 Bowery, 2nd floor",
                "email": "edna_anne_pytlak_10011@gmail.com"
            },
            {
                "id": "6231eeefeccc5ad41885f17f6831669a",
                "name": "Ashley Ray",
                "address": "3071 Perry Avenue",
                "email": "ashley_ray_10453@gmail.com"
            },
            {
                "id": "f771d5e916bcf03f2f19a4cd306cf7ed",
                "name": "Himanshu Goel",
                "address": "753 Classon Avenue Suite LJ",
                "email": "himanshu_goel_11219@gmail.com"
            },
            {
                "id": "a66ed6b33ec88de8a1f8ce751c7fcac5",
                "name": "Rosemarie Pezzulo",
                "address": "5303 8th ave",
                "email": "rosemarie_pezzulo_11220@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "9f28d03032d3b46b81831dd126d2e9a4",
                "name": "Maria Qyezada",
                "address": "41-60 Main St. #205B",
                "email": "maria_qyezada_11354@gmail.com"
            },
            {
                "id": "916eae313e48a728a2908fed69ffda95",
                "name": "Fazlul Yusuf",
                "address": "1627 Broadway",
                "email": "fazlul_yusuf_10032@gmail.com"
            },
            {
                "id": "118e47ffca32e308114d891b96fc76cf",
                "name": "Juan Chabla",
                "address": "2248 Richmond Road",
                "email": "juan_chabla_10312@gmail.com"
            },
            {
                "id": "c227f1f057286d974e41b4b0c4b9a270",
                "name": "Franz Goyzueta",
                "address": "3907 Prince St",
                "email": "franz_goyzueta_11418@gmail.com"
            },
            {
                "id": "17cf8a48bee5711d21deef261d3d55b4",
                "name": "Jee Sook Lee",
                "address": "75-80 184th Street, Union Tpk.",
                "email": "jee_sook_lee_11372@gmail.com"
            },
            {
                "id": "d963c160eede8425f9125e4db743b1f3",
                "name": "Jin Wang",
                "address": "4434 Amboy Road",
                "email": "jin_wang_11356@gmail.com"
            },
            {
                "id": "4bac50640fd363dc8dab2aa4be0d3684",
                "name": "Joseph Caruana",
                "address": "37-11 88th Street",
                "email": "joseph_caruana_11355@gmail.com"
            },
            {
                "id": "f2e1a9647d40dc197d258042ea9b9133",
                "name": "Temitope Jose",
                "address": "225A E. 149th Street",
                "email": "temitope_jose_10467@gmail.com"
            },
            {
                "id": "fb758730c7408a0817f324395820f92e",
                "name": "Rosemarie St. Victor",
                "address": "2 West 86th Street Suite 4",
                "email": "rosemarie_st._victor_10013@gmail.com"
            },
            {
                "id": "8d7d01107c6523561d7f4c17fbce59df",
                "name": "Stephanie Chambers",
                "address": "124 E 43rd St",
                "email": "stephanie_chambers_11213@gmail.com"
            },
            {
                "id": "708e90b8499141209c14a114f30536d0",
                "name": "Susan Merguerian",
                "address": "112-03 Queens Blvd, Suite 207",
                "email": "susan_merguerian_11368@gmail.com"
            },
            {
                "id": "bf024293e2ac0ec5bca2128d643615a5",
                "name": "Juan Estevez",
                "address": "2091 Nostrant Avenue",
                "email": "juan_estevez_11210@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "440c2b132b7b53403d183ebe0fa287b7",
                "name": "Dalia Olivier",
                "address": "20 Park Avenue",
                "email": "dalia_olivier_10013@gmail.com"
            },
            {
                "id": "227ec4b0cd7231b272f2f9960f2f09ef",
                "name": "Charles Chan",
                "address": "43-20A Roosevelt Avenue",
                "email": "charles_chan_11355@gmail.com"
            },
            {
                "id": "a1be7bc1329eff05e17673fcb5de8eb8",
                "name": "Diana Wynt",
                "address": "800 manor road suite 4",
                "email": "diana_wynt_10304@gmail.com"
            },
            {
                "id": "d25a7f203ee8ffeed90afe6515582f58",
                "name": "Norman Klein",
                "address": "3131 Grand Concourse Site 113",
                "email": "norman_klein_10467@gmail.com"
            },
            {
                "id": "ebb038ed963da5531b167f42614bc083",
                "name": "Sudha Patel",
                "address": "1204 Beach 9 St",
                "email": "sudha_patel_11103@gmail.com"
            },
            {
                "id": "d71c3c35b529e41fd677c13f940978c9",
                "name": "Dalan Sow Read",
                "address": "112-03 Queens Blvd, Suite 207",
                "email": "dalan_sow_read_11368@gmail.com"
            },
            {
                "id": "0feeeaa645c8a201cfaa5be5983c1847",
                "name": "Julio Ramirez",
                "address": "1963-A DALY AVE",
                "email": "julio_ramirez_10457@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "a9123f897c54e4a92b2c92489ea9efdf",
                "name": "Arturo Caesar",
                "address": "40-08 Forley Street",
                "email": "arturo_caesar_11432@gmail.com"
            },
            {
                "id": "e6c694070f791ad2f24370583371c815",
                "name": "Van Hong Nguyen",
                "address": "435 FORT WASHINGTON AVE",
                "email": "van_hong_nguyen_10032@gmail.com"
            },
            {
                "id": "fe01118caace6d3d2ab3edb2cc98b382",
                "name": "Yick Moon Lee",
                "address": "254 Canal street, Room 2006",
                "email": "yick_moon_lee_10033@gmail.com"
            },
            {
                "id": "0ac8e0ecfd0e78448d2c3b5a4e74a6ab",
                "name": "David Cotos-Mejia",
                "address": "200 Cabrini Boulevard, Suite 17",
                "email": "david_cotos-mejia_10034@gmail.com"
            },
            {
                "id": "a769baca019872aa77f6107607378295",
                "name": "Norman Greeley",
                "address": "97-77 Queens Blvd, Suite 900",
                "email": "norman_greeley_11373@gmail.com"
            },
            {
                "id": "80a1315fbd5e442cfef9a83c6e4fcf51",
                "name": "Robert Zaloom",
                "address": "147-15 70TH RD",
                "email": "robert_zaloom_11355@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "a83306d4fa4c52513b90694eb8b4d6d9",
                "name": "Polina Liss",
                "address": "8684 15th Avenue",
                "email": "polina_liss_11206@gmail.com"
            },
            {
                "id": "1bfd9074b3d11f00687e63e573a40ffc",
                "name": "Ramakrishna Karibandi",
                "address": "3071 Perry Avenue",
                "email": "ramakrishna_karibandi_10453@gmail.com"
            },
            {
                "id": "85cd4f01f288dcb870d6f0b56f4e03cc",
                "name": "Charles Nordin",
                "address": "2248 Richmond Road",
                "email": "charles_nordin_10312@gmail.com"
            },
            {
                "id": "9f935519b8587e95540ffa700d27a824",
                "name": "Aleksander Shalshin",
                "address": "600 West 150th Street",
                "email": "aleksander_shalshin_10030@gmail.com"
            }
        ]
    },
    "Brooklyn": {
        "pulmonologist": [
            {
                "id": "8aeac5866c3f3735c7e01a7563b195f8",
                "name": "Mun Hong",
                "address": "42-31 Colden Street, #109",
                "email": "mun_hong_11375@gmail.com"
            },
            {
                "id": "614ee19aff5a32f24c9cea6a4eb99b0b",
                "name": "Subrahmanya Bhat",
                "address": "87-04 Rockaway Beach Blvd",
                "email": "subrahmanya_bhat_11377@gmail.com"
            },
            {
                "id": "58e00ddd7fcc9d8d49d1b5a0b343c58d",
                "name": "Pedro Corzo",
                "address": "97-25 63rd Drive, 1st Floor",
                "email": "pedro_corzo_11416@gmail.com"
            },
            {
                "id": "5054603ccabe3f413bf7aab2681606c5",
                "name": "Anu Kothari",
                "address": "391 Eastern Parkway",
                "email": "anu_kothari_11204@gmail.com"
            },
            {
                "id": "c804c79c78c13254ddf847109d5be0dc",
                "name": "Rushita Patel",
                "address": "410 Lakeville Road",
                "email": "rushita_patel_11373@gmail.com"
            },
            {
                "id": "5ff4137e23204f4eb54baf856d315678",
                "name": "Max Bulmash",
                "address": "67 Irving Place",
                "email": "max_bulmash_10065@gmail.com"
            },
            {
                "id": "8445e89effa2e0d916d84b51c3864f43",
                "name": "Enrique Pagan",
                "address": "43-20A Roosevelt Avenue",
                "email": "enrique_pagan_11355@gmail.com"
            },
            {
                "id": "fa1ee941f116d806c4ac6db0115b9599",
                "name": "Melchor Domingo",
                "address": "11412 BEACH CHANNEL DR",
                "email": "melchor_domingo_11372@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "1701d9e8dadb55c9bc570c01caa15328",
                "name": "Rita Grigiene",
                "address": "245 West 19th Street #CF",
                "email": "rita_grigiene_10128@gmail.com"
            },
            {
                "id": "d11735b04c62720bcb8f6ad155380fb5",
                "name": "Manuel Lopez",
                "address": "1211 White Plains Rd",
                "email": "manuel_lopez_10472@gmail.com"
            },
            {
                "id": "e9e70f8f14410cc353dde32b82d4413c",
                "name": "Michael Sands",
                "address": "-305 Seguine Avenue",
                "email": "michael_sands_10304@gmail.com"
            },
            {
                "id": "4b287f25152a1432d3f4f0cb05761b60",
                "name": "Obiora Anyoku",
                "address": "911 Park Avenue",
                "email": "obiora_anyoku_10044@gmail.com"
            },
            {
                "id": "43218543e58ab7afc1bc16deb81a7af7",
                "name": "Jessica Rubinstein",
                "address": "39 East Broadway Suite 307",
                "email": "jessica_rubinstein_10016@gmail.com"
            },
            {
                "id": "8f967700de5015eecb25c4f31e3e5f74",
                "name": "Albert Levy",
                "address": "83-06 Queens Blvd",
                "email": "albert_levy_11361@gmail.com"
            },
            {
                "id": "593ca28b1ee63e4bdbfd610044b7ac87",
                "name": "Donna Ingram",
                "address": "471 Hart Street",
                "email": "donna_ingram_11235@gmail.com"
            },
            {
                "id": "749870485f8223155abec73e19d75966",
                "name": "Moshe Kerstein",
                "address": "305 e 149th st",
                "email": "moshe_kerstein_10472@gmail.com"
            },
            {
                "id": "2ec881513515e578ff18cec2a8fdc506",
                "name": "Zihe Shan",
                "address": "121A West 20th Street",
                "email": "zihe_shan_10021@gmail.com"
            },
            {
                "id": "d1bbff029510a8ff325cc12a0da2b80b",
                "name": "Neera Ahuja",
                "address": "600 West 150th Street",
                "email": "neera_ahuja_10030@gmail.com"
            },
            {
                "id": "570eaada3834cdc0eefdfd5bc91b8c90",
                "name": "Michael Mazza",
                "address": "139 Centre Street Suite 314",
                "email": "michael_mazza_10031@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "ee73659bf24643c40d71cc82f13d7d77",
                "name": "Paolo Perrone",
                "address": "110-45 Queens Boulevard Suite A",
                "email": "paolo_perrone_11516@gmail.com"
            },
            {
                "id": "e326ae49478bdc0ff9ce55cf6c4e025d",
                "name": "Syed Najeeb Hussaini",
                "address": "1468 Richmond Avenue Ste B",
                "email": "syed_najeeb_hussaini_11356@gmail.com"
            },
            {
                "id": "01c7b43a9b12725b44b31037039a5b96",
                "name": "Xin Tan",
                "address": "1103 Cortelyou Road",
                "email": "xin_tan_11230@gmail.com"
            },
            {
                "id": "0e6eae0391b1e0d40e46d15f5425c6a2",
                "name": "Kevin Charlotten",
                "address": "416 37 St",
                "email": "kevin_charlotten_11219@gmail.com"
            },
            {
                "id": "d8777f008100e240c309ba53bb6cfbd9",
                "name": "Adegboyega T. Adebayo",
                "address": "1001 Grand Concourse, #13",
                "email": "adegboyega_t._adebayo_10456@gmail.com"
            },
            {
                "id": "9c0daa180beaac067a7d0cc88c42a5b1",
                "name": "Faisal Ali",
                "address": "39-07 PRINCE ST. 6H",
                "email": "faisal_ali_11372@gmail.com"
            },
            {
                "id": "d168333e07da9e8fb7cf8207c2e7e33f",
                "name": "Richard Francisco",
                "address": "1650 Selwyn Ave, 6th Floor",
                "email": "richard_francisco_10458@gmail.com"
            },
            {
                "id": "2ec5df52a2acd4b6cc56a422dba792c0",
                "name": "Tze On Poon",
                "address": "796 Drew Street",
                "email": "tze_on_poon_11204@gmail.com"
            },
            {
                "id": "7a9eb390bc3eb7d2478e934e7e9d275a",
                "name": "Israel Bochner",
                "address": "94-13 Flatlands Ave. Suite 101",
                "email": "israel_bochner_11210@gmail.com"
            },
            {
                "id": "8d2717083cf57763f80af41001a49b98",
                "name": "REBECCA RAOOF",
                "address": "1421 E 2ND ST",
                "email": "rebecca_raoof_11219@gmail.com"
            },
            {
                "id": "6457041c534378bc11981aeeec41084b",
                "name": "Virginia Martinez",
                "address": "97-03 Springfield Blvd",
                "email": "virginia_martinez_11377@gmail.com"
            },
            {
                "id": "11a944b9b8f32142b733cb598b515308",
                "name": "Roger Villi",
                "address": "64-17 Broadway",
                "email": "roger_villi_11691@gmail.com"
            },
            {
                "id": "47dd5edb31ced460647685a42487032b",
                "name": "Yoram Amsalem",
                "address": "763 56th Street, 1st floor",
                "email": "yoram_amsalem_11219@gmail.com"
            },
            {
                "id": "0575a2595557c38384aac912c67c4769",
                "name": "Michelle Ratau",
                "address": "3589 Hylan Blvd",
                "email": "michelle_ratau_10312@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "85b90a6adc369cffba76222d0f4b5a5e",
                "name": "Alex Racco",
                "address": "2385 Arthur Avenue, Suite 206",
                "email": "alex_racco_10453@gmail.com"
            },
            {
                "id": "0c60b2be3fb58722ba563f5722fe1feb",
                "name": "Furqan Tejani",
                "address": "435 fort Washington Avenue",
                "email": "furqan_tejani_10065@gmail.com"
            },
            {
                "id": "057ad26f614fdd244f6bd90ada36298b",
                "name": "Mohammad Bhatti",
                "address": "2015 Grand Concourse",
                "email": "mohammad_bhatti_10467@gmail.com"
            },
            {
                "id": "32b01f98cda7d50535e4b7c40a15a5f8",
                "name": "Lucia Alva",
                "address": "911 Park Avenue",
                "email": "lucia_alva_10044@gmail.com"
            },
            {
                "id": "52ec430776c0fb2d260630ee0d8ef84e",
                "name": "Steve Hou",
                "address": "-",
                "email": "steve_hou_11205@gmail.com"
            },
            {
                "id": "95ed138472868f26e9b75526081db1e1",
                "name": "Marina Alayev",
                "address": "40 Montgomery St",
                "email": "marina_alayev_10033@gmail.com"
            },
            {
                "id": "f5a22623c085151d05c29de35389d545",
                "name": "Melissa Furman",
                "address": "36-09 Main Street, Suite 8C",
                "email": "melissa_furman_11423@gmail.com"
            },
            {
                "id": "a2bf179584dc41494101241571b10cb6",
                "name": "Violeta Gomez",
                "address": "410 Lakeville Road",
                "email": "violeta_gomez_11373@gmail.com"
            },
            {
                "id": "5e0f467daf30485177cf16278ef052e3",
                "name": "Wenjing Tao",
                "address": "41-60 Main Street",
                "email": "wenjing_tao_11355@gmail.com"
            },
            {
                "id": "f5c24e5db019db0c2b3ed33e8e7ae803",
                "name": "Papanna Ravichandra, MD",
                "address": "109-33 71 Road, Suite 1B",
                "email": "papanna_ravichandra,_md_11355@gmail.com"
            },
            {
                "id": "88974c1f23a21857ca2d2066aa49e088",
                "name": "Veeraf Sanjana",
                "address": "1624 University Avenue",
                "email": "veeraf_sanjana_10453@gmail.com"
            },
            {
                "id": "a9c82b68fd5ed5234f0189ee9cc36a30",
                "name": "Jun Kang",
                "address": "30-96 51 STREET",
                "email": "jun_kang_11418@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "c0226f53aa81d3cc851d2a627e782cc1",
                "name": "Nancy Wallach",
                "address": "112-03 Queens Blvd.",
                "email": "nancy_wallach_11373@gmail.com"
            },
            {
                "id": "3445e1163e9c3f0ba3972a07590faa25",
                "name": "Svetlana Prokhorova",
                "address": "600 West 150th Street",
                "email": "svetlana_prokhorova_10030@gmail.com"
            },
            {
                "id": "29b0242d8bf4533132fea1c37646314a",
                "name": "Keith Greenberg",
                "address": "83-45 Dongan Ave",
                "email": "keith_greenberg_11418@gmail.com"
            },
            {
                "id": "3bee5aadcb3449be2149c066cca0eef1",
                "name": "Wuhua Jing",
                "address": "1103 Cortelyou Road",
                "email": "wuhua_jing_11230@gmail.com"
            },
            {
                "id": "3a2fdd6b9adcf77fe329889ebbfd9415",
                "name": "Robert Goodman",
                "address": "1718 Pitkin Avenue",
                "email": "robert_goodman_11203@gmail.com"
            },
            {
                "id": "ff0d229c625cda58fe7b0ff589a04ce1",
                "name": "Victoria Katz",
                "address": "205-07 Hillside Avenue",
                "email": "victoria_katz_11368@gmail.com"
            },
            {
                "id": "0c17d240a05c31b190a4e035368a4f5a",
                "name": "Alix Dufresne",
                "address": "1125 FULTON STREET 3RD FLOOR",
                "email": "alix_dufresne_11219@gmail.com"
            },
            {
                "id": "2c1f6da32fa695afdc18d85783d2073c",
                "name": "Carl Franzetti",
                "address": "43-12 43rd Street",
                "email": "carl_franzetti_11223@gmail.com"
            },
            {
                "id": "d07906ccea4a3d80945501c2de119508",
                "name": "Dassa Gabriel",
                "address": "29-28 41st Avenue",
                "email": "dassa_gabriel_11355@gmail.com"
            },
            {
                "id": "8aaa3205ab4a623a5dd0ba038c027e09",
                "name": "Ana Olivero",
                "address": "83-45 Dongan Ave",
                "email": "ana_olivero_11418@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "9680e741ce4c650e7531a1ec62cefc4a",
                "name": "Ahmad Kamal Aslam",
                "address": "2494 Williamsbridge Rd.",
                "email": "ahmad_kamal_aslam_10453@gmail.com"
            },
            {
                "id": "daacf85ca4366fefb22aaa85d38889e9",
                "name": "Kevin Charlotten",
                "address": "210 E 86th St",
                "email": "kevin_charlotten_10011@gmail.com"
            },
            {
                "id": "85dbc5bdde3dfd1926e3292295fe623b",
                "name": "Felicitas Santiago",
                "address": "563 Grand Street",
                "email": "felicitas_santiago_11213@gmail.com"
            },
            {
                "id": "6125dad2c0c1ccd42e5f8c062b9efc33",
                "name": "Joseph Roosevelt Clerisme",
                "address": "372 Kingston Avenue",
                "email": "joseph_roosevelt_clerisme_11226@gmail.com"
            },
            {
                "id": "221268dd7d4a108f182c9a9cc11823c4",
                "name": "Henry Bellutta",
                "address": "432 Bedford Avenue",
                "email": "henry_bellutta_11208@gmail.com"
            },
            {
                "id": "b705e3bd9f7aeff794d0239caa7b1458",
                "name": "Madhu Malhotra",
                "address": "172-27 Highland Ave, Suite 1 B",
                "email": "madhu_malhotra_11429@gmail.com"
            },
            {
                "id": "1e463ceb12b2ac95622bf96a6732c95b",
                "name": "Eric Jerome",
                "address": "563 Grand Street",
                "email": "eric_jerome_11213@gmail.com"
            },
            {
                "id": "df39e65e138299a280bdf08d21f8bb2f",
                "name": "Mordechai Beityakov",
                "address": "220 A St. Nicholas Avenue",
                "email": "mordechai_beityakov_11237@gmail.com"
            },
            {
                "id": "ae359bab0bdcd3f95f875fe926b5ef9e",
                "name": "Mark Lew",
                "address": "167 Rutledge St",
                "email": "mark_lew_11203@gmail.com"
            },
            {
                "id": "2e315d80ff937bbc25d005eee249ebf8",
                "name": "Donna Simmons",
                "address": "75-17 41ST AVE",
                "email": "donna_simmons_11432@gmail.com"
            }
        ],
        "urologist": [
            {
                "id": "9b99d873d5dfe5699151de7148de75fe",
                "name": "Gopi Punukollu",
                "address": "1446 Broadway Avenue",
                "email": "gopi_punukollu_11238@gmail.com"
            },
            {
                "id": "b6cbf23cdec39922f32bf45cbde7ada8",
                "name": "Dalia Frumkin",
                "address": "2233 Nostrand Avenue",
                "email": "dalia_frumkin_11237@gmail.com"
            },
            {
                "id": "f4b1354db41f4c07fb33c5305c1fc3bd",
                "name": "Jean-Robert Boursiquot",
                "address": "114-06 Queens Blvd",
                "email": "jean-robert_boursiquot_11419@gmail.com"
            },
            {
                "id": "d5d22ec34179a78b08acacc467b5332c",
                "name": "Ricardo Pou",
                "address": "2426 Eastchester Rd, Suite 201",
                "email": "ricardo_pou_10454@gmail.com"
            },
            {
                "id": "5ad837c25ba5959b95d7101c0bb6da29",
                "name": "Moses Shalit",
                "address": "86 East 49th Street",
                "email": "moses_shalit_11237@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "636a4959d80c2c437beb8f5dd57a69d8",
                "name": "Marjorie Dugue",
                "address": "196-15 Hillside Ave",
                "email": "marjorie_dugue_11377@gmail.com"
            },
            {
                "id": "8801427c278c358c0949c813e64c1400",
                "name": "Emmanuel Fashakin",
                "address": "131-24 Rockaway Blvd",
                "email": "emmanuel_fashakin_11373@gmail.com"
            },
            {
                "id": "ff3eedb4ef259dcb45410477196bcdb5",
                "name": "Vincent Yeung",
                "address": "380 2nd Avenue, Suite 1002",
                "email": "vincent_yeung_10028@gmail.com"
            },
            {
                "id": "7cb943ce0ca8b7a6c5ae2be9712bddc1",
                "name": "David Kaplovitz",
                "address": "5211 16 TH AVE.",
                "email": "david_kaplovitz_11219@gmail.com"
            },
            {
                "id": "065fda44d8156f2f94c22eaa34f98df9",
                "name": "Arsenio Miguel Tio",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "arsenio_miguel_tio_10013@gmail.com"
            },
            {
                "id": "68fd7a55d7e665e90ac95117d9e8b8ca",
                "name": "James Pacholka",
                "address": "108 East 96th Street",
                "email": "james_pacholka_10019@gmail.com"
            },
            {
                "id": "fe1221ac3281d752f3f98e9b2c921db6",
                "name": "Elana Altzman",
                "address": "450 Clarkson Ave",
                "email": "elana_altzman_11203@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "ecaaf5d804fde1307548d84524d3882f",
                "name": "Ernst Jean",
                "address": "140 Wadsworth Avenue",
                "email": "ernst_jean_10016@gmail.com"
            },
            {
                "id": "841c130f02437cf920e8096d0f5e397b",
                "name": "Derily Heredia",
                "address": "37-65 104TH. STREET",
                "email": "derily_heredia_11367@gmail.com"
            },
            {
                "id": "4718a72b6bcc3d07be0a97ed71476f0c",
                "name": "Costas Frousios",
                "address": "41-61 Kissena Blvd.",
                "email": "costas_frousios_11355@gmail.com"
            },
            {
                "id": "e2c505886fb4e76d9194ae57ceb4ace9",
                "name": "Cluny Lefevre",
                "address": "86 Bowery Street, 6F",
                "email": "cluny_lefevre_10065@gmail.com"
            },
            {
                "id": "97cb87261da8edf0a5088e163a1ed56b",
                "name": "Dina Louie",
                "address": "67 Irving Place, 5th Floor",
                "email": "dina_louie_10013@gmail.com"
            },
            {
                "id": "7e638cb194d9266100ed31781ce71437",
                "name": "Indira Kairam",
                "address": "113-11 Jamaica Ave,",
                "email": "indira_kairam_11354@gmail.com"
            },
            {
                "id": "0e25fe56467e189a7aeb6857035eccc2",
                "name": "Subash Malhotra",
                "address": "108 East 96th Street",
                "email": "subash_malhotra_10019@gmail.com"
            },
            {
                "id": "109e169831e4ee1b12883bd74552373c",
                "name": "Harvey Mermelstein",
                "address": "247 3rd Ave",
                "email": "harvey_mermelstein_10128@gmail.com"
            },
            {
                "id": "63a55f86a382b444c1c5d89421bbecfe",
                "name": "Cecilia Calderon",
                "address": "185 West End Ave",
                "email": "cecilia_calderon_10075@gmail.com"
            },
            {
                "id": "ad5d0693fd0d1b5e6d2227d956ef22a2",
                "name": "Jude Arthur",
                "address": "48 Market St., Suite B",
                "email": "jude_arthur_10003@gmail.com"
            },
            {
                "id": "20d783b28e139795249663948d145de2",
                "name": "Chidiadi Ododo",
                "address": "112-03 Queens Blvd",
                "email": "chidiadi_ododo_11354@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "f353f52676fd2d23ce1925b1ac373a99",
                "name": "Bernard Levine",
                "address": "189 Montague St. Ste 700",
                "email": "bernard_levine_11205@gmail.com"
            },
            {
                "id": "ed148f9bdd83585e6c6d253f012a0d1c",
                "name": "Ramon Pimentel",
                "address": "139-16 91st Avenue",
                "email": "ramon_pimentel_10453@gmail.com"
            },
            {
                "id": "c50cd196f8541d7845c2bf6d553adbe0",
                "name": "Adedokun Akinyooye",
                "address": "185 Canal St",
                "email": "adedokun_akinyooye_11215@gmail.com"
            },
            {
                "id": "e982c79a14122acc4981ad1c16a34011",
                "name": "Kevin O'Hara",
                "address": "4506 8th Avenue",
                "email": "kevin_o'hara_11203@gmail.com"
            },
            {
                "id": "9aa2eb0d87fca5a69d494b26f7d0f929",
                "name": "Nirupama Somasundaram",
                "address": "133-38 41st Rd Suite 2C",
                "email": "nirupama_somasundaram_11354@gmail.com"
            },
            {
                "id": "8a42bf0dd0c4043fe470dd3cedfe4d3a",
                "name": "Ishita Thakkar",
                "address": "200-03 Linden Blvd",
                "email": "ishita_thakkar_11422@gmail.com"
            },
            {
                "id": "ada7f23ad4d95169397c162a55e0948d",
                "name": "MOHAMMAD CHHIPA",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "mohammad_chhipa_10013@gmail.com"
            },
            {
                "id": "e5abf7cad6aa067bb86280a0ec08394f",
                "name": "Rafael Bueno",
                "address": "-",
                "email": "rafael_bueno_11205@gmail.com"
            },
            {
                "id": "f3106674180e83f06ee81a21a2ce2d07",
                "name": "Paula Carugno",
                "address": "93-20 A Roosevelt Avenue",
                "email": "paula_carugno_11103@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "ff7e67761a4c5ed6d5a5908df8799c40",
                "name": "Joseph Pierre",
                "address": "64 Nagle Avenue",
                "email": "joseph_pierre_10016@gmail.com"
            },
            {
                "id": "775a5d67834a073fa8bd66deb686082e",
                "name": "Norman Lee",
                "address": "139-16 91st Avenue",
                "email": "norman_lee_10453@gmail.com"
            },
            {
                "id": "cd0e373b418a34aa3168a5a8d05ba95a",
                "name": "Alexander Morden",
                "address": "196 canal st",
                "email": "alexander_morden_10023@gmail.com"
            },
            {
                "id": "b3aa852234fda6dc9d12a7ec9254e6f8",
                "name": "Michelle Jacobs",
                "address": "3071 Perry Avenue",
                "email": "michelle_jacobs_10453@gmail.com"
            },
            {
                "id": "8fa54e83756a46cffca456da2b8d8aa5",
                "name": "Aran Degenhardt",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "aran_degenhardt_10013@gmail.com"
            },
            {
                "id": "57791dfa64551b27d4aa5b61b9365e12",
                "name": "Gladstone Gunnis",
                "address": "326 7th Street",
                "email": "gladstone_gunnis_11230@gmail.com"
            },
            {
                "id": "57e18b562d8a4da2dd062c28e387cc6c",
                "name": "Brian Sumner",
                "address": "1070 Southern Blvd",
                "email": "brian_sumner_10458@gmail.com"
            },
            {
                "id": "9de3c61e55417b0b7ba8508b83fdc102",
                "name": "Ofem Ajah",
                "address": "139-16 91st Avenue",
                "email": "ofem_ajah_10453@gmail.com"
            },
            {
                "id": "15bf8165cd67032aa4b3d0d5ad125450",
                "name": "Howard Eisenstein",
                "address": "8008 Third Avenue",
                "email": "howard_eisenstein_11236@gmail.com"
            },
            {
                "id": "bb0423eeeff9e53cc8f625bc15d00ea7",
                "name": "Pulle Dunstan Ferando",
                "address": "354 Monroe Place",
                "email": "pulle_dunstan_ferando_11203@gmail.com"
            },
            {
                "id": "efc28a6b954fc6b4a603202bbe6d1024",
                "name": "Joshua Pollacil",
                "address": "6638 FOREST AVENUE",
                "email": "joshua_pollacil_11103@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "758591ccd804e20cc1bcb777941fa697",
                "name": "Fei Wang",
                "address": "739 Knickerbocker Avenue",
                "email": "fei_wang_11203@gmail.com"
            },
            {
                "id": "dfd45ecbd9e53dd281fe8fedeba9bff2",
                "name": "Shamim A. Begum",
                "address": "37-44 75th Street",
                "email": "shamim_a._begum_11373@gmail.com"
            },
            {
                "id": "b30d969c54205828a6dd07d2ea472eb2",
                "name": "Shabana Azam",
                "address": "2-12 Sickles Street",
                "email": "shabana_azam_10003@gmail.com"
            },
            {
                "id": "6e2e4415a78cbaca8a5c6ecbac50f056",
                "name": "Demetra Eleftheriou",
                "address": "445 Park Avenue",
                "email": "demetra_eleftheriou_11211@gmail.com"
            },
            {
                "id": "8f26ed4350c68e4bba246de38b4d3bef",
                "name": "Ida Ellen Schwab",
                "address": "136-19 41st Ave 2nd Floor",
                "email": "ida_ellen_schwab_11421@gmail.com"
            },
            {
                "id": "06e162d522e658cc9814b044f8b12017",
                "name": "Dominic Moccia",
                "address": "125 East 86th Street",
                "email": "dominic_moccia_10031@gmail.com"
            },
            {
                "id": "e6808af3999efc9414bb54b403ac7e6d",
                "name": "Genia Bekker",
                "address": "1353 49th Street",
                "email": "genia_bekker_11236@gmail.com"
            },
            {
                "id": "0de0bf4391a24c9d956fee7190caa010",
                "name": "Aysar B Fathallah-Mammo",
                "address": "234-32 Merrick Blvd.",
                "email": "aysar_b_fathallah-mammo_11435@gmail.com"
            },
            {
                "id": "af0513b2d50036ce40e28c3bad460753",
                "name": "James Gough",
                "address": "520 Neptune avenue",
                "email": "james_gough_11224@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "76d01324668a1135a3bc83784162c521",
                "name": "Luz Ares",
                "address": "100 Ross Street",
                "email": "luz_ares_11230@gmail.com"
            },
            {
                "id": "6d46224ea783a3af2b31a172d98c49e2",
                "name": "Shelly Shi",
                "address": "102-11 Roosevelt Avenue",
                "email": "shelly_shi_10011@gmail.com"
            },
            {
                "id": "2df97c72f0cfea1a4c43462576eaf4f2",
                "name": "Derek Liang",
                "address": "3010 Grand Concourse",
                "email": "derek_liang_10462@gmail.com"
            },
            {
                "id": "e546fe3170de25a3f471b4a05652fbdb",
                "name": "Wilson Chau",
                "address": "600 West 150th Street",
                "email": "wilson_chau_10030@gmail.com"
            },
            {
                "id": "11c4c92ec3cad14b3111edac8ee7c1f1",
                "name": "Antonia Subletas Mayol",
                "address": "64-12 Fresh Pond Rd",
                "email": "antonia_subletas_mayol_11422@gmail.com"
            },
            {
                "id": "245f4a5465147df80ed393541e8db974",
                "name": "Ibrahim Carvan",
                "address": "1262 Ocean Parkway",
                "email": "ibrahim_carvan_11209@gmail.com"
            },
            {
                "id": "b3efa96cbb1005e8ac135407284033d5",
                "name": "Stuart Lewis",
                "address": "9-15 166th Street #6A",
                "email": "stuart_lewis_11372@gmail.com"
            },
            {
                "id": "fcbcb8c7543b6e00f9e6e1848f08fb5d",
                "name": "Cynthia Krause",
                "address": "125 East 86th Street",
                "email": "cynthia_krause_10031@gmail.com"
            },
            {
                "id": "e0a0a21b0ce25348633726a89eb4867b",
                "name": "Christina Chou",
                "address": "1070 Southern Blvd",
                "email": "christina_chou_10458@gmail.com"
            },
            {
                "id": "b6fa92a3263cde141a0ca22ca1321c4a",
                "name": "Henry Sardar",
                "address": "413 50th Street",
                "email": "henry_sardar_11216@gmail.com"
            },
            {
                "id": "811afd2a0cb97bee232a99dfff1b80d5",
                "name": "Eddy Vincent",
                "address": "514 Fifth Street",
                "email": "eddy_vincent_11208@gmail.com"
            },
            {
                "id": "3ff21fa92e5a7537af56457b3392292d",
                "name": "Nereida Correa",
                "address": "164-08 65th Ave",
                "email": "nereida_correa_11375@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "02793120b6ace8f2cde737ca1b56ba3b",
                "name": "Genya Frid",
                "address": "2233 Nostrand Avenue",
                "email": "genya_frid_11237@gmail.com"
            },
            {
                "id": "d91f20c7ea3d2aed268db5eee4e11c86",
                "name": "Eduard Levy",
                "address": "94-13 Flatlands Ave. Suite 101",
                "email": "eduard_levy_11210@gmail.com"
            },
            {
                "id": "38be21ae0215568a6b0b4738f9c7f02f",
                "name": "Ramon Delmonte",
                "address": "860 GRAND CONCOURSE",
                "email": "ramon_delmonte_10451@gmail.com"
            },
            {
                "id": "220de694beccb83efc5dfe58fb425bff",
                "name": "Laszlo Feher",
                "address": "68 Bayard Street",
                "email": "laszlo_feher_10013@gmail.com"
            },
            {
                "id": "4a715961bc7692a3ca51d4a68ad7471e",
                "name": "Shuk-Yi Lee",
                "address": "2015 Grand Concourse",
                "email": "shuk-yi_lee_10467@gmail.com"
            },
            {
                "id": "830a4b4abae229abfb0fc01603f68d56",
                "name": "Lidia Garcia",
                "address": "4434 Amboy Road",
                "email": "lidia_garcia_11356@gmail.com"
            },
            {
                "id": "2fbc6f74c1af12ca13f273047ff2477a",
                "name": "Austin Lu",
                "address": "435 Fort Washington Ave #1H",
                "email": "austin_lu_10016@gmail.com"
            },
            {
                "id": "9b3dc7cf45010dd948f0d3f87a322e70",
                "name": "Theresa Wilson",
                "address": "86 East 49th Street",
                "email": "theresa_wilson_11237@gmail.com"
            },
            {
                "id": "08e31d4bb340befaf9f1264bd5702a84",
                "name": "George Moskowitz",
                "address": "295 Ralph Avenue",
                "email": "george_moskowitz_11233@gmail.com"
            },
            {
                "id": "764391c8a08f08e481315aa5e7510582",
                "name": "Michelle Schecter",
                "address": "59-17 Junction Blvd",
                "email": "michelle_schecter_11379@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "d77255021814da28f515ecb04b44dd11",
                "name": "Alberto Marcano",
                "address": "730 58th Street, 1F",
                "email": "alberto_marcano_11220@gmail.com"
            },
            {
                "id": "a466a7eef3a48396368d47c65adba230",
                "name": "Ramakrishnayya Pattumudi",
                "address": "39 East Broadway Suite 307",
                "email": "ramakrishnayya_pattumudi_10016@gmail.com"
            },
            {
                "id": "37b63e93e21e84a9d10a76cfdea177e2",
                "name": "Yelena Shedina",
                "address": "1216 Beach Ave #1",
                "email": "yelena_shedina_10453@gmail.com"
            },
            {
                "id": "659864889d1d9cc98e9c0943d5d6c0f1",
                "name": "Gunther Groning",
                "address": "333 w. 51st street",
                "email": "gunther_groning_10033@gmail.com"
            },
            {
                "id": "3160232adf52de5a7fc65565d5ac2ef8",
                "name": "Bella Binik",
                "address": "95-11 101 Ave",
                "email": "bella_binik_11375@gmail.com"
            },
            {
                "id": "34447bb9b550412636f9973f96aaa05f",
                "name": "Aline Shehigian",
                "address": "58 E. 116th St",
                "email": "aline_shehigian_10028@gmail.com"
            },
            {
                "id": "940b0b6ef940c9d73618619f414483a9",
                "name": "David Fagan",
                "address": "3000 Fulton Street",
                "email": "david_fagan_11218@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "d407001055ffd666f0767ed173a62baa",
                "name": "Anuja Reddy",
                "address": "176-60, Union turnpike, Suite 145",
                "email": "anuja_reddy_11374@gmail.com"
            },
            {
                "id": "54f68150d1e826cdc631fd24d5f2733c",
                "name": "Lyudmila Sorekin",
                "address": "99 University Place, 3Rd floor",
                "email": "lyudmila_sorekin_10024@gmail.com"
            },
            {
                "id": "11ae941883a2a1f7b5c06176f944ac66",
                "name": "Michael Eidelman",
                "address": "75-06 ELIOT AVE",
                "email": "michael_eidelman_11355@gmail.com"
            },
            {
                "id": "2e082732564fb8b40ef657636588fe46",
                "name": "Hui Fang Xiao",
                "address": "1627 Broadway",
                "email": "hui_fang_xiao_10032@gmail.com"
            },
            {
                "id": "4dc0d3b7f1322a664fb140a7e92787a4",
                "name": "Paul De Guzman",
                "address": "70-17 37 Avenue",
                "email": "paul_de_guzman_11372@gmail.com"
            },
            {
                "id": "f2054a14b1cb28267ac2e759054ced4d",
                "name": "Victoria Katz",
                "address": "39-07 Prince Sreet",
                "email": "victoria_katz_11105@gmail.com"
            },
            {
                "id": "5248b44dda826a38553c82d2d9428069",
                "name": "Kuldip Sachdev",
                "address": "2034 Benedict Avenue",
                "email": "kuldip_sachdev_10466@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "befd2a81f865a68d628d87ff9c1ef26d",
                "name": "Amy Su",
                "address": "2426 Eastchester Road",
                "email": "amy_su_10458@gmail.com"
            },
            {
                "id": "b153051e05ba47b262c8bcfdc901d186",
                "name": "Payman Jarrahy",
                "address": "911 Park Avenue",
                "email": "payman_jarrahy_10044@gmail.com"
            },
            {
                "id": "e811952f0f1a3a5b55e4b26d22e17052",
                "name": "Ted Du",
                "address": "445 Park Avenue",
                "email": "ted_du_11211@gmail.com"
            },
            {
                "id": "1d9e963e25b0864cdee20a6b087f79aa",
                "name": "Gustavo Insignares",
                "address": "3200 Bronx Blvd",
                "email": "gustavo_insignares_10463@gmail.com"
            },
            {
                "id": "e1d3526e8f19b69b3e7a6f18e30414b6",
                "name": "Dilia Castanos",
                "address": "745 Nostrand Avenue",
                "email": "dilia_castanos_11220@gmail.com"
            },
            {
                "id": "9b21ce7b542ac34c0cfb1fc2c632668e",
                "name": "Ivan Herstik",
                "address": "911 Park Avenue",
                "email": "ivan_herstik_10044@gmail.com"
            },
            {
                "id": "aaf3b9dfe2e85e09ca0603ac8b97608d",
                "name": "Heuscent James",
                "address": "134-21 Maple Ave, Ground floor",
                "email": "heuscent_james_11209@gmail.com"
            },
            {
                "id": "57d339929e3d217931d94d1e4e105df9",
                "name": "Fayez Guirguis",
                "address": "3229 162nd Street",
                "email": "fayez_guirguis_11364@gmail.com"
            },
            {
                "id": "07a3d66d5049df61657a1c2100ad0820",
                "name": "Saul Feldman",
                "address": "87-04 Rockaway Beach Blvd",
                "email": "saul_feldman_11377@gmail.com"
            },
            {
                "id": "d7595372ec612c883bd48458537f3f7d",
                "name": "Holson S. Hector",
                "address": "629 W 185th St",
                "email": "holson_s._hector_10016@gmail.com"
            },
            {
                "id": "d8966dbc773e53685e1c8cbe57c50b84",
                "name": "Mario Saint-Laurent",
                "address": "217 73rd Street",
                "email": "mario_saint-laurent_11209@gmail.com"
            },
            {
                "id": "12cb038d54ef79d63fa93989ee617544",
                "name": "Bentley Patterson",
                "address": "470 Lenox Avenue Suite 1p",
                "email": "bentley_patterson_10031@gmail.com"
            },
            {
                "id": "ed1b7bfab2525d2962f53a38efa5e559",
                "name": "Baldevbhai V. Patel",
                "address": "1627 Broadway",
                "email": "baldevbhai_v._patel_10032@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "138a8700614ea9a7b52d0d32143f6706",
                "name": "Rabeya Chowdhury",
                "address": "2426 Eastchester Road",
                "email": "rabeya_chowdhury_10458@gmail.com"
            },
            {
                "id": "aaff485b5954c585890700a8de7103a5",
                "name": "Richard Arias",
                "address": "12102 Hillside Avenue",
                "email": "richard_arias_11217@gmail.com"
            },
            {
                "id": "aabe4e335736019dcbe808ceffd3749e",
                "name": "Krisczar Bungay",
                "address": "95-42 Roosevelt Ave",
                "email": "krisczar_bungay_11355@gmail.com"
            },
            {
                "id": "8bc35bb5d1a51e929fd9adbcbe4a8804",
                "name": "Sixto R. Caro",
                "address": "18-12 College Point Blvd",
                "email": "sixto_r._caro_10021@gmail.com"
            },
            {
                "id": "771eff8d83bb64b835debb50b6c36eb5",
                "name": "John Delloso",
                "address": "37-11 88th Street",
                "email": "john_delloso_11355@gmail.com"
            },
            {
                "id": "1ffe09a59bda442255a14cf8133a37e0",
                "name": "Suraj Tikko",
                "address": "600 West 150th Street",
                "email": "suraj_tikko_10030@gmail.com"
            },
            {
                "id": "a75aecd18667643b61a73b26b06a842d",
                "name": "Michael Strongin",
                "address": "86-04 117th. street",
                "email": "michael_strongin_11364@gmail.com"
            },
            {
                "id": "ac20f47a05a5dd50700cc61209c1efdb",
                "name": "Pei Ying Xiao",
                "address": "110-16 Sutphin Ave",
                "email": "pei_ying_xiao_11103@gmail.com"
            },
            {
                "id": "7f57cb5b4f04f75cdadfc3f5e7b34be4",
                "name": "Benjamin Barrah",
                "address": "136-30 MAPLE AVE",
                "email": "benjamin_barrah_11423@gmail.com"
            },
            {
                "id": "254627ee9911f0c2a661f9e14cda2e19",
                "name": "Iftikhar Din",
                "address": "131-06 Liberty Ave",
                "email": "iftikhar_din_11373@gmail.com"
            },
            {
                "id": "87b0abb3985a7c23f1653a2e01613a91",
                "name": "Joseph Ahram",
                "address": "60 W Kingsbridge Road",
                "email": "joseph_ahram_10458@gmail.com"
            },
            {
                "id": "33478cbec8e9223ee8c772e3889f7864",
                "name": "Hyunsoon Beatrice Im",
                "address": "90-50 Parsons Blvd, Suite 211",
                "email": "hyunsoon_beatrice_im_11419@gmail.com"
            },
            {
                "id": "8410e6fe3184ac9295c07ec403051bb8",
                "name": "Valeriy Chorny",
                "address": "4250 Broadway Suite 1C",
                "email": "valeriy_chorny_10032@gmail.com"
            },
            {
                "id": "19b18f4375e4320ad8a0a50a90f7f27e",
                "name": "Muhammad Adam",
                "address": "7513 Ft. Hamilton Pky",
                "email": "muhammad_adam_11205@gmail.com"
            },
            {
                "id": "5fcc9408b4fa05e751ef87491d496691",
                "name": "Julius Johnson",
                "address": "39 East Broadway Suite 307",
                "email": "julius_johnson_10016@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "39df6cd01be323639d25144d9cc7c0ae",
                "name": "Arthur Kaplan",
                "address": "445 Park Avenue",
                "email": "arthur_kaplan_11211@gmail.com"
            },
            {
                "id": "8309499e1219a9a7048716e96ba9f88c",
                "name": "JUAN ALBA",
                "address": "13347 Sanford Ave",
                "email": "juan_alba_11372@gmail.com"
            },
            {
                "id": "392db2cb381c17eeeac9babfb0de822c",
                "name": "Patrick Hu",
                "address": "136-20 38th Ave,Suite 8E",
                "email": "patrick_hu_11354@gmail.com"
            },
            {
                "id": "d55939a854df7478046522c4e6b1ace5",
                "name": "Arkadiy Izrailov",
                "address": "303 9th Avenue, Room 140",
                "email": "arkadiy_izrailov_10032@gmail.com"
            },
            {
                "id": "d10a894910cdc03235d85c133be2c11a",
                "name": "Subodh Datta",
                "address": "90-10 Elmhurst Avenue",
                "email": "subodh_datta_11373@gmail.com"
            },
            {
                "id": "24e22df933206f9319a6319fcb97671d",
                "name": "Jeremy Gutwein",
                "address": "2015 Grand Concourse",
                "email": "jeremy_gutwein_10467@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "a43156c3ae7364d44b013f4b487f9fdf",
                "name": "Alain Fedida",
                "address": "-",
                "email": "alain_fedida_11205@gmail.com"
            },
            {
                "id": "035beb6a2d027bec1b5fa6e7734287f9",
                "name": "Gretchen Throner",
                "address": "600 West 150th Street",
                "email": "gretchen_throner_10030@gmail.com"
            },
            {
                "id": "7f92141a6bce21dc033d5465e31c5d3b",
                "name": "Lisa Minsky-Primus",
                "address": "133-36 41st Road, Suite 1",
                "email": "lisa_minsky-primus_11372@gmail.com"
            },
            {
                "id": "7a03d9602f2e8c60cadce3552e308293",
                "name": "Maria Molina",
                "address": "20 Park Avenue",
                "email": "maria_molina_10013@gmail.com"
            },
            {
                "id": "c6bea221068f923c52ad989ca934e34c",
                "name": "Mark Tsinker",
                "address": "95-42 Roosevelt Avenue",
                "email": "mark_tsinker_11379@gmail.com"
            },
            {
                "id": "b9501c2aa84116da48a3bf9ad45f319e",
                "name": "Jack Sadacka",
                "address": "3654 Godwin Terrace, Suite C",
                "email": "jack_sadacka_10466@gmail.com"
            },
            {
                "id": "b70ad33fe6a07ecb6d3a1ffc9be211a3",
                "name": "Adenike Adeyemo",
                "address": "571 Academy Street, Apt. GLE",
                "email": "adenike_adeyemo_10016@gmail.com"
            },
            {
                "id": "2e343164c8311e951e34ea36f4482b1b",
                "name": "Jacob Esses",
                "address": "464 West 145th Street",
                "email": "jacob_esses_10010@gmail.com"
            }
        ]
    },
    "Cedarhurst": {
        "allergologist": [
            {
                "id": "3957d52917937f9e56a8d32e8feee981",
                "name": "Michael Bruno",
                "address": "314 West 14th Street",
                "email": "michael_bruno_11355@gmail.com"
            },
            {
                "id": "c6a727223dc3914c34a32f971f52096c",
                "name": "Viola Ortiz",
                "address": "2248 Richmond Road",
                "email": "viola_ortiz_10312@gmail.com"
            },
            {
                "id": "89e5ce554eabc121beee5b303ca59931",
                "name": "Ambrose Pipia",
                "address": "2015 Grand Concourse",
                "email": "ambrose_pipia_10467@gmail.com"
            },
            {
                "id": "b2d9980912988afce5a081dcbaec792c",
                "name": "Yuderqui Checo",
                "address": "375 East Fordham Road",
                "email": "yuderqui_checo_10453@gmail.com"
            },
            {
                "id": "02fe743c6a80fe05b7f9f17be739221c",
                "name": "Lori R. Hoch",
                "address": "108 E 96th St",
                "email": "lori_r._hoch_10021@gmail.com"
            },
            {
                "id": "67b9bddd0eec640d2bd6079adac12c03",
                "name": "Reza Chowdhury",
                "address": "97-03 Springfield Blvd",
                "email": "reza_chowdhury_11377@gmail.com"
            },
            {
                "id": "e2ba72426a9101ab1f6604d6f9fe3b0c",
                "name": "Adebola Orafidiya",
                "address": "169-11 Island Avenue",
                "email": "adebola_orafidiya_11368@gmail.com"
            },
            {
                "id": "c339f6d264d4eb2b3490299b1cd92ba7",
                "name": "Emilia Pollack",
                "address": "133-29 41st Rd, 2D",
                "email": "emilia_pollack_11692@gmail.com"
            },
            {
                "id": "4cb9c70903246e5fffb945806a8b87ab",
                "name": "Craig A. Kaiser",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "craig_a._kaiser_10013@gmail.com"
            },
            {
                "id": "321b9dae1ea69d2b48c5b12a37b4e28e",
                "name": "David Weiss",
                "address": "3071 Perry Avenue",
                "email": "david_weiss_10453@gmail.com"
            },
            {
                "id": "c88da29c71fc6c024e95051f0f98c1d8",
                "name": "Rosario Reyes-Rigor",
                "address": "131-24 Rockaway Blvd",
                "email": "rosario_reyes-rigor_11373@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "aaf4d77197ae33666027d16288ffb322",
                "name": "John McCarthy",
                "address": "55 Midland Avenue",
                "email": "john_mccarthy_10306@gmail.com"
            },
            {
                "id": "3f60810eede7415bd1afc70265755de9",
                "name": "David Fastman",
                "address": "320 East 188th Street",
                "email": "david_fastman_10468@gmail.com"
            },
            {
                "id": "8a0ed60eba6edeb9e29e1c09f7444c92",
                "name": "Zhu-Ping Zhou",
                "address": "211-16 Union Turnpike",
                "email": "zhu-ping_zhou_11372@gmail.com"
            },
            {
                "id": "9a87347993c602e2b7b8f236a42788c7",
                "name": "Howard Hinestroza",
                "address": "1163 Manor Avenue",
                "email": "howard_hinestroza_10469@gmail.com"
            },
            {
                "id": "9fd9719cf2c1fd82c37efbaf505aa556",
                "name": "Beverly Hurd",
                "address": "1627 Broadway",
                "email": "beverly_hurd_10032@gmail.com"
            },
            {
                "id": "7d60c83f6cfe8c171ee9368b1ccc09b6",
                "name": "Robert Segal",
                "address": "105-55 62nd Drive Suite 1-H",
                "email": "robert_segal_11423@gmail.com"
            },
            {
                "id": "3d9a7f84e9a0a66f6f9500103c3ef75f",
                "name": "Andrew Black",
                "address": "133-29 41st Rd, 2D",
                "email": "andrew_black_11692@gmail.com"
            },
            {
                "id": "d55b2521b004655d4ef842f8060e4d80",
                "name": "Daniel Zanger",
                "address": "162 Graham Avenue",
                "email": "daniel_zanger_11234@gmail.com"
            },
            {
                "id": "d2e41fddc17cb2364828ba6ccd047b0b",
                "name": "Ronald Jacques",
                "address": "1523 45TH ST",
                "email": "ronald_jacques_1122611201@gmail.com"
            },
            {
                "id": "d52dd1ad05ec924da18213a8f808f4a0",
                "name": "Cary Pollack",
                "address": "252 Driggs Avenue",
                "email": "cary_pollack_11205@gmail.com"
            },
            {
                "id": "82f143a19675776d3666a9412de3d9d5",
                "name": "Paulu Pina",
                "address": "2515 Avenue M",
                "email": "paulu_pina_11210@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "5d19b4a7cb06d8f4078d18362f76a8ac",
                "name": "Anna Marie Scopellito-Olsen",
                "address": "95-42 Roosevelt Avenue",
                "email": "anna_marie_scopellito-olsen_11379@gmail.com"
            },
            {
                "id": "f77c002a4306b45523e1d0b1b45337b0",
                "name": "Suzanne Walker",
                "address": "2201 Amsterdam Avenue",
                "email": "suzanne_walker_10001@gmail.com"
            },
            {
                "id": "7d224c3c532d417524ffc4e61e84a2a5",
                "name": "Kyi Win Yu",
                "address": "445 Park Avenue",
                "email": "kyi_win_yu_11211@gmail.com"
            },
            {
                "id": "41a9fad69b4e43fc511754e2c5629388",
                "name": "Ferdous Khandker, MD",
                "address": "596 Pennsylvania Avenue",
                "email": "ferdous_khandker,_md_11218@gmail.com"
            },
            {
                "id": "ed224f63559b551fce872e78caa7a5fa",
                "name": "Wai-kuen Lam",
                "address": "112-03 Queens Blvd, Suite 207",
                "email": "wai-kuen_lam_11368@gmail.com"
            },
            {
                "id": "6994c9c89c7049056fc40f8ad74d4014",
                "name": "Thomas Lyo",
                "address": "629 W 185th St, 2nd Floor",
                "email": "thomas_lyo_10013@gmail.com"
            },
            {
                "id": "a515872b47a53e2424f97e77c12d0a92",
                "name": "Jeffrey Kwong",
                "address": "450 Clarkson Ave",
                "email": "jeffrey_kwong_11203@gmail.com"
            },
            {
                "id": "13a39c510f3a1597112e7c57daec545a",
                "name": "Emily Jackness",
                "address": "134-21 Maple Ave, Ground floor",
                "email": "emily_jackness_11209@gmail.com"
            },
            {
                "id": "6427b040f139cb5e3ad0a2438422b81e",
                "name": "Rong Xu",
                "address": "585 Knickerbocker Avenue",
                "email": "rong_xu_11230@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "3999dae772b4d639ab382d8ce8a63304",
                "name": "Vijaya Lakshmi Chandrakant",
                "address": "4742 White Plains Rd, Ste1",
                "email": "vijaya_lakshmi_chandrakant_10467@gmail.com"
            },
            {
                "id": "8ba6a90fed8ce4b93763830a5cf30b8b",
                "name": "Gerson Gomes",
                "address": "8306 13th Avenue",
                "email": "gerson_gomes_11204@gmail.com"
            },
            {
                "id": "1c896a52580b704d3d59e26446aaac45",
                "name": "Marina Reznitsky-Royzman",
                "address": "410 Lakeville Road",
                "email": "marina_reznitsky-royzman_11373@gmail.com"
            },
            {
                "id": "b87c5e43754de17491f9807ae050bdbf",
                "name": "Loren Greene",
                "address": "95-42 Roosevelt Ave",
                "email": "loren_greene_11355@gmail.com"
            },
            {
                "id": "76ef394267a216e99533ac06a8300cf6",
                "name": "Todd Linden",
                "address": "40-04 Bowne St",
                "email": "todd_linden_11373@gmail.com"
            },
            {
                "id": "02b644c8667da6cbd501c7be5cfa8239",
                "name": "Caroline Collado",
                "address": "222 Hancock St",
                "email": "caroline_collado_11221@gmail.com"
            },
            {
                "id": "fc4e9d6f9678689e55c637db30aca7ba",
                "name": "Zewge Deribe",
                "address": "2083 East 65 Street",
                "email": "zewge_deribe_11217@gmail.com"
            },
            {
                "id": "255554d0024d6e5784412b6ae56ed918",
                "name": "Mario Manna",
                "address": "113-11 Jamaica Ave,",
                "email": "mario_manna_11354@gmail.com"
            },
            {
                "id": "360f7913728a682a715cb87a43559f68",
                "name": "Guo Yong Dai",
                "address": "4250 Broadway Suite 1C",
                "email": "guo_yong_dai_10032@gmail.com"
            },
            {
                "id": "3f59290e34f9d0a899f41c576442118a",
                "name": "Veena Chadda",
                "address": "2201 Amsterdam Avenue",
                "email": "veena_chadda_10001@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "7ef8a0bbbe9ed1f0a6d51c2378a9bb5c",
                "name": "Sohah Iqbal",
                "address": "739 Knickerbocker Avenue",
                "email": "sohah_iqbal_11203@gmail.com"
            },
            {
                "id": "3d1efa98c43e323a5b1955b3ac653957",
                "name": "Maung Maung",
                "address": "1385 York Avenue, Suite P2",
                "email": "maung_maung_10021@gmail.com"
            },
            {
                "id": "88ff507142a827a7bdc4d59d1c4b8605",
                "name": "Adam Tonis",
                "address": "201 East 69th St",
                "email": "adam_tonis_11355@gmail.com"
            },
            {
                "id": "b32630bf8545b44546332a77889431e5",
                "name": "Inna Gordin",
                "address": "36 Seventh Avenue Suite 423",
                "email": "inna_gordin_10011@gmail.com"
            },
            {
                "id": "420a371383375f4d7f40dac08ce31aa7",
                "name": "Agnes So",
                "address": "125 East 86th Street",
                "email": "agnes_so_10031@gmail.com"
            },
            {
                "id": "947274214f4474924603924e69b0de4f",
                "name": "Marcial Jimenez",
                "address": "441 west end ave 1 j",
                "email": "marcial_jimenez_10033@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "fbc4de2c643b6374ce6883eb5663a290",
                "name": "Joel Baum",
                "address": "42-60 Main Street Suite 1C",
                "email": "joel_baum_11373@gmail.com"
            },
            {
                "id": "ee57dbe4a7c668447bf2f4765ac2ff3e",
                "name": "Dong Hong Shong",
                "address": "1742 East 13th Street",
                "email": "dong_hong_shong_11210@gmail.com"
            },
            {
                "id": "469f9e8ba55175bc84fffabe9f0d9cb5",
                "name": "Marie-Lourdes Roche",
                "address": "117-06 225th Street 1st Floor",
                "email": "marie-lourdes_roche_11372@gmail.com"
            },
            {
                "id": "fd4f4384499ee0e34b96d7f73785d339",
                "name": "Saroj Gupta",
                "address": "121A West 20th Street",
                "email": "saroj_gupta_10021@gmail.com"
            },
            {
                "id": "296ed49d4e9c86623059359366291fb2",
                "name": "Ward Carpenter",
                "address": "342 Beach 54th Street",
                "email": "ward_carpenter_11418@gmail.com"
            },
            {
                "id": "3b42fbabc7d3e133319e4bc98f54f127",
                "name": "Chaya Stern",
                "address": "139 Centre Street Suite 314",
                "email": "chaya_stern_10031@gmail.com"
            },
            {
                "id": "0724f7747549c187ed37f1d75526ce89",
                "name": "Christina Guillen",
                "address": "607 Soundview Ave",
                "email": "christina_guillen_10453@gmail.com"
            },
            {
                "id": "3f1460ca60e22a22d4aee4244555493e",
                "name": "Marie E. Lefevre",
                "address": "15 Wadsworth Ave.",
                "email": "marie_e._lefevre_10021@gmail.com"
            },
            {
                "id": "f3aa60da6cf821c5d57c637979bb9e5d",
                "name": "Jonathan Chang",
                "address": "1103 Cortelyou Road",
                "email": "jonathan_chang_11230@gmail.com"
            },
            {
                "id": "c2cd8d1ac1320489b04d8819846b1cb6",
                "name": "Shervin Mortazavi",
                "address": "3071 Perry Avenue",
                "email": "shervin_mortazavi_10453@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "84f82bb4a8e253cf38b9b5ba2286ae60",
                "name": "Michael Tugetman",
                "address": "2385 Arthur Avenue, Suite 206",
                "email": "michael_tugetman_10453@gmail.com"
            },
            {
                "id": "7734fbf9d30595cebbdb23a97b33d3f6",
                "name": "Farzana Aziz",
                "address": "3010 Grand Concourse",
                "email": "farzana_aziz_10462@gmail.com"
            },
            {
                "id": "74c000b4a7c101a2ef5fb28379c5bf4e",
                "name": "Fermin P. Gonzalez",
                "address": "2248 Richmond Road",
                "email": "fermin_p._gonzalez_10312@gmail.com"
            },
            {
                "id": "85caa8f6d12e89426971672e147ccae8",
                "name": "Vincent Esposito",
                "address": "86-02 MUSKET STREET",
                "email": "vincent_esposito_11375@gmail.com"
            },
            {
                "id": "7613825d45ed68b5ab582ccefaff6cac",
                "name": "Iris Sherman",
                "address": "88-23 Justice Avenue",
                "email": "iris_sherman_10033@gmail.com"
            },
            {
                "id": "c43a636a39c25fbe7d8416cae58fa565",
                "name": "Rushita Patel",
                "address": "305 Seguine Ave Ste. 1",
                "email": "rushita_patel_10305@gmail.com"
            },
            {
                "id": "63f90481a3c4a1fa01226b7a6c5d6e9c",
                "name": "Qaiser Abbas",
                "address": "9 East 63rd Street",
                "email": "qaiser_abbas_10040@gmail.com"
            },
            {
                "id": "deeb9067a60b097d5462f09a0e835b58",
                "name": "Lionel Lefevre",
                "address": "8919 Lefferts Blvd",
                "email": "lionel_lefevre_11372@gmail.com"
            },
            {
                "id": "1fb8bd05ad93287289bde8261e34109d",
                "name": "Rawand Khader",
                "address": "128 Mott Street",
                "email": "rawand_khader_10013@gmail.com"
            },
            {
                "id": "f9d1d4597941010aad274f74d2404129",
                "name": "Owen Golden",
                "address": "140 Clinton Street",
                "email": "owen_golden_11211@gmail.com"
            }
        ],
        "urologist": [
            {
                "id": "23dca6c32a37b4fd4b194f3ff6a86b7c",
                "name": "John Wat",
                "address": "7318 13th Avenue",
                "email": "john_wat_11216@gmail.com"
            },
            {
                "id": "37bf3f2edf15587b7b0b4a216f4f590c",
                "name": "Khalil Solaimanzadeh",
                "address": "113-11 Jamaica Ave,",
                "email": "khalil_solaimanzadeh_11354@gmail.com"
            },
            {
                "id": "8df8e8c7034c91e70fc2b5f0ea4333fb",
                "name": "Maggie Bertisch",
                "address": "600 West 150th Street",
                "email": "maggie_bertisch_10030@gmail.com"
            },
            {
                "id": "ea794d7d42875a89b92cec271f32a064",
                "name": "Luis Astudillo",
                "address": "1718 Pitkin Avenue",
                "email": "luis_astudillo_11203@gmail.com"
            },
            {
                "id": "bc3c17b837cde079f6adc40e68fd56f3",
                "name": "Maria Barbery",
                "address": "25-52 STEINWAY STREET",
                "email": "maria_barbery_11691@gmail.com"
            },
            {
                "id": "0288efacbc400be66269ea39a83813b9",
                "name": "Leon Kohanbasch",
                "address": "170 W.233rd Street",
                "email": "leon_kohanbasch_10457@gmail.com"
            },
            {
                "id": "0e09110a108b7ec09e95857f0d57958a",
                "name": "M Laporte",
                "address": "411 West 113TH Street",
                "email": "m_laporte_10031@gmail.com"
            },
            {
                "id": "4268d1f7ccc03899fcb2f6d12f2613b9",
                "name": "FOUZIA SYED",
                "address": "295 Ralph Avenue",
                "email": "fouzia_syed_11233@gmail.com"
            },
            {
                "id": "6d2545c540ee0472c4a0a7f67d7df486",
                "name": "Jennifer Cheng",
                "address": "108 East 96th Street",
                "email": "jennifer_cheng_10019@gmail.com"
            },
            {
                "id": "27fabbcc97c8afeb7ccf41f36a5d5c53",
                "name": "Jeffrey Teitelbaum",
                "address": "3200 Bronx Blvd",
                "email": "jeffrey_teitelbaum_10463@gmail.com"
            },
            {
                "id": "ca1978e4ec2fd21e4a7041c3884dd86f",
                "name": "Alan Diaz",
                "address": "13176 Laurelton Parkway",
                "email": "alan_diaz_11373@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "2d2370b91f0ece1fc50583e15e0515ad",
                "name": "Nazia Ajani",
                "address": "41-50 78th St., Ground Fl.",
                "email": "nazia_ajani_11373@gmail.com"
            },
            {
                "id": "459a1b0283bbb330b96320d9066c7fcc",
                "name": "Angela Meikle",
                "address": "139-16 91st Avenue",
                "email": "angela_meikle_10453@gmail.com"
            },
            {
                "id": "202ae7a385cc2ee57a6ca9bfd0fb1636",
                "name": "Magdy Mohammed",
                "address": "1446 Broadway Avenue",
                "email": "magdy_mohammed_11238@gmail.com"
            },
            {
                "id": "9c9feb5c675a9e5a413c4c80566989f9",
                "name": "Sandy Cheung",
                "address": "11 Ralph Pl Suite 214",
                "email": "sandy_cheung_10312@gmail.com"
            },
            {
                "id": "14683efb6fc46f3132b08cd4603e796a",
                "name": "Chaya Wald",
                "address": "6805 Fort Hamilton Parkway",
                "email": "chaya_wald_11216@gmail.com"
            },
            {
                "id": "0f468d463ff5c941f9794ec6c734310f",
                "name": "Rainer Mittl",
                "address": "1664 East 14th Street, Suite 401",
                "email": "rainer_mittl_11224@gmail.com"
            },
            {
                "id": "61eab809ef9fa13e9371a14955d4ba74",
                "name": "Hanna Lesicka M.D F.A.A.P., P.C.",
                "address": "410 Lakeville Road",
                "email": "hanna_lesicka_m.d_f.a.a.p.,_p.c._11373@gmail.com"
            },
            {
                "id": "979a367005d35ab59825313a898d6491",
                "name": "Boris Chusid",
                "address": "131-06 Liberty Ave",
                "email": "boris_chusid_11373@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "4ecd253909378519e43141656a851959",
                "name": "Lionel Barrau",
                "address": "1560 GRAND CONCOURSE",
                "email": "lionel_barrau_10452@gmail.com"
            },
            {
                "id": "3fde9e3aa2c0495245b86d483742c51c",
                "name": "Bina Chaudhari-Mody",
                "address": "833 58th Street",
                "email": "bina_chaudhari-mody_11224@gmail.com"
            },
            {
                "id": "330045d27e8021c37d07d56c2dfcab62",
                "name": "Abeer Dabbas",
                "address": "104 Vermilyea Avenue, Suite B",
                "email": "abeer_dabbas_10033@gmail.com"
            },
            {
                "id": "97713fda5ab97509edbb77c9cde42d2b",
                "name": "JYOTI GANDHI",
                "address": "40-35 95th Street",
                "email": "jyoti_gandhi_11372@gmail.com"
            },
            {
                "id": "a47bebe6898db038e1097e9a97e09516",
                "name": "MOHYUDDIN QURESHI",
                "address": "170 W.233rd Street",
                "email": "mohyuddin_qureshi_10457@gmail.com"
            },
            {
                "id": "b1a85df95baeaf4d8a28e1a725313e41",
                "name": "Caesar Villarica",
                "address": "115 Central Park West",
                "email": "caesar_villarica_10011@gmail.com"
            },
            {
                "id": "a21458d87b0714110c8aaa63001a3b31",
                "name": "Bernadette Clement",
                "address": "15 Wadsworth Ave.",
                "email": "bernadette_clement_10021@gmail.com"
            },
            {
                "id": "9a167aa17e04f60b4c9761f20587da3e",
                "name": "Gloria Florez",
                "address": "103 East Burnside Avenue",
                "email": "gloria_florez_10458@gmail.com"
            },
            {
                "id": "db7e215a5ff72529bc1ca27839316be8",
                "name": "Ruben Carvajal",
                "address": "464 West 145th Street",
                "email": "ruben_carvajal_10010@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "35a155f909859f7b667d94801c136de3",
                "name": "Ida Bronfman",
                "address": "895 PARK AVENUE",
                "email": "ida_bronfman_10021@gmail.com"
            },
            {
                "id": "4a43bc774cfb40d060fb3550ab41c033",
                "name": "Betty Mercedes",
                "address": "125 East 86th Street",
                "email": "betty_mercedes_10031@gmail.com"
            },
            {
                "id": "933d56311800d5645ff48fa8a2657275",
                "name": "Delys St. Hill",
                "address": "4434 Amboy Road",
                "email": "delys_st._hill_11356@gmail.com"
            },
            {
                "id": "2ca04fe3a60d8cad3d022cc24b61289b",
                "name": "Shiva Golshan",
                "address": "19 Hamilton Place",
                "email": "shiva_golshan_10013@gmail.com"
            },
            {
                "id": "414ed1d725b41918414af2a889a42b28",
                "name": "Yanhan Huang",
                "address": "136-31 41st Avenue Suite 30",
                "email": "yanhan_huang_11432@gmail.com"
            },
            {
                "id": "7d868a07da7489a0d43360c81ee3978d",
                "name": "Jermel Hawkins",
                "address": "15 Wadsworth Ave.",
                "email": "jermel_hawkins_10021@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "5988600ac2f2cb1a72495437457e5239",
                "name": "Yuchun Chen",
                "address": "125 East 86th Street",
                "email": "yuchun_chen_10031@gmail.com"
            },
            {
                "id": "61dadf2a997072f15d615d528f154b1d",
                "name": "Muntaz Majeed",
                "address": "97-03 Springfield Blvd",
                "email": "muntaz_majeed_11377@gmail.com"
            },
            {
                "id": "c379249053a349f549e2cfd55f6c13f7",
                "name": "Titus Okunola",
                "address": "123 West 86th Street",
                "email": "titus_okunola_10037@gmail.com"
            },
            {
                "id": "0a9391ecb523bf1c8fb5dba671491e1a",
                "name": "Sazia Setaruddin",
                "address": "102 East 22 St Suite 1",
                "email": "sazia_setaruddin_10024@gmail.com"
            },
            {
                "id": "b7e75ab96b232c7cf78897c630ef3517",
                "name": "Hector Florimon",
                "address": "763 56th Street , 1st floor",
                "email": "hector_florimon_11219@gmail.com"
            },
            {
                "id": "0db9026087a50c1f631bbd4199142127",
                "name": "Wilfredo Lao",
                "address": "1407 46th Street",
                "email": "wilfredo_lao_11213@gmail.com"
            },
            {
                "id": "d83f2d381d9a9ff1f3e4e3d68689826d",
                "name": "CARLA LUCACEL",
                "address": "133-47 Sanford Avenue, Suite 1H",
                "email": "carla_lucacel_11354@gmail.com"
            },
            {
                "id": "cc95aa697562a84781b521ea093d1362",
                "name": "Timothy Johnson",
                "address": "211 E 51st St",
                "email": "timothy_johnson_10014@gmail.com"
            },
            {
                "id": "a8b6811773eeeee7ce1d5421cbaaacb5",
                "name": "Craig Metroka",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "craig_metroka_10013@gmail.com"
            },
            {
                "id": "eb4d4222a19296b123eb5bc9bffc78c8",
                "name": "Naomi Molner",
                "address": "1166 Eastern Parkway",
                "email": "naomi_molner_11229@gmail.com"
            },
            {
                "id": "b27c56e99c8e89e3225ad38c4e696750",
                "name": "Frank Spinelli",
                "address": "3131 Kings Highway",
                "email": "frank_spinelli_11228@gmail.com"
            },
            {
                "id": "1effb2c91529121fad3080f7020d3c5d",
                "name": "Thomas V. Tupper",
                "address": "60 Plaza St E # E",
                "email": "thomas_v._tupper_11238@gmail.com"
            },
            {
                "id": "6a58055e3154c286e66c19e961a95c36",
                "name": "Priyanka Gupta",
                "address": "59-17 Junction Blvd",
                "email": "priyanka_gupta_11379@gmail.com"
            },
            {
                "id": "2a4de06559ef7bf3b145bccad107121b",
                "name": "Earl Ellis",
                "address": "2400 Davidson Avenue",
                "email": "earl_ellis_10451@gmail.com"
            },
            {
                "id": "4d0d308a632733afa5b78a9e086078ef",
                "name": "Babu Jasty",
                "address": "95-42 Roosevelt Ave",
                "email": "babu_jasty_11355@gmail.com"
            },
            {
                "id": "3a1d981225bf74e451732815df2833a9",
                "name": "SREENIVASA MURTHY",
                "address": "1250 Shakespeare Avenue",
                "email": "sreenivasa_murthy_10457@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "cdfcac2ba891a64253568ab5628ce8d8",
                "name": "Sellathurai Dhayaparan",
                "address": "1135 Eastern Parkway",
                "email": "sellathurai_dhayaparan_11220@gmail.com"
            },
            {
                "id": "440527faffde370d1536071786d52208",
                "name": "Jose Fulgencio-Delmonte",
                "address": "600 West 150th Street",
                "email": "jose_fulgencio-delmonte_10030@gmail.com"
            },
            {
                "id": "16d61b972d0425d61711b18fa82b00a5",
                "name": "Deborah Martin-Arila",
                "address": "252 Driggs Avenue",
                "email": "deborah_martin-arila_11205@gmail.com"
            },
            {
                "id": "26e9108e422ce068f68a66f738104706",
                "name": "Karen Allison",
                "address": "2426 Eastchester Road",
                "email": "karen_allison_10458@gmail.com"
            },
            {
                "id": "cf83bbb8c2e0afc797ef07d4341fe38f",
                "name": "Hla Tun",
                "address": "162-16 Union Turnpike, Suite 305",
                "email": "hla_tun_11372@gmail.com"
            },
            {
                "id": "bc496acdfe555c76ea76cd3506b6abff",
                "name": "Sandra Gilban",
                "address": "305 e 149th st",
                "email": "sandra_gilban_10472@gmail.com"
            },
            {
                "id": "8d3d6c241c45aff8d3a3a9cb88baecf0",
                "name": "Roberto Gabitto",
                "address": "600 West 150th Street",
                "email": "roberto_gabitto_10030@gmail.com"
            },
            {
                "id": "313b2e677b2b71b1f8a87a91b227917e",
                "name": "Pedro Guzman",
                "address": "7513 Ft. Hamilton Pky",
                "email": "pedro_guzman_11205@gmail.com"
            },
            {
                "id": "ce8bf2f96e7f219cd0f546fb63e81617",
                "name": "Sharon Zheng",
                "address": "75 WEST 190 ST",
                "email": "sharon_zheng_10472@gmail.com"
            },
            {
                "id": "7a59863f02afbd76369a301641762440",
                "name": "Aline Benjamin",
                "address": "1421 E 2ND ST",
                "email": "aline_benjamin_11219@gmail.com"
            },
            {
                "id": "048f1899689b646ba02eaf3f7c0d271c",
                "name": "Robin Chan",
                "address": "1718 Pitkin Avenue",
                "email": "robin_chan_11203@gmail.com"
            },
            {
                "id": "fb79f7af00f81cad0908ab252a19f866",
                "name": "Singmay Siu",
                "address": "189 Montague St. Ste 700",
                "email": "singmay_siu_11205@gmail.com"
            },
            {
                "id": "461d38c349ed9670316f7fb6470a9e16",
                "name": "Annabi Djalo",
                "address": "155 West 19th St",
                "email": "annabi_djalo_10003@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "cad83f66b1379822a1e38dc5885d17a7",
                "name": "Hua Ding",
                "address": "470 Lenox Avenue Suite 1E",
                "email": "hua_ding_10040@gmail.com"
            },
            {
                "id": "8068948068c424c3f6b3579fcae5835d",
                "name": "Sarita Khatri",
                "address": "1153 58 Street",
                "email": "sarita_khatri_11213@gmail.com"
            },
            {
                "id": "46b626729e0b6187ef959186153cab17",
                "name": "Indranil Gupta",
                "address": "3853 WHITE PLAINS RD",
                "email": "indranil_gupta_10451@gmail.com"
            },
            {
                "id": "a22adba5508992832cb981a7890ae68f",
                "name": "Martin Baskin",
                "address": "88-01 Parson Blvd",
                "email": "martin_baskin_11402@gmail.com"
            },
            {
                "id": "18eb5841890c996d92d313f41a889b31",
                "name": "Leonid Bukhman",
                "address": "87-81, 169th Street",
                "email": "leonid_bukhman_11372@gmail.com"
            },
            {
                "id": "c0f41eb7cecf215e82478ba915ab2783",
                "name": "Carl Casimir",
                "address": "231 SOUTH 3RD STREET",
                "email": "carl_casimir_11221@gmail.com"
            },
            {
                "id": "6ce4dd1b447c718abf37ba3f0fa6fd1d",
                "name": "Larisa Litvinova",
                "address": "1153 58th Street",
                "email": "larisa_litvinova_11211@gmail.com"
            },
            {
                "id": "d006d5b7ea02673da48f96e732dcfb5a",
                "name": "Joseph Andrade",
                "address": "133-38 41st Rd Suite 2C",
                "email": "joseph_andrade_11354@gmail.com"
            },
            {
                "id": "41fd6ee60554cc3045c8616bf5b1ed9a",
                "name": "Alyson Smith",
                "address": "410 Lakeville Road, Suite 202",
                "email": "alyson_smith_11377@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "522ee3ac60a2e804c43111b1ef064dd6",
                "name": "Gavriel Fuzaylov",
                "address": "1718 Pitkin Avenue",
                "email": "gavriel_fuzaylov_11203@gmail.com"
            },
            {
                "id": "9a0a740a332cd3f134d46adaf40ae295",
                "name": "Robert Yu",
                "address": "375 East Fordham Road",
                "email": "robert_yu_10453@gmail.com"
            },
            {
                "id": "d98bc68e3718e086709056bc29e2f309",
                "name": "James Blake",
                "address": "117-06 225th Street 1st Floor",
                "email": "james_blake_11372@gmail.com"
            },
            {
                "id": "bd1d09bd635984ade02a7dc1eae3bab5",
                "name": "Hillary Bell",
                "address": "1219 liberty avenue",
                "email": "hillary_bell_11237@gmail.com"
            },
            {
                "id": "4eb3674623dde73ac2cdb0501527c5a0",
                "name": "victor Mok",
                "address": "113-11 Jamaica Ave,",
                "email": "victor_mok_11354@gmail.com"
            },
            {
                "id": "6d73098e0879ac03b6bdf4f1aa946a38",
                "name": "DMITRY KONSKY",
                "address": "37-11 88th Street",
                "email": "dmitry_konsky_11355@gmail.com"
            },
            {
                "id": "9352fb451720680aa99027646d29cc84",
                "name": "Chaim Wanounou",
                "address": "753 Classon Avenue Suite LJ",
                "email": "chaim_wanounou_11219@gmail.com"
            },
            {
                "id": "33e7d1b5a07f11dfd337f3663394821f",
                "name": "Olufunmilayo Adeyanju",
                "address": "113-11 Jamaica Ave,",
                "email": "olufunmilayo_adeyanju_11354@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "de8118e8f0ab704603782342bfc25df1",
                "name": "Paul Leva",
                "address": "42-72 kissena boulevard",
                "email": "paul_leva_11375@gmail.com"
            },
            {
                "id": "c9de3e2a33916d059324dbdfb025494f",
                "name": "Luis Blanco",
                "address": "220 A St. Nicholas Avenue",
                "email": "luis_blanco_11237@gmail.com"
            },
            {
                "id": "428cc34d81f3ef76ace903836939b516",
                "name": "MARGARET KEARNS-STANLEY",
                "address": "121A West 20th Street",
                "email": "margaret_kearns-stanley_10021@gmail.com"
            },
            {
                "id": "009a2903667206bfcc089d1423a1cc29",
                "name": "Anthony G. Purpura",
                "address": "514 Fifth Street",
                "email": "anthony_g._purpura_11208@gmail.com"
            },
            {
                "id": "963ba8450f7e8d4790a915156e0e8308",
                "name": "Bola Olajide",
                "address": "571 Academy Street, Apt. GLE",
                "email": "bola_olajide_10016@gmail.com"
            },
            {
                "id": "714d6daeac59ee64ebb0a1c3418d34b0",
                "name": "Sumir Sahgal",
                "address": "5303 8TH AVENUE",
                "email": "sumir_sahgal_11232@gmail.com"
            },
            {
                "id": "06d1ef8fc12ce1c473ed7398721cefdc",
                "name": "Jason Ogiste",
                "address": "450 clarkson ave",
                "email": "jason_ogiste_11212@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "da7c4ba8936235d46ad8ee9b37e41a8a",
                "name": "Jay Bassell",
                "address": "131-24 Rockaway Blvd",
                "email": "jay_bassell_11373@gmail.com"
            },
            {
                "id": "495c92c70fc4241a783570bec16132a3",
                "name": "Max Jean-Gilles",
                "address": "3250 THIRD AVENUE",
                "email": "max_jean-gilles_10469@gmail.com"
            },
            {
                "id": "1b4fd0ab8d40819306aedf50e65479b8",
                "name": "Zili He",
                "address": "86-02 MUSKET STREET",
                "email": "zili_he_11375@gmail.com"
            },
            {
                "id": "30c7715dcd74651b72ef0fcd9bcabac1",
                "name": "Olugbenga Dawodu",
                "address": "1718 Pitkin Avenue",
                "email": "olugbenga_dawodu_11203@gmail.com"
            },
            {
                "id": "b25c9a40d8d55a89f3ab6ff70584b374",
                "name": "Lewis R. Lipsey",
                "address": "131-24 Rockaway Blvd",
                "email": "lewis_r._lipsey_11373@gmail.com"
            },
            {
                "id": "ac9aeeffb2dc22465ed864cb2117f9c8",
                "name": "Jeffrey Kee Low",
                "address": "-",
                "email": "jeffrey_kee_low_11205@gmail.com"
            },
            {
                "id": "2c170ce50f144ff208ccf5d7fdcb09a2",
                "name": "Ira Blanfarb",
                "address": "650 5th Avenue",
                "email": "ira_blanfarb_11204@gmail.com"
            },
            {
                "id": "d51d17747fd12e6fe8322382b372cfb0",
                "name": "Dorene Soo-Hoo",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "dorene_soo-hoo_10013@gmail.com"
            },
            {
                "id": "f420e131c0afb738f90e9bfe8a4b1aa4",
                "name": "Huifang Xiao",
                "address": "264 1st Street",
                "email": "huifang_xiao_11210@gmail.com"
            },
            {
                "id": "4e46df80f2e0f1b5d637f5da3b74eb7c",
                "name": "Daniel Yadegar",
                "address": "113-11 Jamaica Ave,",
                "email": "daniel_yadegar_11354@gmail.com"
            },
            {
                "id": "80f33d831992be07f75c0210408fc6da",
                "name": "Joseph Paul",
                "address": "85 WEST 118TH STREET",
                "email": "joseph_paul_10023@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "c7c520420076ffa08b8a1c33f4a3ff5a",
                "name": "Weimin Qu",
                "address": "540 East New York Avenue",
                "email": "weimin_qu_11219@gmail.com"
            },
            {
                "id": "68d2142d9d179edbf7b50a6a8ac46c27",
                "name": "Dyan Hes",
                "address": "95-42 Roosevelt Ave",
                "email": "dyan_hes_11355@gmail.com"
            },
            {
                "id": "bc277261e031ff4ba996d0df96ac1bcd",
                "name": "Yasmine Arasta",
                "address": "220 A St. Nicholas Avenue",
                "email": "yasmine_arasta_11237@gmail.com"
            },
            {
                "id": "f741da27ee37c40f6b4c8b14e6491be9",
                "name": "Harrison F. Mitchell",
                "address": "89-18 Lefferts Blvd",
                "email": "harrison_f._mitchell_11375@gmail.com"
            },
            {
                "id": "d383407cc6816e552022e09a5ed9291d",
                "name": "Hanbin Zheng",
                "address": "40-35 95th Street",
                "email": "hanbin_zheng_11372@gmail.com"
            },
            {
                "id": "6d768604fc0a1e5e30b95a853fd13c37",
                "name": "Anita Ahuja",
                "address": "18-12 College Point Blvd",
                "email": "anita_ahuja_10021@gmail.com"
            },
            {
                "id": "12d6ac9bc08d258334ee0b31944000d4",
                "name": "Anita Ong Hui",
                "address": "121A West 20th Street",
                "email": "anita_ong_hui_10021@gmail.com"
            },
            {
                "id": "6c36b409ba7ccfc113edbb35fb399a21",
                "name": "Eldawary Wael",
                "address": "391 East 149th Street",
                "email": "eldawary_wael_11694@gmail.com"
            },
            {
                "id": "d428e3e0aa813bee4c1a6872f428893b",
                "name": "Eric Bates",
                "address": "210 E 86th St",
                "email": "eric_bates_10011@gmail.com"
            },
            {
                "id": "42fb5ad000887791b8fc3da1c9dde75e",
                "name": "Richard Izquierdo",
                "address": "80-37 Broadway",
                "email": "richard_izquierdo_11354@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "1b89b8a1e03e0a74e32dd24be1a2491e",
                "name": "Rehana Sajjad",
                "address": "1135 eastern parkway",
                "email": "rehana_sajjad_11236@gmail.com"
            },
            {
                "id": "06eeaf41021694bee1a52e077c60d50b",
                "name": "Lyudmila Oslon",
                "address": "860 GRAND CONCOURSE",
                "email": "lyudmila_oslon_10451@gmail.com"
            },
            {
                "id": "fa3be1f5dd3d56eb480dd20a60d28962",
                "name": "Kelly Thompson",
                "address": "99 moore st suite A",
                "email": "kelly_thompson_11209@gmail.com"
            },
            {
                "id": "598a25ff1b69f7e95349a6b8df3aa234",
                "name": "Katherine Teets Grimm",
                "address": "1185 Park Ave",
                "email": "katherine_teets_grimm_10016@gmail.com"
            },
            {
                "id": "1ce098462ac52e7e705724ebebf73bb4",
                "name": "Atul Chokshi",
                "address": "160 East 32nd St",
                "email": "atul_chokshi_10010@gmail.com"
            },
            {
                "id": "600dbf5fc6027bed11cb9bb4aebb25ce",
                "name": "Patricia Hart",
                "address": "3071 Perry Avenue",
                "email": "patricia_hart_10453@gmail.com"
            },
            {
                "id": "e1019d61e72e5727683bbaa0fea8ba30",
                "name": "Rahila Butt",
                "address": "3904 16th Avenue",
                "email": "rahila_butt_11211@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "befccbc511134cb08769bef567f9a707",
                "name": "Helen Cheung",
                "address": "-",
                "email": "helen_cheung_11205@gmail.com"
            },
            {
                "id": "1c8ca7bfc220d2cfed3412f79cbbcd9d",
                "name": "Kimberly Green-Mayer",
                "address": "410 Lakeville Road",
                "email": "kimberly_green-mayer_11373@gmail.com"
            },
            {
                "id": "67a25184d00ce600fa4432c247357abb",
                "name": "Syed Hussaini",
                "address": "763 56th Street, 1st floor",
                "email": "syed_hussaini_11219@gmail.com"
            },
            {
                "id": "d018111bad0e2b5bc51ecf267577b013",
                "name": "Jimmy Wong",
                "address": "110-45 Queens Boulevard Suite A",
                "email": "jimmy_wong_11516@gmail.com"
            },
            {
                "id": "acdc7a851171a13f90dccf4938f05d0a",
                "name": "Gary Mucciolo",
                "address": "9817 Queens Boulevard, LL2",
                "email": "gary_mucciolo_11368@gmail.com"
            },
            {
                "id": "0b171ea5c68a4b45e45cc9ef147ace25",
                "name": "Robert Feldman",
                "address": "160 East 32nd St",
                "email": "robert_feldman_10010@gmail.com"
            },
            {
                "id": "6d50627af6c4fcef4010f05f223685e5",
                "name": "Ali Saleh",
                "address": "450 Clarkson Ave",
                "email": "ali_saleh_11203@gmail.com"
            },
            {
                "id": "53510aa1ab351c6bdb263d28764aaee4",
                "name": "Edwin Quinones",
                "address": "20 Park Avenue",
                "email": "edwin_quinones_10013@gmail.com"
            },
            {
                "id": "8a57cf4bec61aff8d9a42d2200e994ec",
                "name": "Olive Osborne",
                "address": "15 Wadsworth Ave.",
                "email": "olive_osborne_10021@gmail.com"
            }
        ]
    },
    "Flushing": {
        "infectiologist": [
            {
                "id": "d3e46cd8984787be31afecbb1faf1554",
                "name": "Donald McCord",
                "address": "8684 15th Avenue",
                "email": "donald_mccord_11206@gmail.com"
            },
            {
                "id": "7bc80103a1579b3b277dbdd4b332a95a",
                "name": "Mayer Ballas",
                "address": "36-09 Main Street, Suite 8C",
                "email": "mayer_ballas_11423@gmail.com"
            },
            {
                "id": "41cfd148141f1a9ecb88aa87d6749de1",
                "name": "Afshin Tavakoly",
                "address": "314 West 14th Street",
                "email": "afshin_tavakoly_11355@gmail.com"
            },
            {
                "id": "c256777ca1273e5e258bbf735763a89e",
                "name": "William Shay",
                "address": "1560 GRAND CONCOURSE",
                "email": "william_shay_10452@gmail.com"
            },
            {
                "id": "8893e1f449614d3a2c31085e7d746b86",
                "name": "Caryn Selick",
                "address": "219-02 Linden Blvd",
                "email": "caryn_selick_11366@gmail.com"
            },
            {
                "id": "67a449f8453423c7d6af783ce602f100",
                "name": "Jonathan Leung",
                "address": "160 East 32nd St",
                "email": "jonathan_leung_10010@gmail.com"
            },
            {
                "id": "29e8cdfb4a9866bd5bdd47fdaea8178b",
                "name": "Christiana Nichols",
                "address": "4053 75th Street",
                "email": "christiana_nichols_11368@gmail.com"
            },
            {
                "id": "f2132200ba8269027c2917da3bd39d7c",
                "name": "Won S. Cho",
                "address": "125 East 86th Street",
                "email": "won_s._cho_10031@gmail.com"
            },
            {
                "id": "3ffc5406ffe2f11c8940f4a4974055b0",
                "name": "Frank Arbucci",
                "address": "37-11 88th Street",
                "email": "frank_arbucci_11355@gmail.com"
            },
            {
                "id": "5475252756efee60d139dba70e23550f",
                "name": "Ayman Hassan Elkhouly",
                "address": "95-42 Roosevelt Avenue",
                "email": "ayman_hassan_elkhouly_11379@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "e7d2a853567875430f55018e00c37948",
                "name": "Ajay Shah",
                "address": "33 W. 125th St",
                "email": "ajay_shah_10022@gmail.com"
            },
            {
                "id": "e7e7ce5508c6660adcd6b4d25a15f41b",
                "name": "Andrew Kim",
                "address": "2310 65th Street, 2nd floor",
                "email": "andrew_kim_11215@gmail.com"
            },
            {
                "id": "f9ded071ef3a83c9f206526572feca60",
                "name": "Rumana A. Rahman",
                "address": "15 Wadsworth Ave.",
                "email": "rumana_a._rahman_10021@gmail.com"
            },
            {
                "id": "36ce725c7c462015c5bb16eef900decd",
                "name": "Marie-Paule Dupiton",
                "address": "1931 Williamsbridge Road",
                "email": "marie-paule_dupiton_10453@gmail.com"
            },
            {
                "id": "ae9a2b2d77ac177a52517c4d4a1952c8",
                "name": "Arkadiy Takhalov",
                "address": "68 Bayard Street",
                "email": "arkadiy_takhalov_10013@gmail.com"
            },
            {
                "id": "794b3e5f4cfea93931e460f51bfd77c4",
                "name": "Robert Cohen",
                "address": "67 Irving Place, 5th Floor",
                "email": "robert_cohen_10013@gmail.com"
            },
            {
                "id": "34c67f3e56a7e3645910cfdc895d7495",
                "name": "Mindy Weiss",
                "address": "133-38 41st Rd Suite 2C",
                "email": "mindy_weiss_11354@gmail.com"
            },
            {
                "id": "fd5672582a735bca4bd5a8df31a1beeb",
                "name": "SUSAN MARGOLIS",
                "address": "833 58th Street",
                "email": "susan_margolis_11224@gmail.com"
            },
            {
                "id": "7083acfbc2c20bf9d433eb42c73cdfd4",
                "name": "Limeng Wang",
                "address": "2869 Grand Concourse Avenue Ste. 1",
                "email": "limeng_wang_10458@gmail.com"
            },
            {
                "id": "ce655a35c5b531cb02b8eb251c1e83e4",
                "name": "Yan Wolfson",
                "address": "432 Bedford Avenue",
                "email": "yan_wolfson_11208@gmail.com"
            },
            {
                "id": "1b1acb0f18cd0c0cf39dea1d76895bb2",
                "name": "Olga Tseyko",
                "address": "47 Sickles suite 1A",
                "email": "olga_tseyko_10038@gmail.com"
            },
            {
                "id": "c207c0851ea6257399e7559b6c45c05e",
                "name": "Ingrid Williams",
                "address": "4053 75th Street",
                "email": "ingrid_williams_11368@gmail.com"
            },
            {
                "id": "66cc245f97a6ea1028a9685ab1612f90",
                "name": "BABU PATEL",
                "address": "629 West 185th Street",
                "email": "babu_patel_11372@gmail.com"
            },
            {
                "id": "ebd7feaeeefeb52a09164f935af29a2f",
                "name": "Nedal Samarneh",
                "address": "314 West 14th Street",
                "email": "nedal_samarneh_11355@gmail.com"
            },
            {
                "id": "8a5be79d27ca49d7661030d3cc7ffeee",
                "name": "Leonardo Vando",
                "address": "822 54th Street, 1Flr133-19 41st. Road, 1F",
                "email": "leonardo_vando_11220@gmail.com"
            },
            {
                "id": "66a0245c681e80aa75313e89d80b5a24",
                "name": "Julissa Baez",
                "address": "5303 8th ave",
                "email": "julissa_baez_11220@gmail.com"
            },
            {
                "id": "7c26d0347c12762c999c51549171f52a",
                "name": "Delsa Compres",
                "address": "600 West 150th Street",
                "email": "delsa_compres_10030@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "67041f063add7f41b4f017485006d114",
                "name": "Jean Pierre Barakat",
                "address": "22-31 33 Street",
                "email": "jean_pierre_barakat_11355@gmail.com"
            },
            {
                "id": "5442a0ba418dbe16d8de94d656fdadc7",
                "name": "Rosa Gonzalez-Freire",
                "address": "834 CONEY ISLAND AVENUE",
                "email": "rosa_gonzalez-freire_11226@gmail.com"
            },
            {
                "id": "52f0fce6a78ca97a8e6320968a528a6e",
                "name": "Jose Goris",
                "address": "769 Concourse Vlg W",
                "email": "jose_goris_10453@gmail.com"
            },
            {
                "id": "bed7f841fc9db79042d5e8ce4598cb25",
                "name": "Melissa Chan",
                "address": "133-36 41st Road, Suite 1",
                "email": "melissa_chan_11372@gmail.com"
            },
            {
                "id": "2dba099a3eb857ddb9d55c13a4c224f8",
                "name": "Jerome Cariaso",
                "address": "600 West 150th Street",
                "email": "jerome_cariaso_10030@gmail.com"
            },
            {
                "id": "795172103f7fe7d3f64acf643a37d0a5",
                "name": "Yvonne Essandoh",
                "address": "1624 University Avenue",
                "email": "yvonne_essandoh_10453@gmail.com"
            },
            {
                "id": "8057d25f5a4f47498170b6959cf78b72",
                "name": "Sam Weissman",
                "address": "59-17 Junction Blvd",
                "email": "sam_weissman_11379@gmail.com"
            },
            {
                "id": "c45df7e07f7733a926575653da44e3fa",
                "name": "Daniel St-Pierre",
                "address": "136-20 38th Ave Suite 6M",
                "email": "daniel_st-pierre_11368@gmail.com"
            },
            {
                "id": "9137eee23ba9d1ef29221d85310b62ee",
                "name": "Olusanya Rufai",
                "address": "166 5th Ave",
                "email": "olusanya_rufai_10019@gmail.com"
            },
            {
                "id": "1b0649da9aaa93ce92f90eef4dea4e34",
                "name": "Charles Jean Cloude",
                "address": "214-08 Hillside Avenue",
                "email": "charles_jean_cloude_11411@gmail.com"
            },
            {
                "id": "e281fae57a773858ffdf15d65aad49ef",
                "name": "George Owusu",
                "address": "-",
                "email": "george_owusu_11205@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "add2943c0bc339b402dc91626dead2e5",
                "name": "Jaxier Chacon",
                "address": "435 fort Washington Avenue",
                "email": "jaxier_chacon_10065@gmail.com"
            },
            {
                "id": "635a1e3cb9bb061fc67e21615e496c4b",
                "name": "Larisa Khesina",
                "address": "68 Bayard Street",
                "email": "larisa_khesina_10013@gmail.com"
            },
            {
                "id": "eda51ea45f4d979a79fa3214971c92e2",
                "name": "Rafael Rodriguez",
                "address": "90-01 A Rosevelt Ave.",
                "email": "rafael_rodriguez_11355@gmail.com"
            },
            {
                "id": "a4d91194ff7157b52e6b55c2ba60fa91",
                "name": "Brett Wu",
                "address": "8701A Shore Road",
                "email": "brett_wu_11203@gmail.com"
            },
            {
                "id": "0aee2ddce0b40af3e9e84893e6f9e06f",
                "name": "Jamilah Grant-Guimaraes",
                "address": "225 east 149th street",
                "email": "jamilah_grant-guimaraes_10453@gmail.com"
            },
            {
                "id": "49c8011cf129cfcf57bb2c47547b4dfa",
                "name": "Eileen Hoffman",
                "address": "245 East 35th Street",
                "email": "eileen_hoffman_10012@gmail.com"
            },
            {
                "id": "c8119e36b1828018e69c152e22dd41d5",
                "name": "Michelle Senbertrand",
                "address": "2015 Grand Concourse",
                "email": "michelle_senbertrand_10467@gmail.com"
            },
            {
                "id": "1b5529624fd13473e71fed4e2d8c97e3",
                "name": "Jose Jerez",
                "address": "41-60 Main St. #205B",
                "email": "jose_jerez_11354@gmail.com"
            },
            {
                "id": "40854ca939344a1520e3d8d5b53ffd76",
                "name": "Jerry Uduevbo",
                "address": "12102 Hillside Avenue",
                "email": "jerry_uduevbo_11217@gmail.com"
            },
            {
                "id": "1a74459c3c8f3b4963572e3a9d2f77e1",
                "name": "Michael Abbey-Mensah",
                "address": "5 Avenue I",
                "email": "michael_abbey-mensah_11211@gmail.com"
            },
            {
                "id": "92d8c19c1831ddea5e21bec7922082e9",
                "name": "Francis DeVito",
                "address": "136-17 39th Avenue, Flushing NY, 11354, Suite CFC, 4th Floor",
                "email": "francis_devito_11374@gmail.com"
            },
            {
                "id": "88c07aed63ece7285bbc31aa9274c657",
                "name": "Shira Selevan",
                "address": "147-15 70TH RD",
                "email": "shira_selevan_11355@gmail.com"
            }
        ],
        "urologist": [
            {
                "id": "dbdfc996261d7e7ed15ddc2766842fe5",
                "name": "Austin Epstein",
                "address": "70-17 37 Avenue",
                "email": "austin_epstein_11372@gmail.com"
            },
            {
                "id": "6918e48a9b676a2d6d9e95c45bb9b058",
                "name": "Tarek Hegazi",
                "address": "435 Fort Washington Avenue #1H",
                "email": "tarek_hegazi_10022@gmail.com"
            },
            {
                "id": "f6309c0116df0c535f64985885c23ceb",
                "name": "Batool Hussaini",
                "address": "4434 Amboy Road",
                "email": "batool_hussaini_11356@gmail.com"
            },
            {
                "id": "7a5bc15372739f0d4e77eee87b348eaf",
                "name": "Alisa Minkin",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "alisa_minkin_10013@gmail.com"
            },
            {
                "id": "520249860dbf69728ab42e269164ce10",
                "name": "Henry Sardar",
                "address": "210 W 139th St",
                "email": "henry_sardar_10002@gmail.com"
            },
            {
                "id": "227bd753b1a5558b45bdff690af23ed9",
                "name": "Arthur Hall",
                "address": "856 Dekalb Avenue",
                "email": "arthur_hall_11211@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "3108ca24a0ed7a7fce101bc77653d59c",
                "name": "Larisa Malisova",
                "address": "211-16 Union Turnpike",
                "email": "larisa_malisova_11372@gmail.com"
            },
            {
                "id": "c63462d135719a731ddb4411f5d8ceb3",
                "name": "Marie Belotte",
                "address": "142-03 60th Ave",
                "email": "marie_belotte_11372@gmail.com"
            },
            {
                "id": "c006cf238de83d4115975a69fbeda3d7",
                "name": "Violeta Gomez",
                "address": "821 57th Street",
                "email": "violeta_gomez_11205@gmail.com"
            },
            {
                "id": "b3039b9a864f71a8247fd9f6dca4ae99",
                "name": "Mario Saint-Laurent",
                "address": "1153 58 Street",
                "email": "mario_saint-laurent_11213@gmail.com"
            },
            {
                "id": "a5237a1e698666ff891c032f0a78cdea",
                "name": "Eddie Yang",
                "address": "4028 82ND STREET",
                "email": "eddie_yang_11372@gmail.com"
            },
            {
                "id": "33fa8621fed97beb6f13c46ff90647ef",
                "name": "Nina Huberman",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "nina_huberman_10462@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "0a69790d8105529e408bf2dc9728261a",
                "name": "Lenard Marchetta",
                "address": "88-01 Parson Blvd",
                "email": "lenard_marchetta_11402@gmail.com"
            },
            {
                "id": "ed81a990130ea88a97faded35a29709f",
                "name": "Ghanshyam Bhambhani",
                "address": "15 Wadsworth Ave.",
                "email": "ghanshyam_bhambhani_10021@gmail.com"
            },
            {
                "id": "42e3b864d67578892d362c773e1fea70",
                "name": "Dharamjit N. Kumar",
                "address": "133-29 41st Road, Suite 2B",
                "email": "dharamjit_n._kumar_11375@gmail.com"
            },
            {
                "id": "ca3ce4534c83b43be221bb2338ceddae",
                "name": "Farzana Nizami",
                "address": "2015 Grand Concourse",
                "email": "farzana_nizami_10467@gmail.com"
            },
            {
                "id": "d774491fe47706c38dbd1b9363e52169",
                "name": "Daniel Wasserman",
                "address": "9817 Queens Boulevard, LL2",
                "email": "daniel_wasserman_11368@gmail.com"
            },
            {
                "id": "a9078cf318a8b81779d9a5f689353455",
                "name": "George McMillan",
                "address": "245 East 35th Street",
                "email": "george_mcmillan_10012@gmail.com"
            },
            {
                "id": "270c6a80333e0b939604b83c024b5c14",
                "name": "Samina Raghid",
                "address": "185 Canal St",
                "email": "samina_raghid_11215@gmail.com"
            },
            {
                "id": "6bc7027558a8fe3d07b609838a126fea",
                "name": "Julio Ramirez",
                "address": "67 Irving Place, 5th Floor",
                "email": "julio_ramirez_10013@gmail.com"
            },
            {
                "id": "cb31cfe08fac03d85eab4f21ece1f35c",
                "name": "Yadiera Brown",
                "address": "37-33 77th Street",
                "email": "yadiera_brown_11422@gmail.com"
            },
            {
                "id": "1099002a63fbd322edbd59bc1d7b586d",
                "name": "Po Cheng Chu",
                "address": "314 West 14th Street",
                "email": "po_cheng_chu_11355@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "7963726559cb70a30a3ab32f37b0d4fd",
                "name": "Khurram Awan",
                "address": "13710 FRANKLIN AVE",
                "email": "khurram_awan_11692@gmail.com"
            },
            {
                "id": "4129e8ce9a15961dd6599529f5228723",
                "name": "Qurrath Ain",
                "address": "121-02 Hillside Avenue",
                "email": "qurrath_ain_11203@gmail.com"
            },
            {
                "id": "224e70f2d16347c2d75b919bd6f45c3c",
                "name": "YUMEI DING",
                "address": "37-57 91st Street",
                "email": "yumei_ding_11354@gmail.com"
            },
            {
                "id": "9c4b8af92089c090edf4d82c6423b5b5",
                "name": "Franklin Sencion",
                "address": "109-33 71 Road, Suite 1B",
                "email": "franklin_sencion_11355@gmail.com"
            },
            {
                "id": "bdef99380febe1db4881ab464da598c5",
                "name": "Emilio Villegas",
                "address": "2233 Nostrand Avenue",
                "email": "emilio_villegas_11237@gmail.com"
            },
            {
                "id": "8650d986253c6765be209a1411105f7c",
                "name": "Muhammad M. Haque",
                "address": "2386 Jerome Avenue",
                "email": "muhammad_m._haque_10458@gmail.com"
            },
            {
                "id": "2810f912a9ad87f90ad1e798ba3494a1",
                "name": "Michelle K Samuels",
                "address": "47 Sickles suite 1A",
                "email": "michelle_k_samuels_10038@gmail.com"
            },
            {
                "id": "33353e5a68a2e808f9b74add71d0ac9f",
                "name": "Manuel Sy",
                "address": "730 58th Street, 1F",
                "email": "manuel_sy_11220@gmail.com"
            },
            {
                "id": "e9f001f1d098723b6721ae9ddefd3bd8",
                "name": "Calvin Chin",
                "address": "23-22 30th Ave.",
                "email": "calvin_chin_11373@gmail.com"
            },
            {
                "id": "95522463cbddb37673653e0dd0f450af",
                "name": "Eugene Dinkevich",
                "address": "120 E. 36th Street",
                "email": "eugene_dinkevich_10023@gmail.com"
            },
            {
                "id": "7b410cfb04a9c3b3f71d5037280fe0cc",
                "name": "Ari Klapholz",
                "address": "471 Hart Street",
                "email": "ari_klapholz_11235@gmail.com"
            },
            {
                "id": "45547edfecda33f2fdbdd3ea8206ad52",
                "name": "Michael M. Koegel",
                "address": "1335 Ocean Parkway",
                "email": "michael_m._koegel_11213@gmail.com"
            },
            {
                "id": "dca9199d8525e96e39790ef3dd200856",
                "name": "Pervaiz I. Qureshi",
                "address": "6506 Roosevelt Ave",
                "email": "pervaiz_i._qureshi_11375@gmail.com"
            },
            {
                "id": "a52bd1f352082b1afdb47dd9c9424894",
                "name": "Laura Dattner",
                "address": "4250 Broadway Suite 1C",
                "email": "laura_dattner_10032@gmail.com"
            },
            {
                "id": "06dc8dc279a2dc54a54b3497b773b066",
                "name": "Llewellyn Hyacinthe",
                "address": "1103 Cortelyou Road",
                "email": "llewellyn_hyacinthe_11230@gmail.com"
            },
            {
                "id": "1fc659931a750e42d210dc5ae01ff6d3",
                "name": "Vera Antonios",
                "address": "219-49 Jamaica Avenue",
                "email": "vera_antonios_11354@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "28f279d87bbabe61fa5715c9f15d4bca",
                "name": "Jung-ah Han",
                "address": "594 Broadway Suite 310",
                "email": "jung-ah_han_10016@gmail.com"
            },
            {
                "id": "db3776b3de8df4d6e249708d1c1be3cd",
                "name": "Alexander Choi",
                "address": "196-15 Hillside Ave",
                "email": "alexander_choi_11377@gmail.com"
            },
            {
                "id": "9284acb7de90eabfee9aad39551c4f3a",
                "name": "Pedro Corzo",
                "address": "241-08 140th Ave",
                "email": "pedro_corzo_11354@gmail.com"
            },
            {
                "id": "c655d785e31ae80a64bfadd7c7f8e20e",
                "name": "Himanshu Pandya",
                "address": "93-15 Roosevelt Avenue",
                "email": "himanshu_pandya_11372@gmail.com"
            },
            {
                "id": "f76ffcb3a7dcb08f27873a5c05545e3f",
                "name": "Victor Peralta",
                "address": "1125 Fulton Street",
                "email": "victor_peralta_11233@gmail.com"
            },
            {
                "id": "c466378fdf73c86669871131491fd576",
                "name": "Sarah Ponce",
                "address": "95-42 Roosevelt Avenue",
                "email": "sarah_ponce_11379@gmail.com"
            },
            {
                "id": "d51b0f20efd94aec91b12375f9fe09bb",
                "name": "Joseph Poon",
                "address": "594 Broadway, Suite 310",
                "email": "joseph_poon_10013@gmail.com"
            },
            {
                "id": "5aa03ac1bd315ec455f1928ed73a6d71",
                "name": "Givvi Lauren",
                "address": "8008 Third Avenue",
                "email": "givvi_lauren_11236@gmail.com"
            },
            {
                "id": "8fbb1e548c2e001c2e76f626a2d8c458",
                "name": "Mohamed Azam",
                "address": "354 Monroe Place",
                "email": "mohamed_azam_11203@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "994f4d1634c03572779fd4dc372ca4c0",
                "name": "Sultan Ahmed",
                "address": "39-07 Prince Street, Suite 3A",
                "email": "sultan_ahmed_11435@gmail.com"
            },
            {
                "id": "16d5ab6fc8da447d82b3884e0ac0680f",
                "name": "Alain Sosa",
                "address": "196-21 Hillside Avenue",
                "email": "alain_sosa_11418@gmail.com"
            },
            {
                "id": "64789d3e741e464fbe17043b0ca5eb06",
                "name": "Helen Na-Chuang",
                "address": "-",
                "email": "helen_na-chuang_11205@gmail.com"
            },
            {
                "id": "4443a0e93dd236a79ef3cea6b8296547",
                "name": "Blanche Mercedes",
                "address": "360 1st Avenue Apartment MG",
                "email": "blanche_mercedes_10018@gmail.com"
            },
            {
                "id": "f332b6fb25c068cec2dc87acc71f820e",
                "name": "Yelena Vayntrub",
                "address": "1509 Rockaway Parkway",
                "email": "yelena_vayntrub_11209@gmail.com"
            },
            {
                "id": "4be591d267b6d42ac2387debb7e37de1",
                "name": "Bill Wagner",
                "address": "131-76 Laurelton Parkway",
                "email": "bill_wagner_11411@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "816bd942a8a948450e377ce335d7e18a",
                "name": "Tak Chan",
                "address": "706 Banner Ave.",
                "email": "tak_chan_11220@gmail.com"
            },
            {
                "id": "25f22e35589776340007ae72cee5289e",
                "name": "Jae Lee",
                "address": "60 W Kingsbridge Road",
                "email": "jae_lee_10458@gmail.com"
            },
            {
                "id": "10f552759cd26e3ba0c298a322240593",
                "name": "Catherine Alikor Mpi",
                "address": "3134 E. Tremont Ave",
                "email": "catherine_alikor_mpi_10461@gmail.com"
            },
            {
                "id": "cb9d4c451e842e13e680fb86855ecb76",
                "name": "Jose Aponte",
                "address": "2015 Grand Concourse",
                "email": "jose_aponte_10467@gmail.com"
            },
            {
                "id": "cc76c887e4255d92ef8dd10d01259bc6",
                "name": "Larisa Veksman",
                "address": "92-11 35TH AVENUE, SUITE 1E",
                "email": "larisa_veksman_11373@gmail.com"
            },
            {
                "id": "d744f097c8d14ab3d0ddffa9b92d314a",
                "name": "Jack Apelbaum",
                "address": "166 5th Ave",
                "email": "jack_apelbaum_10019@gmail.com"
            },
            {
                "id": "60332b9ffdd8a05073f7b2373f22c818",
                "name": "Alfonso Ortiz",
                "address": "311 Audubon Ave, 2nd Fl",
                "email": "alfonso_ortiz_10033@gmail.com"
            },
            {
                "id": "fd6f031b2236f4dd7897fb87f8520fb7",
                "name": "S Gandhi",
                "address": "833 58th Street",
                "email": "s_gandhi_11224@gmail.com"
            },
            {
                "id": "c2754f4d497e7b6d7c5ddaa74ac968d6",
                "name": "Iqbal Merchant",
                "address": "112-03 Queens Blvd",
                "email": "iqbal_merchant_11354@gmail.com"
            },
            {
                "id": "efa487e3d37f3dcf6dfbde425ec5675e",
                "name": "Maria Diaz",
                "address": "3709 9th Street",
                "email": "maria_diaz_11221@gmail.com"
            },
            {
                "id": "95355705e30588a771f9ebaf2b68d26f",
                "name": "Yves Verna",
                "address": "739 Knickerbocker Avenue",
                "email": "yves_verna_11203@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "80c46d73842e1d0a6571e80980c552db",
                "name": "Marie Dy-Guillaume",
                "address": "800 A 5th Avenue Suite 301",
                "email": "marie_dy-guillaume_10003@gmail.com"
            },
            {
                "id": "ef2f5d956ca087e722233496089ac1e9",
                "name": "Kira Gelfenshteyn",
                "address": "3134 E. Tremont Ave",
                "email": "kira_gelfenshteyn_10461@gmail.com"
            },
            {
                "id": "e08155c2fbde098992cf3e58e25143bd",
                "name": "Elizabeth Cruz",
                "address": "29-22 30th Avenue",
                "email": "elizabeth_cruz_11368@gmail.com"
            },
            {
                "id": "e1d960bbc000679bc797b2c07ac3d2f4",
                "name": "Marrissa Pelletier",
                "address": "762 59th Street",
                "email": "marrissa_pelletier_11210@gmail.com"
            },
            {
                "id": "dc44db0c59db9634f309fb4f9a8475ef",
                "name": "Jonathan MT Chang",
                "address": "353 Fort Washington Avenue #1E",
                "email": "jonathan_mt_chang_10025@gmail.com"
            },
            {
                "id": "db179a20be12dcb5c764c7f5692705ea",
                "name": "Yanfeng Chen",
                "address": "18-12 College Point Blvd",
                "email": "yanfeng_chen_10021@gmail.com"
            },
            {
                "id": "98fb32a4c0cd6b7462ee2f8dd6305676",
                "name": "Carmen Co",
                "address": "9817 Queens Boulevard, LL2",
                "email": "carmen_co_11368@gmail.com"
            },
            {
                "id": "80939e7f5a3566a80e4ae565ba29dce6",
                "name": "Sayera Haque",
                "address": "314 West 14th Street",
                "email": "sayera_haque_11355@gmail.com"
            },
            {
                "id": "1ef83697b2811c3efd185ee90a4e676b",
                "name": "Thomas Bustros",
                "address": "136-403 9th Avnue",
                "email": "thomas_bustros_11103@gmail.com"
            },
            {
                "id": "4c57cd315da9358ca82c7956ec8c874a",
                "name": "Melissa Hutt",
                "address": "19 Hamilton Place",
                "email": "melissa_hutt_10013@gmail.com"
            },
            {
                "id": "165103d378ffad47749ec9059800abb8",
                "name": "Howard J Rosman",
                "address": "571 Academy Street, Apt. GLE",
                "email": "howard_j_rosman_10016@gmail.com"
            },
            {
                "id": "d01c3143931948d41bbb4d370d165dc0",
                "name": "Jay Bienenfeld",
                "address": "1664 East 14th Street, Suite 401",
                "email": "jay_bienenfeld_11224@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "1e3981fda95c9d7ee28c1c7f25d5cc13",
                "name": "CHAUDHRY GHUMMAN",
                "address": "90-01 A Rosevelt Ave.",
                "email": "chaudhry_ghumman_11355@gmail.com"
            },
            {
                "id": "c50a724fe604d1ed795c87c3abfca6d8",
                "name": "Mikhail Pinkhasov",
                "address": "314 West 14th Street",
                "email": "mikhail_pinkhasov_11355@gmail.com"
            },
            {
                "id": "e0fdceeda54e9dc02f3fd1f1a3d3d0ab",
                "name": "Maria Gomez",
                "address": "3125 TIBBETT AVENUE",
                "email": "maria_gomez_10459@gmail.com"
            },
            {
                "id": "7bc709ce5542daba2194943f25822deb",
                "name": "Ian Lustbader",
                "address": "141-49 70 Road",
                "email": "ian_lustbader_11385@gmail.com"
            },
            {
                "id": "167fdf0e996d580ce9c7fbc783bedfcc",
                "name": "Lucille L. Pak",
                "address": "196-02 hillside",
                "email": "lucille_l._pak_11432@gmail.com"
            },
            {
                "id": "17673a783c573fcca06b5df2ed4dbd0e",
                "name": "Edward Chan",
                "address": "102-11 Roosevelt Avenue",
                "email": "edward_chan_10011@gmail.com"
            },
            {
                "id": "14344ac0197ee06c0629343f76e6be3c",
                "name": "Francois Brutus",
                "address": "1664 East 14th Street, Suite 501",
                "email": "francois_brutus_11209@gmail.com"
            },
            {
                "id": "7adbaccaca2d7ebcbeef318a1d0be114",
                "name": "Leonore Max",
                "address": "141-49 70 Road",
                "email": "leonore_max_11385@gmail.com"
            },
            {
                "id": "6ac214588d01d160358fbd2327095f63",
                "name": "Maria Perea-Barbosa",
                "address": "1421 Carroll Street",
                "email": "maria_perea-barbosa_11220@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "c66b3b62804208008080b4032b43316a",
                "name": "Gabriel Gustin",
                "address": "9425 59th Avenue Suite f7",
                "email": "gabriel_gustin_11368@gmail.com"
            },
            {
                "id": "7017b611019b71178fa32a92f80aae6a",
                "name": "Mitchell Locke",
                "address": "342 Beach 54th Street",
                "email": "mitchell_locke_11418@gmail.com"
            },
            {
                "id": "3fa5dc125a58f68c083be12c8493d92f",
                "name": "Jeffrey Chess",
                "address": "1497 Richmond Road",
                "email": "jeffrey_chess_11418@gmail.com"
            },
            {
                "id": "034e8eeef4c11279841142da53f12e2c",
                "name": "Sunanda Chugh",
                "address": "41-61 Kissena Blvd.",
                "email": "sunanda_chugh_11355@gmail.com"
            },
            {
                "id": "fd254f2a3bbc21508e1ada14038e272d",
                "name": "Sofya Kostanyan",
                "address": "41 Mott St",
                "email": "sofya_kostanyan_10033@gmail.com"
            },
            {
                "id": "88774a99a8605b12495e32b88bd9ea5a",
                "name": "Mandy Marantz",
                "address": "87-04 Rockaway Beach Blvd",
                "email": "mandy_marantz_11377@gmail.com"
            },
            {
                "id": "25c14c0c9f4a608c0dfef2e2c11fc6a5",
                "name": "Hector Valencia",
                "address": "4250 Broadway Suite 1A",
                "email": "hector_valencia_10024@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "949142583ee63e27a20a41d441c5bf94",
                "name": "Jay Kripalani",
                "address": "40-04 Bowne Street, Suite 1i",
                "email": "jay_kripalani_11355@gmail.com"
            },
            {
                "id": "427c0fdd942aed8c98cce964f4d46a9e",
                "name": "Eman Soultan",
                "address": "111 West 110 Street",
                "email": "eman_soultan_10031@gmail.com"
            },
            {
                "id": "bbf8a85c4d515966f9d13c209a627ab0",
                "name": "Raji Ayinla",
                "address": "410 Lakeville Road, Suite 202",
                "email": "raji_ayinla_11377@gmail.com"
            },
            {
                "id": "2ee7c9adb12e223a2a5df266c1aa98d3",
                "name": "Meron Kristos",
                "address": "250 W57th Street Ste 1430",
                "email": "meron_kristos_10031@gmail.com"
            },
            {
                "id": "9785e0bfb17476d52d8f52f84ced75a9",
                "name": "Kevin Armington",
                "address": "1742 East 13th Street",
                "email": "kevin_armington_11210@gmail.com"
            },
            {
                "id": "314a0d810c4058e73c59165e11ec8eea",
                "name": "Altaf Khan",
                "address": "170 W.233rd Street",
                "email": "altaf_khan_10457@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "1e917b1bc7844e478b13d37377f26ed4",
                "name": "Richard Perrin",
                "address": "125 11 LIBERTY AVENUE",
                "email": "richard_perrin_11372@gmail.com"
            },
            {
                "id": "b1b959963231308e4a1e161cacc2fbf9",
                "name": "Erica Amianda",
                "address": "305 Seguine Ave Ste. 1",
                "email": "erica_amianda_10305@gmail.com"
            },
            {
                "id": "f6d86db126cb8ac94466d4b6d92d6195",
                "name": "Damaris Collado",
                "address": "155 West 19th St",
                "email": "damaris_collado_10003@gmail.com"
            },
            {
                "id": "197fc5b31e601ec59340775b65fa85ec",
                "name": "Tatyana Ledovsky",
                "address": "-3728 77th St",
                "email": "tatyana_ledovsky_11432@gmail.com"
            },
            {
                "id": "6b23380486143ae11b1adfd297f5a13c",
                "name": "Nathaniel Brownlow",
                "address": "133-04 41st Ave",
                "email": "nathaniel_brownlow_11354@gmail.com"
            },
            {
                "id": "88e2ee07c3ce14c157def01741c4b482",
                "name": "Florentino Reyes",
                "address": "221 Canal Street, Suite#302",
                "email": "florentino_reyes_10028@gmail.com"
            },
            {
                "id": "1cd035a73f1b0af6b3f9d891d2c31564",
                "name": "Norayr Baboumian MD",
                "address": "161 St. NIcholas Avenue",
                "email": "norayr_baboumian_md_11221@gmail.com"
            },
            {
                "id": "794a8e379ca43db1c82db62634f816b2",
                "name": "Eugene (Chien K.) Chiang",
                "address": "2015 Grand Concourse",
                "email": "eugene_(chien_k.)_chiang_10467@gmail.com"
            },
            {
                "id": "9b62e2158773a3b4d8c057e635c04cc5",
                "name": "John Mark",
                "address": "1125 Fulton Street",
                "email": "john_mark_11233@gmail.com"
            },
            {
                "id": "a1db5bf5d0d050eb6dd1ec8e25748197",
                "name": "Richard Myint",
                "address": "501 Main Street",
                "email": "richard_myint_10034@gmail.com"
            },
            {
                "id": "a52082af8b8567adc791597e4f45eb01",
                "name": "Altagracia Navarro",
                "address": "217 Ovington Avenue",
                "email": "altagracia_navarro_11210@gmail.com"
            },
            {
                "id": "e9a803b271dbaf688c5490d513a91461",
                "name": "Tinatin Urphanishvili",
                "address": "432 Bedford Avenue",
                "email": "tinatin_urphanishvili_11208@gmail.com"
            },
            {
                "id": "acccf8d2922a5ec09a981c33c7c26f9e",
                "name": "Eric Zhou",
                "address": "170 W.233rd Street",
                "email": "eric_zhou_10457@gmail.com"
            },
            {
                "id": "a040230bd148271d7376f4f2c4dc3c58",
                "name": "NABIL RAOOF",
                "address": "1664 East 14th Street, Suite 302",
                "email": "nabil_raoof_11221@gmail.com"
            },
            {
                "id": "288b9eae7f75e8000c74fddd476b6e45",
                "name": "Maria Soto",
                "address": "245 West 19th Street #CF",
                "email": "maria_soto_10128@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "78a9f9448fbd52016a054beb6eca8197",
                "name": "Jiansheng Zhao",
                "address": "314 W. 14th Street",
                "email": "jiansheng_zhao_10027@gmail.com"
            },
            {
                "id": "7796f9f03d9535a3cd45f7065892b88b",
                "name": "Karen Adamson",
                "address": "1280 Givan Avenue",
                "email": "karen_adamson_10453@gmail.com"
            },
            {
                "id": "a24b2e252e146b4dfbeac5868ee7edc2",
                "name": "Michael Gehl",
                "address": "136-20 38th Ave,Suite 8E",
                "email": "michael_gehl_11354@gmail.com"
            },
            {
                "id": "2ef1f2b13c3316479d47b61f33cbf61e",
                "name": "George Fernaine",
                "address": "501 Main Street",
                "email": "george_fernaine_10034@gmail.com"
            },
            {
                "id": "6cee39c12187c62483331a68399cda4a",
                "name": "Sudhakar Bhagavath",
                "address": "108 E 96th St",
                "email": "sudhakar_bhagavath_10021@gmail.com"
            },
            {
                "id": "485e049ee8afd5110fcf378999327d22",
                "name": "Angela Davydov",
                "address": "33 8th Ave, Ground Floor",
                "email": "angela_davydov_11217@gmail.com"
            },
            {
                "id": "9c4b16220922df1b19fa842663799752",
                "name": "Chaim Backman",
                "address": "629 W 185th St, 2nd Floor",
                "email": "chaim_backman_10013@gmail.com"
            },
            {
                "id": "902f19836c6705d426423badc9c18d72",
                "name": "Vandana Patil",
                "address": "7318 13th Avenue445 Park Avenue",
                "email": "vandana_patil_11220@gmail.com"
            },
            {
                "id": "d2db7e8361a0e6aa4bbd841730de0680",
                "name": "Kim Woods",
                "address": "1250 Shakespeare Avenue",
                "email": "kim_woods_10457@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "e185bc0c6af35b523bd29f37ab4f34b2",
                "name": "Petr Itzhak",
                "address": "675 Nereid Avenue",
                "email": "petr_itzhak_10453@gmail.com"
            },
            {
                "id": "7bad8d7c15eb2b6a4f916dc6cc2170b3",
                "name": "Ing-Yann Jeng",
                "address": "730 58th Street, 1F",
                "email": "ing-yann_jeng_11220@gmail.com"
            },
            {
                "id": "b4ccc2b2831b0c58044bb4297cc56f46",
                "name": "Cheng Gonjon",
                "address": "2386 Jerome Avenue",
                "email": "cheng_gonjon_10458@gmail.com"
            },
            {
                "id": "24aaa503bcd1256354bc4e4f8ebb7c8e",
                "name": "Howard Grossman",
                "address": "3410-3418 Broadway, 2nd floor",
                "email": "howard_grossman_10033@gmail.com"
            },
            {
                "id": "2bdfdd14b7b35b2feac8eed253b63d40",
                "name": "Zurab Abayev",
                "address": "80-37 Broadway",
                "email": "zurab_abayev_11354@gmail.com"
            },
            {
                "id": "c571389f2bb869b58c9c823255dd3732",
                "name": "Velko Voynov",
                "address": "241-11 147th Ave",
                "email": "velko_voynov_11418@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "388ba7535f23567183f4bc42b316c98d",
                "name": "YAO QIKAI",
                "address": "1973 University Avenue",
                "email": "yao_qikai_10453@gmail.com"
            },
            {
                "id": "fb971cff96b249742aff9df9066dfb17",
                "name": "Larry Bishop",
                "address": "1627 Broadway",
                "email": "larry_bishop_10032@gmail.com"
            },
            {
                "id": "59f75fd1178662e9080858b5ba9a0a37",
                "name": "Suresh Hemrajani",
                "address": "1718 Pitkin Avenue",
                "email": "suresh_hemrajani_11203@gmail.com"
            },
            {
                "id": "63fa5c8d9c377bd1e92dd0b74b466133",
                "name": "Keith Joseph",
                "address": "39-07 Prince Street, Suite 3A",
                "email": "keith_joseph_11435@gmail.com"
            },
            {
                "id": "0d2e507911dd70a50995b17d58e8671c",
                "name": "Changhee Paek",
                "address": "1715 University Blvd",
                "email": "changhee_paek_10458@gmail.com"
            },
            {
                "id": "4163177504b85f1b39b50186bc4d308b",
                "name": "Vincent Pedre",
                "address": "12102 Hillside Avenue",
                "email": "vincent_pedre_11217@gmail.com"
            },
            {
                "id": "a59d72cb4249604260038daec32f0883",
                "name": "Lise Vincent",
                "address": "445 Park Avenue",
                "email": "lise_vincent_11211@gmail.com"
            },
            {
                "id": "ae693d2322da8a2805a5983bd5bedee8",
                "name": "Aaron Berger",
                "address": "1641 3rd Ave suite 27H",
                "email": "aaron_berger_10013@gmail.com"
            },
            {
                "id": "a1b131f58f74aded11bc23151f865e61",
                "name": "Amir Mayer",
                "address": "170 W.233rd Street",
                "email": "amir_mayer_10457@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "3410367f404ba62c709a2a7593c8e849",
                "name": "Rohini Thodge",
                "address": "155 West 19th St",
                "email": "rohini_thodge_10003@gmail.com"
            },
            {
                "id": "e24ac3194565fa40abbe933dcaf579b0",
                "name": "Erin Dalton",
                "address": "520 Neptune avenue",
                "email": "erin_dalton_11224@gmail.com"
            },
            {
                "id": "7e1d97927341e372db2c1510b7376ff7",
                "name": "Marcia Pehr",
                "address": "112-03 Queens Blvd, Suite 207",
                "email": "marcia_pehr_11368@gmail.com"
            },
            {
                "id": "4d5cca33658b6cdbed1347a48ca1270d",
                "name": "Amit Saxena",
                "address": "345 E37th Street Ste 303C",
                "email": "amit_saxena_10002@gmail.com"
            },
            {
                "id": "278c4cbbc54b1d8a6bb8848fa2b3b8c8",
                "name": "Sean Byrne",
                "address": "2385 Arthur Avenue, Suite 206",
                "email": "sean_byrne_10453@gmail.com"
            }
        ]
    },
    "Jackson Heights": {
        "general practitioner": [
            {
                "id": "2be5f8632364ac9f9dcd3b6ade02918a",
                "name": "Inna Bukharovich",
                "address": "136-30 Maple Ave/ #1A",
                "email": "inna_bukharovich_11411@gmail.com"
            },
            {
                "id": "867d693eba9b79710507b55083d9b048",
                "name": "Asbar Haaris",
                "address": "201 East 69th St",
                "email": "asbar_haaris_11355@gmail.com"
            },
            {
                "id": "13f349bf3744f10c2c2b121450ae390b",
                "name": "Michele Reed",
                "address": "445 Park Avenue",
                "email": "michele_reed_11211@gmail.com"
            },
            {
                "id": "4d7c00da454507af0e9ece518bc1ae96",
                "name": "GUSTAVO MELAMEDOFF",
                "address": "108-14 101th Avenue",
                "email": "gustavo_melamedoff_11104@gmail.com"
            },
            {
                "id": "eabb093c142e3d6e365cbcffb7aa8091",
                "name": "Maria Duran-Soriano",
                "address": "629W 185st",
                "email": "maria_duran-soriano_10040@gmail.com"
            },
            {
                "id": "1801d0899e7d98574199dcab79d1d861",
                "name": "Howard Naas",
                "address": "185 Canal Street",
                "email": "howard_naas_10033@gmail.com"
            },
            {
                "id": "0ded6d50313125dd43ae68df7ad08af3",
                "name": "Shivani Paliwal",
                "address": "1610 WILLIAMSBRIDGE RD",
                "email": "shivani_paliwal_10455@gmail.com"
            },
            {
                "id": "d69ba85eaffc8a35afcf96d10b799957",
                "name": "Eneida Agosto",
                "address": "220 A St. Nicholas Avenue",
                "email": "eneida_agosto_11237@gmail.com"
            },
            {
                "id": "5217a05d84b5f5685a725e97aef8808b",
                "name": "Marilyn Jackson",
                "address": "1545 Atlantic Avenue, Suite 108.",
                "email": "marilyn_jackson_11368@gmail.com"
            },
            {
                "id": "9968138c9e2a1fde3b04d5f2f32054d4",
                "name": "Elizabeth Schwartzburt",
                "address": "25-92 steinway street",
                "email": "elizabeth_schwartzburt_11374@gmail.com"
            },
            {
                "id": "4ac9ef381d4e8df3bc79a38c0afeff42",
                "name": "Rivka Stein",
                "address": "4207 30th Avenue",
                "email": "rivka_stein_11435@gmail.com"
            },
            {
                "id": "27d0a70e740cd04f8854c64d759636e9",
                "name": "Robert Bressner",
                "address": "121A West 20th Street",
                "email": "robert_bressner_10021@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "4852c65a8a299d16ee168bcb52bc9ac4",
                "name": "Aldo Arpaia",
                "address": "450 Clarkson Ave",
                "email": "aldo_arpaia_11203@gmail.com"
            },
            {
                "id": "64ddc2a15971d4abaa6e2c53eb589162",
                "name": "Louis Heisler",
                "address": "33 8th Ave, Ground Floor",
                "email": "louis_heisler_11217@gmail.com"
            },
            {
                "id": "44da0dfac7325df83b8b210f94a499bc",
                "name": "Pervaiz Qureshi",
                "address": "1931 Williamsbridge Road",
                "email": "pervaiz_qureshi_10453@gmail.com"
            },
            {
                "id": "61271668e36af758fdc60fb9750076ce",
                "name": "Dilruba Nabi",
                "address": "8 Chatham Square, Suite 800",
                "email": "dilruba_nabi_10021@gmail.com"
            },
            {
                "id": "97c86ffce45958a72d2c7d6019d13aec",
                "name": "Elaine Alvarez",
                "address": "121A West 20th Street",
                "email": "elaine_alvarez_10021@gmail.com"
            },
            {
                "id": "f611be9f920352024bc55a0f007c64cd",
                "name": "Olga Belostotsky",
                "address": "230 Beach 102nd St",
                "email": "olga_belostotsky_11373@gmail.com"
            },
            {
                "id": "efad78a14fe9aea9da2937bc927bf24d",
                "name": "Flora Lau",
                "address": "92-12 175th Street",
                "email": "flora_lau_11375@gmail.com"
            },
            {
                "id": "4a71fb2cdf32a3880690ee2d99416254",
                "name": "Fu Fu He",
                "address": "600 West 150th Street",
                "email": "fu_fu_he_10030@gmail.com"
            },
            {
                "id": "9c789c07c5f1ef6503dce2467e3593ec",
                "name": "Gulam Khan",
                "address": "121A West 20th Street",
                "email": "gulam_khan_10021@gmail.com"
            },
            {
                "id": "413a8f2026e2e142a4af3afdf4c453f5",
                "name": "Gardith Joseph",
                "address": "58 E. 116th St",
                "email": "gardith_joseph_10028@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "7e96738c59e6c15a5cfc7146a38be155",
                "name": "Sydney Chen",
                "address": "142 Joralemon Street, Suite 11B",
                "email": "sydney_chen_11238@gmail.com"
            },
            {
                "id": "a65b849d548f5703bb915942e0d3a57a",
                "name": "Sarat Bhumi MD",
                "address": "9317 Roosevelt Ave",
                "email": "sarat_bhumi_md_11354@gmail.com"
            },
            {
                "id": "a04df21e6f9936c952ead98e29ca3358",
                "name": "William Ankobiah",
                "address": "136-30 MAPLE AVENUE #2F",
                "email": "william_ankobiah_11206@gmail.com"
            },
            {
                "id": "9174161c7e754badd09afac798512a35",
                "name": "Raymond Jones",
                "address": "60 Plaza St E # E",
                "email": "raymond_jones_11238@gmail.com"
            },
            {
                "id": "f22d030e688e18187a8c80dfb14bb401",
                "name": "Hector Holson",
                "address": "1 Hanson pl, Ste. 708",
                "email": "hector_holson_11211@gmail.com"
            },
            {
                "id": "6262fd2cdd4f556a1144517591b31a2c",
                "name": "Sergey Prokhorov",
                "address": "89-18 134 street",
                "email": "sergey_prokhorov_11420@gmail.com"
            },
            {
                "id": "4f2cfa0412b7f60ab2e012f15592ad1a",
                "name": "Stephen Dillon",
                "address": "86 East 49th Street",
                "email": "stephen_dillon_11237@gmail.com"
            },
            {
                "id": "efdd5acb417617ea75d15c2f4d64d535",
                "name": "Felix Florimon",
                "address": "131-24 Rockaway Blvd",
                "email": "felix_florimon_11373@gmail.com"
            },
            {
                "id": "44fe07c893827b71b6f6450f9c3bb93d",
                "name": "Felix Rodriguez",
                "address": "4819 14th Avenue",
                "email": "felix_rodriguez_11221@gmail.com"
            },
            {
                "id": "41bc6717397e824d4180cbfdf5c6f0d6",
                "name": "Paul Nacier",
                "address": "131-24 Rockaway Blvd",
                "email": "paul_nacier_11373@gmail.com"
            },
            {
                "id": "f935a36c7b1805b7ffc30f3a39e8988d",
                "name": "Liliya Drukman",
                "address": "303 9th Avenue, Room 140",
                "email": "liliya_drukman_10032@gmail.com"
            },
            {
                "id": "5b168a41a915b362e1ae6990aadd7499",
                "name": "Susheel Kodail",
                "address": "1655 Richmond Ave",
                "email": "susheel_kodail_10306@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "5fecf8ae87df037e102bd037916cd1d6",
                "name": "Billy Geris",
                "address": "600 W 150th Ste. 4",
                "email": "billy_geris_10022@gmail.com"
            },
            {
                "id": "ec1e3d327d50ffe390f44b210930c981",
                "name": "Ching-Yin Lam",
                "address": "42-31 Colden Street, #109",
                "email": "ching-yin_lam_11375@gmail.com"
            },
            {
                "id": "f4adddd32b5250f4cfc3ab9c8e0c9cca",
                "name": "Danielle Ogopozo",
                "address": "2248 Richmond Road",
                "email": "danielle_ogopozo_10312@gmail.com"
            },
            {
                "id": "1840da55d0b8e8d8867b0d2fca7ce75a",
                "name": "Madhu Rajaram",
                "address": "3709 9th Street",
                "email": "madhu_rajaram_11221@gmail.com"
            },
            {
                "id": "6c2dbc62aeae0026feb14250921f67d9",
                "name": "Sveltana Spivak",
                "address": "7318 13th Avenue",
                "email": "sveltana_spivak_11216@gmail.com"
            },
            {
                "id": "77288ed2e8e5db6c2d2b992ae9428e25",
                "name": "Ernst Ducena",
                "address": "121-02 Hillside Avenue",
                "email": "ernst_ducena_11203@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "926b0ed27978a55c6fd8c4d75b0ea4bd",
                "name": "Donna Seminara",
                "address": "117-06 225th Street 1st Floor",
                "email": "donna_seminara_11372@gmail.com"
            },
            {
                "id": "262f85569cbd18e998f670d48fe0e823",
                "name": "Sudha Vijaykumar",
                "address": "650 First Ave - 7th F",
                "email": "sudha_vijaykumar_10033@gmail.com"
            },
            {
                "id": "1f656d33fc35a38c4215d03be6610fba",
                "name": "Kenneth Tam",
                "address": "40-08 Forley Street",
                "email": "kenneth_tam_11432@gmail.com"
            },
            {
                "id": "d8e4b2ea0c2e8365cf02ea7de1386907",
                "name": "Mayreen Kelleher",
                "address": "629 W 185th St",
                "email": "mayreen_kelleher_10016@gmail.com"
            },
            {
                "id": "bf29784abf764fb8a9e0f2e0b22d8dd1",
                "name": "Arnold Berlin",
                "address": "210 W 139th St",
                "email": "arnold_berlin_10002@gmail.com"
            },
            {
                "id": "9881ed74fd1a5e85300ee72cd9bd75d1",
                "name": "Rahila Butt",
                "address": "5 Debevoise Street",
                "email": "rahila_butt_11238@gmail.com"
            },
            {
                "id": "39e04eb7505dac0b9d3de609e25be611",
                "name": "Robin Frankel-Ovitsh",
                "address": "911 Park Avenue",
                "email": "robin_frankel-ovitsh_10044@gmail.com"
            },
            {
                "id": "254b7bd31b605003d784a74865bea55c",
                "name": "Ilora Rafique",
                "address": "3071 Perry Avenue",
                "email": "ilora_rafique_10453@gmail.com"
            },
            {
                "id": "4ab54f7aa3031b8302102b443a2e8535",
                "name": "Aleska Pelaez-Acosta",
                "address": "1153 58 Street",
                "email": "aleska_pelaez-acosta_11213@gmail.com"
            }
        ],
        "urologist": [
            {
                "id": "e72d28ae49aee882e7adc5f9e0875a50",
                "name": "Rounak Ahmed",
                "address": "93-20 A Roosevelt Avenue",
                "email": "rounak_ahmed_11103@gmail.com"
            },
            {
                "id": "8cd6625ee08e4e9f187971f2cddda330",
                "name": "Michael Richter",
                "address": "38-34 Parsons blvd #1A",
                "email": "michael_richter_11385@gmail.com"
            },
            {
                "id": "0649b5bf241f88e84e913f197b12b875",
                "name": "Urmila Shivaram",
                "address": "2385 Arthur Avenue, Suite 206",
                "email": "urmila_shivaram_10453@gmail.com"
            },
            {
                "id": "0fd622d150cfca2997e5b1909bdadb6b",
                "name": "Paul Romanello",
                "address": "160 East 32nd Street #102",
                "email": "paul_romanello_10028@gmail.com"
            },
            {
                "id": "3d21d27468aeea202152a221c4126e39",
                "name": "Ethan Ciment",
                "address": "1610 WILLIAMSBRIDGE RD",
                "email": "ethan_ciment_10455@gmail.com"
            },
            {
                "id": "56c5051ead18f7f03f7caf94fb405462",
                "name": "Lalit Patel",
                "address": "93-20 A Roosevelt Avenue",
                "email": "lalit_patel_11103@gmail.com"
            },
            {
                "id": "b1dc36ca5993b752becb3a1a35d8d0f3",
                "name": "Anthony R. Sgarlato",
                "address": "47-10 Greenpoint Avenue",
                "email": "anthony_r._sgarlato_11372@gmail.com"
            },
            {
                "id": "9899dfca1613dc7ec454a24cc523673e",
                "name": "Mitchell Kaphan",
                "address": "4434 Amboy Road",
                "email": "mitchell_kaphan_11356@gmail.com"
            },
            {
                "id": "8c20dca034430640c0d884098c753f38",
                "name": "EMMANUEL PEPRAH",
                "address": "9 East 63rd Street",
                "email": "emmanuel_peprah_10040@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "afeb76b8d16799d7000670335691dbbc",
                "name": "Mery Gomez",
                "address": "39-07 Prince St. Suite 3J",
                "email": "mery_gomez_11427@gmail.com"
            },
            {
                "id": "59957d3890f3941af55dae46e5231c25",
                "name": "Nahar Most",
                "address": "629 West 185th Street",
                "email": "nahar_most_11372@gmail.com"
            },
            {
                "id": "72e51df88434f22d1f91f6f546e701dc",
                "name": "Betty E. Stewart",
                "address": "160 E 72nd",
                "email": "betty_e._stewart_10012@gmail.com"
            },
            {
                "id": "d0093366641d45bdbce19224dc70727e",
                "name": "Garman Ho",
                "address": "67 Irving Place, 5th Floor",
                "email": "garman_ho_10013@gmail.com"
            },
            {
                "id": "dd916372192af031bbd1db6a5726c327",
                "name": "Betty Mercedes",
                "address": "209 Beach 125st",
                "email": "betty_mercedes_11354@gmail.com"
            },
            {
                "id": "69fc652db1c0d2990cae1924a784bc3c",
                "name": "Gerald Schulman",
                "address": "2385 Arthur Avenue, Suite @206",
                "email": "gerald_schulman_10468@gmail.com"
            },
            {
                "id": "55bd5225d518419d96d7696c51f7053f",
                "name": "Luiza Gusenon",
                "address": "125 East 86th Street",
                "email": "luiza_gusenon_10031@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "b7f5bee682a1e9ff50826da7592d5d3d",
                "name": "Byung Kang",
                "address": "196-15 Hillside Ave",
                "email": "byung_kang_11377@gmail.com"
            },
            {
                "id": "fd71bed8ae5a8aba92451142b9c2903d",
                "name": "George Liu",
                "address": "380 2nd Avenue, Suite 1002",
                "email": "george_liu_10028@gmail.com"
            },
            {
                "id": "a3eaa307ca3a23d3fe96ae0d02729655",
                "name": "Nadia Martinez de Pimentel",
                "address": "1517 Voorhies ave 1st floor",
                "email": "nadia_martinez_de_pimentel_11205@gmail.com"
            },
            {
                "id": "a2a55b13408cdaee420a66a8b001ad25",
                "name": "Claudia Ravins",
                "address": "3010 Grand Concourse",
                "email": "claudia_ravins_10462@gmail.com"
            },
            {
                "id": "1c0546a59e9e82a93eb4824495eef7dd",
                "name": "Carmina Rivera",
                "address": "1715 University Blvd",
                "email": "carmina_rivera_10458@gmail.com"
            },
            {
                "id": "f416d3e1ff732382befb144aba4d8371",
                "name": "Daniel Despen",
                "address": "2015 Grand Concourse",
                "email": "daniel_despen_10467@gmail.com"
            },
            {
                "id": "dc89b1776cad66906da73628b2ea03b1",
                "name": "Dana Jacobs",
                "address": "39 E Broadway Suite 606",
                "email": "dana_jacobs_10033@gmail.com"
            },
            {
                "id": "a46361f798b45dcc0f1532eb5626cceb",
                "name": "Elbert St. Claire, III",
                "address": "1627 Broadway",
                "email": "elbert_st._claire,_iii_10032@gmail.com"
            },
            {
                "id": "c5e3fa3d322d99aa95bdb5464b553dc8",
                "name": "Mark Schiffer",
                "address": "629 West 185th Street",
                "email": "mark_schiffer_11372@gmail.com"
            },
            {
                "id": "929bac5eae64c632c80ba5ca64c518c9",
                "name": "Tumika Williams Wilson",
                "address": "470 Malcolm X Boulevard",
                "email": "tumika_williams_wilson_10014@gmail.com"
            },
            {
                "id": "482ca42f850a0bfbca99594ae98eda6e",
                "name": "Gillian Haans",
                "address": "1262 Ocean Parkway",
                "email": "gillian_haans_11209@gmail.com"
            },
            {
                "id": "5051c5d08dd0daa5410a689f7d729dfb",
                "name": "Moshe Lazar",
                "address": "445 Park Avenue",
                "email": "moshe_lazar_11211@gmail.com"
            },
            {
                "id": "fb6cb64b6bd1fe5b4d8ae9c746186740",
                "name": "Robert Sable",
                "address": "2922 30TH AVENUE",
                "email": "robert_sable_11367@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "8a65359094e87180057a25a574d20e2b",
                "name": "Joseph Louis",
                "address": "90-10 Elmhurst Avenue",
                "email": "joseph_louis_11373@gmail.com"
            },
            {
                "id": "1d9f6ece68c2189094f140587f85386e",
                "name": "Darnley Renaud",
                "address": "629 West 185th Street",
                "email": "darnley_renaud_11372@gmail.com"
            },
            {
                "id": "d3a1c97072fc9f3b40e3c9c2415da0ff",
                "name": "Qaiser Abbas",
                "address": "4250 Broadway Suite 1A",
                "email": "qaiser_abbas_10024@gmail.com"
            },
            {
                "id": "7ea67fb9b46d0a5559e45e825ee7690a",
                "name": "Fausto Gonzalez",
                "address": "100 Ross Street",
                "email": "fausto_gonzalez_11230@gmail.com"
            },
            {
                "id": "844af8338422e6941fd02df1018e3910",
                "name": "Jaime Roman",
                "address": "730 58th Street, 1F",
                "email": "jaime_roman_11220@gmail.com"
            },
            {
                "id": "28875c3c212ce913533a998b121f95fd",
                "name": "Yan Wang",
                "address": "68 Bayard Street",
                "email": "yan_wang_10013@gmail.com"
            },
            {
                "id": "137b0593474a21a51abadf277c7133f6",
                "name": "Vikas Varma",
                "address": "2015 Grand Concourse",
                "email": "vikas_varma_10467@gmail.com"
            },
            {
                "id": "346f2c0155f26facda540ba24d3e0826",
                "name": "Deepak Amin",
                "address": "42-65 Kissena Blvd L4",
                "email": "deepak_amin_11416@gmail.com"
            },
            {
                "id": "437583a8579f43e6c9462acf471085fa",
                "name": "Futrell Junie",
                "address": "833 58th Street",
                "email": "futrell_junie_11224@gmail.com"
            },
            {
                "id": "659b69e39a2f023be43c7ccc30d3f941",
                "name": "Edward Geisler",
                "address": "4250 Broadway Suite 1C",
                "email": "edward_geisler_10032@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "3f851c361e50cc5003c020c17cffad4a",
                "name": "Farooq Umar Qureshi",
                "address": "1236 Fulton Street",
                "email": "farooq_umar_qureshi_11203@gmail.com"
            },
            {
                "id": "98014bf139b0c7a3e14831c514a3bcbe",
                "name": "Shazia Sami",
                "address": "38-34 Parsons Blvd #1-D",
                "email": "shazia_sami_11372@gmail.com"
            },
            {
                "id": "ac7b2eba19cd2b3b9fb5787b9281603d",
                "name": "Nayaz Ahmed",
                "address": "25-52 STEINWAY STREET",
                "email": "nayaz_ahmed_11691@gmail.com"
            },
            {
                "id": "092c377ce1840e2e37afd2cf13b8a2c9",
                "name": "Ingrid Felix-Peralta",
                "address": "1627 Broadway",
                "email": "ingrid_felix-peralta_10032@gmail.com"
            },
            {
                "id": "fa27e9512db8a8f70d5b68bcc90f1198",
                "name": "Rafael Barranco",
                "address": "196-15 Hillside Ave",
                "email": "rafael_barranco_11377@gmail.com"
            },
            {
                "id": "fa5eedfb65c729fa3b33031b07da5996",
                "name": "Juan Tapia-Mendoza",
                "address": "121-02 Hillside Avenue",
                "email": "juan_tapia-mendoza_11203@gmail.com"
            },
            {
                "id": "96175fef99134254ba74021e5beccf7f",
                "name": "Douglas Birns",
                "address": "25-92 steinway street",
                "email": "douglas_birns_11374@gmail.com"
            },
            {
                "id": "13f583cc869822acacfc31afb181d517",
                "name": "Simon Fensterszaub",
                "address": "911 Park Avenue",
                "email": "simon_fensterszaub_10044@gmail.com"
            },
            {
                "id": "0f2b200227f3af9f9eafbabf8f82c22b",
                "name": "Claude Pericles",
                "address": "121A West 20th Street",
                "email": "claude_pericles_10021@gmail.com"
            },
            {
                "id": "9bbf611e4f454a5dcb21c35c6030319a",
                "name": "David Treatman",
                "address": "139 Centre St.",
                "email": "david_treatman_10033@gmail.com"
            },
            {
                "id": "25265cf5e472725c65c27b9e966ec2fe",
                "name": "Steven Siegal",
                "address": "2-12 Sickles Street",
                "email": "steven_siegal_10003@gmail.com"
            },
            {
                "id": "54209d49f06a85da900aec2eb1c7cfdc",
                "name": "Caesar Mimieux",
                "address": "2847 Webster Avenue",
                "email": "caesar_mimieux_10467@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "efd4d49d066fb5588bc794bbc24ba691",
                "name": "Zamar Raza",
                "address": "3071 Perry Avenue",
                "email": "zamar_raza_10453@gmail.com"
            },
            {
                "id": "495b924a8349c89950a0ebd4154407f2",
                "name": "PANKAJ MAMTORA",
                "address": "372 Kingston Avenue",
                "email": "pankaj_mamtora_11226@gmail.com"
            },
            {
                "id": "8347fcdfd7af83b562feaa2e878e8f62",
                "name": "Geddis Abel-Bey",
                "address": "13620 38ave ste 6L",
                "email": "geddis_abel-bey_11411@gmail.com"
            },
            {
                "id": "c9b99c3fb8d15bad61a3e8dfa302b741",
                "name": "Ella Zavolunova",
                "address": "124 East 43rd Street",
                "email": "ella_zavolunova_11204@gmail.com"
            },
            {
                "id": "a75ab0fa01322971b136f103d4a4f38b",
                "name": "Jesika Shah",
                "address": "4506 8th Avenue",
                "email": "jesika_shah_11203@gmail.com"
            },
            {
                "id": "6bdc9ce59e7d8fee867b5f539d5ef1f6",
                "name": "Lin Gong",
                "address": "629W 185st",
                "email": "lin_gong_10040@gmail.com"
            },
            {
                "id": "9877d30fb747c1121bfd6a88b19b3b50",
                "name": "Josef Shimonov",
                "address": "114-06 Queens Blvd",
                "email": "josef_shimonov_11419@gmail.com"
            },
            {
                "id": "a09fe167514fc9fa5635403792086c9c",
                "name": "Gonzalo Urbano",
                "address": "159-05 92nd St.",
                "email": "gonzalo_urbano_11367@gmail.com"
            },
            {
                "id": "8948f75f1b18700df8651570c383e6f8",
                "name": "Raphael Novogrodski",
                "address": "25-52 STEINWAY STREET",
                "email": "raphael_novogrodski_11691@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "cd743d4e5008682e395122eb17b32ff1",
                "name": "Daysi Baez",
                "address": "112-03 Queens Blvd, Suite 207",
                "email": "daysi_baez_11368@gmail.com"
            },
            {
                "id": "7d6dd0e0ed5eb79c42453dadd63b3df6",
                "name": "Devbala Ramanathan",
                "address": "139-16 91st Avenue",
                "email": "devbala_ramanathan_10453@gmail.com"
            },
            {
                "id": "539132720a90d060af6b0f09c3a4bce2",
                "name": "Hector Florimon",
                "address": "600 West 150th Street",
                "email": "hector_florimon_10030@gmail.com"
            },
            {
                "id": "b9803890359242ccd22ca35232857a54",
                "name": "Coralys Vega",
                "address": "136-20 38th Ave. #7G",
                "email": "coralys_vega_11435@gmail.com"
            },
            {
                "id": "589460b12a1acf534400a2897fe66d73",
                "name": "Gunther Groning",
                "address": "6506 Roosevelt Ave",
                "email": "gunther_groning_11375@gmail.com"
            },
            {
                "id": "532accc1d0b29a5dcf9b2ace4e92d5dd",
                "name": "Max Francois",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "max_francois_10013@gmail.com"
            },
            {
                "id": "45ad116d22f1e5d1a8ce32afcb026fe6",
                "name": "Sirisha R. Tikko",
                "address": "1517 Voorhies ave 1st floor",
                "email": "sirisha_r._tikko_11205@gmail.com"
            },
            {
                "id": "179874fe89357950a7baffaac835e01b",
                "name": "Geraldo Lombardo",
                "address": "95 University Place",
                "email": "geraldo_lombardo_10011@gmail.com"
            },
            {
                "id": "cb23642f19588fe92f2686160dabc904",
                "name": "Wesner Moise",
                "address": "1211 White Plains Rd",
                "email": "wesner_moise_10472@gmail.com"
            },
            {
                "id": "2f1042081a2be0a0f9f952dd25837a64",
                "name": "Christopher Kacin",
                "address": "303 9th Avenue, Room 140",
                "email": "christopher_kacin_10032@gmail.com"
            },
            {
                "id": "cca9e9f984c1eba77e089e78205e380d",
                "name": "Rasik Lal Patel",
                "address": "600 West 150th Street",
                "email": "rasik_lal_patel_10030@gmail.com"
            },
            {
                "id": "bf3277c4e03660a1f8551915aff1f9cd",
                "name": "Louisa Ziglar",
                "address": "820 2nd Ave",
                "email": "louisa_ziglar_10011@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "bd0b4635fa20280966386d3bc05d81ff",
                "name": "Mario Lavelanet",
                "address": "3200 Bronx Blvd",
                "email": "mario_lavelanet_10463@gmail.com"
            },
            {
                "id": "98cbb8354a0f228a9984d00b071be01f",
                "name": "Yuan Yi Li",
                "address": "4207 30th Avenue",
                "email": "yuan_yi_li_11435@gmail.com"
            },
            {
                "id": "6c3cc9cb6e08eb5145d28f0931d68ad6",
                "name": "Mikhail Pinkhasov",
                "address": "211-16 Union Turnpike",
                "email": "mikhail_pinkhasov_11372@gmail.com"
            },
            {
                "id": "357c7f2d11907102a774971cfd23d4a2",
                "name": "Alejandra Wilson",
                "address": "4039 Junction Blvd",
                "email": "alejandra_wilson_11042@gmail.com"
            },
            {
                "id": "cea26a9c4e4baae1e5854dd5b292f0a3",
                "name": "Nurun N. Yusuf",
                "address": "42 Broadway Ave",
                "email": "nurun_n._yusuf_10028@gmail.com"
            },
            {
                "id": "ba233c61bfc5a1c7aa984c5c01a11b0f",
                "name": "Naghma Burney",
                "address": "833 58th Street",
                "email": "naghma_burney_11224@gmail.com"
            },
            {
                "id": "57647cd7db1a35731d92b36970d99121",
                "name": "Denise West",
                "address": "15 Wadsworth Ave.",
                "email": "denise_west_10021@gmail.com"
            },
            {
                "id": "ee042f8e7758b687e490ff13b7f167e7",
                "name": "Robert Vaccarino",
                "address": "201 East 69th St",
                "email": "robert_vaccarino_11355@gmail.com"
            },
            {
                "id": "7473cf054c186d186a7b6fdf1d5b14e1",
                "name": "Sara Buros",
                "address": "25-52 STEINWAY STREET",
                "email": "sara_buros_11691@gmail.com"
            },
            {
                "id": "227afcc57810de420301e8f4c050a20d",
                "name": "Elizabeth Lee-Rey",
                "address": "42-42 Golden Street, Suite L17",
                "email": "elizabeth_lee-rey_11355@gmail.com"
            },
            {
                "id": "4d3c513e881d0862b1ea181a3da88472",
                "name": "Drepaul Loris",
                "address": "114-06 Queens Blvd",
                "email": "drepaul_loris_11419@gmail.com"
            },
            {
                "id": "6125602b0b0ddd861f0725769efebb6a",
                "name": "Luisa Perez",
                "address": "87-81, 169th Street",
                "email": "luisa_perez_11372@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "9adb210f7500c113874b56b21129206f",
                "name": "Jonathan Mohrer",
                "address": "64-17 Broadway, Woodside, NY 11377",
                "email": "jonathan_mohrer_11366@gmail.com"
            },
            {
                "id": "dbdf88f5bc31fc3c365cb8c0e039b96b",
                "name": "RICHARD BELLI",
                "address": "911 Park Avenue",
                "email": "richard_belli_10044@gmail.com"
            },
            {
                "id": "79496dfdffa7036b0b4e8dd20c7036d0",
                "name": "Eliscer Guzman",
                "address": "501 Main Street",
                "email": "eliscer_guzman_10034@gmail.com"
            },
            {
                "id": "85ba03809a1e5e7b56852503e472f3c9",
                "name": "Haleh Milani",
                "address": "160 East 32nd St",
                "email": "haleh_milani_10010@gmail.com"
            },
            {
                "id": "6850117c76a2a722f79a16c127ac2591",
                "name": "Newsha Ghodsi",
                "address": "305 Seguine Ave Ste. 1",
                "email": "newsha_ghodsi_10305@gmail.com"
            },
            {
                "id": "962dd657f99ceb97f6c456334568b3c4",
                "name": "Salvatore Degliuomini",
                "address": "263, 7th Ave Suite 4D",
                "email": "salvatore_degliuomini_11203@gmail.com"
            },
            {
                "id": "462db7ef429d98776e2533de3e500452",
                "name": "Thomas Fuchs",
                "address": "9613 Flatlands Ave",
                "email": "thomas_fuchs_11220@gmail.com"
            },
            {
                "id": "c5b349f1ba01a3f4c4297ed13c0abbcb",
                "name": "Samuel Bekar",
                "address": "18-12 College Point Blvd",
                "email": "samuel_bekar_10021@gmail.com"
            },
            {
                "id": "ca09b05c75cf5b38a4357955410b285e",
                "name": "Ajith Karayil",
                "address": "231 SHERMAN AVENUE #1F",
                "email": "ajith_karayil_10013@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "92b8d203f4c073f5622303c570da29a6",
                "name": "Sidney Rosman",
                "address": "333 w. 51st street",
                "email": "sidney_rosman_10033@gmail.com"
            },
            {
                "id": "6fbf43bc5abe486b5d2c87d47e3220b6",
                "name": "Xianyang Yio",
                "address": "160 Parkside Ave, Suite 1D",
                "email": "xianyang_yio_11220@gmail.com"
            },
            {
                "id": "fe9e76556b5ec369add03a76677c5d2f",
                "name": "Laura Victor",
                "address": "70-17 37 Avenue",
                "email": "laura_victor_11372@gmail.com"
            },
            {
                "id": "48f4defbae708cf7b48fb071792a5f69",
                "name": "Hari Krishna Shukla",
                "address": "201 E. 65th ST",
                "email": "hari_krishna_shukla_10040@gmail.com"
            },
            {
                "id": "e93167ad3ad8745893dbd020057cd68b",
                "name": "Elliot Belenkov",
                "address": "730 58th Street, 1F",
                "email": "elliot_belenkov_11220@gmail.com"
            },
            {
                "id": "d5312a0f1fa02831c9180a5beddaac09",
                "name": "Patricia Pugni",
                "address": "314 W. 14th Street",
                "email": "patricia_pugni_10027@gmail.com"
            },
            {
                "id": "4ad98ac5fe3d6a8cb497d61717330303",
                "name": "Tien-Tsai Tsai",
                "address": "3134 E. Tremont Ave",
                "email": "tien-tsai_tsai_10461@gmail.com"
            },
            {
                "id": "0ff0353c7ac7b14e202067ac3227cc98",
                "name": "Li-Min Yang",
                "address": "1627 Broadway",
                "email": "li-min_yang_10032@gmail.com"
            },
            {
                "id": "df030a3d80e2e8b5ff8f510d3698e079",
                "name": "Lili Ren",
                "address": "303 9th Avenue, Room 140",
                "email": "lili_ren_10032@gmail.com"
            },
            {
                "id": "21ebc3f70f5ae593cb59f8dbf82da5a6",
                "name": "John F. Lazzara",
                "address": "13710 FRANKLIN AVE",
                "email": "john_f._lazzara_11692@gmail.com"
            },
            {
                "id": "0f058749d946f7993fbd11dc3a265a08",
                "name": "Ravindra Goyal",
                "address": "43-20A Roosevelt Avenue",
                "email": "ravindra_goyal_11355@gmail.com"
            },
            {
                "id": "8a7931006ff74cd677f747471a53dc0d",
                "name": "Archana Saxena",
                "address": "863 50th street suite M5",
                "email": "archana_saxena_11205@gmail.com"
            },
            {
                "id": "3a359d26f412ef933186725db53c538a",
                "name": "Eva Gomolinski",
                "address": "124 E 43rd St",
                "email": "eva_gomolinski_11213@gmail.com"
            },
            {
                "id": "4e75f3b3dc315fc6256d61fb90a74834",
                "name": "Rekha Mahale",
                "address": "231 South 3rd Street",
                "email": "rekha_mahale_11219@gmail.com"
            },
            {
                "id": "e34cdf1d0ff3a21733392dec97490ba6",
                "name": "Vijay Alla",
                "address": "1163 Manor Avenue",
                "email": "vijay_alla_10469@gmail.com"
            },
            {
                "id": "f1465a16333117459e48d8665e600586",
                "name": "Maria Del Carmen Hidalgo",
                "address": "616 West 184th Street",
                "email": "maria_del_carmen_hidalgo_10027@gmail.com"
            },
            {
                "id": "072df0f37b365f4c8326a2d086eae626",
                "name": "Editha Figurasin",
                "address": "42-07 30th Avenue",
                "email": "editha_figurasin_11422@gmail.com"
            },
            {
                "id": "b01cbef901535fbacb962a9053878838",
                "name": "G Sahni",
                "address": "445 Park Avenue",
                "email": "g_sahni_11211@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "332be2ea24d1c49b82d85a75d5a75ee1",
                "name": "Lance Rubel",
                "address": "86-04 117th. street",
                "email": "lance_rubel_11364@gmail.com"
            },
            {
                "id": "765554994fc1da6a8d56af3a9305f549",
                "name": "Charles Paolino",
                "address": "160 Bennett Avenue",
                "email": "charles_paolino_10032@gmail.com"
            },
            {
                "id": "a6ce8805a528c1bdee894c44d96b5898",
                "name": "Rick Chou",
                "address": "124 East 43rd Street",
                "email": "rick_chou_11204@gmail.com"
            },
            {
                "id": "927e18eb9fba5f976922fc7c946b30cf",
                "name": "Michael Lavianlivi",
                "address": "6506 Roosevelt Ave",
                "email": "michael_lavianlivi_11375@gmail.com"
            },
            {
                "id": "f4e9139aa124c549cd0f4cb052f1f592",
                "name": "Joseph Gelbfish",
                "address": "410 Lakeville Road, Suite 202",
                "email": "joseph_gelbfish_11377@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "17283a21fe4163a44ee0ce4d754112aa",
                "name": "Edison Ruiz",
                "address": "48 Market St., Suite B",
                "email": "edison_ruiz_10003@gmail.com"
            },
            {
                "id": "29bcfdf95d8591fbb68f81dd4490c16f",
                "name": "Michael Terrani",
                "address": "235-20 147th Avenue",
                "email": "michael_terrani_11372@gmail.com"
            },
            {
                "id": "ea40c83b4c6cb15a124e34fda3c31e2a",
                "name": "Jih- Ling Chiang",
                "address": "5 Avenue I",
                "email": "jih-_ling_chiang_11211@gmail.com"
            },
            {
                "id": "7acfffa1601209cf660bdf588b49cdbc",
                "name": "Olga Echeverria",
                "address": "29-22 30th Avenue",
                "email": "olga_echeverria_11368@gmail.com"
            },
            {
                "id": "eb5632e8cb041aca1a0a392141360b0f",
                "name": "Tuyen Trinh",
                "address": "1417 Wythe Place, 1st Floor",
                "email": "tuyen_trinh_10458@gmail.com"
            },
            {
                "id": "5c87a52ee1e3bbbad13c60c4bda5eccc",
                "name": "O Jean Pierre",
                "address": "416 37 St",
                "email": "o_jean_pierre_11219@gmail.com"
            },
            {
                "id": "cc794bd302a4173111e199c68a09259b",
                "name": "Elaine Brown",
                "address": "2202 Grand Concourse",
                "email": "elaine_brown_10463@gmail.com"
            },
            {
                "id": "0322b9ba352cc77ceea138a125d5feb6",
                "name": "Verlaine Brunot",
                "address": "410 Lakeville Road",
                "email": "verlaine_brunot_11373@gmail.com"
            },
            {
                "id": "9f71e1ffcf2b34f7e24084cedf1a3655",
                "name": "Ella-Jean Richards",
                "address": "117-06 225th Street 1st Floor",
                "email": "ella-jean_richards_11372@gmail.com"
            },
            {
                "id": "cec6627b4f81ddb7d7d4afc21ca40667",
                "name": "Feliks Tsatskin",
                "address": "112-03 Queens Blvd",
                "email": "feliks_tsatskin_11354@gmail.com"
            },
            {
                "id": "7c824457fed0e91bb8062c7b0c11acc8",
                "name": "Emilio Villegas",
                "address": "39-45 Queens Blvd",
                "email": "emilio_villegas_11103@gmail.com"
            },
            {
                "id": "423eaab423ea39dd50fd85733b2c8de5",
                "name": "Mohsani Hossain",
                "address": "87-46 168th Street",
                "email": "mohsani_hossain_11355@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "706209d68d6d58ee3a55df2eb4165e04",
                "name": "Nuzhat Syed",
                "address": "94-11 59th Avenue Suite A-10",
                "email": "nuzhat_syed_11374@gmail.com"
            },
            {
                "id": "515f183938d16c1ca3445c5b156858c2",
                "name": "Nancy L. Chiang",
                "address": "99 Moore Street, 1A",
                "email": "nancy_l._chiang_11220@gmail.com"
            },
            {
                "id": "8649bdc6733ad52ad6a3ebca89d5e5ed",
                "name": "Gillian Katz",
                "address": "1153 58th Street",
                "email": "gillian_katz_11211@gmail.com"
            },
            {
                "id": "65e8d8e6a30c3d1559aeb39d3fc522b3",
                "name": "Elizabeth Cruz",
                "address": "59-17 Junction Blvd",
                "email": "elizabeth_cruz_11379@gmail.com"
            },
            {
                "id": "f3ff3d40c7d3a1aa4aed4e313997bb90",
                "name": "Shen-Han Lin",
                "address": "370 9th Street",
                "email": "shen-han_lin_11237@gmail.com"
            },
            {
                "id": "9ca7245c1be162b6b9494d52c0320ca5",
                "name": "Wei Wang",
                "address": "856 Dekalb Avenue",
                "email": "wei_wang_11211@gmail.com"
            },
            {
                "id": "40a0a686f2e519cf7fdf4d8088895c91",
                "name": "Ala-May Lumibao",
                "address": "3010 Grand Concourse",
                "email": "ala-may_lumibao_10462@gmail.com"
            },
            {
                "id": "72485edf844e1cef7d73d5a68444280e",
                "name": "Afamefune Onejemie",
                "address": "100 Ross Street",
                "email": "afamefune_onejemie_11230@gmail.com"
            },
            {
                "id": "b7533e6e5a661a36746a1fc2dcbf151b",
                "name": "Tziporah Thall",
                "address": "1216 Beach Ave #1",
                "email": "tziporah_thall_10453@gmail.com"
            },
            {
                "id": "e29051bca55195fba94785c559e64147",
                "name": "Loris Omesh Drepaul",
                "address": "1718 Pitkin Avenue",
                "email": "loris_omesh_drepaul_11203@gmail.com"
            },
            {
                "id": "418055ba373284092a4ea9880415fffb",
                "name": "Dina Kornblau",
                "address": "136-20 38th Ave",
                "email": "dina_kornblau_11432@gmail.com"
            },
            {
                "id": "f57e022715ae4c8af0a4ae24fecda78e",
                "name": "Rita Ahuja",
                "address": "Doctors Office",
                "email": "rita_ahuja_10460@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "81a2ff1b8ebf3b5ebfe1cd5417bea762",
                "name": "Henry Ting",
                "address": "1911 Avenue L",
                "email": "henry_ting_11211@gmail.com"
            },
            {
                "id": "57a93e31dd54a5e6d75684c7aeac3ab1",
                "name": "Jose Mendez",
                "address": "234-32 Merrick Blvd.",
                "email": "jose_mendez_11435@gmail.com"
            },
            {
                "id": "4ef1023875226116234a3157aeff8b0b",
                "name": "Lauri Romanzi",
                "address": "4250 Broadway Suite 1C",
                "email": "lauri_romanzi_10032@gmail.com"
            },
            {
                "id": "01f8aaf364bd522cc2ba7385a3f35917",
                "name": "Carmen Runiga-Kartachou",
                "address": "-342 Beach 54th Street",
                "email": "carmen_runiga-kartachou_11377@gmail.com"
            },
            {
                "id": "3616064f9785294a3f47c3e847abff80",
                "name": "Charles Brum",
                "address": "141-49 70 Road",
                "email": "charles_brum_11385@gmail.com"
            },
            {
                "id": "8eeac2f7f8dac620db7eb617d1bd41e6",
                "name": "Syed Hassan",
                "address": "102-11 Roosevelt Avenue",
                "email": "syed_hassan_10011@gmail.com"
            },
            {
                "id": "330b6811b0e7920bcc38aadc51abb487",
                "name": "Angela Badiner",
                "address": "800 Grand Concouse Office #5",
                "email": "angela_badiner_10462@gmail.com"
            },
            {
                "id": "1488ec0a873b79585272c453e5eb9b24",
                "name": "ROBERT TAGLIA",
                "address": "210 East 86 Street",
                "email": "robert_taglia_10028@gmail.com"
            },
            {
                "id": "cab10874249838c5cc1301ff2e677f21",
                "name": "Belkis Colon",
                "address": "2270 University Avenue, Suite 1A",
                "email": "belkis_colon_10472@gmail.com"
            },
            {
                "id": "17ae2f5916911d1df0966834d97d7c07",
                "name": "Melaine McLean",
                "address": "106 Fort Washington Ave, Suite 1B",
                "email": "melaine_mclean_10017@gmail.com"
            },
            {
                "id": "1064255c384fdf36b8947f802c5c595e",
                "name": "Clotilde Pena",
                "address": "391 Eastern Parkway",
                "email": "clotilde_pena_11204@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "fe70f5d87f021e8f940214e7aece9487",
                "name": "Jack Bruder",
                "address": "110-16 Sutphin Ave",
                "email": "jack_bruder_11103@gmail.com"
            },
            {
                "id": "95cb3a67e9e68aa13e8884a9b5a7fcd9",
                "name": "Suzanne Flower",
                "address": "333 w. 51st street",
                "email": "suzanne_flower_10033@gmail.com"
            },
            {
                "id": "bf2932d252a388a551fb1f80ee4d8211",
                "name": "Rogelio Lucas",
                "address": "1262 Boston Road, suite 2",
                "email": "rogelio_lucas_10461@gmail.com"
            },
            {
                "id": "f7cf51b3fa6ea554185753186237baab",
                "name": "Charles Francis",
                "address": "2119 West 6th Street",
                "email": "charles_francis_11230@gmail.com"
            },
            {
                "id": "f67ac0d21bcc8da15bb0159c783a49f9",
                "name": "Masoud Moarefi",
                "address": "94-11 59th Avenue Suite A-10",
                "email": "masoud_moarefi_11374@gmail.com"
            },
            {
                "id": "8f72c92d6eaab57c8f5688f0ba781518",
                "name": "Edwin Quinones",
                "address": "104-14 113 ST",
                "email": "edwin_quinones_11420@gmail.com"
            },
            {
                "id": "4804342eff5a5858b4f227e319a45597",
                "name": "Rudabah Hasan",
                "address": "600 West 150th Street",
                "email": "rudabah_hasan_10030@gmail.com"
            }
        ]
    },
    "Manhattan": {
        "rheumatologist": [
            {
                "id": "30adb95891765b0b807c726b4e83bd4f",
                "name": "Marianne LaBarbera, MD",
                "address": "706 Banner Ave.",
                "email": "marianne_labarbera,_md_11220@gmail.com"
            },
            {
                "id": "ae3d68b9f7131ce085ab3388a289127c",
                "name": "Michele Reed",
                "address": "1262 Ocean Parkway",
                "email": "michele_reed_11209@gmail.com"
            },
            {
                "id": "bd955fee89486376ff9e9009ba47524b",
                "name": "Barbara Berger",
                "address": "911 Park Avenue",
                "email": "barbara_berger_10044@gmail.com"
            },
            {
                "id": "015a27184025afbe74ef414f3ac6c82f",
                "name": "Yuderqui Checo",
                "address": "128 Fort Washington Ave",
                "email": "yuderqui_checo_10031@gmail.com"
            },
            {
                "id": "95fbd63edf258608f1669ec0f1b7ef77",
                "name": "Jacqueline Dumornay",
                "address": "247 3rd Ave",
                "email": "jacqueline_dumornay_10128@gmail.com"
            },
            {
                "id": "33b960867c16962f28a89cee5780c90e",
                "name": "Lyudmila Sorkin",
                "address": "38-39 Bell Blvd #233",
                "email": "lyudmila_sorkin_11105@gmail.com"
            },
            {
                "id": "fed8f38fd50b2a18e330622d272a4f77",
                "name": "Stacy Kreiswirth",
                "address": "221 W. 138th St., Ground Flr, Medical Suite",
                "email": "stacy_kreiswirth_10013@gmail.com"
            },
            {
                "id": "4858b9d5aa45b94ed9845c248f154e76",
                "name": "Elliot Rayfield",
                "address": "13338 41st Rd # C03",
                "email": "elliot_rayfield_11355@gmail.com"
            },
            {
                "id": "600bea8bf8d866d8101977071804a65a",
                "name": "Liu Zhechun",
                "address": "90-45,Pitkin Ave",
                "email": "liu_zhechun_11372@gmail.com"
            },
            {
                "id": "57e4dd8cda6b80babec8989234e5b0da",
                "name": "Paul McClung",
                "address": "305 Seguine Ave Ste. 1",
                "email": "paul_mcclung_10305@gmail.com"
            },
            {
                "id": "634e047f14587ded9e374330847bc4ed",
                "name": "Manana Petrov",
                "address": "2248 Richmond Road",
                "email": "manana_petrov_10312@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "facdf58ee0e6356b36984b11fbdb9a60",
                "name": "Paul C. Gazzara",
                "address": "121 East 60th Street",
                "email": "paul_c._gazzara_10013@gmail.com"
            },
            {
                "id": "228f036133ab8c97c8cfa1ad93688f42",
                "name": "Jeffrey Belmon",
                "address": "9542 Roosevelt Avenue",
                "email": "jeffrey_belmon_11374@gmail.com"
            },
            {
                "id": "8dcc607a923f7f7ebec53636029c91c3",
                "name": "Mridula Dogra",
                "address": "585 Knickerbocker Avenue",
                "email": "mridula_dogra_11230@gmail.com"
            },
            {
                "id": "be0b5f675693360de817fa2f1086e5e7",
                "name": "Alberto Tan",
                "address": "117-06 225th Street 1st Floor",
                "email": "alberto_tan_11372@gmail.com"
            },
            {
                "id": "15130b50fbd34b00bac6b4a878b07e36",
                "name": "Anna Saporito",
                "address": "2 West 86th Street Suite 4",
                "email": "anna_saporito_10013@gmail.com"
            },
            {
                "id": "9182905e565d5253019dbd73dbe0d12e",
                "name": "H. Robert Bearnot",
                "address": "1624 University Avenue",
                "email": "h._robert_bearnot_10453@gmail.com"
            },
            {
                "id": "a38a7b0ae3db4a86f03a7951b250a9ae",
                "name": "Saimamba Veeramachaneni",
                "address": "131-24 Rockaway Blvd",
                "email": "saimamba_veeramachaneni_11373@gmail.com"
            },
            {
                "id": "c5669e3112456a50c971aff4ed179542",
                "name": "Mitchell Seidman",
                "address": "121-02 Hillside Avenue",
                "email": "mitchell_seidman_11203@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "92bbe102c2bc57212a79cde2604094ec",
                "name": "Keith Kouroupos",
                "address": "40-04 Bowne St",
                "email": "keith_kouroupos_11373@gmail.com"
            },
            {
                "id": "e50f4903fe6bc65c427d1f03c0504521",
                "name": "Sameet Palkhiwala",
                "address": "863 50th street suite M5",
                "email": "sameet_palkhiwala_11205@gmail.com"
            },
            {
                "id": "fe1f8c1fed48efd0ff493bb49682524b",
                "name": "Adil Farooki",
                "address": "18-12 College Point Blvd",
                "email": "adil_farooki_10021@gmail.com"
            },
            {
                "id": "de9771fdbbe847bc1fd5613025a92e2f",
                "name": "Franklyn Sencion",
                "address": "41 Mott Street, Chinatown",
                "email": "franklyn_sencion_10031@gmail.com"
            },
            {
                "id": "222022bc5f266e84e138f70e2a28cd28",
                "name": "Weiguo Lin",
                "address": "5721-A 5th Ave",
                "email": "weiguo_lin_11222@gmail.com"
            },
            {
                "id": "ce57056962bd82799cf6c317a87958e6",
                "name": "Chinta Chiu",
                "address": "353 Ft. Washington Ave. Ste 1F",
                "email": "chinta_chiu_10027@gmail.com"
            },
            {
                "id": "6485a8de39f02ae068b7ac5ea7cf719f",
                "name": "David Hosten",
                "address": "115 Central Park West",
                "email": "david_hosten_10011@gmail.com"
            },
            {
                "id": "1e958f4f310afec5ae384b9b62a8a423",
                "name": "Mohammed Yousufuddin",
                "address": "6933 169th street",
                "email": "mohammed_yousufuddin_11355@gmail.com"
            },
            {
                "id": "521e53451cf8eb913a5d230c6e267bd6",
                "name": "Stephan Simons",
                "address": "1455 East 24th Street",
                "email": "stephan_simons_11211@gmail.com"
            },
            {
                "id": "d37789c927fc4888dbe1c3e4ec30d833",
                "name": "Atkuri Subah",
                "address": "739 Knickerbocker Avenue",
                "email": "atkuri_subah_11203@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "02bd56a287b04975ad76e932a59465ee",
                "name": "Robert La Penna",
                "address": "416 37 St",
                "email": "robert_la_penna_11219@gmail.com"
            },
            {
                "id": "43cdc9f4ce905d9d86d0762c87e6b428",
                "name": "Yeahseon Bruinings",
                "address": "629 West 185th Street",
                "email": "yeahseon_bruinings_11372@gmail.com"
            },
            {
                "id": "b0c11c5e079bf3070766f2a125e7fabb",
                "name": "Carlos Melendez",
                "address": "234-32 Merrick Blvd.",
                "email": "carlos_melendez_11435@gmail.com"
            },
            {
                "id": "7efbec248f6c59ce99a8ef19b7d88dbe",
                "name": "Sameera Haroon",
                "address": "1250 Shakespeare Avenue",
                "email": "sameera_haroon_10457@gmail.com"
            },
            {
                "id": "fc726a3ca25c7c42cb8904a942c6a90e",
                "name": "Leonid Bukhman",
                "address": "707 West 171st Suite A",
                "email": "leonid_bukhman_10034@gmail.com"
            },
            {
                "id": "14423308e6f9ca69832e2a79861e2702",
                "name": "Matthew Martinez",
                "address": "753 Classon Avenue Suite LJ",
                "email": "matthew_martinez_11219@gmail.com"
            },
            {
                "id": "0e2286dff19d9a4ce10f1ce820318178",
                "name": "Ilan Semandov",
                "address": "86-04 117th. Street",
                "email": "ilan_semandov_11418@gmail.com"
            },
            {
                "id": "cd98684bb7da0fbc8cd45851e27c8e9b",
                "name": "Uzma Chatha",
                "address": "1627 Broadway",
                "email": "uzma_chatha_10032@gmail.com"
            },
            {
                "id": "5b5bab950a83f82acbab30a0d2e983ff",
                "name": "Khalid Chaughtai",
                "address": "410 Lakeville Road",
                "email": "khalid_chaughtai_11373@gmail.com"
            },
            {
                "id": "5a4d708a794f78ac07ac1509acf9da4f",
                "name": "Marina Oks",
                "address": "1446 Broadway Avenue",
                "email": "marina_oks_11238@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "1ea349922b77a39e14325a6d49b15e95",
                "name": "Bart Savino",
                "address": "131-24 Rockaway Blvd",
                "email": "bart_savino_11373@gmail.com"
            },
            {
                "id": "0868f600bc542e1f49c77a0836fbfcf5",
                "name": "Barnali Hasan",
                "address": "305 e 149th st",
                "email": "barnali_hasan_10472@gmail.com"
            },
            {
                "id": "cbb6b83bffce8ab77e23bbd132c38ba3",
                "name": "Afzal Hossain",
                "address": "400 Broadway, 4th Floor",
                "email": "afzal_hossain_10021@gmail.com"
            },
            {
                "id": "62cc539d9cd6219f2b8b58dd60019f4f",
                "name": "Magalie Alfred",
                "address": "444 Willis Avenue",
                "email": "magalie_alfred_10468@gmail.com"
            },
            {
                "id": "52d2088660a955d80069c76ea86082d4",
                "name": "Maria Del Carmen Hidalgo",
                "address": "354 Monroe Place",
                "email": "maria_del_carmen_hidalgo_11203@gmail.com"
            },
            {
                "id": "9d42e66e63af747090b7f49e533bf765",
                "name": "Tina Wong",
                "address": "64-15 Fresh Pond Rd",
                "email": "tina_wong_11418@gmail.com"
            },
            {
                "id": "ecdc550a2280a2ce548b443b1d137f7c",
                "name": "Jose Perez",
                "address": "58 E. 116th St",
                "email": "jose_perez_10028@gmail.com"
            },
            {
                "id": "6fb88829d5668c34769ead9d7b5e65a3",
                "name": "Gunjeet Sahni",
                "address": "8656 105th Street",
                "email": "gunjeet_sahni_11418@gmail.com"
            },
            {
                "id": "a0f44c1ecfac691a12d814c36762a4d8",
                "name": "Yelena Karasina",
                "address": "1211 White Plains Rd",
                "email": "yelena_karasina_10472@gmail.com"
            },
            {
                "id": "d803a44427a9c213491362da5d9d48d1",
                "name": "Prasanta Chandra",
                "address": "59-17 Junction Blvd",
                "email": "prasanta_chandra_11379@gmail.com"
            },
            {
                "id": "9236fc178954d62fbe1a9888cae1ef80",
                "name": "Ewa Gawlik",
                "address": "1715 University Blvd",
                "email": "ewa_gawlik_10458@gmail.com"
            },
            {
                "id": "3e2326ce7a089962c8dd327484a44200",
                "name": "Reynaldo Alonso",
                "address": "2503 Church Ave",
                "email": "reynaldo_alonso_11201@gmail.com"
            },
            {
                "id": "bc114536f0f95b789e04cb9af15f8e8b",
                "name": "Mehmet Cetin",
                "address": "75-06 ELIOT AVE",
                "email": "mehmet_cetin_11355@gmail.com"
            },
            {
                "id": "daea7076ba613680883fef232dbbf849",
                "name": "Manuel Mejia",
                "address": "4434 Amboy Road",
                "email": "manuel_mejia_11356@gmail.com"
            },
            {
                "id": "5976d396cedb18b7a308bda6c8e53ef4",
                "name": "Marcia Morgan",
                "address": "258 Henry Street",
                "email": "marcia_morgan_11230@gmail.com"
            },
            {
                "id": "86ef848cfa1e9645c5e8b8a2a6f5cbfe",
                "name": "Gloria Murray",
                "address": "123 Layfayette Street, 6th Floor",
                "email": "gloria_murray_10013@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "aa0948f9a2794ee50cf59d4f5f0e3cad",
                "name": "James Flesher",
                "address": "2015 Grand Concourse",
                "email": "james_flesher_10467@gmail.com"
            },
            {
                "id": "392a2f5031fa3b825c1f6eb569cd629d",
                "name": "Shaheen Ahmed",
                "address": "60 Plaza St E # E",
                "email": "shaheen_ahmed_11238@gmail.com"
            },
            {
                "id": "afb40e5f4259133ac53b3f42b348796e",
                "name": "Naginder Puri",
                "address": "2311 Adam Clayton Powell Jr.Boulevard",
                "email": "naginder_puri_10031@gmail.com"
            },
            {
                "id": "fc941c6696cecd07b663d5c49b5e2b06",
                "name": "Nicholas Cannone",
                "address": "18-12 College Point Blvd",
                "email": "nicholas_cannone_10021@gmail.com"
            },
            {
                "id": "4ff616da59c71838093b3c3bb6151e48",
                "name": "Abdul-Haki Issah",
                "address": "42-64 KISSENA BLVD",
                "email": "abdul-haki_issah_11373@gmail.com"
            },
            {
                "id": "dd45f828431588b821057fa6ab43b890",
                "name": "Elsa J. Reyes",
                "address": "4819 14th Avenue",
                "email": "elsa_j._reyes_11221@gmail.com"
            },
            {
                "id": "2326decc4525be110eac56f251bb4811",
                "name": "Mayra Mahadin",
                "address": "314 West 14th Street",
                "email": "mayra_mahadin_11355@gmail.com"
            },
            {
                "id": "b380fd0b4af86e8119ca10b527fcabbe",
                "name": "Jacob George",
                "address": "1627 Broadway",
                "email": "jacob_george_10032@gmail.com"
            },
            {
                "id": "98b1f8321121e5ce4c29624cbded610f",
                "name": "John C. Riggs",
                "address": "2119 West 6th Street",
                "email": "john_c._riggs_11230@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "d3939f3e82f4b6b0a1f0bff6c9069f11",
                "name": "Alfredo Maduro",
                "address": "113-11 Jamaica Ave,",
                "email": "alfredo_maduro_11354@gmail.com"
            },
            {
                "id": "c61b73360e84acbde1152c3752e18122",
                "name": "Rakesh Gupta",
                "address": "1153 58 Street",
                "email": "rakesh_gupta_11213@gmail.com"
            },
            {
                "id": "9a3b644bc2e56cac9d7693a7c69769c5",
                "name": "Intazam Khan",
                "address": "170 W.233rd Street",
                "email": "intazam_khan_10457@gmail.com"
            },
            {
                "id": "ffb36c51b48176eeb8b10cc09cb0fb3b",
                "name": "Olga Falkowski",
                "address": "158 East 84th St",
                "email": "olga_falkowski_10022@gmail.com"
            },
            {
                "id": "311d24b9801e990fb19920733b2c0b56",
                "name": "Victor Peralta",
                "address": "131-24 Rockaway Blvd",
                "email": "victor_peralta_11373@gmail.com"
            },
            {
                "id": "ec6ba1049feac35b5e1ca51bbd19f131",
                "name": "Selman Leticia Vargas",
                "address": "629 W 185th St, 2nd Floor",
                "email": "selman_leticia_vargas_10013@gmail.com"
            },
            {
                "id": "9e10cf6d84363e2bbd1452939420c023",
                "name": "Todd Cowdery",
                "address": "4039 Junction Blvd",
                "email": "todd_cowdery_11042@gmail.com"
            },
            {
                "id": "bca4da5f3332327d97e21b71211facc9",
                "name": "Larry Landphair",
                "address": "102-11 Roosevelt Avenue",
                "email": "larry_landphair_10011@gmail.com"
            },
            {
                "id": "e9e115b1f05c26895ee4fea0f5fc71fb",
                "name": "Eileen Chen",
                "address": "1624 University Avenue",
                "email": "eileen_chen_10453@gmail.com"
            },
            {
                "id": "9a0839d795bdd74622839c849222b8ee",
                "name": "Alicia Massop-Flowers",
                "address": "650 5th Avenue",
                "email": "alicia_massop-flowers_11204@gmail.com"
            },
            {
                "id": "13e11c7af83bd66f26241c485f1afa8a",
                "name": "Antoine Fernaine",
                "address": "217 Ovington Avenue",
                "email": "antoine_fernaine_11210@gmail.com"
            },
            {
                "id": "a562d94131918abfde99c4a05a5a1625",
                "name": "Yechiel Zagelbaum",
                "address": "125 East 86th Street",
                "email": "yechiel_zagelbaum_10031@gmail.com"
            },
            {
                "id": "b8bd95e2145d97c07865fe2323c25fc5",
                "name": "Vinod Bhagat",
                "address": "4250 Broadway Suite 1C",
                "email": "vinod_bhagat_10032@gmail.com"
            },
            {
                "id": "40ab5aa9e3255bc092c9e8c68544770b",
                "name": "Giancarlo Guido",
                "address": "114-06 Queens Blvd",
                "email": "giancarlo_guido_11419@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "c6b5b85b3c93ef0df163066d9e49d64e",
                "name": "Saulius Skeivys",
                "address": "170 W.233Rd Street",
                "email": "saulius_skeivys_10467@gmail.com"
            },
            {
                "id": "732998bb7abaf9e2a507fc8680f5a434",
                "name": "Robert Sarnataro",
                "address": "-",
                "email": "robert_sarnataro_11205@gmail.com"
            },
            {
                "id": "faff8c18ab1d9cc9688464543950ed1f",
                "name": "Elizabeth Avaricio",
                "address": "217 Ovington Avenue",
                "email": "elizabeth_avaricio_11210@gmail.com"
            },
            {
                "id": "7a6aee0204ca57f61000a4d1beaa14eb",
                "name": "Sandra Rosado",
                "address": "232 Sherman Ave. Suite #4",
                "email": "sandra_rosado_11230@gmail.com"
            },
            {
                "id": "c283168c11f5d7dca6e65278d279cc29",
                "name": "Austin Chen",
                "address": "25-52 STEINWAY STREET",
                "email": "austin_chen_11691@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "79e33fe45426c52f1d285652c2cc8b20",
                "name": "Pin Mei Yao",
                "address": "87-46 168th Street",
                "email": "pin_mei_yao_11355@gmail.com"
            },
            {
                "id": "546588fc5889793ce1b27e3c4b390afb",
                "name": "Paul Lombardi",
                "address": "1407 46th Street",
                "email": "paul_lombardi_11213@gmail.com"
            },
            {
                "id": "db7e0bb24652dbd921a3f2f1a155cf12",
                "name": "Zaw Oo",
                "address": "87-08 JUSTICE AVE SUITE CX",
                "email": "zaw_oo_11103@gmail.com"
            },
            {
                "id": "81c114f402fe9d4dcad1e16629524604",
                "name": "Israel Aviles",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "israel_aviles_10013@gmail.com"
            },
            {
                "id": "6620463311a1276960cfc65f674f12ca",
                "name": "Emilio Villegas",
                "address": "222 Hancock St",
                "email": "emilio_villegas_11221@gmail.com"
            },
            {
                "id": "b27704f60cda024f479f574b91be49cd",
                "name": "Emilio Villegas",
                "address": "13710 FRANKLIN AVE",
                "email": "emilio_villegas_11692@gmail.com"
            },
            {
                "id": "011bba05825284c8b0063aa195ad9a88",
                "name": "Arpana Modi",
                "address": "76-01 113 Street",
                "email": "arpana_modi_11372@gmail.com"
            },
            {
                "id": "380a47221c5c01f9b9765a6a57f41128",
                "name": "Aldo Torrente",
                "address": "30-96 51 st",
                "email": "aldo_torrente_11354@gmail.com"
            },
            {
                "id": "c739a284230e286e583f8aea4a1d01fc",
                "name": "Rosemary Jackson",
                "address": "629 W 185th St",
                "email": "rosemary_jackson_10016@gmail.com"
            },
            {
                "id": "3df7c82fd1dae4ed749df0cb75566dea",
                "name": "Rameen Hashemiyoon",
                "address": "1070 Southern Blvd",
                "email": "rameen_hashemiyoon_10458@gmail.com"
            },
            {
                "id": "8b94c5059edd213deaf8571b1ce6d210",
                "name": "Rajendra RAMPERSAUD",
                "address": "2426 Eastchester Road",
                "email": "rajendra_rampersaud_10458@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "231146b440a549d50e9904ba2468e9e9",
                "name": "Khaleeq Arshed",
                "address": "258 Henry Street",
                "email": "khaleeq_arshed_11230@gmail.com"
            },
            {
                "id": "7fb7c24531756dc1f2ae286ad36ef6fd",
                "name": "Chaudhary Ghumman",
                "address": "470 Lenox Avenue Suite 1p",
                "email": "chaudhary_ghumman_10031@gmail.com"
            },
            {
                "id": "3b606ee128384ac2a7265de25643c8f8",
                "name": "Afroz Pervin",
                "address": "178 EAST 85TH STREET 4TH FLOOR",
                "email": "afroz_pervin_11230@gmail.com"
            },
            {
                "id": "9dbfbf5da74d1f336dbdcf32e2438972",
                "name": "Nicasio Arana",
                "address": "58 E. 116th St",
                "email": "nicasio_arana_10028@gmail.com"
            },
            {
                "id": "45476c94aceb9fb8666570535264e796",
                "name": "Maksudul Chowdhury",
                "address": "18 Eastwood Blvd",
                "email": "maksudul_chowdhury_11355@gmail.com"
            },
            {
                "id": "247ea014a34e98a8ad82ea34019f1da7",
                "name": "Federico Pichardo",
                "address": "2248 Richmond Road",
                "email": "federico_pichardo_10312@gmail.com"
            },
            {
                "id": "76ef01d1339b6fd2b1aa7f06e01ea83f",
                "name": "Andrew Tzellas",
                "address": "1204 Beach 9 St",
                "email": "andrew_tzellas_11103@gmail.com"
            },
            {
                "id": "55bcb214b210c0bebe6fd8c1ed1ead87",
                "name": "Richard Chan",
                "address": "83-45 Dongan Ave",
                "email": "richard_chan_11418@gmail.com"
            },
            {
                "id": "6dbb4c882fdb0100703a0c2e23071a96",
                "name": "Caroline Coccado",
                "address": "247 Grand St",
                "email": "caroline_coccado_11220@gmail.com"
            },
            {
                "id": "685106ff5ec97973e8922261c43f45b2",
                "name": "Lidia Garcia",
                "address": "18 E Broadway",
                "email": "lidia_garcia_10013@gmail.com"
            },
            {
                "id": "549f63235bccc2b6f7c50749c3cc12ae",
                "name": "Roger Chung",
                "address": "8306 13th Avenue",
                "email": "roger_chung_11204@gmail.com"
            },
            {
                "id": "cabe3632f652494eefb1a78486e337ec",
                "name": "Allan Santiago",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "allan_santiago_10462@gmail.com"
            },
            {
                "id": "1e333c17b23b68a7f7c20a69a0afd0fe",
                "name": "Margaret Clarke-Golden",
                "address": "33 W. 125th St",
                "email": "margaret_clarke-golden_10022@gmail.com"
            },
            {
                "id": "ba877e15f1abd96f36847becd8e02f16",
                "name": "Oded Preis",
                "address": "43-48 Colden St.",
                "email": "oded_preis_11103@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "9b3244d79d7fe9cffffc6c32b083b25a",
                "name": "Daysi Baez",
                "address": "87 08 Justice Avenue",
                "email": "daysi_baez_11435@gmail.com"
            },
            {
                "id": "29e874ffb8303e8ad665867aa31f75f5",
                "name": "Kee Shum",
                "address": "63 Catherine St.",
                "email": "kee_shum_10032@gmail.com"
            },
            {
                "id": "073c4d35c18dadc1773e8f935fd0cc24",
                "name": "Steven Straus",
                "address": "19 Hamilton Place",
                "email": "steven_straus_10013@gmail.com"
            },
            {
                "id": "5fb4f636fed62e8b6041f0fcf2226a39",
                "name": "Kevin Myers",
                "address": "2960 Grand Concourse L1",
                "email": "kevin_myers_10451@gmail.com"
            },
            {
                "id": "b28273c3ff271f76c6888f26e0098603",
                "name": "Lucy Sourial",
                "address": "1125 FULTON STREET 3RD FLOOR",
                "email": "lucy_sourial_11219@gmail.com"
            },
            {
                "id": "09952d641a98ad59ff56e9218929f198",
                "name": "Syed Z. Hussaini",
                "address": "741 New Lots Avenue",
                "email": "syed_z._hussaini_11206@gmail.com"
            },
            {
                "id": "1e9d236472b7cfa9f8e78be7f78705db",
                "name": "Hari Polavarapu",
                "address": "364 Junius Street",
                "email": "hari_polavarapu_11205@gmail.com"
            },
            {
                "id": "7ca4d58d1c6873ec7711a26ea7b00709",
                "name": "Hui Chih Yang",
                "address": "445 Park Avenue",
                "email": "hui_chih_yang_11211@gmail.com"
            },
            {
                "id": "dd0dca11c61fe5c793eecdd4590b85c9",
                "name": "CHAULA PATEL",
                "address": "18-12 College Point Blvd",
                "email": "chaula_patel_10021@gmail.com"
            },
            {
                "id": "3154da3d0650d02cab9d2a462fddd603",
                "name": "Julie Hurtado",
                "address": "3904 16th Avenue",
                "email": "julie_hurtado_11211@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "cb8d752e57e1d1bb32f9bc008da8a206",
                "name": "Kent B. Cao",
                "address": "3031 Bedford Avenue",
                "email": "kent_b._cao_11211@gmail.com"
            },
            {
                "id": "c0f25d338be1b862bdb14f250bda4ed7",
                "name": "Carl Guillaume",
                "address": "99 moore st suite A",
                "email": "carl_guillaume_11209@gmail.com"
            },
            {
                "id": "4ac066862d0a71880f82538e17a61ea7",
                "name": "Salvador Perez",
                "address": "115 Central Park West",
                "email": "salvador_perez_10011@gmail.com"
            },
            {
                "id": "3f2b9f4ab957641e9224facd33a6d020",
                "name": "Kendy Verpile",
                "address": "1627 Broadway",
                "email": "kendy_verpile_10032@gmail.com"
            },
            {
                "id": "490641f302fb860f26ae4233128145b6",
                "name": "Edwin Chan",
                "address": "730 58th Street, 1F",
                "email": "edwin_chan_11220@gmail.com"
            },
            {
                "id": "465af42ea0a27a3c3bef907cc9b05aa1",
                "name": "Keyan Ma",
                "address": "14 East 4th Street",
                "email": "keyan_ma_10033@gmail.com"
            },
            {
                "id": "9ee386abd3386d237501fb9008779b65",
                "name": "Raisa Slootsky",
                "address": "160 East 32nd Street #102",
                "email": "raisa_slootsky_10028@gmail.com"
            },
            {
                "id": "2706813352a2e86bdee3f87a33fbf695",
                "name": "Xin Pang",
                "address": "37-35 72nd Street",
                "email": "xin_pang_10031@gmail.com"
            },
            {
                "id": "1edb6621e27ba8714a7f4c1654e1076d",
                "name": "Anna Suponya",
                "address": "8008 Third Avenue",
                "email": "anna_suponya_11236@gmail.com"
            },
            {
                "id": "0d5cfd43797949fbcc03a253d3afc894",
                "name": "Dana DeVito",
                "address": "2379 65th Street",
                "email": "dana_devito_11203@gmail.com"
            },
            {
                "id": "0b145fbc306e72d2fc9d80d3c196b71e",
                "name": "David Weiss",
                "address": "629 West 185th Street",
                "email": "david_weiss_11372@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "2e40552f62c332a1ab30ac5d7628a4ab",
                "name": "Perry Frankel",
                "address": "136-31 41st Avenue Suite 30",
                "email": "perry_frankel_11432@gmail.com"
            },
            {
                "id": "ead07714b3f6b0dab4336fb26b90136d",
                "name": "Nazmul Hossain Khan",
                "address": "1545 Atlantic Avenue #108",
                "email": "nazmul_hossain_khan_11228@gmail.com"
            },
            {
                "id": "82176523c2cd74ed0f322ac2b9168fdb",
                "name": "Wendy Ramirez",
                "address": "2099 Forest Ave",
                "email": "wendy_ramirez_11040@gmail.com"
            },
            {
                "id": "000206f588aafa34a43fdf85b70b8c16",
                "name": "Shu Yain Chin",
                "address": "75-17 41ST AVE",
                "email": "shu_yain_chin_11432@gmail.com"
            },
            {
                "id": "27941c1cf47c4418a618fc8bb139a54a",
                "name": "Alexander Krishtul",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "alexander_krishtul_10013@gmail.com"
            },
            {
                "id": "016de26931f56d3ec8d4e875e12772b7",
                "name": "Doug Bailyn",
                "address": "900 WEST END AVE",
                "email": "doug_bailyn_10032@gmail.com"
            },
            {
                "id": "46689716f655bf643df1f0c7d30f522c",
                "name": "Dean Fong",
                "address": "629 W 185th St",
                "email": "dean_fong_10016@gmail.com"
            },
            {
                "id": "ad17cfd091fa9d13cb1c7f8e6616ec5a",
                "name": "Zil Goldstein",
                "address": "370 9th Street",
                "email": "zil_goldstein_11237@gmail.com"
            },
            {
                "id": "a5c79098f11b4979201e2d0a6e00a3d9",
                "name": "Henghe Tien",
                "address": "100 Ross Street",
                "email": "henghe_tien_11230@gmail.com"
            },
            {
                "id": "0e8ce3d0ebb79f535a8e9fff77df7abe",
                "name": "Yelena Havryliuk",
                "address": "360 1st Avenue Apartment MG",
                "email": "yelena_havryliuk_10018@gmail.com"
            },
            {
                "id": "baffb2776cf21e2abbebd57333318852",
                "name": "Shazah Khawaja",
                "address": "620 columbus ave",
                "email": "shazah_khawaja_10011@gmail.com"
            },
            {
                "id": "ce96ab82eb4a11c78eae74ef05213174",
                "name": "edward Mok",
                "address": "136-21 Roosevelt Ave, Suite #205",
                "email": "edward_mok_11373@gmail.com"
            },
            {
                "id": "8d6ba12b407c0aab996257edd07201a1",
                "name": "Susan Dunn",
                "address": "295 Ralph Avenue",
                "email": "susan_dunn_11233@gmail.com"
            },
            {
                "id": "3fa8fe0f3d13bce99a36daff18495087",
                "name": "Ka Li",
                "address": "83-10 Queens Blvd",
                "email": "ka_li_11372@gmail.com"
            },
            {
                "id": "6b71c3da35bf14ccc717ca48067b4ef5",
                "name": "Inna Gelfand",
                "address": "1204 Beach 9 St",
                "email": "inna_gelfand_11103@gmail.com"
            },
            {
                "id": "5361cb8b82561d01ee24770c7c51ed48",
                "name": "Daniel Zakhary",
                "address": "9851 QUEENS BLVD",
                "email": "daniel_zakhary_11374@gmail.com"
            },
            {
                "id": "98ce56be8c2ac7a19edbc2f8883597e2",
                "name": "Taiye Apoeso",
                "address": "2960 Grand Concourse L1",
                "email": "taiye_apoeso_10451@gmail.com"
            },
            {
                "id": "b7b28913ab4f789b865e4e94514c909b",
                "name": "Thapvongse Chin",
                "address": "3071 Perry Avenue",
                "email": "thapvongse_chin_10453@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "4d93648924ee61ff48c9c0d10f7d36c5",
                "name": "Ellimottil Kuriakose",
                "address": "250 W 57th Street Ste 1430",
                "email": "ellimottil_kuriakose_10040@gmail.com"
            },
            {
                "id": "ea84713a0de3d02a69b659be6f84bf77",
                "name": "Ginny Leva",
                "address": "464 West 145th Street",
                "email": "ginny_leva_10010@gmail.com"
            },
            {
                "id": "a5019f717f57c6a5a7100fa3d171ec19",
                "name": "Lorraine Williams",
                "address": "234-32 Merrick Blvd.",
                "email": "lorraine_williams_11435@gmail.com"
            },
            {
                "id": "222ab6089e683c795f1575f05f50fceb",
                "name": "Andrew Bohmart",
                "address": "501 Main Street",
                "email": "andrew_bohmart_10034@gmail.com"
            },
            {
                "id": "acccc898c487265d3d66bcd4bb23f60b",
                "name": "Luis E. Moquete",
                "address": "529 NOSTRAND AVE",
                "email": "luis_e._moquete_11235@gmail.com"
            },
            {
                "id": "8db1534d3ac0d07daff5fac7e9f40b5b",
                "name": "Harvey Benovitz",
                "address": "59-17 Junction Blvd",
                "email": "harvey_benovitz_11379@gmail.com"
            },
            {
                "id": "e05983c5ea031168f7f0ce7ac97fd061",
                "name": "Muhammad K Qadri",
                "address": "247 3rd Ave",
                "email": "muhammad_k_qadri_10128@gmail.com"
            },
            {
                "id": "a111b91f150af3fc998ef643815b9987",
                "name": "Jilan Shah",
                "address": "121A West 20th Street",
                "email": "jilan_shah_10021@gmail.com"
            },
            {
                "id": "25abe9a14f705b280588fa06f03ead02",
                "name": "Mindy Galagher",
                "address": "1153 58 Street",
                "email": "mindy_galagher_11213@gmail.com"
            },
            {
                "id": "220b6505f5873cf0a81a088b0c5cce07",
                "name": "Zahava Miller",
                "address": "620 columbus ave",
                "email": "zahava_miller_10011@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "c2f16a4f561c294f6fa4a086a6eb1795",
                "name": "Bella Sandler",
                "address": "139 Centre Suite, Suite 506",
                "email": "bella_sandler_11373@gmail.com"
            },
            {
                "id": "70aaf82ecc4b0b134dfe554da0012aa9",
                "name": "Rabeena Fazal",
                "address": "41-61 Kissena Boulevard, Suite 20",
                "email": "rabeena_fazal_11101@gmail.com"
            },
            {
                "id": "ca3fb6eec9b8ad8302700ec42cee9f56",
                "name": "Collier Chan",
                "address": "3071 Perry Avenue",
                "email": "collier_chan_10453@gmail.com"
            },
            {
                "id": "04f44d3bc1bafe56e14c4a9738a2ac07",
                "name": "Richard Neufeld",
                "address": "739 Knickerbocker Avenue",
                "email": "richard_neufeld_11203@gmail.com"
            },
            {
                "id": "ea952856befe0623e5296a381af43271",
                "name": "Gino Zunino",
                "address": "30-55 21st Street",
                "email": "gino_zunino_11103@gmail.com"
            },
            {
                "id": "81866276d9215ec9c2ad2e5dafaee751",
                "name": "Zuheir Said",
                "address": "76-01 113 Street",
                "email": "zuheir_said_11372@gmail.com"
            },
            {
                "id": "6f20e408fc1b6fbeff7139f060d07e27",
                "name": "Alyssa Siegel",
                "address": "432 Bedford Avenue",
                "email": "alyssa_siegel_11208@gmail.com"
            },
            {
                "id": "dda003318bfd37928d85de695b9b921e",
                "name": "Peter Lo",
                "address": "435 Fort Washington Avenue Suite 1C",
                "email": "peter_lo_10013@gmail.com"
            },
            {
                "id": "502e73496f5198e472597e8c049eda67",
                "name": "Francois G. Tellus",
                "address": "104-17 LEFFERTS BLVD",
                "email": "francois_g._tellus_11361@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "8b0d7c11a99c0aff487e63cdfcc6cfda",
                "name": "Gary Guarnaccia, MD",
                "address": "25-92 steinway street",
                "email": "gary_guarnaccia,_md_11374@gmail.com"
            },
            {
                "id": "486b11f435ded8f1219710d5189ddaa6",
                "name": "Godwin Onyeike",
                "address": "43-20A Roosevelt Avenue",
                "email": "godwin_onyeike_11355@gmail.com"
            },
            {
                "id": "dd88e64078562e212d960bdc435b4206",
                "name": "Patricia Herko",
                "address": "1627 Broadway",
                "email": "patricia_herko_10032@gmail.com"
            },
            {
                "id": "9934f532612cffa0432a3e2046485951",
                "name": "Harry Gruenspan",
                "address": "1236 Fulton Street",
                "email": "harry_gruenspan_11203@gmail.com"
            },
            {
                "id": "5fe706847f2800b5cac0f11551b49c57",
                "name": "Kuo Nan-Hsien",
                "address": "83-10 Queens Blvd",
                "email": "kuo_nan-hsien_11372@gmail.com"
            },
            {
                "id": "a378642bc53383da620e0905aa56579e",
                "name": "Lamont Freeman",
                "address": "375 East Fordham Road",
                "email": "lamont_freeman_10453@gmail.com"
            }
        ],
        "urologist": [
            {
                "id": "dbf1450254f091ce721fdf04f267b304",
                "name": "Daniela Atanassova-Lineva",
                "address": "2847 Webster Avenue",
                "email": "daniela_atanassova-lineva_10467@gmail.com"
            },
            {
                "id": "bf1b29212fc54bb4dc2c25ac8a8fded5",
                "name": "Manuel R. Esteban-Galindo",
                "address": "37-47 77 Street",
                "email": "manuel_r._esteban-galindo_11692@gmail.com"
            },
            {
                "id": "eca81862e849b4243061de3f95d878f9",
                "name": "Judy Marren",
                "address": "136-21 Roosevelt Ave, Suite #205",
                "email": "judy_marren_11373@gmail.com"
            },
            {
                "id": "5d04656dfc9793f86cdd64f9f0f22787",
                "name": "Tak Yein Lim",
                "address": "711 Cedar Lawn",
                "email": "tak_yein_lim_11418@gmail.com"
            },
            {
                "id": "674adc52cf39a1079cdcc2577a174dcd",
                "name": "Bhavana Japi",
                "address": "4260 Broadway",
                "email": "bhavana_japi_10027@gmail.com"
            },
            {
                "id": "27503ddfb9a8eafcb58cd006f0f658de",
                "name": "Meir Kessler",
                "address": "112-03 Queens Blvd.",
                "email": "meir_kessler_11373@gmail.com"
            },
            {
                "id": "969b9cc7bdb86244b4cbad90134c3a18",
                "name": "Angelo D. Michilli",
                "address": "445 Park Avenue",
                "email": "angelo_d._michilli_11211@gmail.com"
            },
            {
                "id": "f0d4cfb1e480005f5ca16cafc1f1c3e8",
                "name": "Nina Chao",
                "address": "8000 4th avenue",
                "email": "nina_chao_11219@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "d7314471a61c014bc29aa223ec8955e7",
                "name": "Man Yee Tong",
                "address": "1070 Southern Blvd",
                "email": "man_yee_tong_10458@gmail.com"
            },
            {
                "id": "d614c00b94ce7b6704c0a8fefa912095",
                "name": "Rita P. Verna",
                "address": "246-03 81st Ave.",
                "email": "rita_p._verna_11375@gmail.com"
            },
            {
                "id": "38be23faa9be447d5f4eade98c1394ca",
                "name": "Aylin Kiyici",
                "address": "2378 Ralph Ave",
                "email": "aylin_kiyici_11203@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "fea4b842cf12960567a0e13a44c90027",
                "name": "Mark Horowitz",
                "address": "464 West 145th Street",
                "email": "mark_horowitz_10010@gmail.com"
            },
            {
                "id": "fc22eb70930641a45a8ede1c80a1cdaa",
                "name": "Lucien Mocombe",
                "address": "202 Foster Ave. Suite C",
                "email": "lucien_mocombe_11209@gmail.com"
            },
            {
                "id": "0d30dc31e77a8e78ec580082b8edbc29",
                "name": "Keisha Sinha",
                "address": "420 Lyndale Avenue",
                "email": "keisha_sinha_10303@gmail.com"
            },
            {
                "id": "666ff8d1a58846af0943df82f00bf9dc",
                "name": "Linli Yan-Rosenberg",
                "address": "38-34 Parsons blvd #1A",
                "email": "linli_yan-rosenberg_11385@gmail.com"
            },
            {
                "id": "64bb3580061eb754d93a138db0f19aff",
                "name": "Jack Levine",
                "address": "40 West 135th Street",
                "email": "jack_levine_10128@gmail.com"
            },
            {
                "id": "420eb4942392ec75937e3c431f0b63e0",
                "name": "Fe T. Reyes-Arcangel",
                "address": "3016 Glenwood Rd",
                "email": "fe_t._reyes-arcangel_11212@gmail.com"
            },
            {
                "id": "f84b051522103c5f196520f134a78399",
                "name": "Arnold Wilson",
                "address": "118 Baxter Street",
                "email": "arnold_wilson_10034@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "d065f28f9a77394948690e6fa5da7b4f",
                "name": "Yolanda Tun-Chiong",
                "address": "420 Lyndale Avenue,",
                "email": "yolanda_tun-chiong_10309@gmail.com"
            },
            {
                "id": "38c08b641f9cc742822adddcfc42f737",
                "name": "Michael Frank",
                "address": "834 Coney Island Avenue",
                "email": "michael_frank_11243@gmail.com"
            },
            {
                "id": "3dfbc498acb27e23f8ac5fa2e5869d85",
                "name": "Elizabeth Woodford",
                "address": "464 West 145th Street",
                "email": "elizabeth_woodford_10010@gmail.com"
            },
            {
                "id": "83472b3c4de4baa0eb4a65c49bdbabe0",
                "name": "Fievre Garnes Marie",
                "address": "4626 White Plains Rd",
                "email": "fievre_garnes_marie_10463@gmail.com"
            },
            {
                "id": "fb0e7c0834c6622f4ff45b09ef738c9f",
                "name": "Sylvia Cotto",
                "address": "253-02 147th Ave",
                "email": "sylvia_cotto_11419@gmail.com"
            },
            {
                "id": "80b75b08deb68f70750a34bf08b36cdd",
                "name": "George Klein",
                "address": "3071 Perry Avenue",
                "email": "george_klein_10453@gmail.com"
            },
            {
                "id": "51092a9413aea13f0c756766118e1a6d",
                "name": "Hui Er Teng",
                "address": "104-14 113 ST",
                "email": "hui_er_teng_11420@gmail.com"
            },
            {
                "id": "49823a532757d5da167ab7d49e216d20",
                "name": "Emil Baccash",
                "address": "36-09 Main Street, Suite 8C",
                "email": "emil_baccash_11423@gmail.com"
            },
            {
                "id": "805f166c23f5f5f40b5a2b78c2c7a8c7",
                "name": "Vincent Dowling",
                "address": "911 Park Avenue",
                "email": "vincent_dowling_10044@gmail.com"
            },
            {
                "id": "4fb3de3b73f04871ee3f1937c1a1f35d",
                "name": "Seth Kurtz",
                "address": "209 Beach 125st",
                "email": "seth_kurtz_11354@gmail.com"
            }
        ]
    },
    "New York": {
        "nephrologist": [
            {
                "id": "d39e5bdc759350eab00372b945198611",
                "name": "Yeoman Chan",
                "address": "1718 Pitkin Avenue",
                "email": "yeoman_chan_11203@gmail.com"
            },
            {
                "id": "9b62aefa0bc9d893662ab71fdf72736b",
                "name": "Zia Ahmed",
                "address": "443 Linden Blvd",
                "email": "zia_ahmed_11210@gmail.com"
            },
            {
                "id": "48af9a8d8f82989150731af46e5f784a",
                "name": "Jean-Robert Boursiquot",
                "address": "98-11 Queens Blvd, # 1E",
                "email": "jean-robert_boursiquot_11357@gmail.com"
            },
            {
                "id": "683a456d99ed36e7c71362d054e9fdf4",
                "name": "Franklyn Sencion",
                "address": "1560 GRAND CONCOURSE",
                "email": "franklyn_sencion_10452@gmail.com"
            },
            {
                "id": "ff6f151bbece0177df39d288c8606e67",
                "name": "Ramon Ferrand",
                "address": "41-60 Main St. #205B",
                "email": "ramon_ferrand_11354@gmail.com"
            },
            {
                "id": "666b5b6afb6fbed4b9bed422c38cb9cd",
                "name": "Dov Landa",
                "address": "1627 Broadway",
                "email": "dov_landa_10032@gmail.com"
            },
            {
                "id": "58b47daf52172e7c1e5fef696ba404ca",
                "name": "Ijaz Ahmad",
                "address": "1262 Boston Road Suite 1",
                "email": "ijaz_ahmad_10458@gmail.com"
            },
            {
                "id": "54381a3176e0500497f77445492483a6",
                "name": "Carol De Costa",
                "address": "2760 Amboy Road",
                "email": "carol_de_costa_11418@gmail.com"
            },
            {
                "id": "8d6cd5999608f2dd080c59b3e8fd0244",
                "name": "Ramon Tallaj",
                "address": "45 EAST 85 STREET",
                "email": "ramon_tallaj_10033@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "faed9fe8a576cf90a77a6e9e2e8fdda1",
                "name": "Cherry Mar-Chan",
                "address": "1150 Park Avenue",
                "email": "cherry_mar-chan_10031@gmail.com"
            },
            {
                "id": "5620cc67dfd13f056b831ebe559d0630",
                "name": "Alma Mesquita",
                "address": "8008 Third Avenue",
                "email": "alma_mesquita_11236@gmail.com"
            },
            {
                "id": "4bce74b026fdf484da1eb7759b0232a8",
                "name": "Song Ja Choi",
                "address": "110-45 Queens Boulevard Suite A",
                "email": "song_ja_choi_11516@gmail.com"
            },
            {
                "id": "047f8e63cf34ccb25a69c015456a671d",
                "name": "Daniel Reinharth",
                "address": "70-17 37 Avenue",
                "email": "daniel_reinharth_11372@gmail.com"
            },
            {
                "id": "f67bb6b9af05c0c9819ef37ca7399411",
                "name": "WON SOHN",
                "address": "629 W 185th St, 2nd Floor",
                "email": "won_sohn_10013@gmail.com"
            },
            {
                "id": "d5c46abdbe5631fa037bfc7cd836039a",
                "name": "James Lax",
                "address": "1718 Pitkin Avenue",
                "email": "james_lax_11203@gmail.com"
            },
            {
                "id": "7a24eb22afb0f866b843348b463d5434",
                "name": "Martha Valdivia",
                "address": "10 W 86 St, Apt. 1A",
                "email": "martha_valdivia_10031@gmail.com"
            },
            {
                "id": "5e9222c87190946bf0e2a77e5e0f2101",
                "name": "Margaret Cheung",
                "address": "2379 65th Street",
                "email": "margaret_cheung_11203@gmail.com"
            },
            {
                "id": "c8ebcdfb047e95ec6aa296b899680641",
                "name": "Marino Torres",
                "address": "242 DeKalb Ave",
                "email": "marino_torres_11228@gmail.com"
            },
            {
                "id": "8242a85ea2d34b76993a3667afbf8d0c",
                "name": "Rummana Rahman",
                "address": "211-16 Union Turnpike",
                "email": "rummana_rahman_11372@gmail.com"
            },
            {
                "id": "89e6de8788e40aa28aeac59cfef2b20d",
                "name": "Prudence Osei-Tutu",
                "address": "3134 E. Tremont Ave",
                "email": "prudence_osei-tutu_10461@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "a7bab75cee9b8c898482aace03525ba3",
                "name": "Vincent Calamia",
                "address": "35 East 35th Street",
                "email": "vincent_calamia_10033@gmail.com"
            },
            {
                "id": "d4add71b392e7dbe98364b860649e5c3",
                "name": "Mamoun Alhajjouman",
                "address": "730 58th Street, 1F",
                "email": "mamoun_alhajjouman_11220@gmail.com"
            },
            {
                "id": "6f41a8c6c82f35c8f7142e1831cf9e65",
                "name": "Michael Landor",
                "address": "97-03 Springfield Blvd",
                "email": "michael_landor_11377@gmail.com"
            },
            {
                "id": "f530f51e2017dd7204fb0cfb93e0d44f",
                "name": "Vishwanath Puttaswamy Gowda",
                "address": "225 east 149th street",
                "email": "vishwanath_puttaswamy_gowda_10453@gmail.com"
            },
            {
                "id": "9cf5807f082669f5d15afc787dc9662f",
                "name": "Chhaya Chakrabarti",
                "address": "209-22 Hillside Avenue",
                "email": "chhaya_chakrabarti_11356@gmail.com"
            },
            {
                "id": "fbfb78149a92aeeba3899aeec59a171b",
                "name": "Gonzalo Sabogal",
                "address": "360 1st Avenue Apartment MG",
                "email": "gonzalo_sabogal_10018@gmail.com"
            },
            {
                "id": "e4838cf7f4e5f2da47da63ca0bbcf6df",
                "name": "Wenjing Zhou",
                "address": "600 West 150th Street",
                "email": "wenjing_zhou_10030@gmail.com"
            },
            {
                "id": "09db7f679ef3785fd75a4d4639e989c9",
                "name": "Robin Campos",
                "address": "234-32 Merrick Blvd.",
                "email": "robin_campos_11435@gmail.com"
            },
            {
                "id": "71cdbad0ddce3993c6cc88396e94e5f7",
                "name": "Chun Kit Chan",
                "address": "231 SOUTH 3RD STREET",
                "email": "chun_kit_chan_11221@gmail.com"
            },
            {
                "id": "e8cd4d442e47e3954922215a065c4505",
                "name": "Kazuko Ko",
                "address": "739 Knickerbocker Avenue",
                "email": "kazuko_ko_11203@gmail.com"
            },
            {
                "id": "6cd882e0aaa4667f9bd8cdeb950e0d6a",
                "name": "Shirley Li",
                "address": "400 Broadway, 4th Floor",
                "email": "shirley_li_10021@gmail.com"
            },
            {
                "id": "f760e7d09f518b186f52cc9bf83153dd",
                "name": "Benjamin Wu",
                "address": "121-02 Hillside Avenue",
                "email": "benjamin_wu_11203@gmail.com"
            },
            {
                "id": "fa9188eb893bb0eb5a68e482d5077dbb",
                "name": "Tajammal Gilani",
                "address": "1125 Fulton Street",
                "email": "tajammal_gilani_11233@gmail.com"
            },
            {
                "id": "6b7046797c9ff9a52270a2224afdb95b",
                "name": "Arpita Datta",
                "address": "730 58th Street, 1F",
                "email": "arpita_datta_11220@gmail.com"
            }
        ],
        "urologist": [
            {
                "id": "14b57c4b53f4c3af2b666df645161824",
                "name": "Giovannie Jean-Baptiste",
                "address": "1001 Grand Concourse, #13",
                "email": "giovannie_jean-baptiste_10456@gmail.com"
            },
            {
                "id": "8a7eaf6aec5fa0dc8343fc939a00471d",
                "name": "Michael Shirazi",
                "address": "75-17 41ST AVE",
                "email": "michael_shirazi_11432@gmail.com"
            },
            {
                "id": "6f8ee00b875044dc66268ea0b87b1376",
                "name": "Chyne C. Tan",
                "address": "3071 Perry Avenue",
                "email": "chyne_c._tan_10453@gmail.com"
            },
            {
                "id": "5c07a071b1f156d198c6fe382efdf195",
                "name": "Gabrielle Severe",
                "address": "140 Wadsworth Avenue",
                "email": "gabrielle_severe_10016@gmail.com"
            },
            {
                "id": "1383ddaf4542d6c9014e7d32b8fd22e3",
                "name": "Jimmy Sitt",
                "address": "112-03 Queens Blvd, Suite 207",
                "email": "jimmy_sitt_11368@gmail.com"
            },
            {
                "id": "9e437f138cdcb52595203ddf620f91f1",
                "name": "Han Zhang",
                "address": "1 Hanson pl, Ste. 708",
                "email": "han_zhang_11211@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "0c0a5f32ab6602c9e75b693d9cb1501a",
                "name": "John Petrungaro",
                "address": "3071 Perry Avenue",
                "email": "john_petrungaro_10453@gmail.com"
            },
            {
                "id": "8bc754b44ca7544025f3f9a595faad99",
                "name": "Igor Ryndin",
                "address": "12102 Hillside Avenue",
                "email": "igor_ryndin_11217@gmail.com"
            },
            {
                "id": "ef1898b655d0ba5724f67bd7726236f0",
                "name": "Aisha Prim",
                "address": "501 Main Street",
                "email": "aisha_prim_10034@gmail.com"
            },
            {
                "id": "f182c836fc22ed2cf7b4633315221edd",
                "name": "Mary Stein",
                "address": "121A West 20th Street",
                "email": "mary_stein_10021@gmail.com"
            },
            {
                "id": "b85fca453bd0522d601bbab91018bcce",
                "name": "Gerard Lombardo",
                "address": "185 West End Ave",
                "email": "gerard_lombardo_10075@gmail.com"
            },
            {
                "id": "9af2657ba78caaf41b63165127a8fce8",
                "name": "Junaid Chohan",
                "address": "159-05 92nd St.",
                "email": "junaid_chohan_11367@gmail.com"
            },
            {
                "id": "7aead1e9c49d2d876d8467ca1cc6e858",
                "name": "Brianne O'Connor",
                "address": "95-42 Roosevelt Ave",
                "email": "brianne_o'connor_11355@gmail.com"
            },
            {
                "id": "0cd758a07ff17d4c2988f0a556203b27",
                "name": "Nisha Patel",
                "address": "1664 EAST 14TH STREET 4TH FLOOR",
                "email": "nisha_patel_11205@gmail.com"
            },
            {
                "id": "e26ff942c4b8f30553429c89386a6ae7",
                "name": "Stephen Zinnanti",
                "address": "2015 Grand Concourse",
                "email": "stephen_zinnanti_10467@gmail.com"
            },
            {
                "id": "d21711019bdaf230f9e41fad54ffb2e8",
                "name": "Michel Lesly",
                "address": "139-16 91st Avenue",
                "email": "michel_lesly_10453@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "d456a8daa10712be4d35b7e653c29eb6",
                "name": "David Pfaff",
                "address": "64-12 Fresh Pond Rd",
                "email": "david_pfaff_11422@gmail.com"
            },
            {
                "id": "54f49fd57ad35fcfc60112212d7ee106",
                "name": "Durga Maddineni",
                "address": "95-42 Roosevelt Ave",
                "email": "durga_maddineni_11355@gmail.com"
            },
            {
                "id": "6109f56026182501439058856806ca1c",
                "name": "Jesse Stoff",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "jesse_stoff_10462@gmail.com"
            },
            {
                "id": "792b45473b1e7cd0dee3579f0352b998",
                "name": "Mario Haro",
                "address": "410 Lakeville Road",
                "email": "mario_haro_11373@gmail.com"
            },
            {
                "id": "4ef5250f8b7f0164c8a884c10660ae0f",
                "name": "Nam H Om",
                "address": "161 Madison Ave",
                "email": "nam_h_om_10027@gmail.com"
            },
            {
                "id": "b149fd081b477c917cf1211a767e4a31",
                "name": "Richard Wang",
                "address": "141-49 70 Road",
                "email": "richard_wang_11385@gmail.com"
            },
            {
                "id": "2f0edbc6910954cbe4ea337a4bfc1d2b",
                "name": "Joseph Grossman",
                "address": "470 Lenox Avenue Suite 1E",
                "email": "joseph_grossman_10040@gmail.com"
            },
            {
                "id": "e32a8b4bca338f0f2768f548c5193026",
                "name": "Jose Ovalle",
                "address": "1641 3rd Ave suite 27H",
                "email": "jose_ovalle_10013@gmail.com"
            },
            {
                "id": "1fb73df0e3d80c71669c6cdad35eedf9",
                "name": "Rosalinda Spatoliatore",
                "address": "87 08 Justice Avenue",
                "email": "rosalinda_spatoliatore_11435@gmail.com"
            },
            {
                "id": "3f3c741bb7cf5e9b9afa9164343638fb",
                "name": "Andres Hernandez-Abreu",
                "address": "769 Concourse Vlg W",
                "email": "andres_hernandez-abreu_10453@gmail.com"
            },
            {
                "id": "e2fd281343d0fbd7deb2b2ec925b7223",
                "name": "Hosneara Masub",
                "address": "338 E 30th St",
                "email": "hosneara_masub_10013@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "93b0d0ce60eb455900b15c315275d3d8",
                "name": "M. Fawzy Saleem",
                "address": "60 East Plaza Street",
                "email": "m._fawzy_saleem_11220@gmail.com"
            },
            {
                "id": "2235b9fa52a6ec24561c3df239bb9435",
                "name": "Nuzhat Faridi",
                "address": "3071 Perry Avenue",
                "email": "nuzhat_faridi_10453@gmail.com"
            },
            {
                "id": "18837cc1956f1d9f0f487612906b6fb9",
                "name": "Dan Krauser",
                "address": "209-22 Hillside Avenue",
                "email": "dan_krauser_11356@gmail.com"
            },
            {
                "id": "4117545c703c2306f3c1a004305bd16f",
                "name": "Ydelfonso Decoo",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "ydelfonso_decoo_10013@gmail.com"
            },
            {
                "id": "862bd2bcead5df1dfbd7b00225454f2f",
                "name": "France Lee",
                "address": "60 Plaza St E # E",
                "email": "france_lee_11238@gmail.com"
            },
            {
                "id": "e5b5c9ea5ac2c112cf43ec649e52fbe9",
                "name": "Leslie Alvarado",
                "address": "464 West 145th Street",
                "email": "leslie_alvarado_10010@gmail.com"
            },
            {
                "id": "eb545b1713244bdb00a507b569f2cde7",
                "name": "Marie France Conde",
                "address": "90-01 A Roosevelt Ave",
                "email": "marie_france_conde_11042@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "93d62806ed6f48bf8f8fb548261a1b4d",
                "name": "Arun Palkhiwala",
                "address": "450 Clarkson Ave",
                "email": "arun_palkhiwala_11203@gmail.com"
            },
            {
                "id": "82f706a307302d201937243a24ca0871",
                "name": "Jovan Milos",
                "address": "160 E 72nd",
                "email": "jovan_milos_10012@gmail.com"
            },
            {
                "id": "d13d6d634754bf77955a1c28372752a7",
                "name": "Brena M. Desai",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "brena_m._desai_10013@gmail.com"
            },
            {
                "id": "787c35e4fed867c8e90a64235ab98b54",
                "name": "Mikhail Paikin",
                "address": "219-02 Linden Blvd",
                "email": "mikhail_paikin_11366@gmail.com"
            },
            {
                "id": "3d976f1a13db04e8acbefbd82027392a",
                "name": "Elliot J Arons",
                "address": "600 West 150th Street",
                "email": "elliot_j_arons_10030@gmail.com"
            },
            {
                "id": "7071f177b9f69ed640a5acb231c378e1",
                "name": "Hemant Patel",
                "address": "435 Fort Washington Avenue #1H",
                "email": "hemant_patel_10022@gmail.com"
            },
            {
                "id": "53360141a85bc7b51b568fbf9fd5c37d",
                "name": "Rosa Gamundi-Joaquin",
                "address": "1125 FULTON STREET 3RD FLOOR",
                "email": "rosa_gamundi-joaquin_11219@gmail.com"
            },
            {
                "id": "64903043fd9aa07b383a4f2389596803",
                "name": "Buddhadev Manvar",
                "address": "211-16 Union Turnpike",
                "email": "buddhadev_manvar_11372@gmail.com"
            },
            {
                "id": "501cb8d4921e43761e215ee21a1b2281",
                "name": "Irina Nelipovich",
                "address": "1070 Southern Blvd",
                "email": "irina_nelipovich_10458@gmail.com"
            },
            {
                "id": "cc22a2897ef4f27ca7876c9fee1ede78",
                "name": "Darren Esposito",
                "address": "562 East 93rd Street",
                "email": "darren_esposito_11211@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "6f35d31cc730c98251e4201b318819eb",
                "name": "Stella Ilyayeva",
                "address": "55 Midland Avenue",
                "email": "stella_ilyayeva_10306@gmail.com"
            },
            {
                "id": "024e4e36bdbe352d5df7ade81874a45a",
                "name": "Khin Aung",
                "address": "136-20 38th Avenue, Suite 6C",
                "email": "khin_aung_11377@gmail.com"
            },
            {
                "id": "e6683389a3a8a84f7fa3fad0239a2e5d",
                "name": "Jean Langhans",
                "address": "97-77 Queens Blvd. Suite 900,",
                "email": "jean_langhans_11432@gmail.com"
            },
            {
                "id": "37e9e23865bfdceffb0427bbf14811b4",
                "name": "Lawrence Rosman",
                "address": "136-40 39th Avenue",
                "email": "lawrence_rosman_11375@gmail.com"
            },
            {
                "id": "c8a78ecd4dbdfd54bf43c58ed636f2bc",
                "name": "Gabriel Sagles",
                "address": "81 IRVING PLACE",
                "email": "gabriel_sagles_11206@gmail.com"
            },
            {
                "id": "889e1089f23e54641f0299feeeab46dc",
                "name": "Monic Kim",
                "address": "762 59th Street",
                "email": "monic_kim_11210@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "e0cbb2a163675c561752cb46c5bfb48c",
                "name": "Joseph Delimon",
                "address": "1153 58th Street",
                "email": "joseph_delimon_11211@gmail.com"
            },
            {
                "id": "69bbd60aeb2c80c60f7fca03db0adbbb",
                "name": "Andrew Maran",
                "address": "445 Park Avenue",
                "email": "andrew_maran_11211@gmail.com"
            },
            {
                "id": "e48e47ae3427670f0ea89468f6e7328f",
                "name": "Francisco Alonso",
                "address": "59-17 Junction Blvd",
                "email": "francisco_alonso_11379@gmail.com"
            },
            {
                "id": "2efdea4ca2f269dd749f2986c0bd0fe6",
                "name": "Kennedy Omonuwa",
                "address": "3965 Sedgewick Ave",
                "email": "kennedy_omonuwa_10453@gmail.com"
            },
            {
                "id": "30697c74de4d1e42b1d1c0c491e5ba2f",
                "name": "Yusuf Mamdani",
                "address": "2027 JEROME AVE.",
                "email": "yusuf_mamdani_10461@gmail.com"
            },
            {
                "id": "08470d773afff45e1f5791d53650d481",
                "name": "Rafael Bueno",
                "address": "170 W.233rd Street",
                "email": "rafael_bueno_10457@gmail.com"
            },
            {
                "id": "8ec61731aa49dd20df2e080443f6bbf1",
                "name": "Judy Honig",
                "address": "1262 Ocean Parkway",
                "email": "judy_honig_11209@gmail.com"
            },
            {
                "id": "0de11d4563fd0cacf4a5eac9c4df231d",
                "name": "Narayana Byagari",
                "address": "87-08 JUSTICE AVE SUITE CX",
                "email": "narayana_byagari_11103@gmail.com"
            },
            {
                "id": "a7a6c562ce5955ba4c79f2047e91cb00",
                "name": "Gaston Sterlin",
                "address": "121-02 Hillside Avenue",
                "email": "gaston_sterlin_11203@gmail.com"
            },
            {
                "id": "05abbe86a4f26fbb3eccef548ca316b7",
                "name": "Donna Henry",
                "address": "133-29 41st Rd, 2D",
                "email": "donna_henry_11692@gmail.com"
            },
            {
                "id": "39a9d3e4a5f4d885e883ddcf26ee1b31",
                "name": "Baah Asante",
                "address": "139-16 91st Avenue",
                "email": "baah_asante_10453@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "045f09412418475a3782eb0335d64911",
                "name": "Lina Hwang",
                "address": "120 E. 36th Street",
                "email": "lina_hwang_10023@gmail.com"
            },
            {
                "id": "1eb24f6b59bae10c7e8397925093e5ab",
                "name": "Ma Jesusa Christina Calagos",
                "address": "450 clarkson Ave",
                "email": "ma_jesusa_christina_calagos_11218@gmail.com"
            },
            {
                "id": "42e01ed33f6cc190013f7bf892333b8b",
                "name": "Khutoretsky Igor",
                "address": "139 centre street, #505",
                "email": "khutoretsky_igor_10028@gmail.com"
            },
            {
                "id": "ae60dce739f409e04e642f5e2a2e6bc0",
                "name": "Salamat Majeed",
                "address": "3071 Perry Avenue",
                "email": "salamat_majeed_10453@gmail.com"
            },
            {
                "id": "1c4dbe19abc39984aefa031221dea503",
                "name": "Richard Shepard",
                "address": "57-18 Woodside Avenue",
                "email": "richard_shepard_11372@gmail.com"
            },
            {
                "id": "f2b084b567ed9c283da82abde143cf0b",
                "name": "Jay Cowan",
                "address": "115 Central Park West",
                "email": "jay_cowan_10011@gmail.com"
            },
            {
                "id": "7c624ebf78e469357f625e5481a67ce3",
                "name": "Fausto Gonzalez",
                "address": "230 Beach 102nd St",
                "email": "fausto_gonzalez_11373@gmail.com"
            },
            {
                "id": "ea8adf91fa1eed018889fcd09d8b5a72",
                "name": "Haque Naghmana",
                "address": "64-15 Fresh Pond Rd",
                "email": "haque_naghmana_11418@gmail.com"
            },
            {
                "id": "4cc9f090b7b626a26ed0f2cb56ee3f45",
                "name": "Katherine Gold",
                "address": "34 PLAZA STREET, SUITE104",
                "email": "katherine_gold_11204@gmail.com"
            },
            {
                "id": "d51dc3328d5949a3863fd865d26c3ba7",
                "name": "Terence Hsuih",
                "address": "117-06 225th Street 1st Floor",
                "email": "terence_hsuih_11372@gmail.com"
            },
            {
                "id": "1929421b69a6a429846a1343e4908ed0",
                "name": "Hinda Krumbein",
                "address": "372 Kingston Avenue",
                "email": "hinda_krumbein_11226@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "f358f4632130b1e06e949f8b40599805",
                "name": "Alvaro Olayo",
                "address": "730 58th Street, 1F",
                "email": "alvaro_olayo_11220@gmail.com"
            },
            {
                "id": "0becc5eb4dd48e6256a165033ed2549e",
                "name": "Reno DiScala",
                "address": "330 WADSWORTH AVE #1A",
                "email": "reno_discala_10031@gmail.com"
            },
            {
                "id": "6e5e496487893064cf86c7374772b5e0",
                "name": "Zia Ahmed",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "zia_ahmed_10013@gmail.com"
            },
            {
                "id": "4b98261a71ae3a3e585711627f72f015",
                "name": "Steven J. Goldstein",
                "address": "410 Lakeville Road, Suite 202",
                "email": "steven_j._goldstein_11377@gmail.com"
            },
            {
                "id": "f552d8fe58fca64bf726c710c26af338",
                "name": "Raymond Yung",
                "address": "350 Ocean Ave, 1B",
                "email": "raymond_yung_11218@gmail.com"
            },
            {
                "id": "27847ff91f2d4610b5bb747064a6eab7",
                "name": "Rodolfo Miranda",
                "address": "50 10 SKILLMAN AVE",
                "email": "rodolfo_miranda_11354@gmail.com"
            },
            {
                "id": "056653ca53d0dc5f87bad856776fad2d",
                "name": "Shaikh M. Hasan",
                "address": "444 Willis Avenue",
                "email": "shaikh_m._hasan_10468@gmail.com"
            },
            {
                "id": "84d319aca33139f2a4b17ddf19d6f247",
                "name": "Sylvia Gonzales",
                "address": "185 Canal Street, 6th Floor",
                "email": "sylvia_gonzales_11420@gmail.com"
            },
            {
                "id": "79cae8d4dd7cf351eb5b6221733f97b3",
                "name": "pervaiz iqbal",
                "address": "11 Ralph Pl Suite 214",
                "email": "pervaiz_iqbal_10312@gmail.com"
            },
            {
                "id": "ec1b90fe5f0eca53c684070cd60178b8",
                "name": "Elizabeth G. Campos",
                "address": "12102 Hillside Avenue",
                "email": "elizabeth_g._campos_11217@gmail.com"
            },
            {
                "id": "0f94934121fbe945e12a4e549c233b24",
                "name": "Richt Ligsay",
                "address": "15 Wadsworth Ave.",
                "email": "richt_ligsay_10021@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "415ae06502fc512119ac1b58099a08eb",
                "name": "Dalai Zhou",
                "address": "247 Grand St",
                "email": "dalai_zhou_11220@gmail.com"
            },
            {
                "id": "01191fd22fd9a88e0e285d2c39571ea4",
                "name": "Kyungmee Kim",
                "address": "531 54 Street",
                "email": "kyungmee_kim_11209@gmail.com"
            },
            {
                "id": "5f667623886210b9690bdbc11a6178db",
                "name": "Jaime F. Roman",
                "address": "64 Nagle Avenue",
                "email": "jaime_f._roman_10016@gmail.com"
            },
            {
                "id": "da6dda8a05030b04ae44f160a33a0871",
                "name": "Sudhanshu Narendra",
                "address": "1324 BERGEN STREET",
                "email": "sudhanshu_narendra_11230@gmail.com"
            },
            {
                "id": "781f11187691ae9b23899f82262cea35",
                "name": "Daljeet Singh",
                "address": "2869 Grand Concourse Avenue Ste. 1",
                "email": "daljeet_singh_10458@gmail.com"
            },
            {
                "id": "39cf903143ecdeff62559d7e04f988e2",
                "name": "Anna Zhivotovsky",
                "address": "87-08 Justice Ave",
                "email": "anna_zhivotovsky_11374@gmail.com"
            },
            {
                "id": "7668d69a4981b37c98a4d26cc2f582ec",
                "name": "Richard Cedeno",
                "address": "248 Roebling Street",
                "email": "richard_cedeno_11205@gmail.com"
            },
            {
                "id": "39251f6631e0af1c93f4ba8f1c18e533",
                "name": "Anthony Starpoli",
                "address": "105-55 62nd Drive Suite 1-H",
                "email": "anthony_starpoli_11423@gmail.com"
            },
            {
                "id": "b4d591b331a602150b78f4a174c1797e",
                "name": "Xin Yu Zhao",
                "address": "121-02 Hillside Avenue",
                "email": "xin_yu_zhao_11203@gmail.com"
            },
            {
                "id": "8bcbaa6fb03db1bc929c3954fc78d7d8",
                "name": "Zaheer Ahmed",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "zaheer_ahmed_10462@gmail.com"
            },
            {
                "id": "6000e269d9deedaa8debf555dbeec67f",
                "name": "Jill Groves",
                "address": "2091 Nostrand Ave",
                "email": "jill_groves_11208@gmail.com"
            },
            {
                "id": "484869bb6c4cc8a7ef011305c6bd8414",
                "name": "Frank Maselli",
                "address": "12102 Hillside Avenue",
                "email": "frank_maselli_11217@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "4b32830638a8d9d7b8e133c71bb3e30f",
                "name": "Violet Abemayor",
                "address": "251 E 33rd Street, 3rd floor",
                "email": "violet_abemayor_10011@gmail.com"
            },
            {
                "id": "017b46d28fd345bd81bfe581f9807db0",
                "name": "AnnMarie Yu",
                "address": "807 St. Nicholas Avenue, Apt A8",
                "email": "annmarie_yu_10023@gmail.com"
            },
            {
                "id": "7320e20d64c5f0561e5a698b7339b4f0",
                "name": "Ling Ling Zeng",
                "address": "4053 75th Street",
                "email": "ling_ling_zeng_11368@gmail.com"
            },
            {
                "id": "6421bd021f3c934530ea8fa2b6a17c7d",
                "name": "Alison Amsterdam",
                "address": "8008 Third Avenue",
                "email": "alison_amsterdam_11236@gmail.com"
            },
            {
                "id": "97640a2fa05a293fe5d0c0e4dd193a3f",
                "name": "Michael Correa",
                "address": "3510 Bainbridge Avenue",
                "email": "michael_correa_10463@gmail.com"
            },
            {
                "id": "799088e6f5de649487a3927ee511358b",
                "name": "Kara Fine",
                "address": "796 Drew Street",
                "email": "kara_fine_11204@gmail.com"
            },
            {
                "id": "7f38e85433b95c62fc46a90166452634",
                "name": "Kenneth Altabef",
                "address": "2450 8th Ave",
                "email": "kenneth_altabef_10014@gmail.com"
            },
            {
                "id": "6259ee772262c98605e06b6d7ac2b688",
                "name": "Nicholas DuBois",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "nicholas_dubois_10462@gmail.com"
            },
            {
                "id": "05752a0a4362840ca2e1840d0c9b6821",
                "name": "Sandra Garcia",
                "address": "4242 Colden St",
                "email": "sandra_garcia_11418@gmail.com"
            },
            {
                "id": "43df9fbbf3c9921ba878ea2db6a3f93a",
                "name": "Shafiqur Rahman",
                "address": "139-87 35th Avenue",
                "email": "shafiqur_rahman_11694@gmail.com"
            },
            {
                "id": "395e0e44ebe0c9a93d495bba30297c8c",
                "name": "Jordan Wong",
                "address": "2015 Grand Concourse",
                "email": "jordan_wong_10467@gmail.com"
            },
            {
                "id": "5e080c5d0272d5a59e3ac64f451f2f3e",
                "name": "Cynthia Sudar Singh Prabahar",
                "address": "167 Rutledge St",
                "email": "cynthia_sudar_singh_prabahar_11203@gmail.com"
            },
            {
                "id": "457f8797f6efabf956222136b4645ff5",
                "name": "Domingo Santana",
                "address": "75-06 ELIOT AVE",
                "email": "domingo_santana_11355@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "6b60da7c0aaeacbe7e9673a80edb575f",
                "name": "Jose Fulgencio Delmonte",
                "address": "220 A St. Nicholas Avenue",
                "email": "jose_fulgencio_delmonte_11237@gmail.com"
            },
            {
                "id": "e026848a0739d9caf9d37d69df19b099",
                "name": "Kenneth Nordlicht",
                "address": "95-42 Roosevelt Avenue",
                "email": "kenneth_nordlicht_11379@gmail.com"
            },
            {
                "id": "6919a33726d3fe81bf3bda3a5b4a0ae0",
                "name": "Yong S. Tak",
                "address": "3907 Prince St",
                "email": "yong_s._tak_11418@gmail.com"
            },
            {
                "id": "36fcaec025ea22fe4ac32f3ce78c57f6",
                "name": "Maritza Archbold",
                "address": "1250 Shakespeare Avenue",
                "email": "maritza_archbold_10457@gmail.com"
            },
            {
                "id": "858eda9bbbe7274e7b561b31b3c7742e",
                "name": "Ellen Blye",
                "address": "650 First Ave - 7th F",
                "email": "ellen_blye_10033@gmail.com"
            },
            {
                "id": "8ef790af763658b832b59a1fa00979e4",
                "name": "Yuderqui Checo",
                "address": "1610 WILLIAMSBRIDGE RD",
                "email": "yuderqui_checo_10455@gmail.com"
            },
            {
                "id": "958e1f92b261afe304c6b58eb1843225",
                "name": "Natalia Peters",
                "address": "37-52 82nd Street 2nd Floor",
                "email": "natalia_peters_10458@gmail.com"
            },
            {
                "id": "8d3c6dbd9334b6514a5e2fe10d2a5f87",
                "name": "Machlah Lopiar",
                "address": "3765 Riverdale Avenue - Suite 7",
                "email": "machlah_lopiar_10462@gmail.com"
            },
            {
                "id": "03c7c052471be0271b8c66fb67aa673d",
                "name": "Bing Lu",
                "address": "2201 Amsterdam Avenue",
                "email": "bing_lu_10001@gmail.com"
            },
            {
                "id": "fd09912ae5f0e26a91dd93652275a891",
                "name": "Usukumah E. Usukumah",
                "address": "201 East 69th St",
                "email": "usukumah_e._usukumah_11355@gmail.com"
            },
            {
                "id": "0ea8aa4fee6be5bc64a9a2422e085e23",
                "name": "VIRGINIA MARTINEZ",
                "address": "136-21 Roosevelt Ave, Suite #205",
                "email": "virginia_martinez_11373@gmail.com"
            },
            {
                "id": "95fc0f5c9606d0193f32d4d50616b9de",
                "name": "Denise Nunez",
                "address": "222 East 19th Street",
                "email": "denise_nunez_10016@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "7578da50ec2c20e0fa2ed8a09dc348a3",
                "name": "Mohammed Rashid",
                "address": "435 FORT WASHINGTON AVE",
                "email": "mohammed_rashid_10032@gmail.com"
            },
            {
                "id": "d7662900fbd36452bcd33621c9e8391e",
                "name": "Cherenfant Lucot",
                "address": "99 University Place, 3Rd floor",
                "email": "cherenfant_lucot_10024@gmail.com"
            },
            {
                "id": "84259f9785c9420bab1576a43c8a8942",
                "name": "Pamela Mahmud",
                "address": "2015 Grand Concourse",
                "email": "pamela_mahmud_10467@gmail.com"
            },
            {
                "id": "3383d78fe9bc8175b5e6d5bcf27105c4",
                "name": "Herbert Chin",
                "address": "217 Ovington Avenue",
                "email": "herbert_chin_11210@gmail.com"
            },
            {
                "id": "4b0fb711496da50820f5012af04d43b5",
                "name": "Steven Field",
                "address": "1262 Ocean Parkway",
                "email": "steven_field_11209@gmail.com"
            },
            {
                "id": "92e5fa96880775cd270733c61afbd0de",
                "name": "Sheldon Lippman",
                "address": "328 East 61st Street",
                "email": "sheldon_lippman_10011@gmail.com"
            },
            {
                "id": "eaed0950cb3f49aa93979f33964a0ccb",
                "name": "Himanshu Patel",
                "address": "1225 Foster Avenue",
                "email": "himanshu_patel_11220@gmail.com"
            },
            {
                "id": "687d8d2c795e8c13bd012f61be375f4c",
                "name": "Jorge Serje",
                "address": "19 East 80th Street",
                "email": "jorge_serje_10037@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "076b60dce6f6dd3a32f1847ae361f4f6",
                "name": "Marissa Santos",
                "address": "87-81, 169th Street",
                "email": "marissa_santos_11372@gmail.com"
            },
            {
                "id": "c53dedabdd269622e1eff16283a13752",
                "name": "Laurence Turnier-Antione",
                "address": "450 Clarkson Ave",
                "email": "laurence_turnier-antione_11203@gmail.com"
            },
            {
                "id": "f72a22814dd2c4557d132e16df64b3c7",
                "name": "Beppy Edasery",
                "address": "2742 brighton 8th street",
                "email": "beppy_edasery_11236@gmail.com"
            },
            {
                "id": "26de9c84c2b3f82a2e154c7155d1cf9b",
                "name": "Elsa Sofia Reynoso",
                "address": "730 58th Street, 1F",
                "email": "elsa_sofia_reynoso_11220@gmail.com"
            },
            {
                "id": "0fe3c1ec908888826252983f059f8001",
                "name": "David Kaplowitz",
                "address": "435 Fort Washington Avenue Suite 1C",
                "email": "david_kaplowitz_10013@gmail.com"
            },
            {
                "id": "7d3394af23f633c2ea31ec1358c431cf",
                "name": "Alan Lee",
                "address": "3125 TIBBETT AVENUE",
                "email": "alan_lee_10459@gmail.com"
            },
            {
                "id": "6d24af668ff38e3f586a01ada09ab712",
                "name": "Theresa Pondok",
                "address": "80-37 Broadway",
                "email": "theresa_pondok_11354@gmail.com"
            },
            {
                "id": "f902dd4ba7501614de6970e0e1208a5a",
                "name": "Anil Saxena",
                "address": "97-03 Springfield Blvd",
                "email": "anil_saxena_11377@gmail.com"
            },
            {
                "id": "840a8ae1b8f5ecd941ead358ff157a77",
                "name": "Alan David",
                "address": "2202 Grand Concourse",
                "email": "alan_david_10463@gmail.com"
            },
            {
                "id": "b32e1358650440a5671d3a7712895fa9",
                "name": "Azra Wasti",
                "address": "600 West 150th Street",
                "email": "azra_wasti_10030@gmail.com"
            },
            {
                "id": "97bdd854a3c3d94c83a5f0cbf3e62fdd",
                "name": "Jean Robert Macenat",
                "address": "103-14 Lefferts Blvd",
                "email": "jean_robert_macenat_11402@gmail.com"
            },
            {
                "id": "6951459372fa1d335efaaa454d33b35c",
                "name": "Patricia Halton",
                "address": "29-28 41st Avenue",
                "email": "patricia_halton_11355@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "e73212e7d6c4eb5e7d99130ae2607cb1",
                "name": "Rafik Khaimov",
                "address": "34 PLAZA STREET, SUITE104",
                "email": "rafik_khaimov_11204@gmail.com"
            },
            {
                "id": "d3ab4fb4f3424ceea8fe9b22e70364d9",
                "name": "Terry Blackett-Bonnett",
                "address": "117-06 225th Street 1st Floor",
                "email": "terry_blackett-bonnett_11372@gmail.com"
            },
            {
                "id": "862963d7cc99c144731c9afdc341158f",
                "name": "Edward T. Fitzpatrick",
                "address": "30-55 21st Street",
                "email": "edward_t._fitzpatrick_11103@gmail.com"
            },
            {
                "id": "7f16fed96ebb338f622a009207d00cbe",
                "name": "Rattanjit Kohli",
                "address": "3654 Godwin Terrace, Suite C",
                "email": "rattanjit_kohli_10466@gmail.com"
            },
            {
                "id": "8fb6bf07560d705027d7194f590e0d68",
                "name": "Alma Mesquita",
                "address": "7220 17th Avenue",
                "email": "alma_mesquita_11213@gmail.com"
            },
            {
                "id": "a644b4a706a75a29bd1a66395dc504a9",
                "name": "Rodolfo Guzman",
                "address": "121 East 60th Street",
                "email": "rodolfo_guzman_10013@gmail.com"
            },
            {
                "id": "32a0766c17c1c8101d7ed31861d3897c",
                "name": "Howard Hochster",
                "address": "4543 43rd Street",
                "email": "howard_hochster_11372@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "21ed29f39b12027968205fb5498920f1",
                "name": "Teresa Chan",
                "address": "158 East 84th St",
                "email": "teresa_chan_10022@gmail.com"
            },
            {
                "id": "e8e5b9d33be7d99c6fb03d6f14e0f550",
                "name": "Jose Perez",
                "address": "305 Seguine Ave Ste. 1",
                "email": "jose_perez_10305@gmail.com"
            },
            {
                "id": "897f73637af51e50bd8149e1d23591a2",
                "name": "S Tokar",
                "address": "110-45 Queens Boulevard Suite A",
                "email": "s_tokar_11516@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "af62b101a97ee3d5174785096dc154bc",
                "name": "David Baskin",
                "address": "911 Park Avenue",
                "email": "david_baskin_10044@gmail.com"
            },
            {
                "id": "0c90599517a6346978332a03a01350a7",
                "name": "Jean Paul Salinas",
                "address": "839 58th Street, 2nd Floor",
                "email": "jean_paul_salinas_11204@gmail.com"
            },
            {
                "id": "33f16ab3969fba8d510e2895329ee8bb",
                "name": "Karen Chiu",
                "address": "95 Seaman Ave",
                "email": "karen_chiu_10031@gmail.com"
            },
            {
                "id": "db75f4da8a63ca0f325d4876e5381b7a",
                "name": "Clotilde Pena",
                "address": "86 Bowery Street, 6F",
                "email": "clotilde_pena_10065@gmail.com"
            },
            {
                "id": "fdcd23b33512eb4a93d3848781e53b2e",
                "name": "Tatyana Gabinskaya",
                "address": "39-07 PRINCE ST. 6H",
                "email": "tatyana_gabinskaya_11372@gmail.com"
            },
            {
                "id": "bd41fb671abb8971ee0e94af18203fd4",
                "name": "Dolores Martinez",
                "address": "99 University Place, 3Rd floor",
                "email": "dolores_martinez_10024@gmail.com"
            }
        ]
    },
    "Queens": {
        "toxicologist": [
            {
                "id": "3347582cb6ab72a46c39ab6cc520f4b6",
                "name": "Nicole Arcentales",
                "address": "4000 SETON AVENUE",
                "email": "nicole_arcentales_10454@gmail.com"
            },
            {
                "id": "83665e4ee2ea1959cedc70449d6e451e",
                "name": "Ramy Hanna",
                "address": "435 Fort Washington Avenue Suite 1C",
                "email": "ramy_hanna_10013@gmail.com"
            },
            {
                "id": "eca5e8a35e99c3323f32edfadd76dd50",
                "name": "Olukayode Ojutiku",
                "address": "1497 Richmond Road",
                "email": "olukayode_ojutiku_11418@gmail.com"
            },
            {
                "id": "21737c92198076025b6a21877d84834f",
                "name": "Hajoon Chun",
                "address": "86-04 117th. street",
                "email": "hajoon_chun_11364@gmail.com"
            },
            {
                "id": "d494d737b2ac198a25710a60705716a0",
                "name": "Daniel Izon",
                "address": "12102 Hillside Avenue",
                "email": "daniel_izon_11217@gmail.com"
            },
            {
                "id": "d4d2f3a38b87482c4214c9f439433efa",
                "name": "Yevgeniya Kaykova",
                "address": "210 East 86 Street",
                "email": "yevgeniya_kaykova_10028@gmail.com"
            },
            {
                "id": "1f842ad77fc57e68cf6c09c84a94dc8c",
                "name": "Elizabeth Salzer",
                "address": "115 13A Merrick Blvd",
                "email": "elizabeth_salzer_11355@gmail.com"
            },
            {
                "id": "ecb7cccfe7e23875c71aa32b5939693c",
                "name": "Konstantinos Zarkadas",
                "address": "34 PLAZA STREET, SUITE104",
                "email": "konstantinos_zarkadas_11204@gmail.com"
            },
            {
                "id": "688426f1009197e2adf9ec9ab091bd1f",
                "name": "Beth Lustgarten",
                "address": "833 58th Street",
                "email": "beth_lustgarten_11224@gmail.com"
            },
            {
                "id": "1740e776831349e8ee9adaacb9b32f1b",
                "name": "Maria Evola",
                "address": "400 Broadway",
                "email": "maria_evola_10033@gmail.com"
            },
            {
                "id": "d0e7af27671bb3e091cbbe663da02ab1",
                "name": "Mercy Brew",
                "address": "41-61 Kissena Blvd.",
                "email": "mercy_brew_11355@gmail.com"
            },
            {
                "id": "d19d07be351fc359bef9898468f26f67",
                "name": "Fausto Gonzalez",
                "address": "125 East 86th Street",
                "email": "fausto_gonzalez_10031@gmail.com"
            },
            {
                "id": "ef07b5ccb98a7be2c630f23da0713440",
                "name": "Pramila Kolisetty",
                "address": "314 West 14th Street",
                "email": "pramila_kolisetty_11355@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "a7853e7f3b9ae97faaad4a5166b202cd",
                "name": "Anna DiBona",
                "address": "133-29 41st Rd, 2D",
                "email": "anna_dibona_11692@gmail.com"
            },
            {
                "id": "f522b25e966cd00a5a2e8b1c88a49a71",
                "name": "Renata Ukowska",
                "address": "217 Grand Street",
                "email": "renata_ukowska_10032@gmail.com"
            },
            {
                "id": "a9ef52116274069e1ec4182a76dc8da9",
                "name": "Farzana Aziz",
                "address": "1807 Randall Avenue,",
                "email": "farzana_aziz_10468@gmail.com"
            },
            {
                "id": "9ad6c7fc4fbdaeb86c47cbd222c7ce38",
                "name": "Carlos Conception",
                "address": "15 Wadsworth Ave.",
                "email": "carlos_conception_10021@gmail.com"
            },
            {
                "id": "91cf3e6d6a0ff19949e165c25695d847",
                "name": "Bahram Alyeshmerni",
                "address": "33 WEST 125TH STREET",
                "email": "bahram_alyeshmerni_10013@gmail.com"
            },
            {
                "id": "8789f7eb9561bcd28cc998bc0d17aaf9",
                "name": "O'Neall E. Parris",
                "address": "121A West 20th Street",
                "email": "o'neall_e._parris_10021@gmail.com"
            },
            {
                "id": "f41b8555480918f79d6632753653595b",
                "name": "Clifford Stark",
                "address": "209 Beach125 ST",
                "email": "clifford_stark_11358@gmail.com"
            },
            {
                "id": "aec9adcdf099842bde51599653f22d83",
                "name": "Ya-Hsiu Yen",
                "address": "33 W. 125th St",
                "email": "ya-hsiu_yen_10022@gmail.com"
            },
            {
                "id": "be38308aa5688f4c5ce00f2b53aeb474",
                "name": "Haydee Blanca",
                "address": "1103 Cortelyou Road",
                "email": "haydee_blanca_11230@gmail.com"
            },
            {
                "id": "04beefe206ae7ac1422c9979d3bcebb9",
                "name": "Paul Lee",
                "address": "13347 Sanford Ave.#C1F",
                "email": "paul_lee_11354@gmail.com"
            },
            {
                "id": "dca98ea2494fa623e15a8bbc1567d16c",
                "name": "Haleh Mohseni",
                "address": "1922 McGraw Ave #1B",
                "email": "haleh_mohseni_10453@gmail.com"
            },
            {
                "id": "4b7876e47055e02389147a7ec65dc223",
                "name": "Anil Gupta",
                "address": "41-60 Main Street",
                "email": "anil_gupta_11355@gmail.com"
            },
            {
                "id": "df9979d6dad66317e99d4cb2529f1a5c",
                "name": "Carmen Lazala",
                "address": "47 E 77th Street, Suite 201",
                "email": "carmen_lazala_10034@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "f3ce64cd89054cc1c9a946c9b9bbce47",
                "name": "Miroslawa Kudej",
                "address": "37-11 88th Street",
                "email": "miroslawa_kudej_11355@gmail.com"
            },
            {
                "id": "67c830597e99f5ea7873847e24eccfd8",
                "name": "Tasbirul Alam",
                "address": "121A West 20th Street",
                "email": "tasbirul_alam_10021@gmail.com"
            },
            {
                "id": "a99f48fce125a4acf384c5730255299c",
                "name": "Lomane Legros",
                "address": "464 West 145th Street",
                "email": "lomane_legros_10010@gmail.com"
            },
            {
                "id": "d2284ec975551ee0602698ea10629a45",
                "name": "Angela Todd",
                "address": "87 08 Justice Avenue",
                "email": "angela_todd_11435@gmail.com"
            },
            {
                "id": "4a2ca12e7878478f4e01b8aeffd011fd",
                "name": "Bisher Akil",
                "address": "520 Neptune Avenue",
                "email": "bisher_akil_11201@gmail.com"
            },
            {
                "id": "4c6266fefcb6cd450a3458ba7d8fa8b3",
                "name": "Maurice Alwaya",
                "address": "60 Plaza St E # E",
                "email": "maurice_alwaya_11238@gmail.com"
            },
            {
                "id": "aa8b6302181d7589ac831ca425bafcf3",
                "name": "Jacob Meltzer",
                "address": "353 Fort Washington Avenue #1E",
                "email": "jacob_meltzer_10025@gmail.com"
            },
            {
                "id": "ad56fd10f126db80e2f3b1ca0f22b390",
                "name": "Jacob George",
                "address": "94-36 59th Avenue",
                "email": "jacob_george_11372@gmail.com"
            },
            {
                "id": "745bacfdecdc4a4d2119fe030ca292fe",
                "name": "Maxine Orris",
                "address": "117-06 225th Street 1st Floor",
                "email": "maxine_orris_11372@gmail.com"
            },
            {
                "id": "30733ae8209b5b1688270e5d38c62fd1",
                "name": "Faina Akselrod",
                "address": "97-13 64th Road",
                "email": "faina_akselrod_11213@gmail.com"
            },
            {
                "id": "0dc6ce38007df2db3b155a958ffe69c2",
                "name": "Veluy Chorm",
                "address": "164-08 65th Ave",
                "email": "veluy_chorm_11375@gmail.com"
            },
            {
                "id": "8f0217cf57f900805e3bff1e4abed72a",
                "name": "Rachelle Namm",
                "address": "1473 Sterling Place",
                "email": "rachelle_namm_11203@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "7fb5c9e2636d51a47e69422afc900dd4",
                "name": "Nair Ramachandran",
                "address": "437 Mother Gaston Blvd",
                "email": "nair_ramachandran_11230@gmail.com"
            },
            {
                "id": "7c33e1525f3ca02adf5cd37ab12b412b",
                "name": "Richard Desmond",
                "address": "400 Broadway",
                "email": "richard_desmond_10033@gmail.com"
            },
            {
                "id": "3ba3eec72be9176a61bd4293ab303117",
                "name": "Lohrasb Ahmadian",
                "address": "121-02 Hillside Avenue",
                "email": "lohrasb_ahmadian_11203@gmail.com"
            },
            {
                "id": "7f7071ebf73efbd0bbef508804be978e",
                "name": "Christel Moran",
                "address": "1150 Park Avenue",
                "email": "christel_moran_10031@gmail.com"
            },
            {
                "id": "32cc0db6e43e2f8c42ab33529f0a025a",
                "name": "Indira Kairam",
                "address": "4434 Amboy Road",
                "email": "indira_kairam_11356@gmail.com"
            },
            {
                "id": "942a38f3f0414ad9ec1c9229330bc021",
                "name": "Jean Zheng",
                "address": "1153 58th Street",
                "email": "jean_zheng_11211@gmail.com"
            },
            {
                "id": "4346b9bc6d0b4baf1bb9156a5e09fe8d",
                "name": "Maria Pirraglia",
                "address": "136-20 38th Avenue, Suite 6C",
                "email": "maria_pirraglia_11377@gmail.com"
            },
            {
                "id": "da7684381f8a2600d3c5331d666afe3d",
                "name": "Cathy Delerme-Pagan",
                "address": "3071 Perry Avenue",
                "email": "cathy_delerme-pagan_10453@gmail.com"
            },
            {
                "id": "4758ed7589267f623e60d67a3b848517",
                "name": "Jiang Ming",
                "address": "47-10 Greenpoint Avenue",
                "email": "jiang_ming_11372@gmail.com"
            },
            {
                "id": "04e03843654b624694acca361c217c92",
                "name": "Albert Bassoul",
                "address": "89-18 134 street",
                "email": "albert_bassoul_11420@gmail.com"
            },
            {
                "id": "7d888eddac659502baffdcc3977714b6",
                "name": "Tinmar Tun",
                "address": "3510 Bainbridge Avenue",
                "email": "tinmar_tun_10463@gmail.com"
            }
        ],
        "urologist": [
            {
                "id": "d6e91667128153ea9e3d92983c41f9ff",
                "name": "Salvatore Volpe",
                "address": "95-42 Roosevelt Avenue",
                "email": "salvatore_volpe_11379@gmail.com"
            },
            {
                "id": "d94fe76f0e39896eff12a39af9b69912",
                "name": "Jia Hong",
                "address": "4039 Junction Blvd",
                "email": "jia_hong_11042@gmail.com"
            },
            {
                "id": "a5b9fafc26c1c190283f7919e526bc3d",
                "name": "Sophia Streete-Smalls",
                "address": "1700 Flatbush Ave",
                "email": "sophia_streete-smalls_11215@gmail.com"
            },
            {
                "id": "7c970949af575b8d0e80d1a17d6c2655",
                "name": "Mohammed M. Rahman",
                "address": "-305 Seguine Avenue",
                "email": "mohammed_m._rahman_10304@gmail.com"
            },
            {
                "id": "e2195762682b4678c0c3e90273012134",
                "name": "Smita Biswas",
                "address": "1627 Broadway",
                "email": "smita_biswas_10032@gmail.com"
            },
            {
                "id": "2ffcb590b207cf8a2154f32e2937d903",
                "name": "Robert Meltzer",
                "address": "2202 Grand Concourse",
                "email": "robert_meltzer_10463@gmail.com"
            },
            {
                "id": "56405b2fa1e2edc0c76660f9460544c2",
                "name": "David Kim",
                "address": "2844 Briggs Avenue",
                "email": "david_kim_10468@gmail.com"
            },
            {
                "id": "480dcb04570907c87251ce9ca68e4ebd",
                "name": "Mara Pulcher",
                "address": "712 Knickerbocker Avenue",
                "email": "mara_pulcher_11218@gmail.com"
            },
            {
                "id": "7454933fbcfcfba0cbcd94b10578b495",
                "name": "Daniel Korin",
                "address": "40-08 Forley Street",
                "email": "daniel_korin_11432@gmail.com"
            },
            {
                "id": "0e4720c0ef33bb9f64414e8c3a5e5300",
                "name": "Jayant Gandhi",
                "address": "1203 Avenue J",
                "email": "jayant_gandhi_11213@gmail.com"
            },
            {
                "id": "cd9225248f4f97341df694b319d511ba",
                "name": "George McMillan",
                "address": "860 Grand Concourse",
                "email": "george_mcmillan_10461@gmail.com"
            },
            {
                "id": "a81d24841b30328fc73afaf1b65575a9",
                "name": "Carole Dubuche",
                "address": "808 New York Avenue",
                "email": "carole_dubuche_11220@gmail.com"
            },
            {
                "id": "7bcc355e4371a18568863069cb1f8e01",
                "name": "Patricia Mullings",
                "address": "4260 Broadway",
                "email": "patricia_mullings_10027@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "c11cc6141f1bbdff712f24f2dde5f92f",
                "name": "Jamshad Wyne",
                "address": "251 E 33rd Street, 3rd floor",
                "email": "jamshad_wyne_10011@gmail.com"
            },
            {
                "id": "f156a180dc7e76fb4fa3e41c0ed1891c",
                "name": "Steve C Chang",
                "address": "711 Cedar Lawn",
                "email": "steve_c_chang_11418@gmail.com"
            },
            {
                "id": "d38d7f5078e83a8bc6198c5e775b44c5",
                "name": "Muntaz Majeed",
                "address": "128 Mott Street Suite 302",
                "email": "muntaz_majeed_10003@gmail.com"
            },
            {
                "id": "aeb72d2737a125594114f3d3c23209c7",
                "name": "Jean Carlos Torres",
                "address": "1509 Rockaway Parkway",
                "email": "jean_carlos_torres_11209@gmail.com"
            },
            {
                "id": "f8dd4b9370ad8c5f27e153192f30f4ca",
                "name": "Luis Vasquez",
                "address": "2426 Eastchester Road",
                "email": "luis_vasquez_10458@gmail.com"
            },
            {
                "id": "021b9dce4e83c1f8ca953dbfe948ffad",
                "name": "MeeYee Yolanda Eng",
                "address": "739 Knickerbocker Avenue",
                "email": "meeyee_yolanda_eng_11203@gmail.com"
            },
            {
                "id": "c71a598cf4934def41564c5839b75b33",
                "name": "Roberto Moran",
                "address": "8008 Third Avenue",
                "email": "roberto_moran_11236@gmail.com"
            },
            {
                "id": "08a655ced35ca8e9dbf390cccd1fc022",
                "name": "Karen Greer",
                "address": "445 Park Avenue",
                "email": "karen_greer_11211@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "3902d5337d60ea60aacb77332aff77c6",
                "name": "Michael Moretti",
                "address": "391 East 149th Street",
                "email": "michael_moretti_11694@gmail.com"
            },
            {
                "id": "6506d224dbe4fa49839d13702c895b11",
                "name": "Amy Xioa Chen Ma",
                "address": "113-11 Jamaica Ave,",
                "email": "amy_xioa_chen_ma_11354@gmail.com"
            },
            {
                "id": "e365a1107e84ea78ab6ff4476d15407f",
                "name": "Daniel Buff",
                "address": "471 Hart Street",
                "email": "daniel_buff_11235@gmail.com"
            },
            {
                "id": "fc6f473f69e96d03c374843adc94b850",
                "name": "Frank Arbucci",
                "address": "13347 Sanford Ave",
                "email": "frank_arbucci_11372@gmail.com"
            },
            {
                "id": "774df49ce000e01cf936be8d64f9e9f6",
                "name": "Hector Holson",
                "address": "231 South 3rd Street",
                "email": "hector_holson_11219@gmail.com"
            },
            {
                "id": "878dad41c424e27e83d830804cb39868",
                "name": "April Lowry",
                "address": "43-48 Colden St.",
                "email": "april_lowry_11103@gmail.com"
            },
            {
                "id": "7566640be8c6c02b7c26e3776e45bf27",
                "name": "Olusegun Adeonigbagbe",
                "address": "121A West 20th Street",
                "email": "olusegun_adeonigbagbe_10021@gmail.com"
            },
            {
                "id": "d16922674f1b52f35c7d8573d027145f",
                "name": "Racquel M Volkowitz",
                "address": "241-08 140th Ave",
                "email": "racquel_m_volkowitz_11354@gmail.com"
            },
            {
                "id": "08c53f17d7b6f2d982b9aedfc819ea46",
                "name": "Saul Feldman",
                "address": "1718 Pitkin Avenue",
                "email": "saul_feldman_11203@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "914b04c957eeceb8fc16e9379cdb43d5",
                "name": "Svetlana Ten",
                "address": "596 Pennsylvania Avenue",
                "email": "svetlana_ten_11218@gmail.com"
            },
            {
                "id": "38cf432fcd42d775fc2aaecb92986a48",
                "name": "Donna Murphy",
                "address": "3071 Perry Avenue",
                "email": "donna_murphy_10453@gmail.com"
            },
            {
                "id": "437e1cc31c9238e7aa601ef163bd7fee",
                "name": "Mohammed Osmani, MD",
                "address": "410 Lakeville Road",
                "email": "mohammed_osmani,_md_11373@gmail.com"
            },
            {
                "id": "04a93c21ac23a8f68e7556f247f9d9c8",
                "name": "Ruben Cerri",
                "address": "1561 Westchester Avenue",
                "email": "ruben_cerri_10457@gmail.com"
            },
            {
                "id": "dffccca53b00443aa5517ec24356f8e2",
                "name": "Jose Ortiz",
                "address": "1624 University Avenue",
                "email": "jose_ortiz_10453@gmail.com"
            },
            {
                "id": "f169a80ee2b30b0f6cfdf4b048a98a91",
                "name": "Walt Sargeant",
                "address": "629 West 185th Street",
                "email": "walt_sargeant_11372@gmail.com"
            },
            {
                "id": "c4f3674f327d7d899771589f76b39861",
                "name": "Larry Shemen",
                "address": "136-20 38th Ave",
                "email": "larry_shemen_11432@gmail.com"
            },
            {
                "id": "e3bbd3f98d78e8f06f30d3e43dced3d0",
                "name": "Ashok Sinha",
                "address": "739 Knickerbocker Avenue",
                "email": "ashok_sinha_11203@gmail.com"
            },
            {
                "id": "5a77ee8bc0d9ff5806a6462d90048817",
                "name": "Ronnie Chiu",
                "address": "95-42 Roosevelt Avenue",
                "email": "ronnie_chiu_11379@gmail.com"
            },
            {
                "id": "66cca92ada2a02eaac8218eb0aa2b290",
                "name": "Imtiyaz Kapadwala",
                "address": "1509 Rockaway Parkway",
                "email": "imtiyaz_kapadwala_11209@gmail.com"
            },
            {
                "id": "a5a45bf6e8dcd89380c657c5269727d7",
                "name": "Domenic Onyema",
                "address": "81 IRVING PLACE",
                "email": "domenic_onyema_11206@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "14f3a1a7d1f5e6d34c8ed4af7573150b",
                "name": "Tooraj Zahedi",
                "address": "46 Fort Washington Avenue #2",
                "email": "tooraj_zahedi_10034@gmail.com"
            },
            {
                "id": "547bf130b155abf32043532fc0ad0e47",
                "name": "Gloria Dunnder Leacock",
                "address": "136-30 MAPLE AVENUE #2F",
                "email": "gloria_dunnder_leacock_11206@gmail.com"
            },
            {
                "id": "96eba85930d4f53071a66f0e16b89cc9",
                "name": "Hung-Sam Lee",
                "address": "3071 Perry Avenue",
                "email": "hung-sam_lee_10453@gmail.com"
            },
            {
                "id": "0bf4da136a94b61da6e7fe56444ba24d",
                "name": "Nayaz Ahmed",
                "address": "87-46 168th Street",
                "email": "nayaz_ahmed_11355@gmail.com"
            },
            {
                "id": "c01f70eb2cc293b0528028ffa267518e",
                "name": "Edgar Flores-Castillo",
                "address": "870 centaal ave",
                "email": "edgar_flores-castillo_11385@gmail.com"
            },
            {
                "id": "7021bd3e9429f21677afdaae3fee5622",
                "name": "Fabio Mehrgut",
                "address": "1650 Selwyn Ave, 6th Floor",
                "email": "fabio_mehrgut_10458@gmail.com"
            },
            {
                "id": "7fa05c94ad550748e1732920f1c7dabb",
                "name": "Pedro Guzman",
                "address": "1627 Broadway",
                "email": "pedro_guzman_10032@gmail.com"
            },
            {
                "id": "42010b92bcdbdb7cd76c81106e4a1c64",
                "name": "Paul Knoepflmacher",
                "address": "86 East 49 St , Suite G",
                "email": "paul_knoepflmacher_11221@gmail.com"
            },
            {
                "id": "de9fcbc9a9d35a4784f88c9f675ad98a",
                "name": "Todd Mcniff",
                "address": "37-57 91st Street",
                "email": "todd_mcniff_11354@gmail.com"
            },
            {
                "id": "6e62acb03bc717a6bb7d7418b67028da",
                "name": "Francisco Rosario",
                "address": "241-08 140th Ave",
                "email": "francisco_rosario_11354@gmail.com"
            },
            {
                "id": "06ee9260aeb9dae4a4def6d8643e6ed8",
                "name": "Joseph Grossman",
                "address": "102 East 22 St Suite 1",
                "email": "joseph_grossman_10024@gmail.com"
            },
            {
                "id": "3cdb594c6919567b754b3df30b2460b1",
                "name": "Flor, De La Cadena",
                "address": "217 Ovington Avenue",
                "email": "flor,_de_la_cadena_11210@gmail.com"
            },
            {
                "id": "ac68990c2af6db82fb02037fd5dbc0fa",
                "name": "Marjorie Ordene",
                "address": "3017 Colden Avenue",
                "email": "marjorie_ordene_10461@gmail.com"
            },
            {
                "id": "f50cb8dd3875122d245773bc6898db20",
                "name": "Kotresha Neelakantappa",
                "address": "4139 Wickham Ave",
                "email": "kotresha_neelakantappa_10468@gmail.com"
            },
            {
                "id": "d7f7de21faf50a2d02efccbfcf71ba78",
                "name": "Samuel DeLeon",
                "address": "2378 Ralph Ave",
                "email": "samuel_deleon_11203@gmail.com"
            },
            {
                "id": "a3fdd370e37a8fabdf8e8d40ea1cf718",
                "name": "Zia Ghavami",
                "address": "2385 Arthur Avenue, Suite @206",
                "email": "zia_ghavami_10468@gmail.com"
            },
            {
                "id": "b41f13cfabc90ce143949c7d75914573",
                "name": "JUAN PILARTE",
                "address": "739 Knickerbocker Avenue",
                "email": "juan_pilarte_11203@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "7bcc5cd47922bd4d2f25dedd91796f99",
                "name": "Rudrama Duggirala",
                "address": "707 West 171st Suite A",
                "email": "rudrama_duggirala_10034@gmail.com"
            },
            {
                "id": "c752827c9f15144dc2e484862a353047",
                "name": "George V Jhagroo",
                "address": "1627 Broadway",
                "email": "george_v_jhagroo_10032@gmail.com"
            },
            {
                "id": "1b547314d107e46e05f143e85a913463",
                "name": "Ira Casson",
                "address": "121A West 20th Street",
                "email": "ira_casson_10021@gmail.com"
            },
            {
                "id": "85c798355c8b10437de27fa0337ae9b3",
                "name": "Nicasio Arana",
                "address": "839 58th Street, 2nd Floor",
                "email": "nicasio_arana_11204@gmail.com"
            },
            {
                "id": "9e635b05740f7e068555c6f5e725f13e",
                "name": "Sara Donnelly",
                "address": "763 56th Street , 1st floor",
                "email": "sara_donnelly_11219@gmail.com"
            },
            {
                "id": "305fa68649b5fcdebf28475de8cd289c",
                "name": "Marissa Pelletier",
                "address": "34 PLAZA STREET, SUITE104",
                "email": "marissa_pelletier_11204@gmail.com"
            },
            {
                "id": "9de85f6512a8b0c97af5f4f56f48f563",
                "name": "Todd Schlifstein",
                "address": "830 Marcy Avenue",
                "email": "todd_schlifstein_11237@gmail.com"
            },
            {
                "id": "b294812a73e3592b4ffa2174f443bdfd",
                "name": "Nagi Bustros",
                "address": "13176 Laurelton Parkway",
                "email": "nagi_bustros_11373@gmail.com"
            },
            {
                "id": "edbcaf66b32b9f265b0d449420822bb0",
                "name": "Madan Paul",
                "address": "136-20 38th Ave",
                "email": "madan_paul_11432@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "540a0775a3817416d1dfd2edf398da6b",
                "name": "Yi Ngai",
                "address": "600 West 150th Street",
                "email": "yi_ngai_10030@gmail.com"
            },
            {
                "id": "a71ab94eb40f9e661330f29f18d23c17",
                "name": "Diego Ratzlaff",
                "address": "205-16 Linden blvd",
                "email": "diego_ratzlaff_11377@gmail.com"
            },
            {
                "id": "aeffd62bdd3f0dd8d90bb52652e07d4d",
                "name": "Ming Zhu",
                "address": "9817 Queens Boulevard, LL2",
                "email": "ming_zhu_11368@gmail.com"
            },
            {
                "id": "4941a868c46f05fcc51fbc38eef304cf",
                "name": "Annette Perea",
                "address": "2202 Grand Concourse",
                "email": "annette_perea_10463@gmail.com"
            },
            {
                "id": "ab34d339c75ae6ab533c4754fd4cd2dd",
                "name": "Tina Dobsevage",
                "address": "83-10 Queens Blvd",
                "email": "tina_dobsevage_11372@gmail.com"
            },
            {
                "id": "c640545bc04837b3a5e2fdfcb6d83f73",
                "name": "Lilia Gorodinsky",
                "address": "3747-77th St",
                "email": "lilia_gorodinsky_11373@gmail.com"
            },
            {
                "id": "92abcf20d1a6ba19123d0a4e7b50c3f4",
                "name": "Jeffrey Graf",
                "address": "2 Mott street,suite203",
                "email": "jeffrey_graf_10033@gmail.com"
            },
            {
                "id": "ba3af3780eb851ad5d4c2d293892f0d9",
                "name": "Robert Murayama-Greenbaum",
                "address": "15 Wadsworth Ave.",
                "email": "robert_murayama-greenbaum_10021@gmail.com"
            },
            {
                "id": "63498cea47a734cc030f3cecf23f05fb",
                "name": "Nadja Pierre",
                "address": "2202 Grand Concourse",
                "email": "nadja_pierre_10463@gmail.com"
            },
            {
                "id": "bbf5c0a34c6a13b21540c17c7018d488",
                "name": "Florence Golamco",
                "address": "416 37 St",
                "email": "florence_golamco_11219@gmail.com"
            },
            {
                "id": "7e7ed6466c39016925e6b6ee7b3c87a9",
                "name": "Zaric Maja",
                "address": "87-81, 169th Street",
                "email": "zaric_maja_11372@gmail.com"
            },
            {
                "id": "df07b93f22087a8d0f65c42e546f66f6",
                "name": "Reina Eisner",
                "address": "5722 7th ave",
                "email": "reina_eisner_11238@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "6b18e1a849b969bdbc206fe7e842de5c",
                "name": "Hifza Qureshi",
                "address": "1627 Broadway",
                "email": "hifza_qureshi_10032@gmail.com"
            },
            {
                "id": "397265483b8ebcdfd0b69ac4e7aaca0f",
                "name": "Rany Condos",
                "address": "217 Ovington Avenue",
                "email": "rany_condos_11210@gmail.com"
            },
            {
                "id": "ce95a31446f474b688bf7bcbbf35fd85",
                "name": "Toni Aspinall-Daley",
                "address": "1153 58 Street",
                "email": "toni_aspinall-daley_11213@gmail.com"
            },
            {
                "id": "b2742a518aa7802d9a5fa7df047be3d6",
                "name": "Goldie Schwarzbard",
                "address": "63-84 Saunders St",
                "email": "goldie_schwarzbard_11368@gmail.com"
            },
            {
                "id": "bb5d0ead7e1e13213e508577d8aba78c",
                "name": "Marievic Villanueva",
                "address": "1153 58 Street",
                "email": "marievic_villanueva_11213@gmail.com"
            },
            {
                "id": "24188e013fec660b93d4d2387a879c2c",
                "name": "Kishore Ahuja",
                "address": "8801 Parsons Blvd",
                "email": "kishore_ahuja_11374@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "c3db4f8aa69143e1bf6da6bbb2da1d11",
                "name": "SURENDRA SUGRIM",
                "address": "1211 White Plains Rd",
                "email": "surendra_sugrim_10472@gmail.com"
            },
            {
                "id": "96253e3be84a09f78ec3c0ce3f68370d",
                "name": "Hector Becil",
                "address": "33 W. 125th St",
                "email": "hector_becil_10022@gmail.com"
            },
            {
                "id": "e176d3fd38381744e269a4dba8849b09",
                "name": "Katie Carmen",
                "address": "2248 Richmond Road",
                "email": "katie_carmen_10312@gmail.com"
            },
            {
                "id": "78d85fb3b948f19872d1f415291bb40f",
                "name": "Marissa Santos",
                "address": "219-02 Linden Blvd",
                "email": "marissa_santos_11366@gmail.com"
            },
            {
                "id": "bea8be3e894a7183ec9e9e084606f8d2",
                "name": "Alexandra Altchek",
                "address": "160 East 32nd Street #102",
                "email": "alexandra_altchek_10028@gmail.com"
            },
            {
                "id": "8eba7b481c63886debaa34bf1d280633",
                "name": "David Woldenberg",
                "address": "43-20A Roosevelt Avenue",
                "email": "david_woldenberg_11355@gmail.com"
            },
            {
                "id": "5055942a31ea75595d2e104334290397",
                "name": "Luis Ortega",
                "address": "10406 Flatlands Avenue",
                "email": "luis_ortega_11207@gmail.com"
            },
            {
                "id": "a3da8c2479803f015b1e7ff1177723d2",
                "name": "Carmen Cardona",
                "address": "445 Park Avenue",
                "email": "carmen_cardona_11211@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "12e16dc4d7db4f0eb6bdcfc84a80e1de",
                "name": "Shamim Ahmed",
                "address": "1166 Eastern Parkway",
                "email": "shamim_ahmed_11229@gmail.com"
            },
            {
                "id": "5b556ef78f311a6e0349204503ae26ff",
                "name": "Sergio A. Martinez",
                "address": "1641 Bergen Street",
                "email": "sergio_a._martinez_11234@gmail.com"
            },
            {
                "id": "0885f1da5b518bec48eb700dbf79b628",
                "name": "Bienvenido Fajardo",
                "address": "220 A St. Nicholas Avenue",
                "email": "bienvenido_fajardo_11237@gmail.com"
            },
            {
                "id": "23025b1b617375a528cfc43218d5cbeb",
                "name": "Lawrence Herman",
                "address": "170 W.233rd Street",
                "email": "lawrence_herman_10457@gmail.com"
            },
            {
                "id": "236908a1b4005f9a0caf907ee7a2504e",
                "name": "Dang Nguyen",
                "address": "118 Baxter Street",
                "email": "dang_nguyen_10034@gmail.com"
            },
            {
                "id": "79e0fac5c2bbf3176ef632b62b4df027",
                "name": "Yomaris Pena",
                "address": "1203 Avenue J",
                "email": "yomaris_pena_11213@gmail.com"
            },
            {
                "id": "f20ebbd6c0ffe331e885a4dd2cc6420c",
                "name": "Henry Chen",
                "address": "470 Lenox Ave Suite 1F",
                "email": "henry_chen_10033@gmail.com"
            },
            {
                "id": "772f3f811cf6f5b4b8a7ca6c783f1491",
                "name": "Calvin Lee",
                "address": "95-42 Roosevelt Avenue",
                "email": "calvin_lee_11379@gmail.com"
            },
            {
                "id": "f055b35e17533e0eca6b79f08af2b924",
                "name": "Steven J. Goldstein",
                "address": "370 9th Street",
                "email": "steven_j._goldstein_11237@gmail.com"
            },
            {
                "id": "342e33f2a6eefa1287626047351b1bcf",
                "name": "Tosan Oruwariye",
                "address": "12102 Hillside Avenue",
                "email": "tosan_oruwariye_11217@gmail.com"
            },
            {
                "id": "f14ff858ea8cb3a6b45a7be85dd407b1",
                "name": "Richard Steiner",
                "address": "59-17 Junction Blvd",
                "email": "richard_steiner_11379@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "f347960e213cdb53d06cb956c5b7445c",
                "name": "SABINA AWWAL",
                "address": "2091 Nostrand Ave",
                "email": "sabina_awwal_11208@gmail.com"
            },
            {
                "id": "c9dad9833cbb3e0bc539d305a5ac3a1e",
                "name": "Luis Blanco",
                "address": "607 Soundview Ave",
                "email": "luis_blanco_10453@gmail.com"
            },
            {
                "id": "50a773f8f21e3db35a546d46af0b8802",
                "name": "Marlene Rodriguez",
                "address": "4434 Amboy Road",
                "email": "marlene_rodriguez_11356@gmail.com"
            },
            {
                "id": "7b6a8f1558c9a20ca4b7c43872d14402",
                "name": "Amanda Valencia",
                "address": "67 Irving Place, 5th Floor",
                "email": "amanda_valencia_10013@gmail.com"
            },
            {
                "id": "0578edef29f71de5eb600d411233a596",
                "name": "Meenu Gupta",
                "address": "1262 Ocean Parkway",
                "email": "meenu_gupta_11209@gmail.com"
            },
            {
                "id": "829543cf0487686f10dcc388c418b821",
                "name": "Magdalena Cadet",
                "address": "8008 Third Avenue",
                "email": "magdalena_cadet_11236@gmail.com"
            },
            {
                "id": "f42bfb1a0fb4828214324c884b356990",
                "name": "Babubhai Patel",
                "address": "924 49th St.",
                "email": "babubhai_patel_11220@gmail.com"
            },
            {
                "id": "6f830f20fd4532b7d084b85cd81df5e6",
                "name": "Jigar Patel",
                "address": "2 Mott Street Suite 304",
                "email": "jigar_patel_10028@gmail.com"
            },
            {
                "id": "4e8f374d8ef72bdf31049db9afd8ffe2",
                "name": "Samia Tayab",
                "address": "136-30 Maple Ave/ #1A",
                "email": "samia_tayab_11411@gmail.com"
            },
            {
                "id": "4ab4a6eb0b68a201268a7dcebc0db0db",
                "name": "Luis Ortiz",
                "address": "707 West 171st Suite A",
                "email": "luis_ortiz_10034@gmail.com"
            },
            {
                "id": "f76e0f3d4be0dd3e24b04055ece72f6e",
                "name": "Isadore Gutwein",
                "address": "80-37 Broadway",
                "email": "isadore_gutwein_11354@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "08e5c8c9665b2983fe61872a3d7c82aa",
                "name": "CANDIDA CATUCCI",
                "address": "1153 58th Street",
                "email": "candida_catucci_11211@gmail.com"
            },
            {
                "id": "c772a42c9f614c3aedabb4dc768f0e53",
                "name": "Asadur R Miah",
                "address": "1446 Broadway Avenue",
                "email": "asadur_r_miah_11238@gmail.com"
            },
            {
                "id": "8d3105e03fb0a140435620c70bdd38eb",
                "name": "Mario Peichev",
                "address": "1236 FULTON STREET",
                "email": "mario_peichev_11419@gmail.com"
            },
            {
                "id": "6c7a5a55fcd474885e47624528eeec11",
                "name": "Richard Altman",
                "address": "2386 Jerome Avenue",
                "email": "richard_altman_10458@gmail.com"
            },
            {
                "id": "30c5e835cffaca862f8021e64419b4a1",
                "name": "Robert Meltzer",
                "address": "133-60 41st Avenue",
                "email": "robert_meltzer_11516@gmail.com"
            },
            {
                "id": "5e363f3f3f3417c8dde6386793ed9a6e",
                "name": "Paul Krantz",
                "address": "136-20 38th Ave",
                "email": "paul_krantz_11432@gmail.com"
            },
            {
                "id": "b04caaf803ec8b7f6e8a147783b5923b",
                "name": "Shira Kaplovitz",
                "address": "117-06 225th Street 1st Floor",
                "email": "shira_kaplovitz_11372@gmail.com"
            },
            {
                "id": "726b91081ca726439a7664f6870d36e2",
                "name": "Ermany Castillon",
                "address": "241-08 140th Ave",
                "email": "ermany_castillon_11354@gmail.com"
            },
            {
                "id": "8f3195f50838931db5e81a4e7b6c3490",
                "name": "Raphael Novogrodsky",
                "address": "1153 58th Street",
                "email": "raphael_novogrodsky_11211@gmail.com"
            },
            {
                "id": "a880d2f37e51bb0869550e41d8e4274c",
                "name": "Chavannes Thomas",
                "address": "25-52 STEINWAY STREET",
                "email": "chavannes_thomas_11691@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "a00e4a255584fca2a1a71ee8e64230f9",
                "name": "Farzana Flora, PA",
                "address": "230 Beach 102nd St",
                "email": "farzana_flora,_pa_11373@gmail.com"
            },
            {
                "id": "b748a07ac58988aff10ca7f7ae7f7582",
                "name": "Gunwant Singh",
                "address": "3016 Glenwood Rd",
                "email": "gunwant_singh_11212@gmail.com"
            },
            {
                "id": "3ba3a63280a508d02853fcbfdba8d8b5",
                "name": "Arumugan Vasanthi",
                "address": "113-11 Jamaica Ave,",
                "email": "arumugan_vasanthi_11354@gmail.com"
            },
            {
                "id": "d92f560a765e6155702acde07f9a6047",
                "name": "Dahua Zhou",
                "address": "64-15 Fresh Pond Rd",
                "email": "dahua_zhou_11418@gmail.com"
            },
            {
                "id": "837a23f01809d0df1a2971c07788a9e1",
                "name": "Olga Zilberstein",
                "address": "133-A West End Avenue",
                "email": "olga_zilberstein_11215@gmail.com"
            },
            {
                "id": "3fa64364592a14316923b05765fd02f2",
                "name": "Howard Grossman",
                "address": "139-16 91st Avenue",
                "email": "howard_grossman_10453@gmail.com"
            },
            {
                "id": "8bfab2657b62bdb110f7ba8e57118246",
                "name": "Masoud Moarefi",
                "address": "833 58th Street",
                "email": "masoud_moarefi_11224@gmail.com"
            },
            {
                "id": "18bc9fec3ac3b8d710be3033f0d8d5f1",
                "name": "Nadia Duvilaire",
                "address": "40-35 95th Street",
                "email": "nadia_duvilaire_11372@gmail.com"
            },
            {
                "id": "e1cbaa493bde3371f298c3c05c4554d6",
                "name": "Lalitha Reddy",
                "address": "600 West 150th Street",
                "email": "lalitha_reddy_10030@gmail.com"
            },
            {
                "id": "ffe7ef6413fc308abb361a7199981bec",
                "name": "Perminder Dhillon",
                "address": "213-02 Hillside Ave,",
                "email": "perminder_dhillon_11373@gmail.com"
            },
            {
                "id": "c22194eb1552f1b64a236f99b16be975",
                "name": "Muhammad Dogar",
                "address": "245 East 35th Street",
                "email": "muhammad_dogar_10012@gmail.com"
            },
            {
                "id": "b190c11808248070e5bfc8e791bcd22e",
                "name": "Michael Hannan",
                "address": "209 Beach 125st",
                "email": "michael_hannan_11354@gmail.com"
            },
            {
                "id": "d65834b3a9018334db59ed0d2eccd611",
                "name": "Janette Torres",
                "address": "311 Audubon Ave, 2nd Fl",
                "email": "janette_torres_10033@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "3708eae8077217f3d1bd5cd6f138f732",
                "name": "Thomas Chen",
                "address": "8656 105th Street",
                "email": "thomas_chen_11418@gmail.com"
            },
            {
                "id": "8c92b5aa4d50896ee740cc9d18405dde",
                "name": "Mary X. Hu",
                "address": "142-03 60th Ave",
                "email": "mary_x._hu_11372@gmail.com"
            },
            {
                "id": "ed07763c9a94f357bbcb93f4f6e603e3",
                "name": "San Shih",
                "address": "1153 58th Street",
                "email": "san_shih_11211@gmail.com"
            },
            {
                "id": "a039908ce9d3aab4d5964ad98986f9e1",
                "name": "Dalsia Acosta",
                "address": "40-35 95th Street",
                "email": "dalsia_acosta_11372@gmail.com"
            },
            {
                "id": "14065b552012252a9ca16dc6c767e3a4",
                "name": "Karen Weisz",
                "address": "70-31 A 108th",
                "email": "karen_weisz_11367@gmail.com"
            },
            {
                "id": "65b7b18158f9b881dd0c8d332b55161c",
                "name": "Wipanee Phupakdi",
                "address": "98-30 67th av",
                "email": "wipanee_phupakdi_11373@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "6736f350b5956763803f664b70251f74",
                "name": "Maya Golbraykh",
                "address": "11216 Jamaica Ave",
                "email": "maya_golbraykh_11372@gmail.com"
            },
            {
                "id": "3ec9465dd30a285608f06acd6aaccad8",
                "name": "Hector Holson",
                "address": "140 Wadsworth Avenue",
                "email": "hector_holson_10016@gmail.com"
            },
            {
                "id": "65ca56d6cd1b734e5b64121846d5e86b",
                "name": "Fawzia Kazmi",
                "address": "40 Montgomery Street",
                "email": "fawzia_kazmi_10019@gmail.com"
            },
            {
                "id": "a8ba3879d749d8f26386a720f24e655e",
                "name": "Sheila Cain",
                "address": "1335 Ocean Parkway",
                "email": "sheila_cain_11213@gmail.com"
            },
            {
                "id": "10cb7ccaefd5841eaebaac3ef5d9b264",
                "name": "Diego Ponieman",
                "address": "112-03 Queens Blvd",
                "email": "diego_ponieman_11354@gmail.com"
            },
            {
                "id": "401463e7d3b57815173228ff4bb4ecd4",
                "name": "Galina Kletsman",
                "address": "800 manor road suite 4",
                "email": "galina_kletsman_10304@gmail.com"
            },
            {
                "id": "cc9bd4a8df644c3ef85bda59dd57c8c9",
                "name": "Gabor Menczelesz",
                "address": "410 Lakeville Road, Suite 202",
                "email": "gabor_menczelesz_11377@gmail.com"
            },
            {
                "id": "21693720a40c810e33c5095b1727d095",
                "name": "Rui Er Teng",
                "address": "1729 E. 12th Street",
                "email": "rui_er_teng_11213@gmail.com"
            },
            {
                "id": "a8a4c77efdb9b92407a59d46c0ed30ef",
                "name": "Stephen J. Kaiser",
                "address": "58 E. 116th St",
                "email": "stephen_j._kaiser_10028@gmail.com"
            },
            {
                "id": "ba3f93b2cefad7dfabc50228206ed361",
                "name": "Yvette Ortiz",
                "address": "4434 Amboy Road",
                "email": "yvette_ortiz_11356@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "3c8b0d012b34bd7e7c0fccccf4f49b92",
                "name": "Frank Babb",
                "address": "2015 Grand Concourse",
                "email": "frank_babb_10467@gmail.com"
            },
            {
                "id": "c9eeb8e96fe7cd6295a39f4fd8ed6046",
                "name": "Maximo D'Oleo",
                "address": "2310 65th Street, 2nd floor",
                "email": "maximo_d'oleo_11215@gmail.com"
            },
            {
                "id": "eb05a33f1e3b7188e5b7c6fa7ec8f49c",
                "name": "CHARLES HWU",
                "address": "2248 Richmond Road",
                "email": "charles_hwu_10312@gmail.com"
            },
            {
                "id": "9bb887fb1a5926db5c8ae0f49518c320",
                "name": "Jacquelin Belamy",
                "address": "170 W.233Rd Street",
                "email": "jacquelin_belamy_10467@gmail.com"
            },
            {
                "id": "ab84205500f820fa0d07ad95bb835038",
                "name": "Albert A. Benchabbat",
                "address": "1262 Boston Road, suite 2",
                "email": "albert_a._benchabbat_10461@gmail.com"
            },
            {
                "id": "7d224c3c532d417524ffc4e61e84a2a5",
                "name": "Kyi Win Yu",
                "address": "445 Park Avenue",
                "email": "kyi_win_yu_11211@gmail.com"
            },
            {
                "id": "f35c485cd7376aafeab040576b8a2019",
                "name": "Patria Gonzalez",
                "address": "134-21 Maple Ave, Ground floor",
                "email": "patria_gonzalez_11209@gmail.com"
            },
            {
                "id": "b56074697016b0a870694acce9c5a8ed",
                "name": "Alla Mesh",
                "address": "730 58th Street, 1F",
                "email": "alla_mesh_11220@gmail.com"
            },
            {
                "id": "4b0ad329f6063312fc914fc2f89561ed",
                "name": "Subha Atluri",
                "address": "629 West 185th Street",
                "email": "subha_atluri_11372@gmail.com"
            },
            {
                "id": "58b26df97d831ba2de60e927c0116735",
                "name": "Mercedes Blanche",
                "address": "775 57th Street",
                "email": "mercedes_blanche_11219@gmail.com"
            }
        ]
    },
    "Staten Island": {
        "urologist": [
            {
                "id": "3291c386b334af38c92cba1bf9268a9a",
                "name": "Jennifer Becker",
                "address": "219-02 LINDEN BLVD",
                "email": "jennifer_becker_11412@gmail.com"
            },
            {
                "id": "36b0eaeca63907e696d1ba180a24385f",
                "name": "Nikolai LaGoduke",
                "address": "18016 Wexford Ter, Suite CA",
                "email": "nikolai_lagoduke_11372@gmail.com"
            },
            {
                "id": "4f35a4d84e441675ba422bee5ff9f8e9",
                "name": "Rafael Rodriguez",
                "address": "1368 NOSTRAND AVE",
                "email": "rafael_rodriguez_11236@gmail.com"
            },
            {
                "id": "28b7a7f2e28406ce563c13475a1bb8f9",
                "name": "Wilfred Herard",
                "address": "2426 Eastchester Rd, Suite 201",
                "email": "wilfred_herard_10454@gmail.com"
            },
            {
                "id": "03a219b0659a25ccdb4265af6fd12a23",
                "name": "Jing Jing Ao",
                "address": "1153 58 Street",
                "email": "jing_jing_ao_11213@gmail.com"
            },
            {
                "id": "dbc0848ae39a33554acf69db2b75e4c0",
                "name": "Igor Kirzhner",
                "address": "12102 Hillside Avenue",
                "email": "igor_kirzhner_11217@gmail.com"
            },
            {
                "id": "05ff037ba5ec64f2ceadec69c28ed56c",
                "name": "Karen Rigor Tarite",
                "address": "2386 Jerome Avenue",
                "email": "karen_rigor_tarite_10458@gmail.com"
            }
        ],
        "general practitioner": [
            {
                "id": "f489412ab4e7cd876b122e2e230c619f",
                "name": "Alexander Beylinson",
                "address": "15 Wadsworth Ave.",
                "email": "alexander_beylinson_10021@gmail.com"
            },
            {
                "id": "83347ddcf25424532cd4c6c1ca83cd89",
                "name": "Tahira Farooqi Ghaffar",
                "address": "8020 Broadway Suite 1F",
                "email": "tahira_farooqi_ghaffar_11104@gmail.com"
            },
            {
                "id": "6b03b1fb6443065e00ed7c24b830656b",
                "name": "David Chiang",
                "address": "18-12 College Point Blvd",
                "email": "david_chiang_10021@gmail.com"
            },
            {
                "id": "84d47d8f9815abfc28fa9229f507ff53",
                "name": "Florence Golamco",
                "address": "741 New Lots Avenue",
                "email": "florence_golamco_11206@gmail.com"
            },
            {
                "id": "3ab6a28739b2f44208ca85124702be0c",
                "name": "Barbara Medlin",
                "address": "411 West 113TH Street",
                "email": "barbara_medlin_10031@gmail.com"
            },
            {
                "id": "84bbbbb6bba23d8727d39032d0ac65e0",
                "name": "P Milord",
                "address": "180-16 Wexford Terrace, Suite CA",
                "email": "p_milord_11427@gmail.com"
            }
        ],
        "ophthalmologist": [
            {
                "id": "9f4605f79babba9a82c0d23f827468a7",
                "name": "James Laffertey",
                "address": "314 West 14th Street",
                "email": "james_laffertey_11355@gmail.com"
            },
            {
                "id": "3d0f4b9394fc670368a06a0e4edc0ca8",
                "name": "Elisabeth Immanuel-Alexis",
                "address": "3410-3418 Broadway, 2nd floor",
                "email": "elisabeth_immanuel-alexis_10033@gmail.com"
            },
            {
                "id": "a51e426b4d811635549e6d4963d83602",
                "name": "Emeka E. Okeke",
                "address": "43-12 43rd Street",
                "email": "emeka_e._okeke_11223@gmail.com"
            },
            {
                "id": "8ab210491055e4e7493e59b896c987fc",
                "name": "Udele Taylor-Randall",
                "address": "155 W. 19th St",
                "email": "udele_taylor-randall_10024@gmail.com"
            },
            {
                "id": "d125a78dc14a5a090165d9236f46a2f5",
                "name": "Melville Hughes",
                "address": "338 E 30th St",
                "email": "melville_hughes_10013@gmail.com"
            },
            {
                "id": "d1d74c0e7d946b0d4a789e350ff99b9c",
                "name": "Lawrence Hitzeman",
                "address": "833 58th Street",
                "email": "lawrence_hitzeman_11224@gmail.com"
            },
            {
                "id": "7cac108d9b6bf70b69c1f50eecee3b62",
                "name": "Grace Wright",
                "address": "93-15 Roosevelt Avenue",
                "email": "grace_wright_11372@gmail.com"
            },
            {
                "id": "ed5feadb6f2dabdffe382007d025ba5f",
                "name": "Ritu Davis",
                "address": "2015 Grand Concourse",
                "email": "ritu_davis_10467@gmail.com"
            },
            {
                "id": "7312c965ac9ef00c5ae23c200fe64428",
                "name": "Jose Vargas",
                "address": "302 Broadway",
                "email": "jose_vargas_10016@gmail.com"
            },
            {
                "id": "2bc0364637dfdf2dfeaea6146e3b87ea",
                "name": "Ainsley Pennant",
                "address": "213-02 Hillside Ave,",
                "email": "ainsley_pennant_11373@gmail.com"
            },
            {
                "id": "be243c967f42fcacee42759038f5d673",
                "name": "Irene Shir",
                "address": "14 East 4th Street",
                "email": "irene_shir_10033@gmail.com"
            },
            {
                "id": "71af60ec85232965fd8f70512524c133",
                "name": "Jose Goris",
                "address": "2201 Amsterdam Avenue",
                "email": "jose_goris_10001@gmail.com"
            },
            {
                "id": "d3e0b7eccd6ba329b71566fefd2fb31e",
                "name": "Patricia Gregory",
                "address": "139 centre street, #505",
                "email": "patricia_gregory_10028@gmail.com"
            }
        ],
        "dermatologist": [
            {
                "id": "10e5b673f8b7d8ebc802cae2a4f85253",
                "name": "Joseph Marchisella",
                "address": "64-12 Fresh Pond Rd",
                "email": "joseph_marchisella_11422@gmail.com"
            },
            {
                "id": "318a9509676a8f0b1784ef2343ac5e9c",
                "name": "Nataly Larson",
                "address": "911 Park Avenue",
                "email": "nataly_larson_10044@gmail.com"
            },
            {
                "id": "df68ab2fdbf1cc66c0224f52746c71a5",
                "name": "Jing Jing Dong",
                "address": "150-34 Union Turnpike",
                "email": "jing_jing_dong_11422@gmail.com"
            },
            {
                "id": "4f1509c6e37d513fe938d32ec9d9371f",
                "name": "Devbala Ramanathan",
                "address": "136-20 38th Ave",
                "email": "devbala_ramanathan_11432@gmail.com"
            },
            {
                "id": "09e5a3b53c123ccd40997df106394953",
                "name": "Lynn A. Hawkins",
                "address": "136-17 39th Avenue, Flushing NY, 11354, Suite CFC, 4th Floor",
                "email": "lynn_a._hawkins_11374@gmail.com"
            },
            {
                "id": "613a2b22818347173f05b4cc10d4188c",
                "name": "Marlene Saint-Hilaire",
                "address": "314 W. 14th Street",
                "email": "marlene_saint-hilaire_10027@gmail.com"
            },
            {
                "id": "425c647d4ea421c1edb8bd2a22f5a7a8",
                "name": "Xinru Qian",
                "address": "3131 Kings Highway",
                "email": "xinru_qian_11228@gmail.com"
            },
            {
                "id": "829fcdce46b1505ae51c3020cef73cbe",
                "name": "Andres Pereira",
                "address": "730 58th Street, 1F",
                "email": "andres_pereira_11220@gmail.com"
            },
            {
                "id": "94f04838b7d8373e4ec1f91402a077fd",
                "name": "Charity Fancis-Munson",
                "address": "314 West 14th Street",
                "email": "charity_fancis-munson_11355@gmail.com"
            },
            {
                "id": "0d111e98a1dd0330e520cc6582f1274c",
                "name": "Luis Blanco",
                "address": "139 Centre Ave Suite 712",
                "email": "luis_blanco_10007@gmail.com"
            },
            {
                "id": "47db174f1381ca09c1ba58b2d46ff9b9",
                "name": "Venkata Ravi",
                "address": "35 East 35th Street",
                "email": "venkata_ravi_10033@gmail.com"
            }
        ],
        "surgeon": [
            {
                "id": "9030faeb66d759e9ebc5f82abea5db0d",
                "name": "Veronika Romashova",
                "address": "178 EAST 85TH STREET 4TH FLOOR",
                "email": "veronika_romashova_11230@gmail.com"
            },
            {
                "id": "dca2b276591bbe358653e1edd5a53c5e",
                "name": "Erie Agustin",
                "address": "40 Montgomery Street",
                "email": "erie_agustin_10019@gmail.com"
            },
            {
                "id": "e64e43433fe665c81feaba2f8550b400",
                "name": "Susan Fitzmaurice",
                "address": "2119 West 6th Street",
                "email": "susan_fitzmaurice_11230@gmail.com"
            },
            {
                "id": "f3b90fd07fdb7a309b2f1ee6e4793054",
                "name": "Sergio A. Martinez",
                "address": "1262 Ocean Parkway",
                "email": "sergio_a._martinez_11209@gmail.com"
            },
            {
                "id": "6016a7ccbc0bb3efea4d76805cd1e4e0",
                "name": "Jose Quiwa",
                "address": "3016 Glenwood Rd",
                "email": "jose_quiwa_11212@gmail.com"
            },
            {
                "id": "e16f914b670dd8cf91cd1b45b812829d",
                "name": "Arthur Maisto",
                "address": "345 E37th Street Ste 303C",
                "email": "arthur_maisto_10002@gmail.com"
            },
            {
                "id": "7f2c9bc864602af651ad3bbcecce7c16",
                "name": "Gregorio Hidalgo",
                "address": "131-24 Rockaway Blvd",
                "email": "gregorio_hidalgo_11373@gmail.com"
            },
            {
                "id": "98971c5654d1813d5aec6f36bbe40f3a",
                "name": "David Brick",
                "address": "464 West 145th Street",
                "email": "david_brick_10010@gmail.com"
            },
            {
                "id": "7c2e3f6dac2e71ccb96980f93cae916f",
                "name": "Mariyum Shakir",
                "address": "2202 Grand Concourse",
                "email": "mariyum_shakir_10463@gmail.com"
            },
            {
                "id": "1a39eac8bcd4452d4e9c2a57c8e7832b",
                "name": "Jianlin Wu",
                "address": "136-30 Maple Ave/ #1A",
                "email": "jianlin_wu_11411@gmail.com"
            },
            {
                "id": "2509fac71cfff8ae640e047b98743d68",
                "name": "Zhang Jian",
                "address": "2503 Church Ave",
                "email": "zhang_jian_11201@gmail.com"
            }
        ],
        "psychologist": [
            {
                "id": "8738a008789ed0acd6c5cfdb04df4a25",
                "name": "Miguel Tirado",
                "address": "247 Grand St",
                "email": "miguel_tirado_11220@gmail.com"
            },
            {
                "id": "00ad8be3357ad20376e993026b0c94b0",
                "name": "Myo Maw",
                "address": "2083 East 65 Street",
                "email": "myo_maw_11217@gmail.com"
            },
            {
                "id": "8c1dbe6486d10409d3314e113513dc34",
                "name": "Claudia Cooke",
                "address": "1262 Boston Road, suite 2",
                "email": "claudia_cooke_10461@gmail.com"
            },
            {
                "id": "b70bd8a89d1effc49b20dad938709fab",
                "name": "Cynthia Myers",
                "address": "60 W Kingsbridge Road",
                "email": "cynthia_myers_10458@gmail.com"
            },
            {
                "id": "509cefdd558c26b2425a1d1cbe23e2c5",
                "name": "Miksha Patel",
                "address": "833 58th Street",
                "email": "miksha_patel_11224@gmail.com"
            },
            {
                "id": "d9fcda78215566f23f4a0e1dee69e1a4",
                "name": "Allan Plaut",
                "address": "128 Mott Street Suite 302",
                "email": "allan_plaut_10003@gmail.com"
            },
            {
                "id": "150381200142056a8b16f22535983ca8",
                "name": "Alex Wright",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "alex_wright_10013@gmail.com"
            }
        ],
        "infectiologist": [
            {
                "id": "37ee7bbbb130ba7aca472508ac960ecc",
                "name": "Aaron Freilich",
                "address": "739 Knickerbocker Avenue",
                "email": "aaron_freilich_11203@gmail.com"
            },
            {
                "id": "34166613b9be1b8f28d83a175585ba84",
                "name": "Lainie Hurst",
                "address": "2015 Grand Concourse",
                "email": "lainie_hurst_10467@gmail.com"
            },
            {
                "id": "3f89751aeb5061d7c341dd0082959405",
                "name": "Francisco Bautista",
                "address": "5716 Myrtle Avenue",
                "email": "francisco_bautista_11422@gmail.com"
            },
            {
                "id": "986a4ca34a4268e916faea71fce5b99a",
                "name": "Pedro Kourtesis",
                "address": "33 8th Ave, Ground Floor",
                "email": "pedro_kourtesis_11217@gmail.com"
            },
            {
                "id": "b01d7cae171cbeed0903470fe742177b",
                "name": "Giancarlo Guido",
                "address": "3071 Perry Avenue",
                "email": "giancarlo_guido_10453@gmail.com"
            },
            {
                "id": "a00bd1c97d390d68361307126c57204a",
                "name": "ARTHUR DOVE",
                "address": "114-06 Queens Blvd",
                "email": "arthur_dove_11419@gmail.com"
            },
            {
                "id": "ef64359ffca773acba105efc17c3dfc5",
                "name": "Chixin Fang",
                "address": "133-29 41st Rd, 2D",
                "email": "chixin_fang_11692@gmail.com"
            },
            {
                "id": "79c29828f21e1567664cc2542e478441",
                "name": "Igor Kletsman",
                "address": "185 Hall Street",
                "email": "igor_kletsman_11375@gmail.com"
            },
            {
                "id": "33fc064ac1898d82564bd7ac3f7b9cb4",
                "name": "Marcia Nelson",
                "address": "40-04 Bowne St",
                "email": "marcia_nelson_11373@gmail.com"
            },
            {
                "id": "d6ce53208c89e63c87000e250aaf49a1",
                "name": "Ferdousi Khan",
                "address": "1236 FULTON STREET",
                "email": "ferdousi_khan_11419@gmail.com"
            },
            {
                "id": "b055a02d56586fc589a1ab126fb769a6",
                "name": "Michael Ader",
                "address": "87-81 169th St",
                "email": "michael_ader_11042@gmail.com"
            }
        ],
        "gastroenterologist": [
            {
                "id": "8028dc8600b5d283323e96740b3f2114",
                "name": "Meera Boppana",
                "address": "7318 13th Avenue",
                "email": "meera_boppana_11216@gmail.com"
            },
            {
                "id": "7b3eb7658af24a620cfecc5521c21f31",
                "name": "Tahira Ghaffar",
                "address": "443 Linden Blvd",
                "email": "tahira_ghaffar_11210@gmail.com"
            },
            {
                "id": "4965d40ee3a41449e66df1cff3b860da",
                "name": "Ferdausi Hassan",
                "address": "83-45 Dongan Ave",
                "email": "ferdausi_hassan_11418@gmail.com"
            },
            {
                "id": "a9d4294fe09f4db6352f09b5405a9d0e",
                "name": "Iwona Mienko",
                "address": "796 Drew Street",
                "email": "iwona_mienko_11204@gmail.com"
            },
            {
                "id": "29696310976362904e565e7a58ee1c92",
                "name": "Liana Dao",
                "address": "121A West 20th Street",
                "email": "liana_dao_10021@gmail.com"
            },
            {
                "id": "67cc136a447d1220b5b70c27d636bf5f",
                "name": "Frederick Ast",
                "address": "-305 Seguine Avenue",
                "email": "frederick_ast_10304@gmail.com"
            },
            {
                "id": "9421f3c6e6fc2dc045109af7f8dbbf6b",
                "name": "Chaim Wanounou",
                "address": "1150 Park Avenue",
                "email": "chaim_wanounou_10031@gmail.com"
            },
            {
                "id": "067d073637647b1336d1093586c5ec5a",
                "name": "Javid Yadegar",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "javid_yadegar_10013@gmail.com"
            }
        ],
        "rheumatologist": [
            {
                "id": "6356bec587c12dcecbfee4b8c27386ed",
                "name": "Mergie Desir",
                "address": "9425 59th Avenue Suite f7",
                "email": "mergie_desir_11368@gmail.com"
            },
            {
                "id": "9eab4e4c9794df2365f5e426d1cf25fd",
                "name": "David Magier",
                "address": "220 A St. Nicholas Avenue",
                "email": "david_magier_11237@gmail.com"
            },
            {
                "id": "48eeb8b083fa8063be636d5f1ed58356",
                "name": "Ramon Tallaj",
                "address": "600 West 150th Street",
                "email": "ramon_tallaj_10030@gmail.com"
            },
            {
                "id": "b7b62de935cb7a8147fa3ff528c3674c",
                "name": "Wayne Joseph",
                "address": "131-24 Rockaway Blvd",
                "email": "wayne_joseph_11373@gmail.com"
            },
            {
                "id": "04da48b9a26c78b54e43836e2d89efba",
                "name": "Archana Singiri",
                "address": "81 Skillman Street",
                "email": "archana_singiri_11220@gmail.com"
            }
        ],
        "gynecologist": [
            {
                "id": "226c2191611580f13552d08d369d3a56",
                "name": "Karin Kalkstein",
                "address": "328 East 61st Street",
                "email": "karin_kalkstein_10011@gmail.com"
            },
            {
                "id": "eb6d57983c7ccc8859fc21c485887e39",
                "name": "Ida Tetro",
                "address": "88-01 Parson Blvd",
                "email": "ida_tetro_11402@gmail.com"
            },
            {
                "id": "df66c34af6e9da1a99d3edd836edd275",
                "name": "Xiaoxia Zhang",
                "address": "142-10B Roosevelt Ave",
                "email": "xiaoxia_zhang_11374@gmail.com"
            },
            {
                "id": "a88d2a43350a11d65e7a796355e297c2",
                "name": "Daniel Boccardo",
                "address": "3410-3418 Broadway, 2nd floor",
                "email": "daniel_boccardo_10033@gmail.com"
            },
            {
                "id": "78c998eee283c86ff7e40542b1a2a9b0",
                "name": "Rabeya Chowdhury",
                "address": "445 Park Avenue",
                "email": "rabeya_chowdhury_11211@gmail.com"
            },
            {
                "id": "30c51ecf3dc8838d74ad4a02162845b3",
                "name": "Haiyan Lu",
                "address": "3016 Glenwood Rd",
                "email": "haiyan_lu_11212@gmail.com"
            },
            {
                "id": "f434d7e2b001c252f72a1adc61e3d3e8",
                "name": "Nemaan Ghuman",
                "address": "2742 brighton 8th street",
                "email": "nemaan_ghuman_11236@gmail.com"
            },
            {
                "id": "785b030444951b019003d3b7fffa9b8a",
                "name": "Syed Ahmad",
                "address": "410 Lakeville Road",
                "email": "syed_ahmad_11373@gmail.com"
            },
            {
                "id": "c49fc06aa3bc90fbeb1405aef7e73beb",
                "name": "San San Wynn",
                "address": "1627 Broadway",
                "email": "san_san_wynn_10032@gmail.com"
            },
            {
                "id": "38b2c14a020ad24a51613086019fc375",
                "name": "Renae Bright",
                "address": "10406 Flatlands Avenue",
                "email": "renae_bright_11207@gmail.com"
            },
            {
                "id": "0f0a1ca16d35f40879b8764e69569bf2",
                "name": "Muhammad S. Alam",
                "address": "89-18 134 street",
                "email": "muhammad_s._alam_11420@gmail.com"
            },
            {
                "id": "a4392654f413e8f7b19a8c14fd931ff0",
                "name": "Sherill Purcell",
                "address": "2311 Adam Clayton Powell Jr.Boulevard",
                "email": "sherill_purcell_10031@gmail.com"
            }
        ],
        "pulmonologist": [
            {
                "id": "b496ef2be245958babbf287c8323040e",
                "name": "Rojasudha Vatti",
                "address": "29-28 41st Avenue",
                "email": "rojasudha_vatti_11355@gmail.com"
            },
            {
                "id": "ed5fd95d2fb10efd093e9b59399981e6",
                "name": "Thangamuthu Arumugam",
                "address": "115 Central Park West",
                "email": "thangamuthu_arumugam_10011@gmail.com"
            },
            {
                "id": "9806073120fd25ebef2487abfdb12a5e",
                "name": "Xian Min Li",
                "address": "2 Mott Street, Suite 304",
                "email": "xian_min_li_10022@gmail.com"
            },
            {
                "id": "54ebbe9140dbcaaadf7e624aab98435b",
                "name": "Jean-Robert Boursiquot",
                "address": "450 Clarkson Ave",
                "email": "jean-robert_boursiquot_11203@gmail.com"
            },
            {
                "id": "e1bff1455ce3641f142c89fdb63521da",
                "name": "Grace Dworan",
                "address": "2 West 86th Street Suite 4",
                "email": "grace_dworan_10013@gmail.com"
            }
        ],
        "endocrinologist": [
            {
                "id": "04bd506f0de282f12099a32722cbdc53",
                "name": "MOHAMMAD AKHTAR",
                "address": "2494 Williamsbridge Rd.",
                "email": "mohammad_akhtar_10453@gmail.com"
            },
            {
                "id": "452f3a98581800301781a7b8ce66ab2e",
                "name": "Mitchell Adler",
                "address": "2 Mott Street Suite 304",
                "email": "mitchell_adler_10028@gmail.com"
            },
            {
                "id": "44c15d01da98ab05dd129a332e835352",
                "name": "Dana Shani",
                "address": "2960 Grand Concourse L1",
                "email": "dana_shani_10451@gmail.com"
            },
            {
                "id": "702da2410c19437bcf6a501ff00d347f",
                "name": "Leonid Chernov",
                "address": "67 Irving Place, 5th Floor",
                "email": "leonid_chernov_10013@gmail.com"
            },
            {
                "id": "4d98f5537f15ff9e25146e1a17fc7e80",
                "name": "Teresita Go",
                "address": "1070 Southern Blvd",
                "email": "teresita_go_10458@gmail.com"
            },
            {
                "id": "70c2f8872d9191a4d7f72ac426174fd0",
                "name": "Seth Kurtz",
                "address": "540 East New York Avenue",
                "email": "seth_kurtz_11219@gmail.com"
            },
            {
                "id": "79ffedff1c0f5674ad5658cf0a34137c",
                "name": "Uzoma Okorrie",
                "address": "2760 Amboy Road",
                "email": "uzoma_okorrie_11418@gmail.com"
            },
            {
                "id": "5583792d01b5c1407b2fdc0df8697fdd",
                "name": "Mihir Basu",
                "address": "1835 Bay Ridge Pkway",
                "email": "mihir_basu_11234@gmail.com"
            },
            {
                "id": "7ac3e0146fea55798d14fd3db720e361",
                "name": "Kenneth Nyer",
                "address": "2960 Grand Concourse L1",
                "email": "kenneth_nyer_10451@gmail.com"
            }
        ],
        "pediatrician": [
            {
                "id": "56f678e84a082ea6b80b19390812f5da",
                "name": "Eric Behrens",
                "address": "87-08 Justice Ave, Ste CS",
                "email": "eric_behrens_11104@gmail.com"
            },
            {
                "id": "ff6638f80b682c6e8bee8a8a107aac08",
                "name": "Swarn Gupta",
                "address": "111-14 76th Ave",
                "email": "swarn_gupta_11373@gmail.com"
            },
            {
                "id": "96c6b2ac6a7bb7458669b894cce43dd9",
                "name": "Baruch Kassover",
                "address": "2015 Grand Concourse",
                "email": "baruch_kassover_10467@gmail.com"
            },
            {
                "id": "2ee7391edbd308cb0e2f85386a48efc4",
                "name": "Jingling Tang",
                "address": "4335 Hylan Blvd",
                "email": "jingling_tang_10312@gmail.com"
            },
            {
                "id": "8813f87c11c88b16f3ec059d3c7987ba",
                "name": "Habib Nazarian",
                "address": "4335 Hylan Blvd",
                "email": "habib_nazarian_10312@gmail.com"
            },
            {
                "id": "34825ad51bb108c17226ee09ecbd484b",
                "name": "Scott Hartman",
                "address": "178 EAST 85TH STREET 4TH FLOOR",
                "email": "scott_hartman_11230@gmail.com"
            },
            {
                "id": "54e495fcc0286aa9e3f1d9e96fe6eabb",
                "name": "Victor Bulnes",
                "address": "823 60th Street, 11 Floor",
                "email": "victor_bulnes_11235@gmail.com"
            },
            {
                "id": "5c693d0975c59101c16d37badcf536b2",
                "name": "Amy Bloomgarden",
                "address": "185 Canal Street",
                "email": "amy_bloomgarden_10033@gmail.com"
            },
            {
                "id": "c00f9cff292bc033afb123c0ec01ff1d",
                "name": "Charles Gordon",
                "address": "9920 4 Avenue, Suite 206",
                "email": "charles_gordon_11214@gmail.com"
            },
            {
                "id": "ae5ab75fe52cda9284a34f7a0bc4d4bc",
                "name": "Dalia Yadegar",
                "address": "34-40 Fulton Street",
                "email": "dalia_yadegar_11230@gmail.com"
            },
            {
                "id": "55783d7b1a143f9e3035a183e6dbec54",
                "name": "Syed M. Hussaini",
                "address": "4250 Broadway Suite 1A",
                "email": "syed_m._hussaini_10024@gmail.com"
            },
            {
                "id": "7bf64182e6d4e14764d75cc8c0509bbf",
                "name": "Mohamad Erfani",
                "address": "97-77 Queens Blvd. Suite 900,",
                "email": "mohamad_erfani_11432@gmail.com"
            },
            {
                "id": "8c42ddf41c865348fc5d5cfcafbca195",
                "name": "Romina Tollerutti",
                "address": "1870 Richmond Road,",
                "email": "romina_tollerutti_10306@gmail.com"
            }
        ],
        "hematologist": [
            {
                "id": "175882616d4b3ada9654435bec48cc26",
                "name": "Marco A. Benitez",
                "address": "380 2nd Avenue, Suite 1002",
                "email": "marco_a._benitez_10028@gmail.com"
            },
            {
                "id": "686506990871faaff3fa3cce0f839ba2",
                "name": "Emerth L. Coburn",
                "address": "172-27 Highland Ave, Suite 1 B",
                "email": "emerth_l._coburn_11429@gmail.com"
            },
            {
                "id": "c3db0cd8163315ebf12315bbd356015b",
                "name": "Kathleen McCabe",
                "address": "833 58th Street",
                "email": "kathleen_mccabe_11224@gmail.com"
            },
            {
                "id": "af83168f0ea34e4b34162d4e5404bcce",
                "name": "Jose Serruya",
                "address": "445 Park Avenue",
                "email": "jose_serruya_11211@gmail.com"
            },
            {
                "id": "2be6a30dd6aa6c9200d6e785b4bfd287",
                "name": "Katherine Zeng",
                "address": "1407 46th Street",
                "email": "katherine_zeng_11213@gmail.com"
            },
            {
                "id": "1809895980dcbe0ce4ddf4abb77b592c",
                "name": "Eleanor Lai",
                "address": "1627 Broadway",
                "email": "eleanor_lai_10032@gmail.com"
            },
            {
                "id": "8e316f8c394b8bbf005c0ee722467657",
                "name": "Alex Wei",
                "address": "2378 Ralph Ave",
                "email": "alex_wei_11203@gmail.com"
            },
            {
                "id": "bc0c974346fc8d9cc092f81db3b805b8",
                "name": "Kalpana Master",
                "address": "37-57 91st Street",
                "email": "kalpana_master_11354@gmail.com"
            },
            {
                "id": "192b2e0f1a4a2a4dfa29e3c65dd590fa",
                "name": "Abdul Malik",
                "address": "133-47 Sanford Avenue, Suite 1H",
                "email": "abdul_malik_11354@gmail.com"
            },
            {
                "id": "8c751edc30d79a70f4a57334f19cfcab",
                "name": "Jennifer Figueroa",
                "address": "41 Mott Street, Chinatown",
                "email": "jennifer_figueroa_10031@gmail.com"
            },
            {
                "id": "bb2b22fda11e92d4a91836eedbe8d692",
                "name": "Stephan Simons",
                "address": "1931 Williamsbridge Road",
                "email": "stephan_simons_10453@gmail.com"
            },
            {
                "id": "f362e2b75e2e5ac8ca6d47e2b17ba3a3",
                "name": "Francis Hayden",
                "address": "-",
                "email": "francis_hayden_11205@gmail.com"
            }
        ],
        "toxicologist": [
            {
                "id": "775b0328357293fb4bd4ec291e952704",
                "name": "Marco A. Garcia",
                "address": "3125 TIBBETT AVENUE",
                "email": "marco_a._garcia_10459@gmail.com"
            },
            {
                "id": "8d7af06269a7701760a8725e76a62750",
                "name": "Mariana Marcu",
                "address": "814 East 156 Street",
                "email": "mariana_marcu_10467@gmail.com"
            },
            {
                "id": "d46343f2ba0223dfac5c200edf3b619b",
                "name": "Robert Mayes",
                "address": "1166 Eastern Parkway",
                "email": "robert_mayes_11229@gmail.com"
            },
            {
                "id": "757b02bab9f53fc278aae560a15d19fb",
                "name": "Sushama Mody",
                "address": "112-03 Queens Blvd, Suite 207",
                "email": "sushama_mody_11368@gmail.com"
            },
            {
                "id": "dd6a3cdf5b7c1395f6c9c48281d651aa",
                "name": "Yaacov Weiss",
                "address": "370 9th Street",
                "email": "yaacov_weiss_11237@gmail.com"
            },
            {
                "id": "9363388d0015fae8c428eaf4cad152d9",
                "name": "Michael Raffinan",
                "address": "2379 65th Street",
                "email": "michael_raffinan_11203@gmail.com"
            },
            {
                "id": "37e90fe201cb70800cb83fe98287fd96",
                "name": "Terry Blackett-Bonnett",
                "address": "-9613 Flatlands Avenue",
                "email": "terry_blackett-bonnett_11207@gmail.com"
            },
            {
                "id": "1ed3487f6bd49e35c03500b0481d2708",
                "name": "Jenny Liu",
                "address": "137 10 FRANKLIN AVENUE",
                "email": "jenny_liu_11375@gmail.com"
            },
            {
                "id": "e7948f61ab52fe333bc9d7eda1c06b2a",
                "name": "Khader Rawand",
                "address": "1664 East 14th Street, Suite 501",
                "email": "khader_rawand_11209@gmail.com"
            }
        ],
        "cardiologist": [
            {
                "id": "5fb7cb12089e4157068e2f62031744ee",
                "name": "Paul Mantia",
                "address": "68 bayard street",
                "email": "paul_mantia_10028@gmail.com"
            },
            {
                "id": "eda333452053b570209d0ef5956af986",
                "name": "Gregorio Hidalgo",
                "address": "29-28 41st Avenue",
                "email": "gregorio_hidalgo_11355@gmail.com"
            },
            {
                "id": "df28dc13f3875edf2705768a50c509f1",
                "name": "Sonia Vinas",
                "address": "136-21 Roosevelt Ave, #205",
                "email": "sonia_vinas_11422@gmail.com"
            }
        ],
        "oncologist": [
            {
                "id": "dc20a1eee1b3c094923e4d856883a53f",
                "name": "Naum Meyerovich",
                "address": "1153 58 Street",
                "email": "naum_meyerovich_11213@gmail.com"
            },
            {
                "id": "f674103d0877276f1b3c35e02e19578c",
                "name": "Eloisa Acosta",
                "address": "8330 Vietor Avenue, Suite P-1",
                "email": "eloisa_acosta_11356@gmail.com"
            },
            {
                "id": "fb6ccf03232e2565e551d6fc36eb3583",
                "name": "David Hurwitz",
                "address": "739 Knickerbocker Avenue",
                "email": "david_hurwitz_11203@gmail.com"
            },
            {
                "id": "de4c3627980ff85bf3a173c78100890c",
                "name": "Allen M. Kaufman",
                "address": "4819 14th Avenue",
                "email": "allen_m._kaufman_11221@gmail.com"
            },
            {
                "id": "e3b97394087847892b6367e1c029d451",
                "name": "Yelena Lindenbaum",
                "address": "1627 Broadway",
                "email": "yelena_lindenbaum_10032@gmail.com"
            },
            {
                "id": "5b6d19ea43ff15559183b0a2c0494fb5",
                "name": "Steve T. Ayanruoh",
                "address": "3747-77th St",
                "email": "steve_t._ayanruoh_11373@gmail.com"
            },
            {
                "id": "55c1cd1d00fcfffe61966f16ebf5b42c",
                "name": "Rafael Guillen",
                "address": "60-14 Roosevelt Ave",
                "email": "rafael_guillen_11354@gmail.com"
            },
            {
                "id": "a8da488ef6529dca52f062d613721630",
                "name": "Chana Lieber",
                "address": "375 East Fordham Road",
                "email": "chana_lieber_10453@gmail.com"
            }
        ],
        "diabetologist": [
            {
                "id": "cb5ca2c447bc1ae225b6df218a0734af",
                "name": "Marlene Pitamber",
                "address": "133-47 Sanford Avenue, Suite 1H",
                "email": "marlene_pitamber_11354@gmail.com"
            },
            {
                "id": "b7acf60aadc0bdeb96fe891f46b8df1c",
                "name": "Sandra Robinson",
                "address": "1911 Avenue L",
                "email": "sandra_robinson_11211@gmail.com"
            },
            {
                "id": "3cc5b6b55c360a406d330a3aad4d4156",
                "name": "Stephen Hofmeister",
                "address": "See Note-",
                "email": "stephen_hofmeister_10034@gmail.com"
            },
            {
                "id": "74b76ada9229d32807526cfbaa6b5536",
                "name": "Irina Fuchs",
                "address": "17 Hamilton Place, 2nd Floor",
                "email": "irina_fuchs_10032@gmail.com"
            },
            {
                "id": "c724229d7cbe597799443a589e1152c3",
                "name": "Maha Awikeh",
                "address": "1421 Carroll Street",
                "email": "maha_awikeh_11220@gmail.com"
            },
            {
                "id": "9ea40712109bb8dd5912ae04d67fa469",
                "name": "Andy Hu",
                "address": "911 Park Ave",
                "email": "andy_hu_10002@gmail.com"
            },
            {
                "id": "151fee05b088ff5962d2a0f00586b7da",
                "name": "Maja Zeric",
                "address": "123 Layfayette Street, 6th Floor",
                "email": "maja_zeric_10013@gmail.com"
            },
            {
                "id": "b3dfd900ea0c9dc3268b11152dcfd335",
                "name": "Daniel Reich",
                "address": "839 58th Street, 2nd Floor",
                "email": "daniel_reich_11204@gmail.com"
            },
            {
                "id": "8ff640eb6600123a3b7114942c843de7",
                "name": "Philip Owusu-Ansah",
                "address": "471 Hart Street",
                "email": "philip_owusu-ansah_11235@gmail.com"
            }
        ],
        "nephrologist": [
            {
                "id": "8ac3ec3e71964c5f27cccd7fa1b5fb26",
                "name": "David Steiner",
                "address": "131-24 Rockaway Blvd",
                "email": "david_steiner_11373@gmail.com"
            },
            {
                "id": "7275640c6a4129b4bc1c47f5da208709",
                "name": "Naveen Pesala",
                "address": "450 clarkson Ave",
                "email": "naveen_pesala_11218@gmail.com"
            },
            {
                "id": "3659993b4c595521f76576bb5cb362ea",
                "name": "Chenna Reddy",
                "address": "450 Clarkson Ave",
                "email": "chenna_reddy_11203@gmail.com"
            },
            {
                "id": "20e83aefb9e6eb386da46f375ce56094",
                "name": "LUIS GUERRERO",
                "address": "63 Catherine St.",
                "email": "luis_guerrero_10032@gmail.com"
            }
        ],
        "allergologist": [
            {
                "id": "461d5a3fdb35085aad15e32abcb03324",
                "name": "Ching Sum Leung",
                "address": "856 Dekalb Avenue",
                "email": "ching_sum_leung_11211@gmail.com"
            },
            {
                "id": "3008c1e6a1aaec75fcb0218b58747d84",
                "name": "Jose de Leon",
                "address": "87-81, 169th Street",
                "email": "jose_de_leon_11372@gmail.com"
            },
            {
                "id": "d2b7b3e7e1f857468225acae14af7a9f",
                "name": "Simcha Ben-David",
                "address": "3410-18 Broadway, 2nd floor",
                "email": "simcha_ben-david_10013@gmail.com"
            },
            {
                "id": "87afb21d7f192734a1ba8a44629a5ff6",
                "name": "Laeeq Ahmad",
                "address": "121-02 Hillside Avenue",
                "email": "laeeq_ahmad_11203@gmail.com"
            },
            {
                "id": "16b6f73939df5f60d6f1ff40d38a8f73",
                "name": "Angela Davydov",
                "address": "108 E 96th St",
                "email": "angela_davydov_10021@gmail.com"
            },
            {
                "id": "b48fddf990aa4c232595d4fcd248541e",
                "name": "Ludmila Sedlackova",
                "address": "314 West 14th Street",
                "email": "ludmila_sedlackova_11355@gmail.com"
            }
        ]
    }
}