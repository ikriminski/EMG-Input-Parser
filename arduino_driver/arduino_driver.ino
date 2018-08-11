static int NUMBER_OF_PINS = 2;

float PINS[2]={0,1};
float pin_values[2]={0.4777,0.68881};

void setup() {
  Serial.begin(9600);
  
}

void loop() {
  readPins();
  sendPins();
  stall();
}

void readPins(){
  for (int i = 0; i < NUMBER_OF_PINS; i++){
    //pin_values[i] = analogRead(PINS[i]);
    pin_values[i] = pin_values[i] + 1;
  }
}

void sendPins(){
  for (int i = 0; i < NUMBER_OF_PINS; i++){
    Serial.print(pin_values[i]);
    Serial.write(':');
  }
  Serial.write('\n');
  Serial.flush();
}

void stall(){

}

