import numpy as np
import pandas as pd

class CreateDice:
    '''
    PURPOSE: Creates a dice. Initializes using faces listed in a numpy array.
    
    METHODS:
    - .change_weights(face2change, newWeight)
    - .roll_dice(rolls=1)
    - .show_current_state()
    '''
    
    def __init__(self, diefaces):
        '''
        PURPOSE: CreateDie class initializer. Throws error if input is not a numpy array 
        or the die does not have all different faces.
        
        INPUTS:
        diefaces - numpy array of list of die faces desired
        
        OUTPUTS:
        None
        
        Note: Instantiates die class as a pd.DataFrame
        '''
        # create default weights of 1
        weights = np.ones(len(diefaces))
        
        if type(diefaces) != np.ndarray:
            raise TypeError("Not a numpy array")
            
        if len(np.unique(diefaces)) != len(diefaces):
            raise ValueError("Need all unique values")
        
        # private attribute -> data frame of die faces as index and current weights of each die face
        self._createdDie = pd.DataFrame(weights, columns = ["weights"], index = diefaces)
        
    def change_weights(self, face2change, newWeight):
        '''
        PURPOSE: Changes the weight of a certain die face
        
        INPUTS:
        face2change - a matching face of instantiated die
                    - throws error if this input does not match any of the faces of the die
        newWeight - int or float
                  - desired new weight for the die face being changed
                  - throws error if new weight is not int or float
        
        OUTPUT:
        None
        
        Note: This method will change the instantiated die dateframe.
        '''
        
        
        if (not any(face2change == self._createdDie.index)): # checks if dice face to change is in existing array of die faces
            raise IndexError("Die face to change not in existing die faces.")
        
        try:
            t_newWeight = float(newWeight) # tries to change weight to float
            # find index of dice face, then change corresponding weight in weight array
            self._createdDie.weights[self._createdDie.index == face2change] = t_newWeight
        except:
            return "New weight is not a number."
        
    def roll_dice(self, rolls = 1):
        '''
        PURPOSE: Rolls die the inputted amount of times. Defaults to 1 roll.
        
        INPUT: 
        rolls - int, desired number of rolls for die
        
        OUTPUT:
        list - list of roll results
        
        Note: weights of each die face is taken into consideration when rolling.
        '''
        # create probability array so the array of weights sums to 1 -> for use with np.random.choice function below
        prob_array = self._createdDie.weights / sum(self._createdDie.weights)
        # np.random.choice(array of die faces, # of rolls to do, probability array)
        # rolls the die the specified number of times, returns a list
        return np.random.choice(self._createdDie.index, rolls, p = prob_array).tolist()
    
    def show_current_state(self):
        '''
        PURPOSE: Shows current state of die by returning privately created die
        
        INPUT:
        None
        
        OUTPUT:
        pd.DataFrame - dateframe of current die
                     - index -> die faces
                     - columns -> weights
        '''
        return self._createdDie
                

        
class GamePlay:
    '''
    PURPOSE: Plays / rolls a list of dice. Initializes using a list of die class dice
    
    METHODS:
    - .play_dice(numrolls)
    - .show_results(size="wide")
    '''
    
    def __init__(self, listofdice):
        '''
        PURPOSE: GamePlay class initializer. Throws error if objects in inputted list are not die class objects 
                 or if the dice in the list have different faces.
        
        INPUT: 
        listofdice - list, list of die class dice
                   - dice in list need to have the same faces
        
        OUTPUT:
        None
        '''
        self.listofdice = listofdice
        
        # all() -> returns true if everything in list is true, else returns false
        # if not all true, ie if at least one is false, raise error
        # purpose: checks to make sure all dice in dice list are dice objects from CreateDice class
        if not all(isinstance(die, CreateDice) for die in self.listofdice):
            raise TypeError("Not a dice in list")
        
        # because all the dice need to have the same faces, it's arbitrary to pick the first one of the list
        # any dice needs to equal any other dice
        for die in self.listofdice:
            if (all(die.show_current_state().index != self.listofdice[0].show_current_state().index)):
                raise ValueError("All dice need the same faces")
    
    def play_dice(self, numrolls):
        '''
        PURPOSE: Rolls the dice in the list of dice the inputted amount of times. Stores results in a pd.DataFrame.
        
        INPUT:
        numrolls - int, number of rolls desired
        
        OUTPUT:
        None
        
        Note: Results of rolls are stored in a dataframe. Index -> rolls, columns -> each die in dice list
        '''
        self.numrolls = numrolls
        self.results = []
        
        # for each die in initilized list of dice
        # append the results of the number of rolls specified in this method
        for die in self.listofdice:
            self.results.append(die.roll_dice(numrolls))
        
        self.dicecolumns = [n for n in range(len(self.results))] # dice column names -> index of dice in list of dice
        self.resultsT = [list(i) for i in zip(*self.results)] # transposed the results list for data frame constructor
        self.diceindex = ["Roll #"+str(m) for m in range(1, len(self.resultsT)+1)] # list of index names
            
        # final data frame construction
        self._resultspd = pd.DataFrame(self.resultsT, index = self.diceindex, columns = self.dicecolumns)
        self._resultspd.index.name = "Rolls"
        
    def show_results(self, size = "wide"):
        '''
        PURPOSE: Shows the results of the rolls in a pd.DataFrame. Can be shown as a wide or narrow dataframe.
        
        INPUT:
        size - string, 2 options: "wide", "narrow"
             - defaults to "wide"
             - throws error if not one of the two options
             
        OUTPUT:
        pd.DataFrame - dataframe of the results of the rolls
                     - returns private results dataframe from .play_dice() method
        '''
        self.size = size
            
        try: #tries to convert input to string
            t_size = str(self.size)
        except:
            return "Narrow or wide only"
        
        # if string conversion is successful
        # if input is not equal to narrow or wide, throw error
        if (t_size.lower() != "narrow") & (t_size.lower() != "wide") :
            raise ValueError("Narrow or wide only")
            #raise TypeError("Narrow or wide data frame only")
        
        if (t_size.lower() == "narrow"):
            return pd.DataFrame(self._resultspd.stack(), columns = ["Results"])
        else:
            return self._resultspd
        
        
        
class AnalyzePlay:
    '''
    PURPOSE: Provides some methods for analyzing the results of rolling dice. Initializes using a GamePlay class object.
    
    METHODS:
    - .find_jackpots()
    - .find_face_counts()
    - .count_combo()
    - .count_perm()
    '''
    
    def __init__(self, game):
        '''
        PURPORSE: AnalyzePlay class object initializer. Throws error if input is not a GamePlay class object.
        
        INPUT:
        game - GamePlay class object
        
        OUTPUT:
        None
        '''
        self.game = game
        # checks to make sure input for initializer is a game object from GamePlay class
        if (not isinstance(game, GamePlay)):
            raise TypeError("Not a game object.")
            
    def find_jackpots(self):
        '''
        PURPOSE: Finds the number of rows that have all the same faces
        
        INPUT:
        None
        
        OUTPUT:
        int - returns the number of rows that have all the same faces
        '''
        # rolls -> the data frame of roll results from gameplay class
        rolls = self.game.show_results()
        # df.nuniquie(axis=1) checks the rows. if all values in row are same, returns 1
        # rolls[boolean] selects all rows that are the same value
        # len() -> number of jackpots
        num_jackpots = len(rolls[rolls.nunique(axis=1) == 1])
        return num_jackpots
    
    def find_face_counts(self):
        '''
        PURPOSE: Counts the faces that are rolled
        
        INPUT:
        None
        
        OUTPUT:
        pd.DataFrame - returns a dataframe of the counts of each die face
                     - index -> rolls
                     - columns -> faces
                     - cells -> count of rolls of each face
        '''
        # index for dataframe -> list comprehension using results dataframe indices from GamePlay class
        self.countsindex = ["Roll #"+str(m+1) for m in range(len(self.game.show_results().index))]
        # columns for dataframe -> uses index from one of the dice in the list of dice to get dice faces
        # since all the dice are the same, it doesn't matter which one to use
        self.countscol = [n for n in self.game.listofdice[0].show_current_state().index]
        counts = []
        # iterate over rows
        for rolls in self.game.show_results().index:
            # jfc this method chaining is out of control
            # dataframe from GamePlay class - iterate over rows using .loc - counts unique values - sorts unique values by index - add 0s for missing values
            # adding 0s method (.reindex) uses same list of dice faces from self.countscol
            sorted_counts = self.game.show_results().loc[rolls].value_counts().sort_index().reindex((self.game.listofdice[0].show_current_state().index), fill_value=0)
            counts.append(sorted_counts)
        # dataframe constructor
        self.counts = pd.DataFrame(counts, index = self.countsindex, columns = self.countscol)
        return self.counts
    
    def count_combo(self):
        '''
        PURPOSE: Find the number of combinations (order-independent) in the results dataframe
        
        INPUT:
        None
        
        OUTPUT:
        pd.Dataframe - returns a dataframe of the unique rows and the count of each time that happens
                     - index -> unique rows, order independent
                     - columns -> count of each unique row
        '''
        # magic
        # this was supposed to be a multi-indexed dataframe, but I couldn't figure it out
        # results data frame -> apply a sort to each row, by column (axis 1) -> count each sorted row
        return pd.DataFrame(self.game.show_results().apply(lambda row: sorted(row.values), axis=1).value_counts())
    
    def count_perm(self):
        '''
        PURPOSE: Find the number of permutations (order-dependent) in the results dataframe
        
        INPUT:
        None
        
        OUTPUT:
        pd.Dataframe - returns a dataframe of the unique rows and the count of each time that happens
                     - index -> unique rows, order dependent
                     - columns -> count of each unique row
        '''
        # also magic
        # this method chaining is out of control
        # results data frame -> groupby columns -> size returns each unique row -> reset index renames the newly created column of counts of unique rows
        return pd.DataFrame(self.game.show_results().groupby(list(self.game.show_results().columns)).size().reset_index(name="count"))
        
    
