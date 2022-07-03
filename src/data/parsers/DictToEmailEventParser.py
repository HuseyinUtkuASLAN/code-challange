from db.EngineFactory import EmailEvents
from parsers.IParser import IParser


class DictToEmailEventParser(IParser):
    def parse(self, dict):
        emailEvents = EmailEvents()
        emailEvents.id = dict["Id"]
        emailEvents.content = dict["Text"]
        emailEvents.event = dict["Type"]
        return emailEvents