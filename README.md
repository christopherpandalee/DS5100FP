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
