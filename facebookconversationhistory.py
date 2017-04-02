from yattag import Doc, indent


class FacebookConversationHistory:
    def __init__(self, message_history, p_name, ah_name):
        self.doc, self.tag, self.text = Doc().tagtext()
        self.message_history = message_history
        self.p_name = p_name
        self.ah_name = ah_name

    def __generate_html_head(self):
        with self.tag("head"):
            with self.tag("title"):
                self.text("Conversations between " + self.p_name + " and " + self.ah_name)

    def __generate_table_header(self):
        with self.tag("tr"):
            with self.tag("th"):
                self.text("Date and Time")
            with self.tag("th"):
                self.text("Sender")
            with self.tag("th"):
                self.text("Message")

    def __generate_message(self, message):
        (date_and_time, sender, message_text) = message
        with self.tag("tr"):
            with self.tag("td"):
                self.text(date_and_time)
            with self.tag("td"):
                self.text(sender)
            with self.tag("td"):
                self.text(message_text)

    def get_output(self):
        with self.tag("html"):
            self.__generate_html_head()
            with self.tag("body"):
                with self.tag("table"):
                    self.__generate_table_header()
                    for message in self.message_history:
                        self.__generate_message(message)
        return indent(self.doc.getvalue())
