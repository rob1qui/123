######################################################
# PLEASE CHANGE FOLLOWING CONFIGS ####################
Twitch_Channel          = 'Sandro4kaa'

Trans_Username          = 'Translato4kaa'
Trans_OAUTH             = 'oauth:o1i7doki12rvin77kuc89nk0k71z56'

#######################################################
# OPTIONAL CONFIGS ####################################
Trans_TextColor         = 'SpringGreen'
# Blue, Coral, DodgerBlue, SpringGreen, YellowGreen, Green, OrangeRed, Red, GoldenRod, HotPink, CadetBlue, SeaGreen, Chocolate, BlueViolet, and Firebrick

lang_TransToHome        = 'ru'
lang_HomeToOther        = ['']

Show_ByName             = True
Show_ByLang             = True

Ignore_Lang             = ['ru', 'sr', 'ja', 'bg', 'be', 'ky', 'kk', 'mn']
Ignore_Users            = ['Nightbot', 'BikuBikuTest', 'Kryabot', 'Moobot', 'Wizebot']
Ignore_Line             = ['http', 'BikuBikuTest', '888', '８８８', 'blobDance', 'catJAM', 'blobHYPERS', '57Funtov', 'SandraALOL', 'SandraBroweyes', 'SandraCherryLook', 'SandraGood', 'SandraJAM', 'SandraNice', 'SandraNotLikeThis', 'SandraPog', 'SandraPuk', 'SandraTasty', 'SandraWink', 'SandraWutFace', 'SandraZzz', 'ScamTrain', 'BlobWave', 'ClapHD2', 'CrabDance', 'hypeE', 'pepeDS', 'pepeJAM', 'PUGPLS', 'pugPls2', 'pugRave', 'Sussy', 'VIBE', 'WeSmart' ]
Delete_Words            = ['saatanNooBow', 'BikuBikuTest']

# Any emvironment, set it to `True`, then text will be read by TTS voice!
# TTS_In:User Input Text, TTS_Out:Bot Output Text
TTS_In                  = False
TTS_Out                 = False
TTS_Kind                = "gTTS" # You can choice "CeVIO" if you want to use CeVIO as TTS.
# CeVIO_Cast            = "さとうささら" # When you are using CeVIO, you must set voice cast name.

# if you make TTS for only few lang, please add langID in the list
# for example, ['ja'] means Japanese only, ['ko','en'] means Korean and English are TTS!
ReadOnlyTheseLang       = []

# Select the translate engine ('deepl' or 'google')
Translator              = 'deepl'

# Use Google Apps Script for tlanslating
# e.g.) GAS_URL         = 'https://script.google.com/macros/s/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx/exec'
GAS_URL                 = ''

# Enter the suffix of the Google Translate URL you normally use.
# Example: translate.google.co.jp -> 'co.jp'
#          translate.google.com   -> 'com'
GoogleTranslate_suffix  = 'co.jp'

# If you meet any bugs, You can check some error message using Debug mode (Debug = True)
Debug                   = False
