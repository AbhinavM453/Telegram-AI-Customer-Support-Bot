import telegram
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatMessage
from .services import generate_ai_response

BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
bot = telegram.Bot(token=BOT_TOKEN)

@api_view(["POST"])
def telegram_webhook(request):
    data = request.data
    message = data["message"]["text"]
    chat_id = data["message"]["chat"]["id"]

    ai_reply = generate_ai_response(message)

    bot.send_message(chat_id=chat_id, text=ai_reply)

    return Response({"status": "Message processed"})

@api_view(["GET"])
def messages_list(request):
    messages = ChatMessage.objects.all().order_by("-id")
    data = [{"message": m.message, "response": m.response} for m in messages]
    return Response(data)


@api_view(["POST"])
def test_send(request):
    user_msg = request.data.get("message", "")
    reply = generate_ai_response(user_msg)

    ChatMessage.objects.create(
        user_id="local_test",
        message=user_msg,
        response=reply
    )

    return Response({"user": user_msg, "ai": reply})
