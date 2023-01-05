#define PI 3.1415926535897932384626433832795
int enX = 8 ;
int dirX = 5 ;
int stepX = 10 ;
int enY = 9 ;
int dirY = 6 ;
int stepY = 11 ;
int enZ = 4 ;
int dirZ = 12;
int stepZ = 13 ;
int endY=2;
int endX=3;
int state=99;
String input;
double temp1=0;
double temp2=0;
double t11=0;
double t22=0;
double temp11=0;
double temp22=0;
float tempy=42.857;
float tempy2=tempy/2;
float list5x[]={120,60,0,-60,-120}; 
float list5y[]={400,340,280,220,160};
float list7x[]={3*tempy,2*tempy,tempy,0,-tempy,-2*tempy,-3*tempy};
float list7y[]={140+13*tempy/2,140+11*tempy/2,140+9*tempy/2,140+7*tempy/2,140+5*tempy/2,140+3*tempy/2,140+tempy/2};
int d=0;
int r=0;
void setup() {
  Serial.begin(9600);
  pinMode(enX,OUTPUT); 
  pinMode(stepX,OUTPUT); 
  pinMode(dirX,OUTPUT); 
  digitalWrite(enX,LOW); 
  pinMode(enY,OUTPUT); 
  pinMode(stepY,OUTPUT); 
  pinMode(dirY,OUTPUT); 
  digitalWrite(enY,LOW); 
  pinMode(enZ,OUTPUT); 
  pinMode(stepZ,OUTPUT); 
  pinMode(dirZ,OUTPUT); 
  digitalWrite(enZ,LOW);
  pinMode(endX,INPUT_PULLUP);
  pinMode(endY,INPUT_PULLUP);
  attachInterrupt(1,setX,LOW);
  attachInterrupt(0,setY,LOW);
}
void loop() {
  input=Serial.readStringUntil('\n');
//  String inpX =input.substring(0,4);
//  int inpX1=inpX.toInt();
//  String inpY =input.substring(4,8);
//  int inpY1=inpY.toInt();
//  String inpZ =input.substring(8,13);
//  int inpZ1=inpZ.toInt();
  String play=input.substring(0,1);
  int play1=play.toInt();
  String row=input.substring(1,2);
  int row1=row.toInt();
  String col=input.substring(2,3);
  int col1=col.toInt();
  String board=input.substring(3,4);
  int board1=board.toInt();
  
//  if (inpX1!=0 || inpY1!=0 ||inpZ1!=0){
//    state=99;
//    movez(inpZ1);
//    move(inpX1,inpY1);   
//  }
  if (play1!=0 || row1!=0 || col1!=0|| board1!=0){
    state=99;
    if (board1==5){
      r=20;
      d=5000;
      if (play1==2){
      circle(list5x[row1],list5y[col1]);
      }
      if (play1==1){
      cross(list5x[row1],list5y[col1]);
      }  
    }
    if (board1==7){
      r=14;
      d=5000;
      if (play1==2){
      circle(list7x[row1],list7y[col1]);
      }
      if (play1==1){
      cross(list7x[row1],list7y[col1]);
      }  
    }
    if (board1==1){
      move(-360,0);
    }
  }
}
void move(float angelX,float angelY){
  float pulseX=abs(angelX)*31.08;
  float pulseY_ro=abs(angelY)*51.771;
  float pulseY_sup=abs(angelX)*51.771*0.532;
  float pulseY;
  float higher_stepper;
  float lower_stepper;
  
  if (angelX<0){
    digitalWrite(dirX, HIGH);
    if (angelY==0){
      digitalWrite(dirY, HIGH);
      pulseY=pulseY_ro+pulseY_sup;
      }
    if (angelY<0){
      digitalWrite(dirY, HIGH);
      pulseY=pulseY_ro+pulseY_sup;
      }
    if (angelY>0){
      if (pulseY_ro>pulseY_sup){
        digitalWrite(dirY, LOW);
        pulseY=pulseY_ro-pulseY_sup;
        }
      if (pulseY_ro<pulseY_sup){
        digitalWrite(dirY, HIGH);
        pulseY=-pulseY_ro+pulseY_sup;
        }  
      }
    }
  if (angelX>0){
    digitalWrite(dirX, LOW);
    if (angelY==0){
      digitalWrite(dirY, LOW);
      pulseY=pulseY_ro+pulseY_sup;
      }
    if (angelY>0){
      digitalWrite(dirY, LOW);
      pulseY=pulseY_ro+pulseY_sup;
      }
    if (angelY<0){
      if (pulseY_ro>pulseY_sup){
        digitalWrite(dirY, HIGH);
        pulseY=pulseY_ro-pulseY_sup;
        }
      if (pulseY_ro<pulseY_sup){
        digitalWrite(dirY, LOW);
        pulseY=-pulseY_ro+pulseY_sup;
        }  
      }
    }
  if (angelX==0){
    if (angelY<0){
      digitalWrite(dirY, HIGH);
      pulseY=pulseY_ro+pulseY_sup;
    }
    if (angelY>0){
      digitalWrite(dirY, LOW);
      pulseY=pulseY_ro+pulseY_sup;
    }  
  } 
    
  int higher_steppin;
  int lower_steppin;

  if (pulseX > pulseY){
    higher_stepper = pulseX;
    lower_stepper = pulseY;
    higher_steppin = stepX;
    lower_steppin =stepY;
    }
  
  if (pulseX < pulseY){
    higher_stepper = pulseY;
    lower_stepper = pulseX;
    higher_steppin = stepY;
    lower_steppin =stepX;
    }
  else{
    higher_stepper = pulseX;
    lower_stepper = pulseY;
    higher_steppin = stepX;
    lower_steppin =stepY;
    }
  
  float rate=higher_stepper/lower_stepper;
  int temp=0;

  for (int i=0;i<=higher_stepper;i++){
    if(i/rate-temp>=1){
      digitalWrite(lower_steppin,HIGH); 
      temp++;
      }
    if(state==0){
      break;}
    digitalWrite(higher_steppin,HIGH);
    delay(1); 
    digitalWrite(higher_steppin,LOW); 
    digitalWrite(lower_steppin,LOW);
    delay(1);  
    }    
}

void movez(float L_Z){
  if (L_Z<0){
    digitalWrite(dirZ,HIGH);
    }
  if (L_Z>0){
    digitalWrite(dirZ,LOW);
    }
  for (int i=0;i<=abs(L_Z);i++){
    digitalWrite(stepZ,HIGH); 
    delay(1);  
    digitalWrite(stepZ,LOW);
    delay(1);  
    }  
}
void circle(float a,float b){
  
  double x;
  double y;

  float a1=235;
  float a2=245;
  double t1;
  double t2;
  for (double i=0;i<2*PI+4*PI/25;i=i+2*PI/25){
      if(i==2*PI/25){
        movez(-d);
        }
      x=r*cos(i)+a;
      y=r*sin(i)+b;
      t2=acos((x*x+y*y-a1*a1-a2*a2)/(2*a1*a2));
      if (x>0 && y>0){
        t1=atan(y/x)-asin((a2*sin(t2))/sqrt(x*x+y*y));
      }
      if (x<0 && y>0){
        t1=atan(y/x)-asin((a2*sin(t2))/sqrt(x*x+y*y))+PI;
      }
      if (t1<(-25*PI/180) || t1>(205*PI/180)){
        t2=-t2;
        t1=atan(y/x)-asin((a2*sin(t2))/sqrt(x*x+y*y));
      }
  t1=t1*180/PI;
  t2=t2*180/PI;
  t11=t1;
  t22=t2;
  t1=t1-temp1;
  t2=t2-temp2;
  temp1=t11;
  temp2=t22;
  move(t1,t2);
  }
  movez(d);
  move(-t11,-t22);
  temp1=0;
  temp2=0;
  t11=0;
  t22=0;
  temp11=0;
  temp22=0;
}
void line(float xA,float yA,float xB,float yB){
  double x;
  double y;
  float a1=235;
  float a2=250;
  double t1;
  double t2;
  for (double i=0;i<1+0.01;i=i+0.01){
      if(i==0.01){
        movez(-d);
        }
      x=(xB-xA)*i+xA;
      y=(yB-yA)*i+yA;
      t2=acos((x*x+y*y-a1*a1-a2*a2)/(2*a1*a2));
      if (x>0 && y>0){
        t1=atan(y/x)-asin((a2*sin(t2))/sqrt(x*x+y*y));
      }
      if (x<0 && y>0){
        t1=atan(y/x)-asin((a2*sin(t2))/sqrt(x*x+y*y))+PI;
      }
      if (t1<(-25*PI/180) || t1>(205*PI/180)){
        t2=-t2;
        t1=atan(y/x)-asin((a2*sin(t2))/sqrt(x*x+y*y));
      }
    
  t1=t1*180/PI;
  t2=t2*180/PI;
  t11=t1;
  t22=t2;
  t1=t1-temp1;
  t2=t2-temp2;
  temp1=t11;
  temp2=t22;
  move(t1,t2);
  }
  movez(d);
}
void cross(float a, float b){

  line(a-r,b+r/2,a+r/4,b-r);
  delay(100);
  line(a+r/4,b+r,a-r,b-r);
  move(-300,0);
  temp1=0;
  temp2=0;
  t11=0;
  t22=0;
  temp11=0;
  temp22=0;
  }
      
void setX(){
  state=0;
  float pulseX=24.5*31.08;
  float pulseY_ro=0*51.771;
  float pulseY_sup=24.5*51.771*0.532;
  float pulseY;
  digitalWrite(dirX, LOW);
  digitalWrite(dirY, LOW);
  pulseY=pulseY_ro+pulseY_sup;
  float rate=pulseY/pulseX;
  int temp=0;
  for (int i=0;i<=pulseX;i++){
    if(i/rate-temp>=1){
      digitalWrite(stepY,HIGH); 
      temp++;
      }
    digitalWrite(stepX,HIGH);
    delay(1); 
    digitalWrite(stepY,LOW); 
    digitalWrite(stepX,LOW);
    delay(1);  
    }
  digitalWrite(dirY, LOW);
  pulseX=0;
  pulseY=360*51.771;
  rate=pulseY/pulseX;
  temp=0;
  for (int i=0;i<=pulseY;i++){
    if(i/rate-temp>=1){
      digitalWrite(stepX,HIGH); 
      temp++;
      }
    if(digitalRead(endY)==0){
      break;}
    digitalWrite(stepY,HIGH);
    delay(1); 
    digitalWrite(stepY,LOW); 
    digitalWrite(stepX,LOW);
    delay(1);  
    }
  digitalWrite(dirY, HIGH);
  pulseX=0;
  pulseY=169.5*51.771;
  rate=pulseY/pulseX;
  temp=0;
  for (int i=0;i<=pulseY;i++){
    if(i/rate-temp>=1){
      digitalWrite(stepX,HIGH); 
      temp++;
      }
    digitalWrite(stepY,HIGH);
    delay(1); 
    digitalWrite(stepY,LOW); 
    digitalWrite(stepX,LOW);
    delay(1);  
    } 
}
void setY(){
  state=0;
}
