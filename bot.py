import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
session = vk_api.VkApi(token="960bde19ae45ba97070e6e4bd45f5a34f58c6be4e6a1ce57c321e65a94fc657b026e1f7a582dc5e300109")

def send_message(user_id, message):
	session.method("message.send",{
		"chat_id": chat_id,
		"message": message,
		"random_id": 0
	})

for event in VkLongPoll(session).listen():
	if event.type == VkEventType.MESSAGE_NEW:
		text = event.text.lower()
		chat_id = event.chat_id

		if text == "hello":
			send_message(chat_id, "Text")