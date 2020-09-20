import random
import time
from collections import Counter

import argparse



class DieGame:
    """
        Encapsulates a dice game.
        @param die_num: number of dice in game
    """
    def __init__(self, die_num=6):
        self.active_dice = die_num


    def play(self):
        """
            Rolls dice until the game is over.
        """
        final_score = 0
        while self.active_dice > 0:
            final_score += self.roll()
            
        return final_score
            
    def roll(self):
        """
            Performs a single dice roll.
            @return Score of the roll
        """
        dice = [random.randint(1, 6) for x in range(self.active_dice)]
        c = Counter(dice)
        
        if c[3] > 0:
            self.active_dice -= c[3]
            return 0
        else:
            self.active_dice -= 1
            return min(c)


def run_simulations(sims, dies):
    """
        Runs the dice game a certain amount of times and prints
        count of each game and number of times each score was reached.
        @param sims number of times to run game
        @param dies number of dies to run per game
    """
    
    print("Number of simulations was {} using {} dice.".format(sims, dies))
    
    game_scores = list()
    for i in range(sims):
        die_game = DieGame(dies)
        score = die_game.play()
        game_scores.append(score)
    
    c = Counter(game_scores)
    for score, num in sorted(c.items(), key=lambda item: item[0]):
        print("Total {} occurs {:.4f} occurred {} times.".format(score, num/float(sims), num))


if __name__ == "__main__":
 
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--simulations', type=int, default=10000, help="Number of sims to run.")
    parser.add_argument("-d", "--dies", type=int, default=6, help="Number of dice to use.")
    args = parser.parse_args()
    
    start_time = time.time()
    run_simulations(args.simulations, args.dies)
    end_time = time.time()
    
    print("Total simulation took {:.2f} seconds.".format(end_time-start_time))
    
    