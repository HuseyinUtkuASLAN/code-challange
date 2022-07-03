class EmailEventRepository:
    def __init__(self, session):
        self._session = session

    def add(self, emailEvents):
        self._session.add(emailEvents)
        self._session.commit()
