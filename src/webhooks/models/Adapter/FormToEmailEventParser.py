from models.EmailEvent import EmailEvent

class FormToEmailEventParser :

    def Map(self, form):
        email = EmailEvent()
        email.Id = form['_id']
        email.Text = form['msg']
        email.Type = form['event']
        return email
