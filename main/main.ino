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
int setPos = 255;
unsigned long debounceTime = millis();
int mode = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("Cloud Online");
  myReceiver.enableIRIn(); // Start the receiver
  
  strip.begin();           // INITIALIZE NeoPixel strip object (REQUIRED)
  strip.show();            // Turn OFF all pixels
  strip.setBrightness(DEFAULT_BRIGHTNESS); // Set BRIGHTNESS to about 1/5 (max = 255)

  pinMode(IR_PWR, OUTPUT);
  digitalWrite(IR_PWR, HIGH);
}


void loop() {
  unsigned long setColor;
  
  if (myReceiver.getResults()) {
    myDecoder.decode();           //Decode it
    myReceiver.enableIRIn();      //Restart receiver
    Serial.println(myDecoder.value, HEX);
  }

  // ========================================= //
  //            Get keypress inputs            //
  // ========================================= //
  if(myDecoder.value == 0xFF4AB5){
    mode = 0;
  }
  else if(myDecoder.value == 0xFF6897){ //1 key
    mode = 1;
  }
  //Solid color mode
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
    mode = 5;
  }
  
  else if(myDecoder.value == 0xFF7A85){ //6 key
    mode = 6;
  }
  
  else if(myDecoder.value == 0xFF10EF){ //7 key  
  }
  
  else if(myDecoder.value == 0xFF38C7){ //8 key
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

  // ========================================= //
  //                Mode Logic                 //
  // ========================================= //

  if(mode == 0){//Off
    strip.fill(strip.Color(0,   0,   0));
    strip.setBrightness(0);
    strip.show();
    Serial.println("Cloud Off");
    delay(200);
  }

  else if (mode == 1){//Lamp mode
    strip.setBrightness(brightness);
    strip.fill(strip.Color(255,   255,   255));    
    strip.show();
    delay(100); //Delay to read IR
  }

  else if (mode == 2){//Solid Color
    strip.setBrightness(brightness);
    setColor = wheel(setPos);
    strip.fill(setColor);  
    strip.show();
    delay(100); //Delay to read IR
  }

  else if (mode == 3){//Color Gradient
    strip.fill(strip.Color(255,   0,   0));
    strip.show();
    delay(100);
  }

  else if (mode == 4){//Relax
  }

  else if (mode == 5){//Lightning
  }

  else if (mode == 6){//Disco
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







// Some functions of our own for creating animated effects -----------------

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
