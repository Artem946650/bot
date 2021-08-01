import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
session = vk_api.VkApi(token="960bde19ae45ba97070e6e4bd45f5a34f58c6be4e6a1ce57c321e65a94fc657b026e1f7a582dc5e300109")
longpoll = VkBotLongPoll(session, 206207722)

def send_message(chat_id, message):
	session.method("message.send",{
		"chat_id": chat_id,
		"message": message,
		"random_id": 0
	})

for event in longpoll.listen():
	if event.type == VkEventType.MASSAGE_NEW:
		if event.from_chat:
			id = event.chat_id
			msg = event.object.nessage['message'].lower()
			if msg == 'hello':
				sender(id, 'privet')