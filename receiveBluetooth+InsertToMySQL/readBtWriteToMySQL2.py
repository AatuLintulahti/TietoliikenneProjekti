import asyncio
from bleak import BleakClient
import tracemalloc
import mysql.connector


tracemalloc.start()

r=0
d=""
x=""
y=""
z=""

def callback(sender, data):
    data2int = int.from_bytes(data, byteorder='little')
    datastr = str(data2int)
    global r
    print (r)
    print (datastr,"\n")
    if r == 0:
        
        global d
        d = datastr
        r=r+1
    elif r==1:
        global x
        x = datastr
        r=r+1
    elif r==2:
        global y
        y = datastr
        r=r+1
    elif r==3:
        global z
        z = datastr
        r=r+1
    
    if r == 4:
        print("d=",d,"x=",x,"y=",y,"z=",z)
        sendToDb()
        r = 0
    
    #datatuple = datastr.splitlines
    
    #print (datatuple,"\n")
    #print(f"{sender}: {data}")
    #return data


def sendToDb():
    if len(d) != 1:
        print("\naborted sending data (out of sync)\n")
        exit()
    sql = "INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d, sensorvalue_e, sensorvalue_f) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = ("12", "nrf5340", "raspi", d, x, y, z, 0, 0)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "measurement set was inserted.") 

mydb = mysql.connector.connect(
  host="172.20.241.9",
  user="dbaccess_rw",
  password="fasdjkf2389vw2c3k234vk2f3",
  database="measurements"
)
mycursor = mydb.cursor()

print(mydb) 


async def main(address):
    async with BleakClient(address) as client:
        #client.pair
        services = client.services
        charUUID='00001526-1212-efde-1523-785feabcd123'
        #print(services.services)
        await client.start_notify(charUUID, callback)
        #print(sensorData)
        runfor = 25
        await asyncio.sleep(runfor)
        
        
address = "DC:89:1F:B4:6C:4B"


asyncio.run(main(address))