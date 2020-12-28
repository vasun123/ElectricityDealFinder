import csv
print("Hello!")
print("I can help you find the best electricity plans in Texas. First, however, I will need some information.")
print("When prompted, please type something and press enter.")
print("What is your name? My name is ElectroBot!")
print()
name = input(">>> My name is ")
print()
print("Nice to meet you, " + name + "!")

print("First, I will need your zip code. This is so I can determine which plans cater to your area.")
print()

canPass = False
while canPass == False:
  zipC = input(">>> My zip code is ")
  print()
  # Finds out zip code
  with open("uszips.csv", encoding='utf-8') as fo:
    reader1 = csv.DictReader(fo)
    area = ""
    for i in reader1:
      State = i["state_name"]
      zipp = i["zip"]
      if State == "Texas" and str(zipp) == str(zipC):
        area = i["city"]
    if area == "":
      preferredArea = "0"

  # Sees if its Oncor
  with open("oncor.csv", encoding='utf-8') as fo:
    reader1 = csv.reader(fo)
    for i in reader1:
      Area = i[0]
      if area == Area:
        preferredArea = "1"

  # Sees if its Texas New Mexico Power Company
  with open("tnmp.csv", encoding='utf-8') as fo:
    reader1 = csv.reader(fo)
    for i in reader1:
      Area = i[0]
      if area == Area:
        preferredArea = "2"
  
  # Sees if its AEP Central
  with open("aepc.csv", encoding='utf-8') as fo:
    reader1 = csv.reader(fo)
    for i in reader1:
      Area = i[0]
      if area == Area:
        preferredArea = "3"

  # Sees if its AEP North
  with open("aepn.csv", encoding='utf-8') as fo:
    reader1 = csv.reader(fo)
    for i in reader1:
      Area = i[0]
      if area == Area:
        preferredArea = "4"

  # Sees if its CenterPoint
  with open("ceh.csv", encoding='utf-8') as fo:
    reader1 = csv.reader(fo)
    for i in reader1:
      Area = i[0]
      if area == Area:
        preferredArea = "5"

  if preferredArea.lower() == "1":
    preferredArea = 'ONCOR ELECTRIC DELIVERY COMPANY'
    canPass = True
  elif preferredArea.lower() == "2":
    preferredArea = 'TEXAS-NEW MEXICO POWER COMPANY'
    canPass = True
  elif preferredArea.lower() == "3":
    preferredArea = 'AEP TEXAS CENTRAL COMPANY'
    canPass = True
  elif preferredArea.lower() == "4":
    preferredArea = 'AEP TEXAS NORTH COMPANY'
    canPass = True
  elif preferredArea.lower() == "5":
    preferredArea = 'CENTERPOINT ENERGY HOUSTON ELECTRIC LLC'
    canPass = True
  else:
    print("Sorry, I didn't catch that. Could you please try again? Make sure that your zip code is in the state of Texas.")
    print()





print("Great! Now I just need the type of plan you are going for. Please just type the first letter of your plan type.")
print("Fixed rate, variable rate, or indexed rate?")
print()
print("Fixed (F): Price per kWh doesn't change during the length of contract.")
print("Variable (V): Price per kWh changes based on decisions made by TDU company.")
print("Indexed (I): Price per kWh changes based on a formula that is caluclated by TDU company.")
print()

canPass = False
while canPass == False:
  preferredRate = input(">>> The first letter of my preferred Plan Type is ")
  print()
  if preferredRate.lower() == "f":
    preferredRate = "Fixed"
    canPass = True
  elif preferredRate.lower() == "v":
    preferredRate = "Variable"
    canPass = True
  elif preferredRate.lower() == "i":
    preferredRate = "Indexed"
    canPass = True
  else:
    print("Sorry, I didn't catch that. Could you please try again? Make sure to type the plan type and make sure that it is spelled correctly.")
    print()

print("All right! Finally, I need the estimated number of kilowatt hours (kwh) used per month.")
print("Do you estimate to use 500, 1000, or 2000 kwh per month? Please just type one of these numbers.")
print()
canPass = False
while canPass == False:
  preferredUsage = input(">>> The number of kwh I plan to use per month is ")
  print()
  if preferredUsage.lower() == "500":
    preferredUsage = "500"
    canPass = True
  elif preferredUsage.lower() == "1000":
    preferredUsage = "1000"
    canPass = True
  elif preferredUsage.lower() == "2000":
    preferredUsage = "2000"
    canPass = True
  else:
    print("Sorry, I didn't catch that. Could you please try again? Make sure that you typed in either 500, 1000, or 2000.")
    print()



print("Awesome! Here are the top three deals I would recommend based on how much kwh you plan to use per month. Since your zip code is " + zipC + ", your TDU company (the company that delivers energy to you) is " + preferredArea.lower().title() + ".")
print()
print()

def checkFunction(reader, condition, knownConditionList):
  for i in reader:
    target = i[condition]
    if target not in knownConditionList:
      print(target)
      print(i["[TduCompanyName]"])

with open("power-to-choose-offers.csv", encoding='utf-8') as f:
  reader = csv.DictReader(f)

  # Key: TDU area, value: all info
  deals = []
  for i in reader:
    TduCompanyName = i["[TduCompanyName]"]
    RateType = i["[RateType]"]
    if TduCompanyName == preferredArea and RateType == preferredRate:
      p = []
      p.append(TduCompanyName)
      p.append(i)
      deals.append(p)


def getKWH500(deal):
  return deal[1]["[kwh500]"]
    
def getKWH1000(deal):
  return deal[1]["[kwh1000]"]

def getKWH2000(deal):
  return deal[1]["[kwh2000]"]

if preferredUsage == "500":
  deals.sort(key=getKWH500)
elif preferredUsage == "1000":
  deals.sort(key=getKWH1000)
elif preferredUsage == "2000":
  deals.sort(key=getKWH2000)

DealList = []
ProductList = []
for deal in deals:
  if len(DealList) < 3:
    canAdd = False
    if deal[1]["[Product]"] not in ProductList:
      canAdd = True
    else:
      canAdd = False
    if canAdd == True:
      DealList.append(deal)
      ProductList.append(deal[1]["[Product]"])
# INCLUDE A WAY TO SORT

#print(deals)

print("Best deal: ")
for Deal in DealList:
  print("REP COMPANY: " + Deal[1]["[RepCompany]"].lower().title())
  print()
  print("CONTRACT LENGTH: " + Deal[1]["[TermValue]"].lower().title())
  print()
  print("PRODUCT: " + Deal[1]["[Product]"])
  print()
  if preferredUsage == "500":
    print("PRICE PER 500 KILOWATT HOURS: " + str(float(Deal[1]["[kwh500]"]) * 100)[0:4] + " Cents")
  elif preferredUsage == "1000":
    print("PRICE PER 1000 KILOWATT HOURS: " + str(float(Deal[1]["[kwh1000]"]) * 100)[0:4] + " Cents")
  elif preferredUsage == "2000":
    print("PRICE PER 2000 KILOWATT HOURS: " + str((float(Deal[1]["[kwh2000]"]) * 100))[0:4] + " Cents")
  print()
  print("CANCEL FEE: " + Deal[1]["[CancelFee]"])
  print()
  print("WEBSITE: " + Deal[1]["[Website]"])
  print()
  print("PHONE NUMBER: " + Deal[1]["[EnrollPhone]"])
  print()
  print()

# Previous code

'''
print("First, I will need the electricity provider. This is also known as a Texas Energy Utility Provider (TDU).")
print("Please take a look at the following information and please type in the number of your preferred TDU company.")
print()
print("(1) Oncor: Dallas-Fort Worth metro, Midland-Odessa, Round Rock, Waco")
print("(2) Texas New Mexico Power Company: Pecos, Glen Rose, League City, Angleton")
print("(3) AEP Central: Corpus Christi, McAllen, Victoria, Laredo, Harlingen")
print("(4) AEP North: Abilene, San Angelo, Vernon")
print("(5) CenterPoint Energy: Houston metro area, Beaumont, Seguin")
print()

canPass = False
while canPass == False:
  preferredArea = input(">>> My TDU Company number is ")
  print()
  if preferredArea.lower() == "1":
    preferredArea = 'ONCOR ELECTRIC DELIVERY COMPANY'
    canPass = True
  elif preferredArea.lower() == "2":
    preferredArea = 'TEXAS-NEW MEXICO POWER COMPANY'
    canPass = True
  elif preferredArea.lower() == "3":
    preferredArea = 'AEP TEXAS CENTRAL COMPANY'
    canPass = True
  elif preferredArea.lower() == "4":
    preferredArea = 'AEP TEXAS NORTH COMPANY'
    canPass = True
  elif preferredArea.lower() == "5":
    preferredArea = 'CENTERPOINT ENERGY HOUSTON ELECTRIC LLC'
    canPass = True
  else:
    print("Sorry, I didn't catch that. Could you please try again? Make sure to type the entire name of the TDU company and make sure that it is spelled correctly.")
    print()
'''

'''
dealList = deals[0:5]
DealList = []
for Deal in dealList:
  if len(DealList) >= 5:
    break
  for deal in deals:
    if deal[1]["[kwh1000]"] < Deal[1]["[kwh1000]"] and deal not in DealList:
      DealList.append(deal)
'''