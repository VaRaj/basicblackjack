#based on https://www.youtube.com/watch?v=Tsof_J1S8QU

import random

cards = [
'2','3','4','5','6','7','8','9','10','J','Q','K','A',
'2','3','4','5','6','7','8','9','10','J','Q','K','A',
'2','3','4','5','6','7','8','9','10','J','Q','K','A',
'2','3','4','5','6','7','8','9','10','J','Q','K','A',
]

def card_sum(lst):
    sum = 0
    for elm in lst:
        try:
            sum = sum + int (elm)
        except:
            if(elm == '?'):
                sum1 = 0
            else:
                sum = sum + 10
    return str(sum)

random.shuffle(cards)

dealer = []
player = []

dealer.append(cards.pop())
player.append(cards.pop())
dealer.append(cards.pop())
player.append(cards.pop())
hidden_dealer = dealer[:]
hidden_dealer[0] = '?'
print ("Your hand:",player, {card_sum(player)}, "\nDealer's hand:",hidden_dealer,
{card_sum(hidden_dealer) + '++'})
inp = 'hit'
while(int(card_sum(player)) < 22 and inp == 'hit'):
     print('stay or hit?')
     inp = input().lower()
     if(inp == 'hit'):
         player.append(cards.pop())
         print ("Your hand:",player, {card_sum(player)},
         "\nDealer's hand:",hidden_dealer,{card_sum(hidden_dealer) + '++'})

if(int(card_sum(player)) > 21):
    print('Dealer wins! Dealer had ', dealer, {card_sum(dealer)}, ' and you had ',
    player, {card_sum(player)})
else:
    while(int(card_sum(dealer)) <= int(card_sum(player))): #change this
        dealer.append(cards.pop())

    if((int(card_sum(dealer)) > int(card_sum(player)) and int(card_sum(dealer))<=21)):
        print('Dealer wins! Dealer had ', dealer, {card_sum(dealer)}, ' and you had ',
        player, {card_sum(player)})
    else:
        print('Player wins! Dealer had ', dealer, {card_sum(dealer)}, ' and you had ',
        player, {card_sum(player)})
#Further improvements:
#ace can be 1 or 10
#add splitting
#add GUI
#extra feature such as if user on 10 loss streak tilt the odds a bit
