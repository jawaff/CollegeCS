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

//The following two are for the HashMap
import java.util.Iterator;
import java.util.Map;
//This is for the Kinect
import SimpleOpenNI.*;
//This will play the created music
import jmetude.*;
//This just will save the created music.
import arb.soundcipher.*;


SimpleOpenNI kinect;

//This is just for convenience, because I wanted to be able
//  to quickly change the path to where the songs are to be saved. 
String songPath;

MoodSkeleton moodSkele;

//This is so the program knows the diferent emotions
//  that are possible, this MUST be up-to-date.
String[] emotionTypes = {"VOID", "HAPPY", "SAD", "ANGER", "DISGUST"};

//The first element is the most recent emotion.
String[] detectedEmotionsQueue = {"VOID", "VOID", "VOID", "VOID", "VOID", "VOID", "VOID",
                                  "VOID", "VOID", "VOID", "VOID", "VOID", "VOID", "VOID", 
                                  "VOID", "VOID", "VOID", "VOID", "VOID", "VOID", "VOID"};

//This is the emotion that is currently being observed from the user.
String curEmotion;

//This is for holding the emotion that we're going to be switching to.
String nextEmotion;

//This will store and play the songs that are generated 
Etude etude;

//This denotes the lastTime Etude was told to play a song in milliseconds.
int lastTimePlayed;

//This is used as an indirect trigger for Etude to play
//  a song. It can be seen in the draw() function.
boolean songReadyToPlay = false;

//This is just so that we can change the name of the saved songs.
//Since there will be more than one saved per emotion, we needed
//  more unique names to prevent files from being overwritten.
int generatedSongs = 0;
                   
//This has all possible patterns for three Measures.
int[][] measurePatterns = { {0, 1, 2, 0},
                            {0, 1, 2, 1},
                            {0, 1, 2, 2},
                            {0, 1, 2, 3},
                            {0, 0, 1, 0},
                            {0, 0, 1, 1},
                            {0, 0, 1, 2},
                            {0, 0, 1, 3},
                            {0, 1, 0, 0},
                            {0, 1, 0, 1},
                            {0, 1, 0, 2},
                            {0, 1, 0, 3},
                            {0, 1, 1, 0},
                            {0, 1, 1, 1},
                            {0, 1, 1, 2},
                            {0, 1, 1, 3} };

void setup() {
  //This is where the generated songs will be saved.
  songPath = "F:/College/CS492/sketchBook/KinectProjectv5/Generated_Songs/";
  
  kinect = new SimpleOpenNI(this);
  kinect.enableDepth();
  kinect.enableUser(SimpleOpenNI.SKEL_PROFILE_ALL);
  kinect.setMirror(true);
  
  //This will store the generated songs and
  //  will play/stop those songs.
  etude = new Etude(this);
  
  //This will draw and interpret the user's pose.
  moodSkele = new MoodSkeleton(kinect);
  
  //The rules that are being added are for 
  //////////////////////////////////
  //rules for the HAPPY
  //////////////////////////////////
  moodSkele.addRule(moodSkele.RARM,
                   "HAPPY",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.ABOVE,
                   SimpleOpenNI.SKEL_RIGHT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.RARM,
                   "HAPPY",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.RIGHT_OF,
                   SimpleOpenNI.SKEL_RIGHT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.RARM,
                   "HAPPY",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_HEAD,
                   250);
                   
  moodSkele.addRule(moodSkele.LARM,
                   "HAPPY",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.ABOVE,
                   SimpleOpenNI.SKEL_LEFT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.LARM,
                   "HAPPY",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.LEFT_OF,
                   SimpleOpenNI.SKEL_LEFT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.LARM,
                   "HAPPY",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_HEAD,
                   250);
                   
  //////////////////////////////////
  //Rules for the Sadness
  /////////////////////////////////
  moodSkele.addRule(moodSkele.TORSO,
                   "SAD",
                   SimpleOpenNI.SKEL_LEFT_HIP,
                   PoseRule.MORE_THAN_ANGLE,
                   SimpleOpenNI.SKEL_LEFT_SHOULDER,
                   7);
  moodSkele.addRule(moodSkele.TORSO,
                   "SAD",
                   SimpleOpenNI.SKEL_NECK,
                   PoseRule.LEFT_OF,
                   SimpleOpenNI.SKEL_RIGHT_HIP,
                   0);
  moodSkele.addRule(moodSkele.TORSO,
                   "SAD",
                   SimpleOpenNI.SKEL_NECK,
                   PoseRule.RIGHT_OF,
                   SimpleOpenNI.SKEL_LEFT_HIP,
                   0);
  moodSkele.addRule(moodSkele.TORSO,
                   "SAD",
                   SimpleOpenNI.SKEL_NECK,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_TORSO,
                   0);
                   
  moodSkele.addRule(moodSkele.HEAD,
                   "SAD",
                   SimpleOpenNI.SKEL_NECK,
                   PoseRule.MORE_THAN_ANGLE,
                   SimpleOpenNI.SKEL_HEAD,
                   5);
  moodSkele.addRule(moodSkele.HEAD,
                   "SAD",
                   SimpleOpenNI.SKEL_NECK,
                   PoseRule.LEFT_OF,
                   SimpleOpenNI.SKEL_RIGHT_HIP,
                   0);
  moodSkele.addRule(moodSkele.HEAD,
                   "SAD",
                   SimpleOpenNI.SKEL_NECK,
                   PoseRule.RIGHT_OF,
                   SimpleOpenNI.SKEL_LEFT_HIP,
                   0);
  moodSkele.addRule(moodSkele.HEAD,
                   "SAD",
                   SimpleOpenNI.SKEL_HEAD,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_NECK,
                   0);
                   

  //////////////////////////////////
  //Rules for the Anger
  /////////////////////////////////
  moodSkele.addRule(moodSkele.RARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.ABOVE,
                   SimpleOpenNI.SKEL_RIGHT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.RARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.LEFT_OF,
                   SimpleOpenNI.SKEL_RIGHT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.RARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.WITHIN,
                   SimpleOpenNI.SKEL_RIGHT_SHOULDER,
                   450);  
  moodSkele.addRule(moodSkele.RARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_HEAD,
                   250);
                   
  moodSkele.addRule(moodSkele.LARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.ABOVE,
                   SimpleOpenNI.SKEL_LEFT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.LARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.RIGHT_OF,
                   SimpleOpenNI.SKEL_LEFT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.LARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.WITHIN,
                   SimpleOpenNI.SKEL_LEFT_SHOULDER,
                   450);                   
  moodSkele.addRule(moodSkele.LARM,
                   "ANGER",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_HEAD,
                   250);
                   
  //////////////////////////////////
  //Rules for the DISGUST
  /////////////////////////////////
  //Check to see if the user's arms are in front of the user.
  moodSkele.addRule(moodSkele.RARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_RIGHT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.RARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_RIGHT_ELBOW,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_RIGHT_SHOULDER,
                   0);
  moodSkele.addRule(moodSkele.RARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.LEFT_OF,
                   SimpleOpenNI.SKEL_RIGHT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.RARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_RIGHT_SHOULDER,
                   450);
  moodSkele.addRule(moodSkele.RARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_RIGHT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_RIGHT_HIP,
                   300);
                   
  moodSkele.addRule(moodSkele.LARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_LEFT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.LARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_LEFT_ELBOW,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_LEFT_SHOULDER,
                   0);
  moodSkele.addRule(moodSkele.LARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.RIGHT_OF,
                   SimpleOpenNI.SKEL_LEFT_ELBOW,
                   0);
  moodSkele.addRule(moodSkele.LARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_LEFT_SHOULDER,
                   450);
  moodSkele.addRule(moodSkele.LARM,
                   "DISGUST",
                   SimpleOpenNI.SKEL_LEFT_HAND,
                   PoseRule.AWAY_FROM,
                   SimpleOpenNI.SKEL_LEFT_HIP,
                   250);
                   
  //The next two rules check to see if the user is leaning back.
  moodSkele.addRule(moodSkele.TORSO,
                   "DISGUST",
                   SimpleOpenNI.SKEL_RIGHT_HIP,
                   PoseRule.MORE_THAN_ANGLE,
                   SimpleOpenNI.SKEL_RIGHT_SHOULDER,
                   8);
  moodSkele.addRule(moodSkele.TORSO,
                   "DISGUST",
                   SimpleOpenNI.SKEL_RIGHT_KNEE,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_RIGHT_SHOULDER,
                   0);

  //The next two rules check to see if the user's head is leaning back.
  /*moodSkele.addRule(moodSkele.HEAD,
                   "DISGUST",
                   SimpleOpenNI.SKEL_HEAD,
                   PoseRule.MORE_THAN_ANGLE,
                   SimpleOpenNI.SKEL_NECK,
                   14);
  moodSkele.addRule(moodSkele.HEAD,
                   "DISGUST",
                   SimpleOpenNI.SKEL_NECK,
                   PoseRule.IN_FRONT,
                   SimpleOpenNI.SKEL_HEAD,
                   0);*/

  curEmotion = "VOID";
  nextEmotion = "VOID";
  
  //Iterate through all of the emotionTypes.
  for (int i = 0; i < emotionTypes.length; i++)
  {
    //Generates a score for an Emotion.
    Section[][] sections = generateScore(emotionTypes[i], 1);
    
    //This will save the generated score as Midi files.
    saveScore(sections, emotionTypes[i]);
    
    //This will add the generated song to the etude, a music libraries' class.
    addScoreToEtude(etude, sections, emotionTypes[i], true);
    
    generatedSongs += 1;
  }
  
  etude.playMIDI(emotionTypes[0]);
  
  lastTimePlayed = millis();

  size(640, 480);
  fill(255);
  
  strokeWeight(5);

  PFont font = createFont("Verdana", 35);
  textFont(font);
}


void draw()
{
  kinect.update();
  image(kinect.depthImage(), 0, 0);

  IntVector userList = new IntVector();
  kinect.getUsers(userList);
  
  //Is there a user at all?
  if (userList.size() > 0)
  {
    //This iterates through all of the users visible by the kinect. 
    //  (They may not be calibrated at all.)
    //This allows multiple users to all contribute to the
    //  detectedEmotionsQueue global array (which should be stored in a class, someday.)
    //  That will make it so that music changes when the majority
    //  of users are conforming to an emotion.  
    for (int userIndx = 0; userIndx < userList.size(); userIndx++) {
      //This gets the id of the current user.
      int userId = userList.get(userIndx);
      
      //Is the current user calibrated and being tracked?
      if(kinect.isTrackingSkeleton(userId))
      {
        //As the skeleton gets drawn, the mood will also be
        //  checked.
        drawMoodSkeleton(userId);
        
        //This draws the status of the user's emotion on the window.
        text("CurrentEmotion: " + curEmotion, 20, 400);
      }
    }
  }
  
  //This checks to see if the song hasn't been triggered to be played
  //  already. If that is so, it will check to see if a new song needs
  //  to be triggered.
  if (!songReadyToPlay) {
    //This is the counter for how many emotions are
    //  in the detectedEmotionsQueue that aren't the
    //  current emotion.
    float sum = 0.0;
    
    //This adds up the emotions that aren't the curEmotion.
    for (int e = 0; e < detectedEmotionsQueue.length; e++) {
      
      //If there was a previous emotion that isn't the
      //  emotion we're using for generating music, we'll
      //  count it.
      if (detectedEmotionsQueue[e] != curEmotion) {
  
        sum += 1.0; 
      }
    }
    
    //If Majority rule is hit, then we trigger a new emotion
    //  to be used (but we have to determine the emotion first.)
    if (sum/(float)detectedEmotionsQueue.length >= 0.6) {
      
      //Determine the Emotion that will take place.
      for (int i = 0; i < emotionTypes.length; i++) {
        
        //Counts occurrences of this emotion in the array of detectedEmotionsQueue
        float curSum = 0.0;
        for (int j = 0; j < detectedEmotionsQueue.length; j++) {
          
          //If the current emotionType was found
          if(detectedEmotionsQueue[j] == emotionTypes[i]) {
           
            curSum += 1.0;
          }
        }
        
        //Checks to see if this emotionType took up 60% or more of the
        //  detectedEmotionsQueue.
        if (curSum/(float)detectedEmotionsQueue.length >= 0.6) {
          //This will signal the score to be played
          songReadyToPlay = true;
          nextEmotion = emotionTypes[i];
        }
      }
    }
  }//End if
  //This waits until 3 seconds after the last score 
  //  was played to prevent an error with stopping
  //  a midi that isn't even playing yet.
  else if((lastTimePlayed + 3000) <= millis()) {
      //playScore will stop the previous score and
      //  play the next one. It will update the curEmotion.
      playScore(etude, nextEmotion);
      lastTimePlayed = millis();
      
      //This tells etude to remove a score. This is so that
      //  we can replace that score with a newly generated one.
      etude.clear(curEmotion);
      
      //This part will generate a new score for the previous emotion.
      //This prevents an emotion from playing the same song every time
      //  it is signaled to play.
      //Generates a score for an Emotion.
      Section[][] sections = generateScore(curEmotion, 1);
      
      //This will save the generated score as Midi files.
      saveScore(sections, curEmotion);
      
      //This will add the generated song to the etude, a music libraries' class.
      addScoreToEtude(etude, sections, curEmotion, false);
      
      //Officially updating the currentEmotion.
      curEmotion = nextEmotion;
      nextEmotion = "VOID";
      
      //This is just to keep track of how many songs are being generated.
      generatedSongs += 1;
      
      //This will make it so that the song isn't played
      //  again until an emotion has changed.
      songReadyToPlay = false;
  }
}



//This should be called when the Section has reached its
//  end. So then we have to add more to the score.
//@param instruments This integer represents how many instruments will have
//  parts generated for them.
Section[][] generateScore(String emotion, int instruments) { 
  //This can't be less than what the size of the maximum pattern
  //   in the measurePatterns array.
  //The first level is for the different instruments in the score.
  //  The second level is for the different sections of the score.
  Section[][] generatedSections = new Section[instruments][4];
  
  for (int j = 0; j < generatedSections.length; j++) {
    //Iterate through the sections that need to be generated.
    for (int i = 0; i < generatedSections[0].length; i++) {
      //Compute the pattern that will be used for all of the instruments
      //  in this section.
      //This grabs a random pattern position from the global SectionPatterns 2D array.
      int[] randPattern = measurePatterns[(int)random(measurePatterns.length)];
  
      if (i == 0) {
        generatedSections[j][i] = generateSection(0.0, 2, emotion, randPattern);
      }
      else {
        generatedSections[j][i] = generateSection(((Section)generatedSections[j][i-1]).getLastPitch(), ((Section)generatedSections[j][i-1]).getLastDuration(), emotion, randPattern);
      }
    }
  }
  
  //This will pick a random pattern indx
  int randInt = (int)random(5, measurePatterns.length);
  
  //Now we must get a random pattern for our Sections and then we must
  //  put the Sections into the new Score with respect to the pattern.
  int[] pattern = measurePatterns[randInt];
  
  //The first level is the instruments
  //  The second level is for the sections
  Section[][] newSections = new Section[instruments][pattern.length];
  
  //This will be for counting the beats that before the current
  //  section that is being added to the score.
  int beatSum = 0;
  
  //Iterates through the instruments
  for (int i = 0; i < newSections.length; i++) {
    //This iterates through each Section that is to be added into the
    //  score according to the pattern.
    for (int j = 0; j < pattern.length; j++) {
      newSections[i][j] = generatedSections[i][pattern[j]];
    }
  }

  return newSections;
}

//This is strictly for saving a song to the hard-drive.
//SoundCipher is only used for this purpose now.
void saveScore(Section[][] sections, String emotion) {
  SCScore newScore = new SCScore();
  
  //Iterates through the instruments in the score
  for (int i = 0; i < sections.length; i++) {
    //counting the beats of the incoming phrases.
    int beatSum = 0;
    
    //iterates through the sections in the score
    for (int j = 0; j < sections[0].length; j++) {
      newScore.addPhrase((double)beatSum,
                      (double)i, (double)i*5,
                      sections[i][j].getPitches(emotion),
                      sections[i][j].getDynamics(),
                      sections[i][j].getDurations(),
                      sections[i][j].getArticulations(),
                      sections[i][j].getPans());    
                     
      //This will update the beatSum so that the next
      //  section is added in at the end of this section.
      beatSum += sections[i][j].getNumBeats();
    }
  }
  
  newScore.writeMidiFile(songPath + "emo-" + emotion + generatedSongs + ".mid");
}

//This will load the generated song into the Etude instance being
//  used to play songs.
void addScoreToEtude(Etude e, Section[][] sections, String emotion, boolean newScore) {
  if (newScore) {
    e.createScore(emotion);
  }
  else {
    e.clear(emotion);
  }
  
  //Counts the beats prior to the section that is being added in.
  float beatSum;
  
  //Iterates through intruments
  for (int i = 0; i < (sections.length*5); i+=5) {
    if (newScore) {
      //This will hold the score for now, but it might not suffice when more
      //  instruments get added.
      e.createPart(emotion+i);
    }
    else {
      e.clear(emotion+i);
    }
    e.setPartInstrument(emotion+i, i);
    e.setPartChannel(emotion+i, i);
    
    //Counts the beats prior to the section that is being added in.
    beatSum = 0.0;
    
    //Iterates through Sections
    for (int j = 0; j < sections[0].length; j++) {
      if (newScore) {
        //Creates a phrase that notes can be added to.
        e.createPhrase(emotion+i+j);
      }
      else {
        e.clear(emotion+i+j);
      }
      e.setPhraseStartTime(emotion+i+j, beatSum);
      
      //Iterates through Measures within Section.
      for (int k = 0; k < sections[i/5][j].getNumMeasures(); k++) {
        //Grabs a Measure from the current Section.
        Measure curMeasure = sections[i/5][j].getMeasure(k);
  
        beatSum += 4.0;
  
        //Fetches the pitches and durations within the current Measure
        float[] pitches = curMeasure.getPitches(emotion);
        float[] durations = curMeasure.getDurations();
        
        //Iterates through Notes within a Measure
        for (int n = 0; n < pitches.length; n++) {
          //Fetches a note from the Measure's pitches
          //  and durations.
          float[] note = {pitches[n], durations[n]};
          e.addPhraseNote(emotion+i+j, note);
        }
      }
      //After adding notes into the phase, we must add it into the part.
      e.addPartPhrase(emotion+i, emotion+i+j);
    }
    //After adding phrases into a part, we can add the part into the score.
    e.addScorePart(emotion, emotion+i);
  }
}

//This simply will trigger the Etude object to play
//  the song associated with the given emotion.
void playScore(Etude e, String emotion) {
  e.stopMIDI();
  e.playMIDI(emotion);
}

//This will draw the skeleton of the user with
//  respect to his/her mood.
//@post Since the mood for the user is checked
//  while the skeleton is being drawn, the detectedEmotionsQueue
//  array will have its elements shifted down one space
//  and a new emotion will be added at the 0th index.
//  The skeleton of the user will also be drawn,
//  but the limbs will be colored with respect to the
//  different signals the user is giving off.
void drawMoodSkeleton(int userId)
{
  moodSkele.drawSkeleton(userId, curEmotion);
  
  //Shift all the detectedEmotionsQueue down so that a new
  //  emotion can be added at first element place.
  for(int i = detectedEmotionsQueue.length-1; i > 0; i--) {
    
    //Shift the detectedEmotionsQueue towards the end.
    detectedEmotionsQueue[i] = detectedEmotionsQueue[i-1];
  }
  
  detectedEmotionsQueue[0] = moodSkele.getMostProminentEmo(userId, moodSkele.ALL_THE_LIMBS, curEmotion);  
}


//This is for generating pitches for a section or measure.
//@return An array of ints of the length specified by the notes parameter.
//  These ints will represent the pitch according to SoundCipher's standards.
//  SC's pitches range from 0-127, each number is a halfstep on the piano.
//  The middle C is at 60.
//@param lastNote This is the value of the last Note that was played according to the current key.
//  it is an integer because it will be used as an index for an array.
//@param emotion This is a value associated with the Emotion enum in the globals.
//@param notes This will be the amount of notes generated and returned.
float[] generatePitches(float lastNote, String emotion, int notes) {
  
  //This creates an empty array of which we'll place the generated notes
  //  represented by their place within the specific key based on the emotion.
  float[] keyNotes = new float[notes];
  
  //A copy Markov Chain for storing the Markov Chain that is needed for this
  //  array of pitches. The emotion is what dictates the MC.
  float[][] markovChain = new float[MCVoid.length][MCVoid[0].length];
  
  //Check to see if there isn't a recognizable emotion
  if(emotion == "VOID") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCVoid[x][y];
      }
    }
  }
  else if(emotion == "HAPPY") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCHappy[x][y];
      }
    }
  }
  else if(emotion == "SAD") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCSad[x][y];
      }
    }
  }
  else if(emotion == "ANGER") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCAnger[x][y];
      }
    }
  }
  else if(emotion == "DISGUST") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCDisgust[x][y];
      }
    }
  }
    
  //Loops through each note that needs to be created.
  for (int i = 0; i < notes; i++) {
    
    //Random number to determine which note is chosen.
    float randNum = random(1);
    //A counter to compare with the randNum var.
    float sum = 0;
    
    //Loops through all of the possible notes that can be generated.
    //  Numbers associated with the particular key.
    for (int j = 0; j < markovChain[0].length; j++) {
      //The first generated note works based on the lastNote parameter.
      if(i == 0) {
        //Check to see if we've found the generated note.
        if(randNum >= sum &&
        randNum < (sum + markovChain[(int)lastNote][j])) {
          //Save the note
          keyNotes[i] = (float)j;
          break;
        }
        else {
          //Add this note's probability.
          sum += markovChain[(int)lastNote][j];
        }
      }
      else {
        //Check to see if we've found the generated note.
        if(randNum >= sum
        && randNum <= (sum + markovChain[(int)keyNotes[i-1]][j])) {
          //Save the note
          keyNotes[i] = (float)j;
          break;
        }
        else {
          //Add this note's probability.
          sum += markovChain[(int)keyNotes[i-1]][j];
        }
      }
    } 
  }

  return keyNotes;
} //End generatePitches()

//This function is used to generate a section that contains a number of measures.
//@return An instance of the Section class. The Section instance will contain a
//  number of Measure class instances, depending on the size of the Section's
//  pattern.
//@param lastNote This number represents the pitch of the last note of the
//  previous section.
//@param emotion This is for differentiating between which Markov Chain to use
//  for the music generation.
Section generateSection(float lastPitch, int lastDuration, String emotion, int[] pattern) {
  //measures(measure(note(pitch, length), note(pitch, length), ...), ...) is the information that needs 
  //  built for representing the generated section.
  Section newSection = new Section();
  
  //These are  the different measures that make up a section.
  Measure[] measures = new Measure[4];
  
  //The measures need to be initialized.
  for (int i = 0; i < measures.length; i++) {
    measures[i] = new Measure();
  }
  
  //A copy Markov Chain for storing the Markov Chain that is needed for this
  //  array of pitches. The emotion is what dictates the MC.
  float[][] markovChain = new float[MCVoidDur.length][MCVoidDur[0].length];
  
  //Check to see if there isn't a recognizable emotion
  if(emotion == "VOID") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCVoidDur[x][y];
      }
    }
  }
  else if(emotion == "HAPPY") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCHappyDur[x][y];
      }
    }
  }
  else if(emotion == "SAD") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCSadDur[x][y];
      }
    }
  }
  else if(emotion == "ANGER") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCAngerDur[x][y];
      }
    }
  }
  else if(emotion == "DISGUST") {
    //This loops through each element in the Jazz Markov Chain.
    for (int x = 0; x < markovChain.length; x++) {
      for (int y = 0; y < markovChain[0].length; y++) {
        //Copy the item
        markovChain[x][y] = MCDisgustDur[x][y];
      }
    }
  }
  
  
  //This loops through all of the measures in the pattern.
  for (int m = 0; m < pattern.length; m++) {
    //This pointer points to a measure that is either empty or full.
    //  The pattern specifies which measure this is to be.
    Measure newMeasure = measures[pattern[m]];
    
    //If the measure hasn't been created.
    if (newMeasure.isEmpty()) {
      //This counts the length of the notes accumulating.
      float lenCounter = 0.0;
      //A list that contains the lengths of the notes in this measure.
      ArrayList durations = new ArrayList();
      
      //This loops until the notes make up a full measure (it uses a sort of brute-force random approach.)
      //A measure's length is assumed to be 4.0.
      while(lenCounter < 4.0 || lenCounter > 4.0) {
        //This checks to see if the note lengths exceed the length of a measure (which is 8.)
        if (lenCounter > 4.0) {
          //Select random item position.
          int item = (int)random(durations.size()); 

          int randDuration = (Integer)durations.get(item); 
          
          //Before the note is removed from the list, we'll subtract its value from the lenCounter.
          lenCounter -= possibleLengths[randDuration];
          
          //This removes the item that's position was randomly selected.
          durations.remove(item);
        } //end if
        else {
          //Get a random element position from the possibleLengths array.
          //int item = (int)random(possibleLengths.length);
          
          float randNum = random(1);
          
          //A counter to compare with the randNum var.
          float sum = 0;
          
          //Loops through all of the possible notes that can be generated.
          //  Numbers associated with the particular key.
          for (int j = 0; j < markovChain[0].length; j++) {
            //The first generated note works based on the lastDuration parameter.
            if(m == 0 && lenCounter == 0.0) {
              //Check to see if we've found the generated note.
              if(randNum >= sum &&
              randNum < (sum + markovChain[lastDuration][j])) {
                //Save the note
                //Add the element from possibleLengths to the counter
                lenCounter += possibleLengths[j];
                
                //This inserts a value of the different notes compatible into the list of notes.
                durations.add(j);
                break;
              }
              else {
                //Add this note's probability.
                sum += markovChain[lastDuration][j];
              }
            }
            //The first generated note of a measure that isn't the first one.
            else if (lenCounter == 0.0) {
              int lastDurationInMeasure = ((Measure)measures[pattern[m-1]]).getLastDuration();
              
              //Check to see if we've found the generated note.
              if(randNum >= sum &&
              randNum < (sum + markovChain[lastDurationInMeasure][j])) {
                //Save the note
                //Add the element from possibleLengths to the counter
                lenCounter += possibleLengths[j];
                
                //This inserts a value of the different notes compatible into the list of notes.
                durations.add(j);
                break;
              }
              else {
                //Add this note's probability.
                sum += markovChain[lastDurationInMeasure][j];
              }              
            }
            else {
              //Gets last duration within the current measure
              int lastDurationInMeasure = (Integer)durations.get(durations.size()-1);  

              //Check to see if we've found the generated note.
              if(randNum >= sum
              && randNum <= (sum + markovChain[lastDurationInMeasure][j])) {
                //Save the note
                //Add the element from possibleLengths to the counter
                lenCounter += possibleLengths[j];
                
                //This inserts a value of the different notes compatible into the list of notes.
                durations.add(j);
                break;
              }
              else {
                //Add this note's probability.
                sum += markovChain[lastDurationInMeasure][j];
              }
            }
          }
          

        } //end else
      } //end while
      
      //The last note needs to be calculated based on what the last measure was.
      float prevPitch;
      
      //Check to see if we've generated previous Measures.
      if (m == 0) {
        prevPitch = lastPitch;
      }
      else {
        //This should grab the pitch of the last note in the previous measure.
        //  The Section class has a method for this.
        prevPitch = newSection.getLastPitch();
      }
      
      float[] pitches = generatePitches(prevPitch, emotion, durations.size());
      
      //This iterates through each note that will be in the current measure.
      for (int n = 0; n < pitches.length; n++) {
        //With a pitch and length integer added into the note.
        newMeasure.insertNote(pitches[n], (Integer)durations.get(n));
      }
    } //end if
    
    //Since we now am sure that the current measure is created,
    //  we can add it into the list of measures.
    newSection.insertMeasure(newMeasure);
  } //end for
  
  return newSection;
} //end generateSection()

void onNewUser(int userId)
{
  println("start pose detection!!!!!!");
  kinect.startPoseDetection("Psi", userId);
}

void onEndCalibration(int userId, boolean successful)
{
  if(successful)
  {
    println("User calibrated!!!");
    kinect.startTrackingSkeleton(userId);
  }
  else
  {
    println("Failed to calibrate user!");
    kinect.startPoseDetection("Psi", userId);
  }
}

void onStartPose(String pose, int userId)
{
  println("Started pose for user");
  kinect.stopPoseDetection(userId);
  kinect.requestCalibrationSkeleton(userId, true);
}
