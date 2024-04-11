from googletrans import Translator

translator = Translator(service_urls=[
      'translate.google.cn',
    ])

def plain_title(title):
    while True:
        try:
            title = translator.translate(title, dest='zh-cn').text
            break
        except Exception as e:
            print("Error - ",e)
            continue
    print(title)
    # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
    return title

if __name__ == "__main__":
    plain_title("『手紙 〜拝啓 十五の君へ〜』　by “くちびるに歌を” 中五島中学校合唱部OB")