import serial

prot = {
    'enquiry_module': '\x03\x12\x00\x15',
    'enquiry_module_return': '\x02\x12\x14',
    'active_buzzer': '\x02\x13\x15',
    'enquiry_card': '\x03\x02\x00\x05',
    'enquiry_cards_return': '\x03\x02\x01\x06', # should return hex 03020106 according to protocol
    'enquiry_all_cards': '\x03\x02\x01\x05',
    'anticollision' : '\x02\x03\x05',
    'select_card' : '\x02\x04\x06',
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
    
# enquiry should return hex 03020106 according to protocol
# but reader doesnt, need a known working rfid card.
ser.write(prot['enquiry_card'])
print ser.read(10).encode('hex')

# should return something starting with 0603
ser.write(prot['anticollision'])
print ser.read(10).encode('hex')

# should return 020406
ser.write(prot['select_card'])
print ser.read(10).encode('hex')


