from facebookconversationhistory import FacebookConversationHistory
from facebookconversationprocessor import FacebookConversationProcessor
from filehelpers import read_message_archive, output_html


class Extractor:
    def __init__(self):
        self.p_id = "509508305@facebook.com"
        self.p_name = "Shantel Arendt"

        self.ah_id = "625786616@facebook.com"
        self.ah_name = "Gordon Reid"

        self.directory = "C:/Users/gordo/Downloads/facebook-gordon1992/html/"

        self.i_file = self.directory + "messages.htm"
        self.o_file = self.directory + self.p_name + " and " + self.ah_name + ".htm"

        self.message_archive = read_message_archive(self.i_file)

    def __extract_message_history(self):
        processor = FacebookConversationProcessor(self.message_archive)
        message_history = processor.process(self.p_id, self.p_name, self.ah_id, self.ah_name)
        doc = FacebookConversationHistory(message_history, self.p_name, self.ah_name)
        return doc.get_output()

    def extract_and_output_file(self):
        message_history = self.__extract_message_history()
        output_html(self.o_file, message_history)


Extractor().extract_and_output_file()
