import yaml
import tweepy
import random


def load_secrets():
    # load in local twitter keys and tokens file
    yaml_secrets = open("secrets.yaml")
    parsed_secrets = parsed_secrets = yaml.load(yaml_secrets, Loader=yaml.FullLoader)
    yaml_secrets.close()
    return parsed_secrets


def create_tweet():

    project = [
        "API development",
        "GitLab CI/CD",
        "NetDevOps",
        "SD-WAN",
        "Docker",
        "Azure",
        "AWS",
        "Ansible",
        "Batfish",
        "Infrastructure-as-Code",
    ]

    buzz = [
        "Transformational",
        "Super Cool",
        "Neat",
        "Disruptive",
        "Innovation",
        "Engagement",
        "Progressive",
        "a Paradigm Shift",
        "a Game Change",
        "Moving the Needle",
    ]
    rando1 = random.randint(0, 9)
    rando2 = random.randint(0, 9)

    tweet = "Working hard on {}, now that's {}!".format(project[rando1], buzz[rando2])
    return tweet


def main():

    # load secrets
    secrets = load_secrets()

    # authenticate to API
    auth = tweepy.OAuthHandler(secrets["api_key"], secrets["api_secret"])
    auth.set_access_token(secrets["access_token"], secrets["access_secret"])
    api = tweepy.API(auth)

    # generate message
    tweet = create_tweet()
    api.update_status(tweet)


if __name__ == "__main__":
    main()
