import asyncio
from bleak import BleakClient
import tracemalloc


tracemalloc.start()


def callback(sender, data):
    data2int = int.from_bytes(data, byteorder='little')
    print (data2int)
    #print(f"{sender}: {data}")
    #return data




async def main(address):
    async with BleakClient(address) as client:
        #client.pair
        #sensorData=bytearray()
        services = client.services
        charUUID='00001526-1212-efde-1523-785feabcd123'
        #print(services.services)
        #await client.read_gatt_char(charUUID)
        await client.start_notify(charUUID, callback)
        #print(sensorData)
        await asyncio.sleep(10)
        
        
address = "DC:89:1F:B4:6C:4B"


asyncio.run(main(address))