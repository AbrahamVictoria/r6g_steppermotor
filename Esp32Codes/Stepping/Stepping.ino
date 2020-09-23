#include <ros.h>
#include <std_msgs/Int64MultiArray.h>

ros::NodeHandle  nh;



int SJ1 = 0; 

void Pasos( const std_msgs::Int64MultiArray& Steps)
{
  SJ1 = Steps.data[0];
  for(int stps = 0; stps <= SJ1; stps++)
  {
    digitalWrite(13, HIGH);
    delay(200);
    digitalWrite(13, LOW);
    delay(200);
  }
}

ros::Subscriber<std_msgs::Int64MultiArray> Micro("Channel",&Pasos);

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
