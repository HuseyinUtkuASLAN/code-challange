import json
from parsers.IParser import IParser


class ByteArrayToDictParser(IParser):
    def parse(self, byteArray) :
        body = byteArray.decode("utf-8")
        return json.loads(body)
