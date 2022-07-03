from db.EngineFactory import EmailEvents


class EmailEventsValidator:
    def validate(self, emailEvents : EmailEvents):
        if not emailEvents.id:
            return False
        if not emailEvents.content:
            return False
        if not emailEvents.event:
            return False
        return True