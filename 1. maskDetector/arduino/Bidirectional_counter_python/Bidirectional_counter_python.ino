int irPin1 = 10;
int irPin2 = 11;
int count = 0;
int t_count = 0;
int door = 13;

boolean state1 = true;
boolean state2 = true;
boolean insideState = false;
boolean outsideIr = false;
boolean isPeopleExiting = false;
char state;

int i = 1;

void setup() {
  Serial.begin(9600);
  pinMode(irPin1, INPUT_PULLUP);
  pinMode(irPin2, INPUT_PULLUP);
  pinMode(door, OUTPUT);
}

void loop() {
  openCloseDoor();
  checkInsidePeople(); 
  closeDoorAfterCount();
}

void openCloseDoor() {
  if(Serial.available() > 0) {
    state = Serial.read();
    Serial.println(state);
    if(state == '1') {
      digitalWrite(door, HIGH);
    }
    if(state == '0') {
      digitalWrite(door, LOW);
    }
  }
}

void checkInsidePeople() {
    if (!digitalRead(irPin1) && i==1 && state1){
     outsideIr=true;
     delay(100);
     i++;
     state1 = false;
  }

   if (!digitalRead(irPin2) && i==2 &&   state2){
     outsideIr=true;
     delay(100);
     i = 1 ;
     count++;
     Serial.println('i');
     state2 = false;
  }

   if (!digitalRead(irPin2) && i==1 && state2 ){
     outsideIr=true;
     delay(100);
     i = 2 ;
     state2 = false;
  }

  if (!digitalRead(irPin1) && i==2 && state1 ){
     outsideIr=true;
     delay(100);
     count--;
     if (count < 0) {
      count = 0;
     }
       Serial.println('o');
     i = 1;
     state1 = false;
  }  

    if (digitalRead(irPin1)){
     state1 = true;
    }

     if (digitalRead(irPin2)){
     state2 = true;
    }
}

void closeDoorAfterCount() {
  if(count == t_count + 1) {
    digitalWrite(door, LOW);
    t_count++;

//  Serial.print(count);
//  Serial.print("  ");
//  Serial.println(t_count);
  }
}
