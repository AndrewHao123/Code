nclude<wiringPi.h>//包含wiringPi头文件  
  
int main(void)  
{  
    wiringPiSetup();        //wiringPi库初始化  
    pinMode(0, OUTPUT);     //设置0口为输出模式  
    for(;;)             //循环执行  
    {  
        digitalWrite(0,  HIGH); //GPIO.0输出高电平  
        delay(1000);        //延迟1000ms  
        digitalWrite(0,  LOW);  // GPIO.0输出高电平  
        delay(1000);        //延迟1000ms  
    }  
    return 0;  



}  
