import json
from db.EngineFactory import EmailEvents
from parsers.IParser import IParser


class EmailEventToJsonParser(IParser):
    def parse(self, emailEvent : EmailEvents):
        tmp = {}
        tmp["id"] = emailEvent.id
        tmp["content"] = emailEvent.content
        tmp["type"] = emailEvent.event
        return json.dumps(tmp)