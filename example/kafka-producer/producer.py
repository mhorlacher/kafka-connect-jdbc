# %%
import sys
import time
import argparse
import datetime
import json

from kafka import KafkaProducer

# %%
class Test():
    def __init__(self, msg) -> None:
        self.received_at = datetime.datetime.utcnow().timestamp()
        self.msg = msg

        # types
        self._types = {
            'received_at': 'int64', 
            'msg': 'string', 
            }
    
    @property
    def dict(self):
        return {'received_at': self.received_at, 'msg': self.msg}
    
    @property
    def json(self):
        return json.dumps(self.dict)

    def _make_field(self, field_name):
        return {'type': self._types[field_name], 'optional': False, 'field': field_name}

    @property
    def schema(self):
        fields = [self._make_field(k) for k in self._types]
        return {'type': 'struct', 'fields': fields, 'optional': False, 'name': 'test'}
    
    def __repr__(self) -> str:
        return f'<msg={self.msg}, received_at={self.received_at}>'

# %%
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('host_port', metavar='<hostname:port>', default='localhost:9092')
    args = parser.parse_args()
    return args

# %%
if __name__ == '__main__':
    args = parse_args()

    producer = KafkaProducer(bootstrap_servers=args.host_port, value_serializer = lambda x: json.dumps(x).encode('UTF-8'))
    print(producer, file=sys.stderr)

    i = 0
    while True:
        test = Test(f'test_{i}')
        msg = {'schema': test.schema, 'payload': test.dict}
        producer.send('test', msg)
        print(msg, file=sys.stderr)
        time.sleep(1)
        i += 1

