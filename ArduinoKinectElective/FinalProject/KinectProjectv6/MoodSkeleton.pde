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



import java.util.Iterator;
import java.util.Map;

class PoseRule
{
  //In MORE/LESS_THAN_ANGLE joint relations
  //  This will be the base joint for creating
  //  an artificial vector to find the angle of the
  //  joints.
  int fromJoint;
  int toJoint;
  PVector fromJointVector;
  PVector toJointVector;
  int jointRelation;
  //This will hold the distance or angle(in degrees)
  //  associated with the WITHIN, AWAY_FROM, 
  //  MORE/LESS_THAN_ANGLE joint relations.
  //It also holds thhresholds for other rules
  //  that need it.
  int threshold;
  
  SimpleOpenNI context;

  static final int ABOVE = 1;
  static final int BELOW = 2;
  static final int LEFT_OF = 3;
  static final int RIGHT_OF = 4;
  static final int IN_FRONT = 5;
  static final int BEHIND = 6;
  static final int WITHIN = 7;
  static final int AWAY_FROM = 8;
  static final int MORE_THAN_ANGLE = 9;
  static final int LESS_THAN_ANGLE = 10;
 
  
  PoseRule(SimpleOpenNI tempContext,
           int tempFromJoint,
           int tempJointRelation,
           int tempToJoint,
           int tempThreshold)
  {
    context = tempContext;
    fromJoint = tempFromJoint;
    toJoint = tempToJoint;
    jointRelation = tempJointRelation;
    threshold = tempThreshold;
    
    fromJointVector = new PVector();
    toJointVector = new PVector();
  }
    
  //@return Returns true if the instance's rule is shown to
  //  be observed true. And it returns false if the rule
  //  is false.
  boolean check(int userID)
  {
    context.getJointPositionSkeleton(userID, fromJoint, fromJointVector);
    context.getJointPositionSkeleton(userID, toJoint, toJointVector);
    
    boolean result = false;
    
    switch(jointRelation)
    {
      case ABOVE:
        result = (fromJointVector.y > toJointVector.y);
        break;
      case BELOW:
        result = (fromJointVector.y < toJointVector.y);
        break;
      case LEFT_OF:
        result = (fromJointVector.x < toJointVector.x);
        break;
      case RIGHT_OF:
        result = (fromJointVector.x > toJointVector.x);
        break;
      case IN_FRONT:
        result = (fromJointVector.z < toJointVector.z);
        break;
      case BEHIND:
        result = (fromJointVector.z > toJointVector.z);
        break;
      case WITHIN:
        result = (PVector.sub(fromJointVector, toJointVector).mag()  <= threshold);
        break;
      case AWAY_FROM:
        result = (PVector.sub(fromJointVector, toJointVector).mag()  > threshold);
        //println("Distance: " + PVector.sub(fromJointVector, toJointVector).mag());
        break;
      //This compares a vector that's straight up and down with the vector between the
      //  two joints to find the angle between them. Then depending on the angle,
      //  we'll return true or false.
      case MORE_THAN_ANGLE:
        PVector verticalVector = new PVector();
        verticalVector.set(0, PVector.sub(fromJointVector, toJointVector).mag(), 0);
        //calculateAngle is passed a vertical vector and the vector between the two joints.
        int angle = (int)calculateAngle(verticalVector, PVector.sub(fromJointVector, toJointVector));
        
        if ( angle > threshold )
        {
          result = true;
        }
        else
        {
          result = false;
        };
        break;
      //This compares a vector that's straight up and down with the vector between the
      //  two joints to find the angle between them. Then depending on the angle,
      //  we'll return true or false.
      case LESS_THAN_ANGLE:
        PVector verticalVector2 = new PVector();
        verticalVector2.set(0, PVector.sub(fromJointVector, toJointVector).mag(), 0);
        //calculateAngle is passed a vertical vector and the vector between the two joints.
        int angle2 = (int)calculateAngle(verticalVector2, PVector.sub(fromJointVector, toJointVector));
        
        if ( angle2 <= threshold )
        {
          result = true;
        }
        else
        {
          result = false;
        };
        break;
    }
    return result;
  }
  
  //This should use law of cosines to find the angle
  //  between the two vectors.
  //The parameters are assumed to be the actual vectors
  //  that the angles are found between (not with respect to
  //  global a position.)
  float calculateAngle(PVector vec1, PVector vec2) {
    //Grab the distances of the vectors
    float a = vec1.mag();
    
    float b = vec2.mag();
    
    //Gets the distance of the hypotenuse.
    float c = PVector.sub(vec1, vec2).mag();
    
    float C = degrees(acos((a*a + c*c - b*b)/(2*a*c)));
    
    //println("Angle: " + C);
    
    //This returns the outcome of the law of cosines calculation for the
    //  angle between the vectors.
    return C;
  }
}





//Each LimbPose represents the position of a limb with respect to an emotion.
//There should be (numBodyParts * numEmotions) LimbPose instances. 
class LimbPose {
  //This holds all of the rules that are associated with this limbPose.
  ArrayList rules;
  
  //This will let us know what emotion
  //  this limbPose represents, so that
  //  we can draw the limb in the right color.
  String emotion;
  
  LimbPose(String tmpEmotion) {
    
    rules = new ArrayList();
    
    emotion = tmpEmotion;
  }
  
  void addRule(PoseRule newRule) {
    rules.add(newRule);
  }
  
  String getEmotion() {
    return emotion;
  }
  
  //@return Returns true if all of the containing rules
  //  are observed as true.
  boolean check(int userID)
  {
    boolean result = true;
    for (int i = 0; i < rules.size(); i++)
    {
      PoseRule rule = (PoseRule)rules.get(i);
      result = result && rule.check(userID);
    }
    return result;
  }
}




//This essentially draws a line between the given jointTypes (which
//  are defined by SimpleOpenNI.)
void drawLimb(int userId, int jointType1, int jointType2)
{
  PVector jointPos1 = new PVector();
  PVector jointPos2 = new PVector();
  float confidence;
  
  confidence = kinect.getJointPositionSkeleton(userId, jointType1, jointPos1);
  kinect.convertRealWorldToProjective(jointPos1, jointPos1);
  
  confidence += kinect.getJointPositionSkeleton(userId, jointType2, jointPos2);
  kinect.convertRealWorldToProjective(jointPos2, jointPos2);

  line(jointPos1.x, jointPos1.y, jointPos2.x, jointPos2.y);
}


//One instance of this can account for all of the emotions
//  and parts of one body.
class MoodSkeleton
{
  SimpleOpenNI context;
  
  //These will hold rules for the individual
  //  limbs that make up the MoodSkeleton.
  HashMap lArmPoses;
  HashMap rArmPoses;
  HashMap lLegPoses;
  HashMap rLegPoses;
  HashMap torsoPoses;
  HashMap headPoses;
  
  //These are the different parts that make up
  //  the mood skeleton. These are commonly used
  //  as arguments for methods in this class, because
  //  it makes it easier to use the class.
  static final int ALL_THE_LIMBS = -1;
  static final int LARM = 0;
  static final int RARM = 1;
  static final int LLEG = 2;
  static final int RLEG = 3;
  static final int TORSO = 4;
  static final int HEAD = 5;
  
  //These are rgb colors that represent 
  //  an emotion.
  //The first level of the array specifies
  //  the color.
  //The second level specifies the rgb value.
  int[][] emotionColors = { {255, 255, 255},   //white
                            {254, 254, 34},    //Yellow
                            {65, 105, 225},    //blue
                            {156, 0, 0},       //red
                            {59, 248, 89} }; //green
  
  //These are the compatible emotions for this 
  //  specific class.
  static final int VOID = 0;
  static final int HAPPY = 1;
  static final int SAD = 2;
  static final int ANGER = 3;
  static final int DISGUST = 4;
  
  //Constructor
  //@param context This will be the SimpleOpenNI object
  //  that the program is using (there's only one of them.)
  MoodSkeleton(SimpleOpenNI context)
  {
    this.context = context;
    
    //These will store the LimbPose instances
    //  for each of the different parts of the body.
    lArmPoses = new HashMap();
    rArmPoses = new HashMap();
    lLegPoses = new HashMap();
    rLegPoses = new HashMap();
    torsoPoses = new HashMap();
    headPoses = new HashMap();
  }
  
  //@param limb This is the limb that this rule will be associated with. 
  //  This limb can be irrelivant to the joints being used for the rule.
  //@param emotion This is the emotion that the rule will be associated with.
  //@param fromJoint This is essentially the first of two joints that will be
  //  compared according to the jointRelation.
  //@param jointRelation This will be one of the joint relations defined within 
  //  the poseRule class. It specifies the type of rule essentially.
  //@param toJoint This is the second of two joints that will be
  //  compared according to the jointRelation.
  //@param jointVariable
  void addRule(int limb,
               String emotion,
               int fromJoint,
               int jointRelation,
               int toJoint,
               int threshold)
  {
    switch(limb) {
      case LARM:
        if (!lArmPoses.containsKey(emotion)) {
          LimbPose newPose = new LimbPose(emotion);
          lArmPoses.put(emotion, newPose);          
        }
        //Add a rule to the pose.
        PoseRule rule1 = new PoseRule(context, fromJoint, jointRelation, toJoint, threshold);
        ((LimbPose)lArmPoses.get(emotion)).addRule(rule1);  
        break;
        
      case RARM:
        if (!rArmPoses.containsKey(emotion)) {
          LimbPose newPose = new LimbPose(emotion);
          rArmPoses.put(emotion, newPose);          
        }
        //Add a rule to the pose.
        PoseRule rule2 = new PoseRule(context, fromJoint, jointRelation, toJoint, threshold);
        ((LimbPose)rArmPoses.get(emotion)).addRule(rule2);  
        break;
        
      case LLEG:
        if (!lLegPoses.containsKey(emotion)) {
          LimbPose newPose = new LimbPose(emotion);
          lLegPoses.put(emotion, newPose);          
        }
        //Add a rule to the pose.
        PoseRule rule3 = new PoseRule(context, fromJoint, jointRelation, toJoint, threshold);
        ((LimbPose)lLegPoses.get(emotion)).addRule(rule3);  
        break;
        
      case RLEG:
        if (!rLegPoses.containsKey(emotion)) {
          LimbPose newPose = new LimbPose(emotion);
          rLegPoses.put(emotion, newPose);          
        }
        //Add a rule to the pose.
        PoseRule rule4 = new PoseRule(context, fromJoint, jointRelation, toJoint, threshold);
        ((LimbPose)rLegPoses.get(emotion)).addRule(rule4);  
        break;
        
      case TORSO:
        if (!torsoPoses.containsKey(emotion)) {
          LimbPose newPose = new LimbPose(emotion);
          torsoPoses.put(emotion, newPose);          
        }
        //Add a rule to the pose.
        PoseRule rule5 = new PoseRule(context, fromJoint, jointRelation, toJoint, threshold);
        ((LimbPose)torsoPoses.get(emotion)).addRule(rule5);  
        break;
      case HEAD:
        if (!headPoses.containsKey(emotion)) {
          LimbPose newPose = new LimbPose(emotion);
          headPoses.put(emotion, newPose);          
        }
        //Add a rule to the pose.
        PoseRule rule6 = new PoseRule(context, fromJoint, jointRelation, toJoint, threshold);
        ((LimbPose)headPoses.get(emotion)).addRule(rule6);  
        break; 
    }
  }
  
  //@param userId This userId is needed when querying the SimpleOpenNI object
  //  for information on the user.
  //@param currentEmotion This is needed to be passed along to the
  //  getMostProminentEmo() method (which is in this class.)
  void drawSkeleton(int userId,
                    String currentEmotion) {
    //Change the color for the head.
    if (getMostProminentEmo(userId, HEAD, currentEmotion) == "VOID") {
      stroke(emotionColors[VOID][0], emotionColors[VOID][1], emotionColors[VOID][2]);
    }
    else if (getMostProminentEmo(userId, HEAD, currentEmotion) == "HAPPY"){
      stroke(emotionColors[HAPPY][0], emotionColors[HAPPY][1], emotionColors[HAPPY][2]);
    }
    else if (getMostProminentEmo(userId, HEAD, currentEmotion) == "SAD"){
      stroke(emotionColors[SAD][0], emotionColors[SAD][1], emotionColors[SAD][2]);
    }
    else if (getMostProminentEmo(userId, HEAD, currentEmotion) == "ANGER"){
      stroke(emotionColors[ANGER][0], emotionColors[ANGER][1], emotionColors[ANGER][2]);
    }
    else if (getMostProminentEmo(userId, HEAD, currentEmotion) == "DISGUST"){
      stroke(emotionColors[DISGUST][0], emotionColors[DISGUST][1], emotionColors[DISGUST][2]);
    }
    drawLimb(userId, SimpleOpenNI.SKEL_HEAD,
                            SimpleOpenNI.SKEL_NECK);
            
    //Change the color for the torso.
    if (getMostProminentEmo(userId, TORSO, currentEmotion) == "VOID") {
      stroke(emotionColors[VOID][0], emotionColors[VOID][1], emotionColors[VOID][2]);
    }
    else if (getMostProminentEmo(userId, TORSO, currentEmotion) == "HAPPY"){
      stroke(emotionColors[HAPPY][0], emotionColors[HAPPY][1], emotionColors[HAPPY][2]);
    }
    else if (getMostProminentEmo(userId, TORSO, currentEmotion) == "SAD"){
      stroke(emotionColors[SAD][0], emotionColors[SAD][1], emotionColors[SAD][2]);
    }
    else if (getMostProminentEmo(userId, TORSO, currentEmotion) == "ANGER"){
      stroke(emotionColors[ANGER][0], emotionColors[ANGER][1], emotionColors[ANGER][2]);
    }
    else if (getMostProminentEmo(userId, TORSO, currentEmotion) == "DISGUST"){
      stroke(emotionColors[DISGUST][0], emotionColors[DISGUST][1], emotionColors[DISGUST][2]);
    }
    drawLimb(userId, SimpleOpenNI.SKEL_NECK,
                            SimpleOpenNI.SKEL_LEFT_SHOULDER);
    
    drawLimb(userId, SimpleOpenNI.SKEL_NECK,
                            SimpleOpenNI.SKEL_RIGHT_SHOULDER);
    
    drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER,
                            SimpleOpenNI.SKEL_TORSO);
                            
    drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER,
                            SimpleOpenNI.SKEL_TORSO);
                            
    drawLimb(userId, SimpleOpenNI.SKEL_TORSO,
                            SimpleOpenNI.SKEL_LEFT_HIP);
  
    drawLimb(userId, SimpleOpenNI.SKEL_TORSO,
                            SimpleOpenNI.SKEL_RIGHT_HIP);
                            
    //Change the color for the left leg.
    if (getMostProminentEmo(userId, LLEG, currentEmotion) == "VOID") {
      stroke(emotionColors[VOID][0], emotionColors[VOID][1], emotionColors[VOID][2]);
    }
    else if (getMostProminentEmo(userId, LLEG, currentEmotion) == "HAPPY"){
      stroke(emotionColors[HAPPY][0], emotionColors[HAPPY][1], emotionColors[HAPPY][2]);
    }
    else if (getMostProminentEmo(userId, LLEG, currentEmotion) == "SAD"){
      stroke(emotionColors[SAD][0], emotionColors[SAD][1], emotionColors[SAD][2]);
    }
    else if (getMostProminentEmo(userId, LLEG, currentEmotion) == "ANGER"){
      stroke(emotionColors[ANGER][0], emotionColors[ANGER][1], emotionColors[ANGER][2]);
    }
    else if (getMostProminentEmo(userId, LLEG, currentEmotion) == "DISGUST"){
      stroke(emotionColors[DISGUST][0], emotionColors[DISGUST][1], emotionColors[DISGUST][2]);
    }
    drawLimb(userId, SimpleOpenNI.SKEL_LEFT_HIP,
                            SimpleOpenNI.SKEL_LEFT_KNEE);
    drawLimb(userId, SimpleOpenNI.SKEL_LEFT_KNEE,
                            SimpleOpenNI.SKEL_LEFT_FOOT);
                            
    //Change the color for the right leg.
    if (getMostProminentEmo(userId, RLEG, currentEmotion) == "VOID") {
      stroke(emotionColors[VOID][0], emotionColors[VOID][1], emotionColors[VOID][2]);
    }
    else if (getMostProminentEmo(userId, RLEG, currentEmotion) == "HAPPY"){
      stroke(emotionColors[HAPPY][0], emotionColors[HAPPY][1], emotionColors[HAPPY][2]);
    }  
    else if (getMostProminentEmo(userId, RLEG, currentEmotion) == "SAD"){
      stroke(emotionColors[SAD][0], emotionColors[SAD][1], emotionColors[SAD][2]);
    }  
    else if (getMostProminentEmo(userId, RLEG, currentEmotion) == "ANGER"){
      stroke(emotionColors[ANGER][0], emotionColors[ANGER][1], emotionColors[ANGER][2]);
    }  
    else if (getMostProminentEmo(userId, RLEG, currentEmotion) == "DISGUST"){
      stroke(emotionColors[DISGUST][0], emotionColors[DISGUST][1], emotionColors[DISGUST][2]);
    }  
    drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_HIP,
                            SimpleOpenNI.SKEL_RIGHT_KNEE);
    drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_KNEE,
                            SimpleOpenNI.SKEL_RIGHT_FOOT);
                            
    //Change the color for the left arm.
    if (getMostProminentEmo(userId, LARM, currentEmotion) == "VOID") {
      stroke(emotionColors[VOID][0], emotionColors[VOID][1], emotionColors[VOID][2]);
    }
    else if (getMostProminentEmo(userId, LARM, currentEmotion) == "HAPPY"){
      stroke(emotionColors[HAPPY][0], emotionColors[HAPPY][1], emotionColors[HAPPY][2]);
    }
    else if (getMostProminentEmo(userId, LARM, currentEmotion) == "SAD"){
      stroke(emotionColors[SAD][0], emotionColors[SAD][1], emotionColors[SAD][2]);
    }
    else if (getMostProminentEmo(userId, LARM, currentEmotion) == "ANGER"){
      stroke(emotionColors[ANGER][0], emotionColors[ANGER][1], emotionColors[ANGER][2]);
    }
    else if (getMostProminentEmo(userId, LARM, currentEmotion) == "DISGUST"){
      stroke(emotionColors[DISGUST][0], emotionColors[DISGUST][1], emotionColors[DISGUST][2]);
    }
    drawLimb(userId, SimpleOpenNI.SKEL_LEFT_SHOULDER,
                            SimpleOpenNI.SKEL_LEFT_ELBOW);
    drawLimb(userId, SimpleOpenNI.SKEL_LEFT_ELBOW,
                            SimpleOpenNI.SKEL_LEFT_HAND);
                            
    //Change the color for the right arm.
    if (getMostProminentEmo(userId, RARM, currentEmotion) == "VOID") {
      stroke(emotionColors[VOID][0], emotionColors[VOID][1], emotionColors[VOID][2]);
    }
    else if (getMostProminentEmo(userId, RARM, currentEmotion) == "HAPPY"){
      stroke(emotionColors[HAPPY][0], emotionColors[HAPPY][1], emotionColors[HAPPY][2]);
    }
    else if (getMostProminentEmo(userId, RARM, currentEmotion) == "SAD"){
      stroke(emotionColors[SAD][0], emotionColors[SAD][1], emotionColors[SAD][2]);
    }
    else if (getMostProminentEmo(userId, RARM, currentEmotion) == "ANGER"){
      stroke(emotionColors[ANGER][0], emotionColors[ANGER][1], emotionColors[ANGER][2]);
    }
    else if (getMostProminentEmo(userId, RARM, currentEmotion) == "DISGUST"){
      stroke(emotionColors[DISGUST][0], emotionColors[DISGUST][1], emotionColors[DISGUST][2]);
    }
    drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_SHOULDER,
                            SimpleOpenNI.SKEL_RIGHT_ELBOW);
    drawLimb(userId, SimpleOpenNI.SKEL_RIGHT_ELBOW,
                            SimpleOpenNI.SKEL_RIGHT_HAND);
  }
  
  //@return An integer that symbolizes how many body parts are all
  //  signaling the given emotion through their poses.
  //@param userID This is essential for querying information
  //  from the SimpleOpenNI object.
  //@param limb This is the limb that is being targeted and
  //  -1 will mean that all limbs are targeted. There are
  //  static integers defined in this class that can be passed
  //  to this parameter.
  // @param emotion This is the emotion that will be looked for
  //  within the LimbPose classes.
  int getDegreeOfEmotion(int userID, int limb, String emotion) {
    int sum = 0;
    
    Iterator[] iter = new Iterator[6];
    
    //Putting these iterators into an array
    //  makes the rest of the code loopable.
    iter[0] = lArmPoses.entrySet().iterator();
    iter[1] = rArmPoses.entrySet().iterator();
    iter[2] = lLegPoses.entrySet().iterator();
    iter[3] = rLegPoses.entrySet().iterator();
    iter[4] = torsoPoses.entrySet().iterator();
    iter[5] = headPoses.entrySet().iterator();
    
    int limbs = 0;
    
    //Check if we're getting emotions for all limbs
    if (limb == -1) {
      //This makes all limbs used in the below loop.
      limb = 0;
      limbs = 6;
    }
    else if (limb >= 0 && limb < 6) {
      //This just makes it so that just the given limb
      //  is used in the below loop.
      limbs = limb + 1;
    }
    
    //Loop through all different LimbPose hashmaps.
    for (int indx = limb; indx < limbs; indx++) {
      //Loop through the LimbPoses within the current hashmap.
      while(iter[indx].hasNext()) {
        Map.Entry curPose = (Map.Entry)iter[indx].next();
        //Checks to see if the LimbPose has the right emotion AND
        //  is being followed currently.
        if (((LimbPose)curPose.getValue()).getEmotion() == emotion
        && ((LimbPose)curPose.getValue()).check(userID)) {
          sum += 1;
        }
      }
    }
    
    return sum;
  }
 
  //This will  
  //@param userId This is essential for querying information from
  //  the SimpleOpenNI object.
  ///@param limb This can either make the returned 
  ///  detectedEmotions for a specific limb. Or if -1 is
  ///  used, all of the limbs will be looked through.
  ArrayList getDetectedEmotions(int userId, int limb) {
    ArrayList emotionsDetected = new ArrayList();

    Iterator[] iter = new Iterator[6];
    
    //Putting these iterators into an array
    //  makes the rest of the code loopable.
    //All of these might not even be used.
    iter[0] = lArmPoses.entrySet().iterator();
    iter[1] = rArmPoses.entrySet().iterator();
    iter[2] = lLegPoses.entrySet().iterator();
    iter[3] = rLegPoses.entrySet().iterator();
    iter[4] = torsoPoses.entrySet().iterator();
    iter[5] = headPoses.entrySet().iterator();

    int limbs = 0;
    
    //Check if we're getting emotions for all limbs
    if (limb == -1) {
      //This makes all limbs used in the below loop.
      limb = 0;
      limbs = 6;
    }
    else if (limb >= 0 && limb < 6) {
      //This just makes it so that just the given limb
      //  is used in the below loop.
      limbs = limb + 1;
    }
    
    
    //Loop through all different LimbPose hashmaps.
    for (int indx = limb; indx < limbs; indx++) {
      //Loop through the LimbPoses within the current hashmap.
      while(iter[indx].hasNext()) {
        Map.Entry curPose = (Map.Entry)iter[indx].next();
        //Checks to see if the LimbPose is being followed currently
        if (((LimbPose)curPose.getValue()).check(userId)) {
          //Add the LimbPose's emotion to the detectedEmotions.
          emotionsDetected.add(((LimbPose)curPose.getValue()).getEmotion());
        }
      }
    }    

    return emotionsDetected;
  }
  
  
  //@return A string that represents the emotion that is most prominent.
  //@param userId Crucial for querying info from the SimpleOpenNI class.
  //@param limb This specifies the limb that will be targeted. The static integers
  //  defined in this class are compatible and can be passed to this parameter.
  //@param currentEmotion This is the current emotion and is only used to
  //  make it harder to change emotions than to keep them the same.
  String getMostProminentEmo(int userId, int limb, String currentEmotion) {
    //The -1 says that we're getting the detectedEmotions from
    //  all of the limbs.
    ArrayList emotionsDetected = getDetectedEmotions(userId, limb);

    //This makes it so that the signal count has to be
    //  strictly greater than the currentEmotion's signals. 
    String mostProminentEmo = currentEmotion;
  
    //Checks if more than one emotion is showing up.
    if (emotionsDetected.size() > 1) {
      for(int i = 0; i < emotionsDetected.size(); i++) {
        //Compares the mostProminantEmotion with the current one
        //  at the ith position of the emotionsDetected ArrayList.
        if (getDegreeOfEmotion(userId, limb, mostProminentEmo)
        < getDegreeOfEmotion(userId, limb, (String)emotionsDetected.get(i))) {
          mostProminentEmo = (String)emotionsDetected.get(i);
        }
      }
    }
    else if (emotionsDetected.size() == 1) {
      mostProminentEmo = (String)emotionsDetected.get(0);
    }
    else {
      mostProminentEmo = "VOID";
    }
    
    return mostProminentEmo;
  }
}
