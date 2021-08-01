import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
session = vk_api.VkApi(token="b8ce663972bc5f3a907ee526a3c3a357f07faa6d77b090e4219ab8c3df7224230b01cdc8f0a5be0680920")

def send_message(user_id, message):
	session.method("message.send",{
		"chat_id": chat_id,
		"message": message,
		"random_id": 0
	})

for event in VkLongPoll(session).listen():
	if event.type == VkEventType.MASSAGE_NEW:
		text = event.text.lower()
		chat_id = event.chat_id

		if text == "hello":
			send_message(chat_id, "Text")