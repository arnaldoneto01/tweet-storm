import sys


def tweet_storm(full_text, trim=False, chars=140, attempt=0):

    tweet_limit = chars
    index_limit = get_index_limit(full_text, tweet_limit) + attempt
    index = index_generator(index_limit)

    bag_of_words = full_text.split() if trim else full_text.split(" ")
    tweets = [create_tweet(bag_of_words, tweet_limit, index)
              for i in range(index_limit)]

    return tweets if not bag_of_words else tweet_storm(full_text, attempt=attempt+1)


def get_index_limit(full_text, tweet_limit):
    # TO DO: handle big indexes (what will happen if the indexes have more than 140 chars?)
    # TO DO: This function is not capable of calculate the exact index number. We may improve performance if we manage to achieve that, because we will be able to remove recursion.
    text_length = len(full_text)
    index_limit_estimate = round_up(text_length, tweet_limit)
    indexes_length = len(" ".join(index_generator(index_limit_estimate))) + 1
    total_lenght = text_length + indexes_length
    return round_up(total_lenght, tweet_limit)


def round_up(numerator, denominator):
    return -(-numerator//denominator)


def index_generator(index_limit):
    n = 1
    while n <= index_limit:
        yield "{}/{}".format(n, index_limit)
        n += 1


def create_tweet(bag_of_words, tweet_limit, index):
    tweet = next(index)
    # TO DO : Handle big words (+30 chars)
    # TO DO : Handle huge words (+chars than tweet limit)
    # TO DO : Break tweets based on ponctuation or sentences that make more sense.
    while len(tweet) <= tweet_limit and bag_of_words:
        if len(tweet) + len(bag_of_words[0]) >= tweet_limit:
            break
        tweet += " " + bag_of_words.pop(0)
    return tweet


if __name__ == "__main__":
    full_text = sys.argv[1]
    print(tweet_storm(full_text))
