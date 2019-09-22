/*
 *    上位机编码：
 *              aa0120ff    控制Base_Servo转到120°
 *              aa1120ff    控制Left_Servo转到120°
 *              aa2120ff    控制Right_Servo转到120°
 *              aa3120ff    控制Claw_Servo转到120°
 *              aa4120120120120ff  控制四个舵机转动到120°
 *              
 *   舵机引脚：
 *            Base_Servo -- 7
 *            Left_Servo -- 8
 *            Right_Servo -- 9
 *            Claw_Servo -- 10
 */
#include<Servo.h>
//定义舵机名称
Servo Base_Servo;
Servo Left_Servo;
Servo Right_Servo;
Servo Claw_Servo;

//储存舵机上一次的角度
static int angle_a = 0;
static int angle_b = 0;
static int angle_c = 0;
static int angle_d = 0;

String command = "";
int angle = 0;
int angle_1 = 0;
int angle_2 = 0;
int angle_3 = 0;

void setup() 
{
    Serial.begin(115200);
    Base_Servo.attach(7);
    Left_Servo.attach(8);
    Right_Servo.attach(9);
    Claw_Servo.attach(10);
}

void loop() 
{
    command = "";
    while(Serial.available()>0)
    {
      command += char(Serial.read());
      delay(2);
    }
    for(int m = 0;m < command.length();m++)
    {
      if(command[m]=='a' && command[m+1]=='a' && command[m+2]=='0' && command[m+6]=='f' && command[m+7]=='f')
      {
          angle = (command[m+5]-'0')+10*(command[m+4]-'0')+100*(command[m+3]-'0');
          Servo_Base();
      }
       if(command[m]=='a' && command[m+1]=='a' && command[m+2]=='1' && command[m+6]=='f' && command[m+7]=='f')
       {
          angle_1 = (command[m+5]-'0')+10*(command[m+4]-'0')+100*(command[m+3]-'0');  
          Servo_Left();
       }
       if(command[m]=='a' && command[m+1]=='a' && command[m+2]=='2' && command[m+6]=='f' && command[m+7]=='f')
       {
          angle_2 = (command[m+5]-'0')+10*(command[m+4]-'0')+100*(command[m+3]-'0');  
          Servo_Right();
       }
       if(command[m]=='a' && command[m+1]=='a' && command[m+2]=='3' && command[m+6]=='f' && command[m+7]=='f')
       {
          angle_3 = (command[m+5]-'0')+10*(command[m+4]-'0')+100*(command[m+3]-'0');  
          Servo_Claw();
       }
       if(command[m]=='a' && command[m+1]=='a' && command[m+2]=='4' && command[m+15]=='f' && command[m+16]=='f')
       {
          angle = (command[m+5]-'0')+10*(command[m+4]-'0')+100*(command[m+3]-'0');
          angle_1 = (command[m+8]-'0')+10*(command[m+7]-'0')+100*(command[m+6]-'0'); 
          angle_2 = (command[m+11]-'0')+10*(command[m+10]-'0')+100*(command[m+9]-'0');
          angle_3 = (command[m+14]-'0')+10*(command[m+13]-'0')+100*(command[m+12]-'0'); 
          Servo_Base();Servo_Left();Servo_Right();Servo_Claw();  
       }
       
       
    }


}

// 底座舵机运动
void Servo_Base()
{
 
              if(angle >= angle_a)
              {
                if(angle > 180)
                {
                  angle = 180;
                }
                else
                {
                    for(angle_a;angle_a <= angle;angle_a ++)  
                    {
                        Base_Servo.write(angle_a);
                        Serial.print("底座舵机角度：");
                        Serial.println(angle_a);
                        delay(15);
                    }
                }

              }
              else
              {
                if(angle < 0)
                {
                  angle = 0;
                }
                else
                {
                    for(angle_a;angle_a >= angle;angle_a --)
                    {
                        Base_Servo.write(angle_a);
                        Serial.print("底座舵机角度：");
                        Serial.println(angle_a);
                        delay(15);
                    }
                }

              }
              angle_a = angle;
              angle = 0;
     
}

// 左舵机运动
void Servo_Left()
{
                if(angle_1 >= angle_b)
              {
                if(angle_1 > 180)
                {
                  angle_1 = 180;
                }
                else
                {
                    for(angle_b;angle_b <= angle_1;angle_b ++)  
                    {
                        Left_Servo.write(angle_b);
                        Serial.print("左舵机角度：");
                        Serial.println(angle_b);
                        delay(15);
                    }
                }

              }
              else
              {
                if(angle_1 < 0)
                {
                  angle_1 = 0;
                }
                else
                {
                    for(angle_b;angle_b >= angle_1;angle_b --)
                    {
                        Left_Servo.write(angle_b);
                        Serial.print("左舵机角度：");
                        Serial.println(angle_b);
                        delay(15);
                    }
                }

              }
              angle_b = angle_1;
              angle_1 = 0;
}

// 右舵机运动
void Servo_Right()
{
                if(angle_2 >= angle_c)
              {
                if(angle_2 > 180)
                {
                  angle_2 = 180;
                }
                else
                {
                    for(angle_a;angle_c <= angle_2;angle_c ++)  
                    {
                        Right_Servo.write(angle_c);
                        Serial.print("右舵机角度：");
                        Serial.println(angle_c);
                        delay(15);
                    }
                }

              }
              else
              {
                if(angle_2 < 0)
                {
                  angle_2 = 0;
                }
                else
                {
                    for(angle_c;angle_c >= angle_2;angle_c --)
                    {
                        Right_Servo.write(angle_c);
                        Serial.print("右舵机角度：");
                        Serial.println(angle_c);
                        delay(15);
                    }
                }

              }
              angle_c = angle_2;
              angle_2 = 0;
}

//爪子舵机运动
void Servo_Claw()
{
               if(angle_3 >= angle_d)
              {
                if(angle_3 > 180)
                {
                  angle_3 = 180;
                }
                else
                {
                    for(angle_d;angle_d <= angle_3;angle_d ++)  
                    {
                        Claw_Servo.write(angle_d);
                        Serial.print("爪子舵机角度：");
                        Serial.println(angle_d);
                        delay(15);
                    }
                }

              }
              else
              {
                if(angle_3 < 0)
                {
                  angle_3 = 0;
                }
                else
                {
                    for(angle_d;angle_d >= angle_3;angle_d --)
                    {
                        Claw_Servo.write(angle_d);
                        Serial.print("爪子舵机角度：");
                        Serial.println(angle_d);
                        delay(15);
                    }
                }

              }
              angle_d = angle_3;
              angle_3 = 0;
}






















  
