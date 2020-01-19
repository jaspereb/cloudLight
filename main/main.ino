// The Cloudlight Code. Adapted from the neopixel library

#include <Adafruit_NeoPixel.h>
#include "IRLibAll.h"

// Default values
#define DEFAULT_BRIGHTNESS 255 //Out of 255
#define debounceThresh 20 //In ms

#define LED_PIN    11
#define IR_PIN 4
#define IR_PWR 7
#define LED_COUNT 120

Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
IRrecv myReceiver(IR_PIN);
IRdecode myDecoder;   

int brightness = DEFAULT_BRIGHTNESS;
int setPos = 128;
int wipePos = 0;
unsigned long debounceTime = millis();
int mode = 0;

//Cloud sections


void setup() {
  Serial.begin(9600);
  Serial.println("Cloud Online");
  myReceiver.enableIRIn(); // Start the receiver
  
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.setBrightness(DEFAULT_BRIGHTNESS); // Set BRIGHTNESS to about 1/5 (max = 255)
  strip.show();
  
  pinMode(IR_PWR, OUTPUT);
  digitalWrite(IR_PWR, HIGH);
}


void loop() {
  long unsigned int setColor;
  checkIR();
  
  // ========================================= //
  //                Mode Logic                 //
  // ========================================= //

  if(mode == 0){//Off
    strip.fill(strip.Color(0,   0,   0));
    strip.setBrightness(0);
    strip.show();
    Serial.println("Cloud Off");
    delay(100);
  }

  else if (mode == 1){//Lamp mode
    strip.setBrightness(brightness);
    strip.fill(strip.Color(255,   255,   255));    
    strip.show();
  }

  else if (mode == 2){//Solid Color
    strip.setBrightness(brightness);
    setColor = wheel(setPos);
    strip.fill(setColor);  
    strip.show();
  }

  else if (mode == 3){//Pulsing White
    strip.fill(strip.Color(255,   255,   255));    
    strip.show();
    while(mode == 3){
      for(int i=200; i>1; i-=1) {
        strip.setBrightness(i);
        strip.show();
        checkIR();
        if(mode != 3){break;};
      }
      for(int i=1; i<200; i+=1) {
        strip.setBrightness(i);
        strip.show();
        checkIR();
        if(mode != 3){break;};
      }
    }
    strip.setBrightness(brightness);
    strip.show();
  }

  else if (mode == 4){//Relax
    for(int i=0; i<255; i+=1) {
      strip.fill(wheel(i));
      strip.show();
      checkIR();
      delay(500);
      if(mode != 4){
        break;
      }
    }
  }

  else if (mode == 5){//Lightning
    int lightningDelay = setPos*3;
    switch(random(1,4)){
      case 1:
        thunderburst(strip.Color(255,255,255),mode);
        delay(random(10,500));
        break;
       
      case 2:
        crack(strip.Color(255,255,255));
        delay(random(50,250));
        checkIR();
        break;
        
      case 3:
        rolling(strip.Color(255,255,255),mode);
        break;
      
    }
    delay(random(lightningDelay,lightningDelay*5));
  }

  else if (mode == 6){//Disco
    disco(mode);
  }

  else if (mode == 7){//Acid
    switch(random(1,4)){
      case 1:
        thunderburst(wheel(random(0,255)),mode);
        delay(random(10,500));
        break; 
      case 2:
        crack(wheel(random(0,255)));
        delay(random(50,250));
        checkIR();
        break;        
      case 3:
        rolling(wheel(random(0,255)),mode);
        break;
    }
  }

  else if (mode == 8){//Strobe!
    strip.fill(strip.Color(255,   255,   255)); 
    strip.show();
    delay(30);
    strip.fill(strip.Color(0,   0,   0)); 
    strip.show();
    delay(setPos*3);
  }

  
  
  /*for(int i=0; i<255; i+=3) {
    colorWipe(strip.Color(255-i,   0,   i), 0);
    
  }
  colorWipe(strip.Color(0,   0,   0), 50); // off
  //rainbow(10);             // Flowing rainbow cycle along the whole strip
  Serial.println("Finished Rainbow");
  if (myReceiver.getResults()) {
    myDecoder.decode();           //Decode it
    myReceiver.enableIRIn();      //Restart receiver
    Serial.println(myDecoder.value, HEX);
    
  }
  delay(1000);  
  //theaterChaseRainbow(200); // Rainbow-enhanced theaterChase variant
  */
}









//Generate rainbow colors across 0-255 positions
unsigned long wheel(unsigned int WheelPos){
  WheelPos = 255 - WheelPos;
  if(WheelPos < 85)
  {
    return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  }
  else if(WheelPos < 170)
  {
      WheelPos -= 85;
      return strip.Color(0, WheelPos * 3, 255 - (WheelPos * 3));
  }
  else
  {
      WheelPos -= 170;
      return strip.Color(WheelPos * 3, 255 - (WheelPos * 3), 0);
  }
}

  // ========================================= //
  //            Get keypress inputs            //
  // ========================================= //
  
void checkIR(void){
  delay(100);
  if (myReceiver.getResults()) {
    myDecoder.decode();           //Decode it
    myReceiver.enableIRIn();      //Restart receiver
    Serial.println(myDecoder.value, HEX);
  }
  
  if(myDecoder.value == 0xFF4AB5){
    mode = 0;
  }
  else if(myDecoder.value == 0xFF6897){ //1 key
    mode = 1;
  }
  else if(myDecoder.value == 0xFF9867){ //2 key
    mode = 2;
  }
  
  else if(myDecoder.value == 0xFFB04F){ //3 key
    mode = 3;
  }
  
  else if(myDecoder.value == 0xFF30CF){ //4 key
    mode = 4;
  }
  
  else if(myDecoder.value == 0xFF18E7){ //5 key
    setPos = 10; //Entering lightning mode
    mode = 5;
  }
  
  else if(myDecoder.value == 0xFF7A85){ //6 key
    setPos = 50; //Entering disco mode
    mode = 6;
  }
  
  else if(myDecoder.value == 0xFF10EF){ //7 key 
    mode = 7; 
  }
  
  else if(myDecoder.value == 0xFF38C7){ //8 key
    setPos = 10; //Entering strobe mode
    mode = 8;
  }
  
  else if(myDecoder.value == 0xFF5AA5){ //9 key
  }
  
  else if(myDecoder.value == 0xFF52AD){ //hash key
  }
  
  else if(myDecoder.value == 0xFF42BD){ //star key
  }
  
  else if(myDecoder.value == 0xFF22DD){ //left key
    if(millis()-debounceTime > debounceThresh){
      if(setPos > 15){
        setPos = setPos - 15;
      }
      else{setPos = 255;}
    }
    debounceTime = millis();
  }
  
  else if(myDecoder.value == 0x0FF629D){ //up key
    if(millis()-debounceTime > debounceThresh){
      if(brightness < (255-20)){
        brightness = brightness + 20;
      }
      else{brightness =  255;}
      strip.setBrightness(brightness);
      strip.show();
    }
    debounceTime = millis();
  }
  
  else if(myDecoder.value == 0xFFC23D){ //right key
    if(millis()-debounceTime > debounceThresh){
      if(setPos < (255-15)){
        setPos = setPos + 15;
      }
      else{setPos = 0;}
    }
    debounceTime = millis();
  }
  
  else if(myDecoder.value == 0xFFA857){ //down key
    if(millis()-debounceTime > debounceThresh){
      if(brightness > 21){
        brightness = brightness - 20;
      }
      else{//Issues with losing the color if it's turned to zero
        brightness = 1;
      }
      strip.setBrightness(brightness);
      strip.show();
    }
    debounceTime = millis();
  }
  
  else if(myDecoder.value == 0xFF02FD){ //ok key
  }
}

void disco(int startMode){
  while(mode == startMode){
    //Flash left half then right
    unsigned long int lc = wheel(random(0,255));
    unsigned long int rc = wheel(random(0,255));
    
    for(int i=0; i<20; i+=1) {
      strip.setPixelColor(i, lc);
    }
    for(int i=60; i<100; i+=1) {
      strip.setPixelColor(i, lc);
    }
    for(int i=21; i<60; i+=1) {
      strip.setPixelColor(i, rc);
    }
    for(int i=100; i<LED_COUNT; i+=1) {
      strip.setPixelColor(i, rc);
    }
    strip.show();
    checkIR();
    delay(setPos*3);
  }
  
}
  // ========================================= //
  //             Lightning Methods             //
  // ========================================= //
  
void rolling(long unsigned int color, int startMode){
  int startPoint = random(10,LED_COUNT);

  if(startPoint < LED_COUNT/2){
    for(int offset=startPoint;offset<LED_COUNT;offset=offset+10){
      for(int i=offset-10;i<offset+10;i++){
        strip.fill(strip.Color(0,   0,   0));  
        if(i > LED_COUNT){break;}
        
        if(random(0,100)>70){
          strip.setPixelColor(i, color);
        }
        if(random(0,100)>80){//Randomly Skip Sections
          offset = offset+25;
        }
        strip.show();
      }
      
      delay(random(20,400));
      checkIR();
      if(mode != startMode){
        return;
      }
    }
  }
  else{
    for(int offset=startPoint;offset>0;offset=offset-10){
      for(int i=offset-10;i<offset+10;i++){
        strip.fill(strip.Color(0,   0,   0));  
        if(i < 0){break;}
        
        if(random(0,100)>70){
          strip.setPixelColor(i, color);
        }
        if(random(0,100)>80){//Randomly Skip Sections
          offset = offset-25;
        }
        strip.show();
      }
      
      delay(random(20,400));
      checkIR();
      if(mode != startMode){
        return;
      }
    }  
  }
}

void crack(long unsigned int color){
   //turn everything white briefly
   strip.fill(color); 
   strip.show();
   delay(random(10,100));
   strip.fill(strip.Color(0,   0,   0)); 
   strip.show();
}

void thunderburst(long unsigned int color, int startMode){

  // this thunder works by lighting two random lengths
  // of the strand from 10-20 pixels. 
  int rs1 = random(0,LED_COUNT/2);
  int rl1 = random(10,20);
  int rs2 = random(rs1+rl1,LED_COUNT);
  int rl2 = random(10,20);
  
  //repeat this chosen strands a few times, adds a bit of realism
  for(int r = 0;r<random(2,8);r++){
    
    for(int i=0;i< rl1; i++){
      strip.setPixelColor(i+rs1, color);
    }
    
    if(rs2+rl2 < LED_COUNT){
      for(int i=0;i< rl2; i++){
        strip.setPixelColor(i+rs2, color);
      }
    }
    
    strip.show();
    //stay illuminated for a set time
    delay(random(10,50));
    strip.fill(strip.Color(0,   0,   0)); 
    strip.show();
    delay(random(10,60));
  }
  
  checkIR();
  if(mode != startMode){
    return;
  }
  delay(random(10,2000));
}

  // ========================================= //
  //             Example Methods             //
  // ========================================= //
 
// Fill strip pixels one after another with a color. Strip is NOT cleared
// first; anything there will be covered pixel by pixel. Pass in color
// (as a single 'packed' 32-bit value, which you can get by calling
// strip.Color(red, green, blue) as shown in the loop() function above),
// and a delay time (in milliseconds) between pixels.
void colorWipe(uint32_t color, int wait) {
  for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
    strip.setPixelColor(i, color);         //  Set pixel's color (in RAM)
    strip.show();                          //  Update strip to match
    delay(wait);                           //  Pause for a moment
  }
}

// Theater-marquee-style chasing lights. Pass in a color (32-bit value,
// a la strip.Color(r,g,b) as mentioned above), and a delay time (in ms)
// between frames.
void theaterChase(uint32_t color, int wait) {
  for(int a=0; a<10; a++) {  // Repeat 10 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      // 'c' counts up from 'b' to end of strip in steps of 3...
      for(int c=b; c<strip.numPixels(); c += 3) {
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show(); // Update strip with new contents
      delay(wait);  // Pause for a moment
    }
  }
}

// Rainbow cycle along whole strip. Pass delay time (in ms) between frames.
void rainbow(int wait) {
  // Hue of first pixel runs 5 complete loops through the color wheel.
  // Color wheel has a range of 65536 but it's OK if we roll over, so
  // just count from 0 to 5*65536. Adding 256 to firstPixelHue each time
  // means we'll make 5*65536/256 = 1280 passes through this outer loop:
  for(long firstPixelHue = 0; firstPixelHue < 5*65536; firstPixelHue += 10*256) {
    for(int i=0; i<strip.numPixels(); i++) { // For each pixel in strip...
      // Offset pixel hue by an amount to make one full revolution of the
      // color wheel (range of 65536) along the length of the strip
      // (strip.numPixels() steps):
      int pixelHue = firstPixelHue + (i * 65536L / strip.numPixels());
      // strip.ColorHSV() can take 1 or 3 arguments: a hue (0 to 65535) or
      // optionally add saturation and value (brightness) (each 0 to 255).
      // Here we're using just the single-argument hue variant. The result
      // is passed through strip.gamma32() to provide 'truer' colors
      // before assigning to each pixel:
      strip.setPixelColor(i, strip.gamma32(strip.ColorHSV(pixelHue)));
    }
    strip.show(); // Update strip with new contents
    delay(wait);  // Pause for a moment
  }
}

// Rainbow-enhanced theater marquee. Pass delay time (in ms) between frames.
void theaterChaseRainbow(int wait) {
  int firstPixelHue = 0;     // First pixel starts at red (hue 0)
  for(int a=0; a<30; a++) {  // Repeat 30 times...
    for(int b=0; b<3; b++) { //  'b' counts from 0 to 2...
      strip.clear();         //   Set all pixels in RAM to 0 (off)
      // 'c' counts up from 'b' to end of strip in increments of 3...
      for(int c=b; c<strip.numPixels(); c += 3) {
        // hue of pixel 'c' is offset by an amount to make one full
        // revolution of the color wheel (range 65536) along the length
        // of the strip (strip.numPixels() steps):
        int      hue   = firstPixelHue + c * 65536L / strip.numPixels();
        uint32_t color = strip.gamma32(strip.ColorHSV(hue)); // hue -> RGB
        strip.setPixelColor(c, color); // Set pixel 'c' to value 'color'
      }
      strip.show();                // Update strip with new contents
      delay(wait);                 // Pause for a moment
      firstPixelHue += 65536 / 90; // One cycle of color wheel over 90 frames
    }
  }
}
