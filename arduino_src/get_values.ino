void setup() {
  Serial.begin(9600);
  for(int i=2;i<=9;i++)
  {
    pinMode(i,INPUT);
  }
}

void loop() {
  int value=0;
  for(int i=2;i<=9;i++)
  {
    if(digitalRead(i))
    {
      value+=1<<(i-2);
    }
  }
  Serial.println(value);
  delay(200);
}
