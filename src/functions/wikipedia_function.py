import wikipedia as wiki
import wikipedia.exceptions as wiki_ex

wiki.set_lang('ru')

def wiki_op(message):
    word = message.strip("/Wikipedia").lower()
    try:
        final_message = wiki.summary(word)
    except wiki_ex.PageError:
        final_message = "\nУпс, я не смог найти слово"
    except wiki_ex.DisambiguationError:
        final_message = '\nУпс, я озадачен вашим запросом, уж больно много вариантов. \nПопробуйте уточнить:'
    except wiki_ex.HTTPTimeoutError:
        final_message = '\nУпс, видимо, мне не хотят отвечать... \nДавайте  подождём, пусть они там немного разгрузятся.'
    except wiki_ex.RedirectError:
        final_message = '\nУпс, нас пытаются куда-то перенаправить... \nПопробуйте поискать еще раз.'
    except wiki_ex.WikipediaException:
        final_message = '\nУпс, что-то пошло не так... \nПопробуйте поискать еще раз.'
    return final_message
