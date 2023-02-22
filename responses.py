import random


def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hate beaned':
        return "Don't tread on those waters."
        client.user.kick(reason=None)

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"
