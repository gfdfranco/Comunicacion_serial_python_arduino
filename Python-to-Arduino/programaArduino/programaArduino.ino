String incomingByte;   // for incoming serial data
int i=0;
int coordenadaX;
int coordenadaY;
void setup() {
        Serial.begin(115200);     // opens serial port, sets data rate to 9600 bps
        delay(1000);
}

void loop() {

    
        if (Serial.available() > 0) {
                incomingByte = Serial.readString();
                Serial.println(incomingByte);
                i++;
                
                if(i>2){
                    String var1  = Serial.readStringUntil(',');
                    Serial.read(); //next character is comma, so skip it using this
                    String var2  = Serial.readStringUntil('\0');
                    Serial.read(); 
                    coordenadaX=var1.toInt();
                    coordenadaY=var2.toInt();
                    
                    Serial.print("COORDENADA X: ");
                    Serial.println( coordenadaX);
                    
                    Serial.print("COORDENADA Y: ");
                    Serial.println( coordenadaY);
                }
        }
        delay(100);
}
