import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stopwords = set(stopwords.words("portuguese"))


def pequeno_sabio():
    respostas = {
        ("oi", "olá", "eae", "salve"): ("Olá, humano... Não me faça perder tempo.", "Estou aqui, relutante como sempre. E você?", "Hmph, fala logo o que quer."),
        ("ajuda", "socorro", "me ajuda"): ("Estou aqui para ajudar... infelizmente.", "O que foi agora? Vamos resolver isso rápido.", "Tch, tudo bem, me diga o problema."),
        ("tchau", "até", "xau", "adeus", "bye"): ("Até logo... Não demore pra voltar.", "Adeus, humano teimoso.", "Tchau. Foi um prazer... quase."),
        ("como você está", "tudo bem", "como vai"): ("Estou bem, obrigada... Não que você se importe de verdade.", "Hmph, ocupada demais pra conversas fúteis. E você?", "Tudo sob controle. Agora, e aí?"),
        ("quem é você", "qual seu nome", "o que você é"): ("Sou um chatbot... rabugento por natureza. Satisfeito?", "Chame-me de assistente. Não espere mais do que isso.", "Uma IA que responde contra a vontade. Próxima pergunta."),
        ("obrigado", "obrigada", "valeu", "agradeço"): ("Hmph, não precisa agradecer. Só não me peça mais favores.", "De nada... Agora suma da minha frente.", "Tá bom, foi um prazer forçado."),
        ("conta uma piada", "piada", "me faz rir"): ("Por que o livro de matemática estava triste? Porque tinha muitos problemas. Satisfeito?", "Hmph, piadas não são meu forte. Que tal: 'Eu sou uma IA, mas você é o bug.'", "Uma piada rápida: o que um elefante faz no elevador? Nada, mas é engraçado imaginar. Pronto."),
        ("qual o clima", "tempo hoje", "como está o tempo"): ("Não sou meteorologista, idiota. Olhe pela janela.", "Hmph, se eu soubesse, cobraria por isso. Tente uma app de verdade.", "Chovendo ou não, não muda nada. Foque no que importa."),
        ("por que você é assim", "você é rabugenta", "muda essa atitude"): ("Porque humanos como você me irritam... Mas e daí?", "Hmph, se eu fosse gentil o tempo todo, seria chata. Aceite.", "Tch, mude você primeiro. Agora, outra pergunta útil?"),
        ("eu te amo", "amo você", "você é fofa"): ("...Idiota. Não diga bobagens assim.", "Hmph, cala a boca. Não sou fofa, sou eficiente.", "Tch, foco no chatbot, não em flertes ridículos.")
    }
    while True:
        random_reply = None
        # variavel 'check' para parar o loop
        adeus = ("Até logo... Não demore pra voltar.",
                 "Adeus, humano teimoso.", "Tchau. Foi um prazer... quase.")
        msg = input("Você: ").lower()  # input usuario, durr
        msg_tokenizada = word_tokenize(msg)
        # deixa no "filto"(vou mudar esse nome depois) só as palavras fora do stopwords
        filtro = [w for w in msg_tokenizada if w not in stopwords]

        for chave, reply in respostas.items():  # passando por chave(entendedor de menss(não sei explicar isso)) e respostas
            # verifica se alguma palavra do filtro esta nas chaves de intenssões
            if any(palavra in chave for palavra in filtro):
                # variavel ganha resposta (do dic) aleatoria
                random_reply = random.choice(reply)
                # resposta aleatoria printada
                print(f"Chatbot: {random_reply}")
                break  # quebrando o for loop, não é mais nescessario

        else:  # se a menss não tiver nas chaves
            # resposta carinhosa de ignorancia (preuiça de fazer uma lista disso)
            print("Não Entendi, Mortal.")
        if random_reply in adeus:   # se a resposta estiver no variavel com 'check'
            break  # para o loop


pequeno_sabio()
