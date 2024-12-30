from hashlib import sha256
from datetime import datetime


NULL_HASH = '0' * 64  # 64 characters long string of 0s. Each character is a nibble (4 bits)
PROTOCOL_VERSION = '1.0'


class transaction:
    def __init__(self, sender: str, receiver: str, amount: int, signature: str):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def __repr__(self):
        return f'{self.sender} -> {self.receiver} : {self.amount}'

class Block:
    def __init__(self, index: int, timestamp: str, data: str, previous_hash: str):
        self.index = index
        self.protocol_ver = PROTOCOL_VERSION
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_str = str(self.index) + self.protocol_ver + self.timestamp + self.data + self.previous_hash

        return sha256(block_str.encode('ASCII')).hexdigest()

    def __repr__(self):
        return (
            f'Block #{self.index}\n'
            f'Protocol Ver. {self.protocol_ver}\n'
            f'Time: {self.timestamp}\n'
            f'Prev. hahs: {self.previous_hash}\n'
            f'Meta hash: {self.hash}\n'
            f'Data:\n\n{self.data}\n'
        )

class BlockChain:
    def __init__(self):
        timestamp = str(datetime.now())
        self.chain = [Block(0, timestamp, '', NULL_HASH)]

    def add_block(self, data: str):
        index = self.chain[-1].index + 1
        timestamp = str(datetime.now())
        previous_hash = self.chain[-1].hash
        block = Block(index, timestamp, data, previous_hash)

        self.chain.append(block)
