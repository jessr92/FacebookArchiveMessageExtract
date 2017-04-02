from bs4 import BeautifulSoup


class FacebookConversationProcessor:
    def __init__(self, message_archive):
        self.data = message_archive

    @staticmethod
    def __get_threads(data):
        return BeautifulSoup(data, "html.parser").findAll("div", {"class": "thread"})

    @staticmethod
    def __get_message_info(data):
        return data.findAll("div", {"class": "message"})[::-1]

    @staticmethod
    def __get_message_text(data):
        return data.findAll("p")[::-1]

    @staticmethod
    def __get_message_date_and_time(message_info):
        return message_info.find("span", {"class": "meta"}).text

    @staticmethod
    def __get_message_sender(message_info, p_id, p_name, ah_id, ah_name):
        return message_info.find("span", {"class": "user"}).text \
            .replace(p_id, p_name) \
            .replace(ah_id, ah_name)

    def __get_messages(self, threads, p_id, p_name, ah_id, ah_name):
        message_history = []
        for thread in threads:
            if thread.text.startswith(p_id + ", " + ah_id):
                messages_info = self.__get_message_info(thread)
                messages_text = self.__get_message_text(thread)
                for message in range(0, len(messages_info)):
                    info = messages_info[message]
                    message_text = messages_text[message].text
                    sender = self.__get_message_sender(info, p_id, p_name, ah_id, ah_name)
                    date_and_time = self.__get_message_date_and_time(info)
                    message_history.append((date_and_time, sender, message_text))
        return message_history

    def process(self, p_id, p_name, ah_id, ah_name):
        threads = self.__get_threads(self.data)
        return self.__get_messages(threads, p_id, p_name, ah_id, ah_name)
