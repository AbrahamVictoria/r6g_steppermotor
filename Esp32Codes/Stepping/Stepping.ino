#include <ros.h>
#include <r6g_steppermotor/Step_Signals.h>

ros::NodeHandle  nh;

int SJ1 = 0; 


void Pasos(r6g_steppermotor::Step_Signals &Steps)
{
  SJ1 = Steps.steps1;
  for(int stps = 0; stps <= SJ1; stps++)
  {
    digitalWrite(13, HIGH);
    delay(200);
    digitalWrite(13, LOW);
    delay(200);
  }
}

ros::Subscriber<r6g_steppermotor::Step_Signals> Micro("Channel",&Pasos);

void setup()
{ 
  pinMode(13, OUTPUT);
  nh.initNode();
  nh.subscribe(Micro);
  digitalWrite(13,LOW);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}
