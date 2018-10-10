/*
This file is part of the "Theme Song Generation," Kinect Project for CS 312.

The "Theme Song Generation," Kinect Project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

The "Theme Song Generation," Kinect Project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
*/




//This is for converting the Vanilla Markov Chain pitches so
//  that they follow a particular scale. The vanilla pitches
//  are values 1-7 of the scale that the music was derived from.
//  Scales use 7 notes of a 12 note octave, that was to reduce
//  the size of the Markov Chain's 2D array. It also allows to
//  convert the song into any scale that we wish too though.
int calculateHalfSteps(String emotion, int keyNote) {
  //This will contain the halfstep offset from the base note of the key.
  int halfStepSum = 0; 

  //"VOID" uses the major scale, so the major scale
  //  conversion is below.
  if (emotion == "VOID") {
    //Iterate through the notes to count the halfsteps.
    for (int i = 1; i < keyNote + 1; i++) {
  
      //This checks to see if there is just one halfstep
      //  between this note and the last.
      if (i%7 == 3 || i%7 == 7) {
  
        halfStepSum += 1;
      }
      //Otherwise there is just a two halfstep difference.
      else {
  
        halfStepSum += 2;
      }
    }  
  }
  //"HAPPY" uses the phrygian scale, so the major scale
  //  conversion is below (this probably will change.)
  else if (emotion == "HAPPY") {
    //Iterate through the notes to count the halfsteps.
    for (int i = 1; i < keyNote + 1; i++) {
  
      //This checks to see if there is just one halfstep
      //  between this note and the last.
      if (i%7 == 1 || i%7 == 5) {
  
        halfStepSum += 1;
      }
      //Otherwise there is just a two halfstep difference.
      else {
  
        halfStepSum += 2;
      }
    }  
  }
  //"SAD" uses the minor scale, so the major scale
  //  conversion is below (this probably will change.)
  else if (emotion == "SAD") {
    //Iterate through the notes to count the halfsteps.
    for (int i = 1; i < keyNote + 1; i++) {
  
      //This checks to see if there is just one halfstep
      //  between this note and the last.
      if (i%7 == 2 || i%7 == 5) {
  
        halfStepSum += 1;
      }
      //Otherwise there is just a two halfstep difference.
      else {
  
        halfStepSum += 2;
      }
    }  
  }
  //"ANGER" uses the harmonic minor scale, so the major scale
  //  conversion is below (this probably will change.)
  else if (emotion == "ANGER") {
    //Iterate through the notes to count the halfsteps.
    for (int i = 1; i < keyNote + 1; i++) {
  
      //This checks to see if there is just one halfstep
      //  between this note and the last.
      if (i%7 == 2 || i%7 == 5) {
  
        halfStepSum += 1;
      }
      //Otherwise there is just a two halfstep difference.
      else {
  
        halfStepSum += 2;
      }
    }  
  }
  //"DISGUST" uses the minor scale, so the major scale
  //  conversion is below (this probably will change.)
  else if (emotion == "DISGUST") {
    //Iterate through the notes to count the halfsteps.
    for (int i = 1; i < keyNote + 1; i++) {
  
      //This checks to see if there is just one halfstep
      //  between this note and the last.
      if (i%7 == 2 || i%7 == 5) {
  
        halfStepSum += 1;
      }
      //Otherwise there is just a two halfstep difference.
      else {
  
        halfStepSum += 2;
      }
    }  
  }
  return halfStepSum;
} //End calculateHalfSteps()

//Pertains to notes
//This is global because I wanted it to be static in the Measure
//  class anyway.
float[] possibleLengths = {0.25, 0.375, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 4.0};

class Measure {
  
  //The pitches are stored in their vanilla version.
  //  (Numbers representing the places strictly on
  //  a scale of 3 octaves, so 21 notes.)
  //  This allows conversion to any sort of scale and key.
  ArrayList pitches;
  ArrayList dynamics;
  ArrayList durations;
  ArrayList articulations;
  ArrayList pans;
  
  //These are for defining characteristics
  //  of the notes.
  float DEFAULT_DYNAMIC;
  float DEFAULT_ARTICULATION;
  float DEFAULT_PAN;

  Measure(){
  
    pitches = new ArrayList();
    dynamics = new ArrayList();
    durations = new ArrayList();
    articulations = new ArrayList();
    pans = new ArrayList();
    
    DEFAULT_DYNAMIC = 64;
    DEFAULT_ARTICULATION = 0.8;
    DEFAULT_PAN = 64;
  }
  
  Measure copyConstructor() {
    
    Measure copy = new Measure();
    
    //Iterate through the notes in this Measure
    for (int i = 0; i < getLength(); i++) {
     
      copy.insertNote((Integer)pitches.get(i), (Integer)durations.get(i));
    }
    
    return copy;
  }
  
  //This inserts each characteristic for a note
  //  into the lists of characteristics.
  //@param pitch This is should be the pure vanilla
  //  pitch straight from the Markov Chain.
  //@param duration This is an integer in its vanilla
  //  form straight from the Markov Chain. To get its
  //  value, use it as an indx for the possibleLengths array.
  void insertNote(float pitch,  
            int duration) {
  
    pitches.add(pitch);
    durations.add(duration);
    dynamics.add(DEFAULT_DYNAMIC);
    articulations.add(DEFAULT_ARTICULATION);
    pans.add(DEFAULT_PAN);
  }
  
  //This is for retrieving the last note that was played.
  //  But this part only focuses on the last note of this
  //  measure.
  //@return A int of the vanilla pitch (pitch unaltered
  //  from the Markov Chain.) Since the pitches get altered
  //  by the key offset, we need to subtract the base key 
  //  offset from the float to get a vanilla pitch.
  float getLastPitch() {
    //Return the last note in the ArrayList of pitches.
    //  but in vanilla form (straight out of the Markov
    //  chain generation [0,21].)
    return (Float)pitches.get(pitches.size()-1); 
  }
  
  int getLastDuration() {
    return (Integer)durations.get(durations.size()-1);
  }
  
  //This is for determining how big the array of
  //  pitches needs to be for the Section of Measures.
  //@return The amount of notes in the
  //  Measure.
  int getLength() {
    
    return pitches.size();
  }
  
  boolean isEmpty() {
    
    return (pitches.size() == 0); 
  }
  
  //Gets an array of floats representing the pitches
  //  of the notes that make up this Measure. The 
  //  pitches are made to work for SoundCipher.
  //Note that the pitches are saved in their vanilla form
  //  that is made to work with Markov chains. So it needs
  //  to be converted to the actual values when fetched
  float[] getPitches(String emotion) {
    
    //This holds Sound CIphers offset
    //  for the key that we want.
    float keyOffset = 0.0;
    
    //Check to see which emotion is being used.
    //  Then alter the keyOffset according to
    //  the emotion's key and SoundCipher.
    if(emotion == "VOID") {
      //VOID uses C3 as its key.
      //C4 in SOundCipher is 60
      //But the Markov Chain notes requires a 
      //  minus 9 offset from what we want
      //  the key to be.
      keyOffset = 51.0;
    }
    else if(emotion == "HAPPY") {
      //E4 in SOundCipher is 64
      keyOffset = 55.0;
    }
    else if (emotion == "SAD") {
      //Db3 in SOundCipher is 49
      keyOffset = 40.0;
    }
    else if (emotion == "ANGER") {
      //B in SOundCipher is 35
      keyOffset = 26.0;
    }
    else if (emotion == "DISGUST") {
      // in SOundCipher is 41
      keyOffset = 32.0;
    }
    
    //Create an array the size of the ArrayList
    //  holding the pitches
    float[] arrayOfPitches = new float[pitches.size()];
   
    //Iterate through the ArrayList of pitches.
    for (int i = 0; i < pitches.size(); i++) {
      
        //Copy from the ArrayList to the array
        //  that is being returned.
        //  But also factor in the conversion to halfsteps
        //  and keyOffset for the pitches.
        //The minus one is because the 0th place on the MC vanilla scale marks a rest.
        //  So to prevent an incorrect keyOffset, the minus 1 was used. 
        arrayOfPitches[i] = calculateHalfSteps(emotion, int((Float)pitches.get(i))-1) + keyOffset;
    } 
    
    return arrayOfPitches;
  }
  
  //Gets an array of floats representing the durations
  //  of the notes that make up this Measure. The 
  //  pitches are made to work for SoundCipher.
  //Note that the durations are saved in their vanilla form
  //  that is made to work with Markov chains. So it needs
  //  to be converted to the actual values when fetched
  float[] getDurations() {
   
    //Create an array the size of the ArrayList
    //  holding the Durations
    float[] arrayOfDurations = new float[durations.size()];
   
    //Iterate through the ArrayList of durations.
    for (int i = 0; i < durations.size(); i++) {
    
      //Copy from the ArrayList to the array
      //  that is being returned.
      //The vanilla indx for the Markov Chain is converted into
      //  the actual length.
      arrayOfDurations[i] = possibleLengths[(Integer)durations.get(i)];
    }
    
    return arrayOfDurations;
  }
  
  //Gets an array of floats representing the dynamics
  //  of the notes that make up this Measure. The 
  //  pitches are made to work for SoundCipher.
  float[] getDynamics() {
   
    //Create an array the size of the ArrayList
    //  holding the dynamics
    float[] arrayOfDynamics = new float[dynamics.size()];
   
    //Iterate through the ArrayList of dynamic.
    for (int i = 0; i < dynamics.size(); i++) {
    
      if ((Float)pitches.get(i) != 0.0) {
        //Copy from the ArrayList to the array
        //  that is being returned.
        arrayOfDynamics[i] = (Float)dynamics.get(i);
      }
      else {
        
        //If the note should be a rest, then we
        //  set the dynamics to zero.
        arrayOfDynamics[i] = 0.0;
      }
    } 
    
    return arrayOfDynamics;
  }
  
  //Gets an array of floats representing the articulations
  //  of the notes that make up this Measure. The 
  //  pitches are made to work for SoundCipher.
  float[] getArticulations() {
   
    //Create an array the size of the ArrayList
    //  holding the articulations
    float[] arrayOfArticulations = new float[articulations.size()];
   
    //Iterate through the ArrayList of articulations.
    for (int i = 0; i < articulations.size(); i++) {
    
      //Copy from the ArrayList to the array
      //  that is being returned.
      arrayOfArticulations[i] = (Float)articulations.get(i);
    } 
    
    return arrayOfArticulations;
  }
  
  //Gets an array of floats representing the pans
  //  of the notes that make up this Measure. The 
  //  pitches are made to work for SoundCipher.
  float[] getPans() {
   
    //Create an array the size of the ArrayList
    //  holding the pans
    float[] arrayOfPans = new float[pans.size()];
   
    //Iterate through the ArrayList of pans.
    for (int i = 0; i < pans.size(); i++) {
    
      //Copy from the ArrayList to the array
      //  that is being returned.
      arrayOfPans[i] = (Float)pans.get(i);
    } 
    
    return arrayOfPans;
  }
}
