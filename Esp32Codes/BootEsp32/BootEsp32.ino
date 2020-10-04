/*
  BootEsp32.ino - Firmware ESP32 para control de r6g_steppermotor.
  Autor: Alejandro Tevera Ruiz
  Contacto: atevera.rz@gmail.com
  Lanzada para dominio público en 2020. 
*/

#include<r6gController.h>

//Declaración de clase Robot.
Robot r6g;

//Declaración de clases DoF.
Joint DoF1;
Joint DoF2;
Joint DoF3;
Joint DoF4;
Joint DoF5;
Joint DoF6;

//Almacenamiento de valores de cada articulación.

struct Joints 
{
  float J1, J2, J3, J4, J5, J6;
};

struct Joints FlagAngles = {0,0,0,0,0,0};


void setup()
{
  //Inicialización de monitor serial.
  Serial.begin(9600);

  //Configuración de pines: Dir, Step.
  DoF1.SetPines(23,22);
  DoF2.SetPines(21,19);
  DoF3.SetPines(18,5);
  DoF4.SetPines(17,16);
  DoF5.SetPines(4,15);
  DoF6.SetPines(32,33);

  //Configuración de Relación Mecánica. 
  DoF1.SetRelation(7.1);
  DoF2.SetRelation(5.75);
  DoF3.SetRelation(5);
  DoF4.SetRelation(2.8);
  DoF5.SetRelation(2.1);
  DoF6.SetRelation(1);

  //Configuración de Velocidad Angular Relativa (Método: Delay entre Pasos). 
  DoF1.SetSpeedRotation(4);
  DoF2.SetSpeedRotation(4);
  DoF3.SetSpeedRotation(4);
  DoF4.SetSpeedRotation(2);
  DoF5.SetSpeedRotation(1);
  DoF6.SetSpeedRotation(2);

  //Configuración de Z+ para Modelo DH.
  DoF1.SetPositiveTurn(LOW);
  DoF2.SetPositiveTurn(LOW);
  DoF3.SetPositiveTurn(HIGH);
  DoF4.SetPositiveTurn(HIGH);
  DoF5.SetPositiveTurn(LOW);
  DoF6.SetPositiveTurn(HIGH);

  //Configuración de límites por Software. 
  DoF1.SetSoftwareLimits(-90,90);
  DoF2.SetSoftwareLimits(-60,100);
  DoF3.SetSoftwareLimits(-70,60);
  DoF4.SetSoftwareLimits(-70,70);
  DoF5.SetSoftwareLimits(-70,70);
  DoF6.SetSoftwareLimits(-200,200);

  //Inicialización de ángulos.
  DoF1.SetInitialAngle(0);
  DoF2.SetInitialAngle(-71);
  DoF3.SetInitialAngle(0);
  DoF4.SetInitialAngle(0);
  DoF5.SetInitialAngle(0);
  DoF6.SetInitialAngle(0);

  ResetMotors();

  //Valores iniciales de cada grado de libertad.
  //O = {0,-54,80,0,0,0};
  //N = {0,0,0,0,0,0};

  //Posición Home.
  //float homePosition[6] = {0};
  MoveJ(FlagAngles);
}

void loop()
{
  FlagAngles.J3 = -90; 
  MoveJ(FlagAngles);
  delay(1000);
  FlagAngles.J3 = 0;
  MoveJ(FlagAngles);
  delay(1000);
  /*
  MoveJ(0,mov,0,0,0,0);  
  delay(1000);
  MoveJ(0,0,0,0,0,0);
  delay(1000);
  MoveJ(0,-1*mov,0,0,0,0);  
  delay(1000);
  MoveJ(0,0,0,0,0,0);
  delay(1000);
  */
}

void MoveJ(struct Joints FlagAngles)
{
  //N = {Jn1, Jn2, Jn3, Jn4, Jn5, Jn6};

  //Calculo de pasos para cada articulación. 
  int Steps[6] = {0,0,0,0,0,0};
  Steps[0] = DoF1.DegreesToSteps(FlagAngles.J1);
  Steps[1] = DoF2.DegreesToSteps(FlagAngles.J2);
  Steps[2] = DoF3.DegreesToSteps(FlagAngles.J3);
  Steps[3] = DoF4.DegreesToSteps(FlagAngles.J4);
  Steps[4] = DoF5.DegreesToSteps(FlagAngles.J5);
  Steps[5] = DoF6.DegreesToSteps(FlagAngles.J6);

  //Cálculo del máximo número de pasos.
  int Pmax = r6g.MaxDegrees(Steps);

  //Envío de pulsos a cada Driver.
  for(int i = 0; i <= Pmax; i++)
  {
    DoF1.AngularMove(FlagAngles.J1,Steps[0],i);
    DoF2.AngularMove(FlagAngles.J2,Steps[1],i);
    DoF3.AngularMove(FlagAngles.J3,Steps[2],i);
    DoF4.AngularMove(FlagAngles.J4,Steps[3],i);
    DoF5.AngularMove(FlagAngles.J5,Steps[4],i);
    DoF6.AngularMove(FlagAngles.J6,Steps[5],i);
  }

  ResetMotors();

  DoF1.Synchronize(FlagAngles.J1);
  DoF2.Synchronize(FlagAngles.J2);
  DoF3.Synchronize(FlagAngles.J3);
  DoF4.Synchronize(FlagAngles.J4);
  DoF5.Synchronize(FlagAngles.J5);
  DoF6.Synchronize(FlagAngles.J6);

  //for(int a = 0; a < 6; a++) Serial.print(String(FlagAngles[a]) + " ");

  //Serial.println("");
  
}

void ResetMotors()
{
  //Reestablecimiento de motores a paso.
  DoF1.Shutdown();
  DoF2.Shutdown();
  DoF3.Shutdown();
  DoF4.Shutdown();
  DoF5.Shutdown();
  DoF6.Shutdown();
}
