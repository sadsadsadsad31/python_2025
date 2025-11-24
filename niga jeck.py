import random, sys
def main():
    print('''Правила: \n
    Постарайтесь набрать как можно больше очков, близких к 21. \n
    Короли, дамы, валеты приносят по 10 очков. \n 
    Тузы приносят от 1 до 11 очков. \n
    Карты от 2 до 10 приносят свой номинал. \n
    (H)it , чтобы прекратить брать карты. \n
    (S)tand , удвоить ставку. \n
    (D)adell , удвоить ставку при первой игре. \n
    В случае ничьи, ставк возвращается игроку. \n
    Диллер не берет карты на 17 очках. \n
    Удачной игры. \n
    ''')
    money = 5000
    while True:
        if money <= 0:
            print("Недостаточно средств , пополни счет и возвращайся в игру.")
            sys.exit()
        print(f"Ваш счет: {money}")
        bet = getBet(money)
        deck = getDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]
        print(f"Ставка: {bet}")
        while True:
            displayHands(playerHand, dealerHand, False)
            print()
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, (money-bet))
            if move =="D":
                additionalBet = getBet(min(bet,(money-bet)))
                bet += additionalBet
                print(f"Ставка увеличина на {additionalBet}")
            if move in ("HD"):
                newCard = deck.pop()
                rank, suit = newCard
                print(f"Вы вытащили карту - {rank} = {suit}")


def getBet(maxBet):
    pass
def displayHands(playerHand,dealerHand, showDealerHand):
    pass
def getHandValue(cards)
    pass
def displayCardds(cards):
    pass









