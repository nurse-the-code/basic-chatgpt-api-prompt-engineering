import os
import json
import openai

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

openai.organization = os.environ.get("OPENAI_ORG_ID")
# TODO: Replace with your environmental variable for your OpenAI API key
openai.api_key = os.environ.get("OPENAI_API_KEY")


def create_user_message(message):
    return {"role": "user", "content": message}


def call_chat_api(messages):
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
        )
        response_messages = completion.choices[0].message.content
        return response_messages
    except Exception as e:
        print('Error calling OpenAi\'s chat api: ', e)


def converse():
    messages = []
    while True:
        user_input = input("user: ")
        messages.append(create_user_message(user_input))
        response = call_chat_api(messages)
        messages.append({"role": "system", "content": "You are a AI assistant who gives short responses"})
        messages.append({"role": "assistant", "content": response})
        print(response)


def write_book():
    book_topic = input('What do you want your fictional book to be about?')
    num_chapters = input('How many chapters do you want your book to have?')
    max_chapters = 20
    book = {}
    while not num_chapters.isnumeric():
        num_chapters = input('How many chapters do you want your book to have?')
    num_chapters = int(num_chapters)
    if num_chapters > max_chapters:
        print(f'That is too many chapters. I will give you {max_chapters} chapters.')
        num_chapters = max_chapters
    print(f'Your book will be about {book_topic} and will have {num_chapters} chapters')
    chapter_list_prompt = f'''Given the prompts below, write the outline summarizing each chapter of a literary award 
    winning, best seller novella in the this JSON format: ["chapter 1 summary", "chapter 2 summary", ...]
    
    number of chapters: {num_chapters}
    user prompt: {book_topic}'''
    print("Generating chapter summaries...")
    chapter_summaries = call_chat_api([create_user_message(chapter_list_prompt)])
    try:
        chapter_summaries = json.loads(chapter_summaries)
        print("Chapter summaries generated successfully.")
    except json.JSONDecodeError:
        print("Received invalid JSON string from OpenAI API. Please try again. If the problem persists, contact the "
              "developer.")
        return
    try:
        for chapter in range(1, num_chapters + 1):
            print(f'Generating chapter {chapter} of {num_chapters}...')
            if chapter / num_chapters < 1 / 3:
                book_stage = 'beginning'
            elif chapter / num_chapters < 2 / 3:
                book_stage = 'middle'
            else:
                book_stage = 'end'
            previous_chapter = book[chapter - 1] if chapter > 1 else 'None'
            chapter_text_prompt = f'''Given the prompt below, write the text for chapter {chapter} of a literary 
            award, best seller novella. End every chapter with a cliffhanger (unless it is the last chapter).
    
                user summary of book: {book_topic}
                previous chapter text (be sure to address any cliffhangers): {previous_chapter}
                {chapter} of {num_chapters} (this means we are towards the {book_stage} of the book)
                chapter summary: {chapter_summaries[chapter - 1]}'''
            chapter_text = call_chat_api([create_user_message(chapter_text_prompt)])
            book[chapter] = chapter_text
            print(f'Chapter {chapter} generated successfully.')
        print('Book generated successfully.\n\n\n\n')
    except Exception as e:
        print('Something went wrong. Let\'s see if we can salvage the book. Please try again. If the problem '
              'persists, contact the developer.', e)
    for chapter in book:
        print(f'{book[chapter]}\n\n\n\n')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    write_book()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
