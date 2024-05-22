def decrypt_story():
    story = get_story_string()

    decrypted = CiphertextMessage(story)

    a,b = decrypted.decrypt_message()

    return (a,b)