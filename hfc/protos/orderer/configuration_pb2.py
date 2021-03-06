# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: orderer/configuration.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='orderer/configuration.proto',
  package='orderer',
  syntax='proto3',
  serialized_pb=_b('\n\x1borderer/configuration.proto\x12\x07orderer\x1a\x13\x63ommon/common.proto\"\x1d\n\rConsensusType\x12\x0c\n\x04type\x18\x01 \x01(\t\"$\n\tBatchSize\x12\x17\n\x0fmaxMessageCount\x18\x01 \x01(\r\"0\n\x0e\x43reationPolicy\x12\x0e\n\x06policy\x18\x01 \x01(\t\x12\x0e\n\x06\x64igest\x18\x02 \x01(\x0c\"!\n\rChainCreators\x12\x10\n\x08policies\x18\x01 \x03(\t\"\x1f\n\x0cKafkaBrokers\x12\x0f\n\x07\x62rokers\x18\x01 \x03(\tB.Z,github.com/hyperledger/fabric/protos/ordererb\x06proto3')
  ,
  dependencies=[common_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONSENSUSTYPE = _descriptor.Descriptor(
  name='ConsensusType',
  full_name='orderer.ConsensusType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='orderer.ConsensusType.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=90,
)


_BATCHSIZE = _descriptor.Descriptor(
  name='BatchSize',
  full_name='orderer.BatchSize',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='maxMessageCount', full_name='orderer.BatchSize.maxMessageCount', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=92,
  serialized_end=128,
)


_CREATIONPOLICY = _descriptor.Descriptor(
  name='CreationPolicy',
  full_name='orderer.CreationPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policy', full_name='orderer.CreationPolicy.policy', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='digest', full_name='orderer.CreationPolicy.digest', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=178,
)


_CHAINCREATORS = _descriptor.Descriptor(
  name='ChainCreators',
  full_name='orderer.ChainCreators',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='policies', full_name='orderer.ChainCreators.policies', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=180,
  serialized_end=213,
)


_KAFKABROKERS = _descriptor.Descriptor(
  name='KafkaBrokers',
  full_name='orderer.KafkaBrokers',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='brokers', full_name='orderer.KafkaBrokers.brokers', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=215,
  serialized_end=246,
)

DESCRIPTOR.message_types_by_name['ConsensusType'] = _CONSENSUSTYPE
DESCRIPTOR.message_types_by_name['BatchSize'] = _BATCHSIZE
DESCRIPTOR.message_types_by_name['CreationPolicy'] = _CREATIONPOLICY
DESCRIPTOR.message_types_by_name['ChainCreators'] = _CHAINCREATORS
DESCRIPTOR.message_types_by_name['KafkaBrokers'] = _KAFKABROKERS

ConsensusType = _reflection.GeneratedProtocolMessageType('ConsensusType', (_message.Message,), dict(
  DESCRIPTOR = _CONSENSUSTYPE,
  __module__ = 'orderer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:orderer.ConsensusType)
  ))
_sym_db.RegisterMessage(ConsensusType)

BatchSize = _reflection.GeneratedProtocolMessageType('BatchSize', (_message.Message,), dict(
  DESCRIPTOR = _BATCHSIZE,
  __module__ = 'orderer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:orderer.BatchSize)
  ))
_sym_db.RegisterMessage(BatchSize)

CreationPolicy = _reflection.GeneratedProtocolMessageType('CreationPolicy', (_message.Message,), dict(
  DESCRIPTOR = _CREATIONPOLICY,
  __module__ = 'orderer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:orderer.CreationPolicy)
  ))
_sym_db.RegisterMessage(CreationPolicy)

ChainCreators = _reflection.GeneratedProtocolMessageType('ChainCreators', (_message.Message,), dict(
  DESCRIPTOR = _CHAINCREATORS,
  __module__ = 'orderer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:orderer.ChainCreators)
  ))
_sym_db.RegisterMessage(ChainCreators)

KafkaBrokers = _reflection.GeneratedProtocolMessageType('KafkaBrokers', (_message.Message,), dict(
  DESCRIPTOR = _KAFKABROKERS,
  __module__ = 'orderer.configuration_pb2'
  # @@protoc_insertion_point(class_scope:orderer.KafkaBrokers)
  ))
_sym_db.RegisterMessage(KafkaBrokers)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z,github.com/hyperledger/fabric/protos/orderer'))
try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
