static int NUMBER_OF_PINS = 0;

float PINS[0]={};
float pin_values[0]={};

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
    pin_values[i] = analogRead(PINS[i]);
  }
}

void sendPins(){
  for (int i = 0; i < NUMBER_OF_PINS; i++){
    Serial.write(pin_values[i]);
    Serial.write(':');
    Serial.write(i);
    Serial.write(';')
  }
  Serial.write("\n poop");
}

void stall(){

}

