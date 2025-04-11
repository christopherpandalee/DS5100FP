# Spring 2025 Final Project - A Monte Carlo Simulator

Metadata

Project title: Spring 2025 DS5100 Final Project - Monte Carlo Simulator 

Author: Christopher Lee

UVA NetID: dkn7rm

Synopsis:

* Installing & importing:

    * pip install -e .
    
    * import montecarlosim

* Create die classes, roll dice using game class, and analyze results using analysis class

* Create die:

    * sampledie = CreateDice(np.array([1,2,3,4,5,6]))
    
    * sampledie.show_current_state()

* Play Dice

    * playsampledie = GamePlay([sampledie, sampledie, sampledie])
    
    * playsampledie.play_dice(10)
    
    * playsampledie.show_results()
    
* Analyze Play

    * analyzeplaydice = AnalyzePlay(playsampledie)
    
    * analyzeplaydice.find_face_counts()
    
API Description:

CreateDice(`numpy array`)

PURPOSE: Creates a dice. Initializes using faces listed in a numpy array.

METHODS:
- .change_weights(face2change, newWeight)

    PURPOSE: CreateDie class initializer. Throws error if input is not a numpy array 
    or the die does not have all different faces.

    INPUTS:
    
    - diefaces 
    
        - numpy array of list of die faces desired

    OUTPUTS:
    
    None

    Note: Instantiates die class as a pd.DataFrame
    
- .roll_dice(rolls=1)

    PURPOSE: Changes the weight of a certain die face

    INPUTS:
    
    - face2change 
    
        - a matching face of instantiated die, data type dependent on die face

        - throws error if this input does not match any of the faces of the die
                
    - newWeight
    
        - int or float

        - desired new weight for the die face being changed

        - throws error if new weight is not int or float

    OUTPUT:
    
    None

    Note: This method will change the instantiated die dateframe.
    
- .show_current_state()

    PURPOSE: Rolls die the inputted amount of times. Defaults to 1 roll.

    INPUT:
    
    - rolls 
    
        - int, desired number of rolls for die

    OUTPUT:
    
    - list 
        - list of roll results

    Note: weights of each die face is taken into consideration when rolling.
    

GamePlay([`list of dice`])

PURPOSE: Plays / rolls a list of dice. Initializes using a list of die class dice

METHODS:

- .play_dice(numrolls)

    PURPOSE: Rolls the dice in the list of dice the inputted amount of times. Stores results in a pd.DataFrame.

    INPUT:
    
    - numrolls 
    
        - int, number of rolls desired

    OUTPUT:
    
    None

    Note: Results of rolls are stored in a dataframe. Index \-\> rolls, columns \-\> each die in dice list
    
- .show_results(size="wide")

    PURPOSE: Shows the results of the rolls in a pd.DataFrame. Can be shown as a wide or narrow dataframe.

    INPUT:
    
    - size
    
        - string, 2 options: "wide", "narrow"
        
        - defaults to "wide"
        
        - throws error if not one of the two options

    OUTPUT:
    
    - pd.DataFrame 
    
        - dataframe of the results of the rolls
        
        - returns private results dataframe from .play_dice() method
        
        
AnalyzePlay(`GamePlay object`)

PURPOSE: Provides some methods for analyzing the results of rolling dice. Initializes using a GamePlay class object.

METHODS:

- .find_jackpots()

    PURPOSE: Finds the number of rows that have all the same faces

    INPUT:
    
    None

    OUTPUT:
    
    - int 
    
        - returns the number of rows that have all the same faces
        
- .find_face_counts()

    PURPOSE: Counts the faces that are rolled

    INPUT:
    
    None

    OUTPUT:
    
    - pd.DataFrame 
    
        - returns a dataframe of the counts of each die face
        
        - index \-\> rolls
        
        - columns \-\> faces
        
        - cells \-\> count of rolls of each face
        
- .count_combo()

    PURPOSE: Find the number of combinations (order-independent) in the results dataframe

    INPUT:
    
    None

    OUTPUT:
    
    - pd.Dataframe 
    
        - returns a dataframe of the unique rows and the count of each time that happens
        
        - index \-\> unique rows, order independent
        
        - columns \-\> count of each unique row
        
- .count_perm()

    PURPOSE: Find the number of permutations (order-dependent) in the results dataframe

    INPUT:
    
    None

    OUTPUT:
    
    - pd.Dataframe 
    
        - returns a dataframe of the unique rows and the count of each time that happens
        
        - index \-\> unique rows, order dependent
        
        - columns \-\> count of each unique row
        