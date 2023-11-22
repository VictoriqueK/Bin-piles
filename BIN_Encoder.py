# Important stuff

import binascii # Used for HEX reading
import csv      # Used for writing down numbers in .txt file
import struct   # Used for HEX float processing
import os       # Used for folder
from collections import defaultdict

# ---------------

# Prompt

if os.path.exists(os.path.dirname(os.path.abspath(__file__)) + 'Encoded .bin files') == 0:
    os.makedirs(os.path.dirname(os.path.abspath(__file__)) + 'Encoded .bin files')

print('Availble commands:')
print('')
print('1. Weapons.csv')
print('2. Ammo.csv')
print('3. Equipment.csv')
print("4. Enemies.csv")
print("5. Augments.csv")
print('')
print('0. Exit the app')
print('')
SelectedCSV = int(input('Select the .csv you want to encode: '))

if SelectedCSV == 0:
    exit()
elif SelectedCSV > 6 or SelectedCSV < 0:
    raise ValueError('The selected number is invalid. Try again.')

# Main code
	
if SelectedCSV == 1 or SelectedCSV == 6:
    CSVFile = os.path.dirname(os.path.abspath(__file__)) + 'Decoded .bin files' + 'weapons.csv'
    BinaryEncoded = open(os.path.dirname(os.path.abspath(__file__)) + 'Encoded .bin files' + 'weapons.bin', "wb")
elif SelectedCSV == 2:
    CSVFile = os.path.dirname(os.path.abspath(__file__)) + 'Decoded .bin files' + 'ammo.csv'
    BinaryEncoded = open(os.path.dirname(os.path.abspath(__file__)) + 'Encoded .bin files' + 'ammo.bin', "wb")
elif SelectedCSV == 3:
    CSVFile = os.path.dirname(os.path.abspath(__file__)) + 'Decoded .bin files' + 'equipment.csv'
    BinaryEncoded = open(os.path.dirname(os.path.abspath(__file__)) + 'Encoded .bin files' + 'equipment.bin', "wb")
elif SelectedCSV == 4:
    CSVFile = os.path.dirname(os.path.abspath(__file__)) + 'Decoded .bin files' + 'enemies.csv'
    BinaryEncoded = open(os.path.dirname(os.path.abspath(__file__)) + 'Encoded .bin files' + 'enemies.bin', "wb")
elif SelectedCSV == 5:
    CSVFile = os.path.dirname(os.path.abspath(__file__)) + 'Decoded .bin files' + 'augments.csv'
    BinaryEncoded = open(os.path.dirname(os.path.abspath(__file__)) + 'Encoded .bin files' + 'augments.bin', "wb")

## DO NOT CHANGE
## -------------
ByteOrder1 = [4, 4, 4, 2, 2, 4, 4, 4, 8, 8, 8, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 4, 2, 4, 2, 8, 8, 4, 8, 8, 8, 2, 4, 4, 4, 2, 2, 4, 4, 4, 4, 4, 4, 2, 8, 8, 4, 4, 4, 8, 4, 4, 4, 2, 4]
ByteOrder2 = [4, 2, 8, 2, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 8, 4, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4, 4]
ByteOrder3 = [4, 4, 4, 2, 4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2, 4]
ByteOrder4 = [8, 'text', 4, 8, 8, 2, 8, 8, 8, 8, 8, 8, 8, 4, 4, 4, 8]
ByteOrder4ES = [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
ByteOrder5 = [4, 2, 2, 2, 8, 4, 8, 4]
ByteOrderA = [4, 2, 2, 2, 2, 2, 2, 2, 2, 8, 4, 8, 4]
IntOrFloat1 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
IntOrFloat2 = [1]
IntOrFloat3 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
IntOrFloat4 = [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1]
IntOrFloat4ES = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
IntOrFloat5 = [0, 1]
EnemyNameSize = [20, 18, 18, 16, 18, 20, 38, 38, 12, 22, 28, 20, 32, 26, 16, 24, 22, 22]
EnemyNameOrder = 0
EnemyGrades = [4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 2, 2, 6, 2, 2, 2, 2, 4]
EnemyGradeOrder = 0
EnemyGradeOrder1 = 0
EnemyGradeOrderES = 0
EnemyName = ['00085368616D626C6572','00075374616C6B6572','000753706974746572','000652756E6E6572','0007426C6F61746572','0008536869656C646572','00115A6F6D6264726F69642053657276616E74','00115A6F6D6264726F696420536F6C64696572','0004576F726D','000950756B6520576F726D','000C526567757267697461746F72','00084E6563726F736973','000E4E6563726F73697320537061776E','000B5A6F6D626965204D656368','00065769636B6572','000A44657661737461746F72','00094C6F61646572626F74', '00094D657263656E617279']
# 0 - int;
# 1 - float
IntOrFloatES = 0
ByteOrderES = ByteOrder4ES
if SelectedCSV == 1 or SelectedCSV == 6:
    ByteOrder = ByteOrder1
    IntOrFloat = IntOrFloat1
elif SelectedCSV == 2:
    ByteOrder = ByteOrder2
    IntOrFloat = IntOrFloat2
elif SelectedCSV == 3:
    ByteOrder = ByteOrder3
    IntOrFloat = IntOrFloat3
elif SelectedCSV == 4:
    ByteOrder = ByteOrder4
    ByteOrderES = ByteOrder4ES
    IntOrFloat = IntOrFloat4
    IntOrFloatES = IntOrFloat4ES
elif SelectedCSV == 5:
    ByteOrder = ByteOrder5
    IntOrFloat = IntOrFloat5
Order = 0
IOFOrder = 0
Numbers = []
RowCleaner = 0
RowsConverted = 0
EncryptMode = 0
EncryptModeReset = 0
HEXString = 0
NormalString = 0
ArmorSlotCount = 5
ArmorCurrent = 0
ArmorBIN = 0
AugmentCounter = 0
EncodedCSVFiles = 0
## -------------

# Reads stuff and cleans empty rows

columns = defaultdict(list)

with open(CSVFile) as Decodedfile:
    Reader = csv.reader(Decodedfile)
    for row in Reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)
Numbers = columns[1]
while RowCleaner < len(Numbers):
    if Numbers[RowCleaner] == '':
        Numbers.pop(RowCleaner)
        RowCleaner = RowCleaner + 1
    else:
        RowCleaner = RowCleaner + 1

RowCleaner = 0
while RowCleaner < len(Numbers):
    if Numbers[RowCleaner] == '':
        Numbers.pop(RowCleaner)
        RowCleaner = RowCleaner + 1
    else:
        RowCleaner = RowCleaner + 1
        
# ----------------------------------
# Fun stuff begins

while RowsConverted < len(Numbers):
    if EnemyGradeOrderES == EnemyGrades[EnemyGradeOrder1]:
        EnemyGradeOrderES=0
        EnemyGradeOrder1=EnemyGradeOrder1+1
        EncryptMode=0
    if IOFOrder >= len(IntOrFloat) and EncryptMode==0:
        IOFOrder = 0
    if SelectedCSV == 4:
        if IOFOrder >= len(IntOrFloatES) and EncryptMode==1:
            IOFOrder = 0
        if EncryptModeReset == 1:
            IOFOrder = 0
            EncryptModeReset = 0
    if AugmentCounter >= 144:
        EncryptMode = 2
    if Order<len(ByteOrder)-2 and ByteOrder[Order]!=8 and str(ByteOrder[Order])!='text' and EncryptMode==0:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrder[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif Order<len(ByteOrder)-2 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and EncryptMode==0:
        NormalString = Numbers[RowsConverted]
        if IntOrFloat[IOFOrder] == 0:
            NormalString = int(Numbers[RowsConverted])
            HEXString = NormalString.to_bytes(ByteOrder[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1:
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif Order==len(ByteOrder)-2 and ByteOrder[Order]!=8 and str(ByteOrder[Order])!='text' and EncryptMode==0:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrder[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        Order=0
        if SelectedCSV == 4:
            EncryptMode=1
            EncryptModeReset=1
        if SelectedCSV == 5:
            AugmentCounter = AugmentCounter + 1
        RowsConverted=RowsConverted+1
    elif Order==len(ByteOrder)-2 and ByteOrder[Order]==8 and str(ByteOrder[Order])!='text' and EncryptMode==0:
        NormalString = Numbers[RowsConverted]
        if IntOrFloat[IOFOrder] == 0 and CSVFile != 2:
            NormalString = int(Numbers[RowsConverted])
            HEXString = NormalString.to_bytes(ByteOrder[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1 or CSVFile == 2:
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        if SelectedCSV == 4:
            EncryptMode=1
            EncryptModeReset = 1
        if SelectedCSV == 5:
            AugmentCounter = AugmentCounter + 1
        BinaryEncoded.write(HEXString)
        Order=0
        RowsConverted=RowsConverted+1
    elif Order<len(ByteOrder)-2 and str(ByteOrder[Order])=='text' and EncryptMode == 0:
        NormalString = EnemyName[EnemyNameOrder]
        HEXString = bytes.fromhex(NormalString)
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted = RowsConverted+1
        EnemyNameOrder = EnemyNameOrder+1
    elif Order<len(ByteOrderES)-2 and ByteOrderES[Order]!=8 and str(ByteOrderES[Order])!='text' and EncryptMode==1:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrderES[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif Order<len(ByteOrderES)-2 and ByteOrderES[Order]==8 and str(ByteOrderES[Order])!='text' and EncryptMode==1:
        NormalString = Numbers[RowsConverted]
        if IntOrFloatES[IOFOrder] == 0:
            NormalString = int(Numbers[RowsConverted])
            HEXString = NormalString.to_bytes(ByteOrderES[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloatES[IOFOrder] == 1:
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif Order==len(ByteOrderES)-2 and ByteOrderES[Order]!=8 and str(ByteOrderES[Order])!='text' and EncryptMode==1:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrderES[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        Order=0
        RowsConverted=RowsConverted+1
    elif Order==len(ByteOrderES)-2 and ByteOrderES[Order]==8 and str(ByteOrderES[Order])!='text' and EncryptMode==1:
        NormalString = Numbers[RowsConverted]
        if IntOrFloatES[IOFOrder] == 0 and CSVFile != 2:
            NormalString = int(Numbers[RowsConverted])
            HEXString = NormalString.to_bytes(ByteOrderES[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloatES[IOFOrder] == 1 or CSVFile == 2:
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        BinaryEncoded.write(HEXString)
        if EncryptMode == 1:
            if EnemyGradeOrderES < EnemyGrades[EnemyGradeOrder1]:
                EnemyGradeOrderES=EnemyGradeOrderES+1
        Order=0
        RowsConverted=RowsConverted+1
    elif (Order<len(ByteOrderA)-2 and (Order == 0 or Order == 1 or Order >=7)) and ByteOrderA[Order]!=8 and str(ByteOrderA[Order])!='text' and EncryptMode==2:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrderA[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        if Order == 1:
            ArmorBIN = int(Numbers[RowsConverted])
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif (Order>=2 and Order<=6) and ByteOrderA[Order]!=8 and str(ByteOrderA[Order])!='text' and EncryptMode==2:
        while ArmorCurrent < ArmorSlotCount:
            if ArmorCurrent < ArmorBIN:
                NormalString = int(Numbers[RowsConverted])
                HEXString = NormalString.to_bytes(int(ByteOrderA[Order]/2), 'big')
                BinaryEncoded.write(HEXString)
                Order=Order+1
                RowsConverted=RowsConverted+1
            else:
                Order=Order+1
                RowsConverted=RowsConverted+1
            ArmorCurrent = ArmorCurrent + 1
    elif Order<len(ByteOrderA)-2 and ByteOrderA[Order]==8 and str(ByteOrderA[Order])!='text' and EncryptMode==2:
        NormalString = Numbers[RowsConverted]
        if IntOrFloat[IOFOrder] == 0:
            NormalString = int(Numbers[RowsConverted])
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = NormalString.to_bytes(ByteOrderA[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1:
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        BinaryEncoded.write(HEXString)
        Order=Order+1
        RowsConverted=RowsConverted+1
    elif Order==len(ByteOrderA)-2 and ByteOrderA[Order]!=8 and str(ByteOrderA[Order])!='text' and EncryptMode==2:
        NormalString = int(Numbers[RowsConverted])
        HEXString = NormalString.to_bytes(int(ByteOrderA[Order]/2), 'big')
        BinaryEncoded.write(HEXString)
        Order=0
        IOFOrder = 0
        RowsConverted=RowsConverted+1
        ArmorCurrent = 0
    elif Order==len(ByteOrderA)-2 and ByteOrderA[Order]==8 and str(ByteOrderA[Order])!='text' and EncryptMode==2:
        NormalString = Numbers[RowsConverted]
        if IntOrFloat[IOFOrder] == 0 and CSVFile != 2:
            NormalString = int(Numbers[RowsConverted])
            HEXString = NormalString.to_bytes(ByteOrderA[Order]-4, 'big')
            IOFOrder = IOFOrder + 1
        elif IntOrFloat[IOFOrder] == 1 or CSVFile == 2:
            HEXString = binascii.hexlify(struct.pack('>f', float(NormalString)))
            HEX2String = str(HEXString)
            HEX2String = HEX2String[2:len(HEX2String)-1]
            HEXString = bytes.fromhex(HEX2String)
            IOFOrder = IOFOrder + 1
        ArmorCurrent = 0
        BinaryEncoded.write(HEXString)
        Order=0
        IOFOrder = 0
        RowsConverted=RowsConverted+1
##if SelectedCSV == 5:
##    AugUnknown = bytes.fromhex(AugmentUnknown)
##    BinaryEncoded.write(AugUnknown)
BinaryEncoded.close()

