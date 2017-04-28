int led = 13;
int ruido=0;
int humo=0;
int luz=0;
int temperatura=335;
void setup () {
   pinMode(led, OUTPUT); //LED 13 como salida
   Serial.begin(9600); //Inicializo el puerto serial a 9600 baudios
}

void loop () {
  Serial.flush();
  Serial.println(String(ruido)+","+String(humo)+","+String(luz)+","+String(temperatura));
  delay(2000);
}

