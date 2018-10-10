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



class Section {
  
  ArrayList measures;
  
  Section() {
    
    measures = new ArrayList();
  }
  
  //Simply inserts a Measure into the Section.
  void insertMeasure(Measure newMeasure) {
  
    measures.add(newMeasure);
  }
  
  //Removes and returns a measure within this section.
  //@return A Measure instance that contains some
  //  notes.
  //@post The measures ArrayList will have one less
  //  Measure in it.
  Section popMeasure(int indx) {
    
    //Save the measure that's being removed.
    Section removedSection = (Section)measures.get(indx);
    
    //Remove it from the Section
    measures.remove(indx);
    
    return removedSection;
  }
  
  Measure getMeasure(int indx) {
    return (Measure)measures.get(indx);
  }
  
  int getNumMeasures() {
    return measures.size();
  }
  
  int getNumBeats() {
    
    return measures.size() * 4;
  }
  
  //@return a int that represents the last note
  //  of this Section.
  float getLastPitch() {
    //Returns the last note of the last Measure of this Section.
    return ((Measure)measures.get(measures.size()-1)).getLastPitch();
  }
  
  int getLastDuration() {
    return ((Measure)measures.get(measures.size()-1)).getLastDuration();
  }
  
  float[] getPitches(String emotion) {
    
    //A counter for the amount of notes in
    //  this Section.
    int noteSum = 0;
    
    //Iterate each Measure to count the notes in
    // the Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //This adds the number of notes in the current
      //  measure to the counter.
      noteSum += ((Measure)measures.get(i)).getLength();
    } 
 
    //Create an array of floats for the pitches
    //  that were all just counted up.
    float[] sectionPitches = new float[noteSum];
   
    //This will record the place notes need to be 
    //  added to.
    int sectionIndx = 0;
    
    //Iterate each Measure to get all the pitches
    //  for this Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //A tmp var for the current Measure pitches.
      float[] measurePitches = ((Measure)measures.get(i)).getPitches(emotion);
      
      //Iterate through the notes in this Measure.
      for (int j = 0; j < measurePitches.length; j++) {
        
        //Add the pitch into the section of pitches.
        sectionPitches[sectionIndx] = measurePitches[j];
        
        //Move to the next position in the array for
        //  the next note.
        sectionIndx++;
      } //end for
    } //end for
    
    return sectionPitches;
  } //end getPitches()
  
  
  float[] getDurations() {
    
    //A counter for the amount of notes in
    //  this Section.
    int noteSum = 0;
    
    //Iterate each Measure to count the notes in
    // the Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //This adds the number of notes in the current
      //  measure to the counter.
      noteSum += ((Measure)measures.get(i)).getLength();
    } 
    //Create an array of floats for the Durations
    //  that were all just counted up.
    float[] sectionDurations = new float[noteSum];
   
    //This will record the place notes need to be 
    //  added to.
    int sectionIndx = 0;
    
    //Iterate each Measure to get all the Durations
    //  for this Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //A tmp var for the current Measure Durations.
      float[] measureDurations = ((Measure)measures.get(i)).getDurations();
      
      //Iterate through the notes in this Measure.
      for (int j = 0; j < measureDurations.length; j++) {
        
        sectionDurations[sectionIndx] = measureDurations[j];
        
        //Move to the next position in the array for
        //  the next note.
        sectionIndx++;
      } //end for
    } //end for
    
    return sectionDurations;
  } //end getDurations()
  
  float[] getDynamics() {
    
    //A counter for the amount of notes in
    //  this Section.
    int noteSum = 0;
    
    //Iterate each Measure to count the notes in
    // the Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //This adds the number of notes in the current
      //  measure to the counter.
      noteSum += ((Measure)measures.get(i)).getLength();
    } 
    
    //Create an array of floats for the Dynamics
    //  that were all just counted up.
    float[] sectionDynamics = new float[noteSum];
   
    //This will record the place notes need to be 
    //  added to.
    int sectionIndx = 0;
    
    //Iterate each Measure to get all the pitches
    //  for this Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //A tmp var for the current Measure Dynamics.
      float[] measureDynamics = ((Measure)measures.get(i)).getDynamics();
      
      //Iterate through the notes in this Measure.
      for (int j = 0; j < measureDynamics.length; j++) {
        
        //Add the pitch into the section of Dynamics.
        sectionDynamics[sectionIndx] = measureDynamics[j];
        
        //Move to the next position in the array for
        //  the next note.
        sectionIndx++;
      } //end for
    } //end for
    
    return sectionDynamics;
  } //end getDynamics()
  
 float[] getArticulations() {
    
    //A counter for the amount of notes in
    //  this Section.
    int noteSum = 0;
    
    //Iterate each Measure to count the notes in
    // the Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //This adds the number of notes in the current
      //  measure to the counter.
      noteSum += ((Measure)measures.get(i)).getLength();
    } 
    
    //Create an array of floats for the Articulations
    //  that were all just counted up.
    float[] sectionArticulations = new float[noteSum];
   
    //This will record the place notes need to be 
    //  added to.
    int sectionIndx = 0;
    
    //Iterate each Measure to get all the Articulations
    //  for this Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //A tmp var for the current Measure Articulations.
      float[] measureArticulations = ((Measure)measures.get(i)).getArticulations();
      
      //Iterate through the notes in this Measure.
      for (int j = 0; j < measureArticulations.length; j++) {
        
        //Add the pitch into the section of Articulations.
        sectionArticulations[sectionIndx] = measureArticulations[j];
        
        //Move to the next position in the array for
        //  the next note.
        sectionIndx++;
      } //end for
    } //end for
    
    return sectionArticulations;
  } //end getArticulations()
  
 float[] getPans() {
    
    //A counter for the amount of notes in
    //  this Section.
    int noteSum = 0;
    
    //Iterate each Measure to count the notes in
    // the Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //This adds the number of notes in the current
      //  measure to the counter.
      noteSum += ((Measure)measures.get(i)).getLength();
    } 
    
    //Create an array of floats for the Pans
    //  that were all just counted up.
    float[] sectionPans = new float[noteSum];
   
    //This will record the place notes need to be 
    //  added to.
    int sectionIndx = 0;
    
    //Iterate each Measure to get all the Pans
    //  for this Section.
    for (int i = 0; i < measures.size(); i++) {
      
      //A tmp var for the current Measure Pans.
      float[] measurePans = ((Measure)measures.get(i)).getPans();
      
      //Iterate through the notes in this Measure.
      for (int j = 0; j < measurePans.length; j++) {
        
        //Add the pitch into the section of Pans.
        sectionPans[sectionIndx] = measurePans[j];
        
        //Move to the next position in the array for
        //  the next note.
        sectionIndx++;
      } //end for
    } //end for
    
    return sectionPans;
  } //end getPans()  
} //end Section

