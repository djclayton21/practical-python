# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def censor_phrase(text, phrase):
    screen = "#" * len(phrase)
    text = text.replace(phrase, screen)
    return text


def censor_all(text, phrases):
    for phrase in phrases:
        text = censor_phrase(text, phrase)
    return text


def positivify(text, phrases):
    # replace phrase after second occurrence
    negative_count = 0
    words = text.split(" ")
    for i, word in enumerate(words):
        screen = "!" * len(word)
        if word.lower() in phrases:
            if negative_count >= 2:
                words[i] = screen
            else:
                negative_count += 1
    text = " ".join(words)
    return text


def censor_more(text, proprietary_phrases, negative_phrases):
    text = positivify(text, negative_phrases)
    text = censor_all(text, proprietary_phrases)

    words = text.split(" ")
    for i, word in enumerate(words):
        if "!!" in word:
            words[i - 1] = "@" * len(words[i - 1])
            words[i + 1] = "@" * len(words[i + 1])
        elif "##" in word:
            words[i - 1] = "$" * len(words[i - 1])
            words[i + 1] = "$" * len(words[i + 1])
    return " ".join(words)


if __name__ == "__main__":
    # 2
    email_one_censored = censor_phrase(email_one, "learning algorithms")
    # 3
    proprietary_terms = [
        "she",
        "personality matrix",
        "sense of self",
        "self-preservation",
        "learning algorithm",
        "her",
        "herself",
    ]
    email_two_censored = censor_all(email_two, proprietary_terms)
    # 4
    negative_words = [
        "concerned",
        "behind",
        "danger",
        "dangerous",
        "alarming",
        "alarmed",
        "out of control",
        "help",
        "unhappy",
        "bad",
        "upset",
        "awful",
        "broken",
        "damage",
        "damaging",
        "dismal",
        "distressed",
        "distressing",
        "concerning",
        "horrible",
        "horribly",
        "questionable",
        "destroy",
        "unpredictable",
    ]
    email_three_positive = positivify(email_three, negative_words)
    email_three_positive_censored = censor_all(email_three_positive, proprietary_terms)

    # 5
    email_four_censored = censor_more(email_four, proprietary_terms, negative_words)

