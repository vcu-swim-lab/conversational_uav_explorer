# api to get grpc data or send data to grpc server, called from app.py
# Ju Wang, 10/2023

import grpc
import asyncio
import sys
import jackal_grpc_client
from vision_grpc.vision_grpc import auth_pb2_grpc
from vision_grpc.vision_grpc import serve_pb2_grpc
from vision_grpc.vision_grpc import manage_pb2_grpc
from vision_grpc.vision_grpc import manage_pb2  # noqa: F401
from vision_grpc.vision_grpc import message_pb2  # noqa: F401
from google.protobuf import text_format  # noqa: F401
from google.protobuf import wrappers_pb2  # noqa: F401
from google.protobuf import timestamp_pb2  # noqa: F401
from google.protobuf import duration_pb2  # noqa: F401
from google.protobuf import empty_pb2  # noqa: F401
from google.protobuf import any_pb2  # noqa: F401
from google.protobuf import json_format

import datetime
import jwt
import server.robot_uuid as robot_uuid

import numpy as np
from scipy.spatial.transform import Rotation as R
import zlib

jwt_secret = "123456"
sub = "github:6932348"
exp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(weeks=1)
access_token = jwt.encode(
    {
        "sub": sub,
        "exp": exp,
    },
    jwt_secret,
)
authorization = f"Bearer {access_token}"

channel = grpc.secure_channel(
    "robot.coldspringworks.com",
    grpc.ssl_channel_credentials(),
)

stub = manage_pb2_grpc.ManageStub(channel)
stub2 = serve_pb2_grpc.ServeStub(channel)
device = robot_uuid.robot_uuid_dict['baal_real']['uuid']
#device = robot_uuid.robot_uuid_dict['baal_hp8000']['uuid']
#device = "649dcfba-4dbf-11e6-9c43-bc0000c00000" #baal_hp8000
print('device uuid: ', device)

#from a location/landmark string to x/y
def parse_location(command_l):
    return (0,0)

def jackal_grpc_joy(axes=-1, buttons=1): #joy task hacked for sending ctl info
    message = message_pb2.Joy()
    message.axes.append(axes)
    message.buttons.append(buttons)
    print("message :", message)
    request = any_pb2.Any()
    request.Pack(message)
    response = stub2.SendTask(
        iter([request]),
        metadata=[
            ("device", device),
            ("authorization", authorization),
            ("function", "joy"),
        ],
    )
    print(response)

#goto should treat x/y as relative from current position, not absolute pose in map frame
# this actually does not need to create additional grpc message
# goalrel.py ros node, with metadata "goalrel" for interceptor
# ration in degree
def jackal_grpc_gotorel(x=0,y=0, rotation=0):
    message = message_pb2.Pose()
    message.frame = "base_link" 
    #message.frame = "map" 
    message.position.x = x
    message.position.y = y
    
    rotVec = np.array([[0, 0  , rotation*3.14/180  ]], dtype=float)
    quat = R.from_rotvec(rotVec).as_quat().reshape((-1,)) #(xyzw)

    message.orientation.x = quat[0]
    message.orientation.y = quat[1]
    message.orientation.z = quat[2]
    message.orientation.w = quat[3]
    print("message :", message)
    request = any_pb2.Any()
    request.Pack(message)
    response = stub2.SendTask(
        iter([request]),
        metadata=[
            ("device", device),
            ("authorization", authorization),
            ("function", "goalrel"),
        ],
    )
    print(response)

#goto an absolute position in map frame
def jackal_grpc_goto(x=0,y=0):
    message = message_pb2.Pose()
    message.orientation.w = 1.0
    message.position.x = x
    message.position.y = y
    message.frame = "map" 
    request = any_pb2.Any()
    request.Pack(message)
    response = stub2.SendTask(
        iter([request]),
        metadata=[
            ("device", device),
            ("authorization", authorization),
            ("function", "goal"),
        ],
    )
    print("goto TEST2")
    print(response)

def jackal_grpc_test():
    print("testing jackal_grpc")
    request = manage_pb2.ListDeviceRequest(project=0)
    response = stub.ListDevice(
        request,
        metadata=[
            ("authorization", authorization),
        ],
    )
    print(response)

# not working so far
async def jackal_grpc_getpose():
    index = 0
    request = any_pb2.Any()
    request.Pack(empty_pb2.Empty())
    async for response in stub2.RecvPost(
        request,
        metadata=[
            ("function", "temperature")
        ]
        ):
        message = message_pb2.Temperature();
        response.Unpack(message)
        #print(message)
        yield message
        index +=1
        if index >=0:
            break
        #print(message)

# async call inside main_post(), this works but would be better to have a blocking call that
# ride off the async stuff
def jackal_grpc_get_temperatureasync():
#    run=run_serve()
#    asyncio.run(run)
    #sys.argv = ['client_test.py', '--jwt_secret', '123456', '--function', 'temperature:Temperature', 'post']
    #jackal_grpc_client.main()
    msg_ret = jackal_grpc_client.main_post(function='temperature:Temperature')
    print('temperatrue msg return: ', msg_ret)

def jackal_grpc_get_mapasync():
    msg_ret = jackal_grpc_client.main_post(function="map:Map", device=device)
    #print('message return: ', msg_ret)
    print('map w/h: ', msg_ret.width, msg_ret.height)
    print('map orig: ', msg_ret.origin)
    print('map orig: ', msg_ret.timestamp.ToJsonString())
    deflated = msg_ret.svg
    maptype = msg_ret.svg[-3:]
    print("maptype is: ", maptype)
    if maptype==b'pgm':
        deflated = deflated[:-3]
    decomp = zlib.decompressobj()
    restored_svg = zlib.decompress(deflated,wbits=-zlib.MAX_WBITS)
    print(len(restored_svg), type(restored_svg))
    if maptype == b'pgm':
        mapfn = "map2.pgm"
        print("saving pgm ")
        with open(mapfn, "wb") as f:
            f.write(restored_svg) #decode convert bytes to str
    else:
        #default case svg
        mapfn = "map2.svg"
        print("saving svg ")
        with open(mapfn, "w") as f:
            f.write(restored_svg.decode("utf-8")) #decode convert bytes to str

def jackal_grpc_get_poseasync():
    msg_ret = jackal_grpc_client.main_post(function="pose:Pose", device=device)
    print('message return: ', msg_ret)
    print('pose position: x/y/z ', msg_ret.position.x, msg_ret.position.y, msg_ret.position.z)
    print('map orig: ', msg_ret.timestamp.ToJsonString())

# called in app.py
def jackal_grpc_send_command(commandstr_gpt, commandstr):
    print('commandstr: ', commandstr, "\n*****\n")
    print('commandstr_gpt: ', commandstr_gpt, "\n*****\n")
    if commandstr==None:
        print('commandstr is None, return')
        return
    command_l = commandstr.split(' ')
    #below are command 
    if command_l[0] =='goto':
        (x,y)=parse_location(command_l[1])
        jackal_grpc_gotorel(x=x,y=y)
    elif command_l[0] =='turn':
        if command_l[1]=='left':
            jackal_grpc_gotorel(rotation=-30) #for now turn 30 deg
        else:
            jackal_grpc_gotorel(rotation=30)
    elif command_l[0] =='forward':
        jackal_grpc_gotorel(x=1) # x, y relative pose from current
    elif command_l[0] =='backward':
        jackal_grpc_gotorel(x=-1)

    #below are update data stream display
    elif command_l[0] =='update':
        if len(command_l)<2:
            print('update command need 2nd param, return')
            return
        if command_l[1]=='pose':
            jackal_grpc_get_poseasync()
        elif command_l[1] =='temperature':
            jackal_grpc_get_temperatureasync()
        elif command_l[1] =='map':
            jackal_grpc_get_mapasync()

if __name__ == '__main__':
    #jackal_grpc_test()
    jackal_grpc_goto()
#    jackal_grpc_get_poseasync()
#    jackal_grpc_get_mapasync()
#    jackal_grpc_get_temperatureasync()
    jackal_grpc_gotorel(x=0.5, rotation=-10)
    jackal_grpc_joy(axes=-1, buttons=1) #joy task hacked for sending ctl info

