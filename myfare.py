import serial

prot = {
    'enquiry_module': '\x03\x12\x00\x15',
    'enquiry_module_return': '\x02\x12\x14',
    'active_buzzer': '\x02\x13\x15',
    'enquiry_cards': '\x03\x02\x00\x05',
    'enquiry_cards_return': '\x03\x02\x01\x06', # 03020106
    'enquiry_all_cards': '\x03\x02\x01\x05',
    'anticollision' : '\x02\x03\x05',
}

ser = serial.Serial('/dev/ttyUSB0',9600,timeout=1)
ser.write(prot['enquiry_module'])

f =  ser.read(10)
if f == prot['enquiry_module_return']:
    print "enquiry module OK"

ser.write(prot['active_buzzer'])
f = ser.read(10)

if f == prot['active_buzzer']:
    print "buzzer is active"

ser.write(prot['enquiry_all_cards'])
data = ser.read(10)
print data.encode('hex')
