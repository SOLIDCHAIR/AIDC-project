from pyedhrec import EDHRec
import random
#set up pyedhrec
edhrec = EDHRec()
#get name of commander we need to find
print("enter the name of your commander")
commander = input()
counter = 0
#create lists
creatures = []
instants = []
sorceries = []
artifacts = []
enchantments = []
lands = []
#get color identity to find basic lands after all other cards have been found
details = edhrec.get_card_details(commander)
color_identity = details['color_identity']
#isolate top card types and put into respective list
top_cards = edhrec.get_top_cards(commander)
while True:
    if (counter) >= len(top_cards['Top Cards']) - 1: 
        counter = 0
        break
    else :
        card = edhrec.get_card_details(top_cards['Top Cards'][counter]['name'])
        if card['type'].find("Creature") != -1:
            creatures.append(top_cards['Top Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Instant") != -1:
            instants.append(top_cards['Top Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Sorcery") != -1:
            sorceries.append(top_cards['Top Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Artifact") != -1:
            artifacts.append(top_cards['Top Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Enchantment") != -1:
            enchantments.append(top_cards['Top Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Land") != -1:
            lands.append(top_cards['Top Cards'][counter]['name'])
            counter = counter + 1
        else :
            counter = counter + 1
#isolate high synergy cards and put into respective list
high_cards = edhrec.get_high_synergy_cards(commander)
while True:
    if (counter) >= len(high_cards['High Synergy Cards']) - 1: 
        counter = 0
        break
    else :
        card = edhrec.get_card_details(high_cards['High Synergy Cards'][counter]['name'])
        if card['type'].find("Creature") != -1:
            creatures.append(high_cards['High Synergy Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Instant") != -1:
            instants.append(high_cards['High Synergy Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Sorcery") != -1:
            sorceries.append(high_cards['High Synergy Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Artifact") != -1:
            artifacts.append(high_cards['High Synergy Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Enchantment") != -1:
            enchantments.append(high_cards['High Synergy Cards'][counter]['name'])
            counter = counter + 1
        elif card['type'].find("Land") != -1:
            lands.append(high_cards['High Synergy Cards'][counter]['name'])
            counter = counter + 1
#Get cards of each type
top_creatures = edhrec.get_top_creatures(commander)
top_instants = edhrec.get_top_instants(commander)
top_sorceries = edhrec.get_top_sorceries(commander)
top_enchantments = edhrec.get_top_enchantments(commander)
top_artifacts = edhrec.get_top_artifacts(commander)
top_mana_artifacts = edhrec.get_top_mana_artifacts(commander)
top_battles = edhrec.get_top_battles(commander)
top_planeswalkers = edhrec.get_top_planeswalkers(commander)
top_utility_lands = edhrec.get_top_utility_lands(commander)
top_lands = edhrec.get_top_lands(commander)
#put all creatures into creature list
while True:
    if (counter) >= len(top_creatures['Creatures']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        creatures.append(top_creatures['Creatures'][counter]['name'])
#put all instants into instants list
while True:
    if (counter) >= len(top_instants['Instants']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        instants.append(top_instants['Instants'][counter]['name'])
#put all sorceries into sorceries list
while True:
    if (counter) >= len(top_sorceries['Sorceries']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        sorceries.append(top_sorceries['Sorceries'][counter]['name'])
#put all ultility artifacts into artifact list
while True:
    if (counter) >= len(top_artifacts['Utility Artifacts']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        artifacts.append(top_artifacts['Utility Artifacts'][counter]['name'])
#put all mana artifacts into artifact list
while True:
    if (counter) >= len(top_mana_artifacts['Mana Artifacts']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        artifacts.append(top_mana_artifacts['Mana Artifacts'][counter]['name'])
#put all enchantments into enchantment list
while True:
    if (counter) >= len(top_enchantments['Enchantments']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        enchantments.append(top_enchantments['Enchantments'][counter]['name'])
#put all ulitity lands into lands list
while True:
    if (counter) >= len(top_utility_lands['Utility Lands']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        lands.append(top_utility_lands['Utility Lands'][counter]['name'])
#put all lands into lands list
while True:
    if (counter) >= len(top_lands['Lands']) - 1: 
        counter = 0
        break
    else :
        counter = counter + 1
        lands.append(top_lands['Lands'][counter]['name'])
#look for cards
#create a list for all the cards to go into
print("enter # of cards you already have")
cards_owned = int(input())
deck = []
#add cards to deck and remove duplicates from original card lists 
while True:
    if counter >= cards_owned:
        counter = 0
        break
    else :
        print("enter the name of your card")
        userin = input()
        deck.append(userin)
        if userin in creatures :
            creatures.remove(userin)
        elif userin in instants :
            instants.remove(userin)
        elif userin in sorceries :
            sorceries.remove(userin)
        elif userin in artifacts :
            artifacts.remove(userin)
        elif userin in enchantments :
            enchantments.remove(userin)
        elif userin in lands :
            lands.remove(userin)
        counter = counter + 1
cards_to_find = 99 - cards_owned
#get inputs for each card type
#get input for creature
while True:
    print("input number of creatures to find, limit:", len(creatures), "you have ", cards_to_find, " cards remaining")
    find_num = int(input())
    if ((find_num <= len(creatures)) & ((cards_to_find - find_num) > 0)):
        cards_to_find = cards_to_find - find_num
        break
    else:
        print("not a valid input")
while True:
    if counter >= find_num :
        counter = 0
        break
    elif (((len(creatures) -1) > 0)):
        ran_num = random.randrange(0, (len(creatures) - 1))
        deck.append(creatures[ran_num])
        del creatures[ran_num]
        counter = counter + 1
    else :
        deck.append(creatures[0])
        del creatures[0]
        counter = counter + 1
#get input for instant
while True:
    print("input number of instants to find, lmit:", len(instants), "you have ", cards_to_find, " cards remaining")
    find_num = int(input())
    if ((find_num <= len(instants)) & (cards_to_find - find_num > 0)):
        cards_to_find = cards_to_find - find_num
        break
while True:
    if counter >= find_num :
        counter = 0
        break
    elif (((len(instants) -1) > 0)):
        ran_num = random.randrange(0, (len(instants) - 1))
        deck.append(instants[ran_num])
        del instants[ran_num]
        counter = counter + 1
    else :
        deck.append(instants[0])
        del instants[0]
        counter = counter + 1
#get input for sorceries
while True:
    print("input number of sorceries to find, lmit:", len(sorceries), "you have ", cards_to_find, " cards remaining")
    find_num = int(input())
    if ((find_num <= len(sorceries)) & (cards_to_find - find_num > 0)):
        cards_to_find = cards_to_find - find_num
        break
while True:
    if counter >= find_num :
        counter = 0
        break
    elif (((len(sorceries) -1) > 0)):
        ran_num = random.randrange(0, (len(sorceries) - 1))
        deck.append(sorceries[ran_num])
        del sorceries[ran_num]
        counter = counter + 1
    else :
        deck.append(sorceries[0])
        del sorceries[0]
        counter = counter + 1
#get input for artifacts
while True:
    print("input number of artifacts to find, lmit:", len(artifacts), "you have ", cards_to_find, " cards remaining")
    find_num = int(input())
    if ((find_num <= len(artifacts)) & (cards_to_find - find_num > 0)):
        cards_to_find = cards_to_find - find_num
        break
while True:
    if counter >= find_num :
        counter = 0
        break
    elif (((len(artifacts) -1) > 0)):
        ran_num = random.randrange(0, (len(artifacts) - 1))
        deck.append(artifacts[ran_num])
        del artifacts[ran_num]
        counter = counter + 1
    else :
        deck.append(artifacts[0])
        del artifacts[0]
        counter = counter + 1
#get input for enchantments
while True:
    print("input number of enchantments to find, lmit:", len(enchantments), "you have ", cards_to_find, " cards remaining")
    find_num = int(input())
    if ((find_num <= len(enchantments)) & (cards_to_find - find_num > 0)):
        cards_to_find = cards_to_find - find_num
        break
while True:
    if counter >= find_num :
        counter = 0
        break
    elif (((len(enchantments) -1) > 0)):
        ran_num = random.randrange(0, (len(enchantments) - 1))
        deck.append(enchantments[ran_num])
        del enchantments[ran_num]
        counter = counter + 1
    else :
        deck.append(enchantments[0])
        del enchantments[0]
        counter = counter + 1 
#get input for lands
while True:
    print("input number of lands to find, lmit:", len(lands), "you have ", cards_to_find, " cards remaining")
    find_num = int(input())
    if ((find_num <= len(lands)) & (cards_to_find - find_num >= 0)):
        cards_to_find = cards_to_find - find_num
        break
while True:
    if counter >= find_num :
        counter = 0
        break
    elif (((len(lands) -1) > 0)):
        ran_num = random.randrange(0, (len(lands) - 1))
        deck.append(lands[ran_num])
        del lands[ran_num]
        counter = counter + 1
    else :
        deck.append(lands[0])
        del lands[0]
        counter = counter + 1
#use remaining deck slots for basic lands
while True:
    print(counter, cards_to_find)
    if counter >= cards_to_find :
        break
    if (('G' in color_identity) & (counter < cards_to_find)) :
        deck.append("Forest")
        counter = counter + 1
    if (('W' in color_identity) & (counter < cards_to_find)) :
        deck.append("Plains")
        counter = counter + 1
    if (('U' in color_identity) & (counter < cards_to_find)) :
        deck.append("Island")
        counter = counter + 1
    if (('B' in color_identity) & (counter < cards_to_find)) :
        deck.append("Swamp")
        counter = counter + 1
    if (('R' in color_identity) & (counter < cards_to_find)) :
        deck.append("Mountain")
        counter = counter + 1
    if ((color_identity == []) & (counter < cards_to_find)):
        deck.append("Waste")
        counter = counter + 1

print("finished decklist:")
for card in deck:
    print(card)