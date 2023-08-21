import mailmaestro


class EmailDraftingAgent:

    def __init__(self):
        self.mailmaestro = mailmaestro.MailMaestro()

    def generate_email_draft(self, bullet_points, tone, language):
        email_draft = self.mailmaestro.generate_email(bullet_points, tone, language)
        return email_draft


agent = EmailDraftingAgent()