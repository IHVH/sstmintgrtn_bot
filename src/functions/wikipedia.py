import wikipedia

wikipedia.set_lang('ru')

def wiki_op(message):
    word = message.strip("/Wikipedia").lower()
    try:
        final_message = wikipedia.summary(word)
    except wikipedia.exceptions.PageError:
        final_message = "\nУпс, я не смог найти слово"
    except wikipedia.exceptions.DisambiguationError:
        final_message = '\nУпс, я озадачен вашим запросом, уж больно много вариантов. \nПопробуйте уточнить:'
    except wikipedia.exceptions.HTTPTimeoutError:
        final_message = '\nУпс, видимо, мне не хотят отвечать... \nДавайте  подождём, пусть они там немного разгрузятся.'
    except wikipedia.exceptions.RedirectError:
        final_message = '\nУпс, нас пытаются куда-то перенаправить... \nПопробуйте поискать еще раз.'
    except wikipedia.exceptions.WikipediaException:
        final_message = '\nУпс, что-то пошло не так... \nПопробуйте поискать еще раз.'
    return final_message
