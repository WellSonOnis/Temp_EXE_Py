#define TEMP_PIN A0 // i use A0 pin 

#define B_VALUE 3950

#define PULLUP_RESISTOR 10000

void setup() {
  Serial.begin(9600);
}

void loop() {
  int temp_raw = analogRead(TEMP_PIN); // read values over LM35 sensor

  float temp_c = (log(PULLUP_RESISTOR * (1023.0 / temp_raw - 1) / 10000.0) / B_VALUE) + (1 / (25.0 + 273.15));
  
  // i know you can fix temperature value ;) .
  
  //Serial.print("T:");
  Serial.print(temp_c);
  //Serial.println("C");

  delay(500);
}




/*int v;
int t=A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  v=analogRead(t);
  float m=(v/1024.0)*5;
  float c=m/0.01;
  Serial.print("T= ");
  Serial.print(v);
  Serial.print("*C");
  Serial.println();
  delay(1000);
  
}
*/
