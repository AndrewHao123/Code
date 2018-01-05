#coding:utf-8
#import necessary package
import socket
import time
import sys
import RPi.GPIO as GPIO
#define host ip: Rpi's IP
HOST_IP = "192.168.1.109"
HOST_PORT = 8888
print("Starting socket: TCP...")
#1.create socket object:socket=socket.socket(family,type)
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("TCP server listen @ %s:%d!" %(HOST_IP, HOST_PORT) )
host_addr = (HOST_IP, HOST_PORT)
#2.bind socket to addr:socket.bind(address)
socket_tcp.bind(host_addr)
#3.listen connection request:socket.listen(backlog)
socket_tcp.listen(1)
#4.waite for client:connection,address=socket.accept()
socket_con, (client_ip, client_port) = socket_tcp.accept()
print("Connection accepted from %s." %client_ip)
socket_con.send("Welcome to RPi TCP server!")
#5.handle
GPIO.setmode(GPIO.BCM)	##信号引脚模式定义，BCM模式
GPIO.setwarnings(False)

########电机驱动接口定义#################
ENA = 13	#//L298使能A
ENB = 20	#//L298使能B
IN1 = 19	#//电机接口1
IN2 = 16	#//电机接口2
IN3 = 21	#//电机接口3
IN4 = 26	#//电机接口4

#########电机初始化为LOW##########
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT,initial=GPIO.LOW)

####PWM初始化，并设置频率为200HZ####
GPIO.setup(ENA,GPIO.OUT,initial=GPIO.LOW)	#初始匿
p1 = GPIO.PWM(ENA,200) 			    #200HZ 
p1.start(40)

####定义电机正转函数
def gogo():
	print 'motor gogo'
#	GPIO.output(ENA,True)
	GPIO.output(IN1,True)
	GPIO.output(IN2,False)
	
	GPIO.output(ENB,True)
	GPIO.output(IN3,True)
	GPIO.output(IN4,False)

###定义电机反转函数
def back():
	print 'motor_back'
	GPIO.output(ENA,True)
	GPIO.output(IN1,False)
	GPIO.output(IN2,True)
	
	GPIO.output(ENB,True)
	GPIO.output(IN3,False)
	GPIO.output(IN4,True)

###定义电机停止函数
def stop():
	print 'motor_stop'
	#GPIO.output(ENA,False)
	p1.stop
	GPIO.output(ENB,False)
	GPIO.output(IN1,False)
	
	GPIO.output(IN2,False)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)	
print("Receiving package...")

###主循环
while True:
    try:
        data=socket_con.recv(512)
        if len(data)>0:
            print("Received:%s"%data)
            if data=='stop':
			    stop();
            elif data=='gogo':
			    gogo();
            socket_con.send(data)
            time.sleep(1)
            continue
    except Exception:
            socket_tcp.close()
            sys.exit(1)
