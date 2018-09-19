import argparse

from facebookconversationhistory import FacebookConversationHistory
from facebookconversationprocessor import FacebookConversationProcessor
from filehelpers import read_message_archive, output_html


class Extractor:
    def __init__(self, arguments):
        self.p_id = arguments.p_id
        self.p_name = arguments.p_name

        self.ah_id = arguments.ah_id
        self.ah_name = arguments.ah_name

        self.directory = arguments.directory

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


arg_parser = argparse.ArgumentParser(description='Process Facebook message archive.')
arg_parser.add_argument("--p_id",
                        help='Facebook ID with @facebook.com of conversation participant')
arg_parser.add_argument("--p_name",
                        help='Name of conversation participant')
arg_parser.add_argument("--ah_id",
                        help='Facebook ID with @facebook.com of account holder')
arg_parser.add_argument("--ah_name",
                        help='Name of account holder')
arg_parser.add_argument("--directory",
                        help='Directory containing messages.htm archive file')

Extractor(arg_parser.parse_args()).extract_and_output_file()
