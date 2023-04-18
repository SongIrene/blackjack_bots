import random

class Bot:
    def get_decision(self, dealer_up_card, hand, dealer_prev_hand):
        score = 0
        ace_count = 0
        for card in hand:
            if card.rank == 1:
                score += 10
                ace_count += 1
            elif card.rank >= 11:
                score += 10
            else:
                score += card.rank
        for i in range(ace_count):
            if score>21:
                score-=10
        if score > 1:
            return "hit"
