# DS5100FP

Metadata
Project title: Spring 2025 DS5100 Final Project - Monte Carlo Simulator 

Author: Christopher Lee

UVA NetID: dkn7rm

Synopsis:
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
CreateDice(np.array([]))

PURPOSE: Creates a dice. Initializes using faces listed in a numpy array.

METHODS:
- .change_weights(face2change, newWeight)
    PURPOSE: CreateDie class initializer. Throws error if input is not a numpy array 
    or the die does not have all different faces.

    INPUTS:
    diefaces - numpy array of list of die faces desired

    OUTPUTS:
    None

    Note: Instantiates die class as a pd.DataFrame
    
- .roll_dice(rolls=1)
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
    
- .show_current_state()
    PURPOSE: Rolls die the inputted amount of times. Defaults to 1 roll.

    INPUT: 
    rolls - int, desired number of rolls for die

    OUTPUT:
    list - list of roll results

    Note: weights of each die face is taken into consideration when rolling.