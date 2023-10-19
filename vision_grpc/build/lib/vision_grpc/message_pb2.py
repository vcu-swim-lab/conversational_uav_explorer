# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vision_grpc/vision_grpc/message.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%vision_grpc/vision_grpc/message.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"$\n\x03Joy\x12\x0c\n\x04\x61xes\x18\x01 \x03(\x02\x12\x0f\n\x07\x62uttons\x18\x02 \x03(\x05\"n\n\x06NavSat\x12\x10\n\x08latitude\x18\x01 \x01(\x01\x12\x11\n\tlongitude\x18\x02 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\x03 \x01(\x01\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xee\x01\n\x04Pose\x12\x1d\n\x08position\x18\x01 \x01(\x0b\x32\x0b.Pose.Point\x12%\n\x0borientation\x18\x02 \x01(\x0b\x32\x10.Pose.Quaternion\x12\r\n\x05\x66rame\x18\x03 \x01(\t\x12-\n\ttimestamp\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a(\n\x05Point\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x1a\x38\n\nQuaternion\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\x12\t\n\x01z\x18\x03 \x01(\x01\x12\t\n\x01w\x18\x04 \x01(\x01\"w\n\x03Map\x12\x0b\n\x03svg\x18\x01 \x01(\x0c\x12\r\n\x05width\x18\x02 \x01(\x02\x12\x0e\n\x06height\x18\x03 \x01(\x02\x12\x15\n\x06origin\x18\x04 \x01(\x0b\x32\x05.Pose\x12-\n\ttimestamp\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"L\n\x07\x42\x61ttery\x12\x12\n\npercentage\x18\x01 \x01(\x01\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1e\n\x0bTemperature\x12\x0f\n\x07measure\x18\x01 \x01(\x01\x42\n\xba\x02\x07Vision_b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'vision_grpc.vision_grpc.message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\272\002\007Vision_'
  _globals['_JOY']._serialized_start=74
  _globals['_JOY']._serialized_end=110
  _globals['_NAVSAT']._serialized_start=112
  _globals['_NAVSAT']._serialized_end=222
  _globals['_POSE']._serialized_start=225
  _globals['_POSE']._serialized_end=463
  _globals['_POSE_POINT']._serialized_start=365
  _globals['_POSE_POINT']._serialized_end=405
  _globals['_POSE_QUATERNION']._serialized_start=407
  _globals['_POSE_QUATERNION']._serialized_end=463
  _globals['_MAP']._serialized_start=465
  _globals['_MAP']._serialized_end=584
  _globals['_BATTERY']._serialized_start=586
  _globals['_BATTERY']._serialized_end=662
  _globals['_TEMPERATURE']._serialized_start=664
  _globals['_TEMPERATURE']._serialized_end=694
# @@protoc_insertion_point(module_scope)