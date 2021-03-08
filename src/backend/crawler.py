import requests


class UnableToReachOECI(Exception):
    pass


class InvalidLoginCreds(Exception):
    pass


# attempt login function that takes in a username and password and
# returns a success (0) or throws an exception detailing why failure occured
# attempts to login to the OECI website

class Crawler:
    def __init__(self):
        pass

    @staticmethod
    def attempt_login(username, password):
        url = 'https://publicaccess.courts.oregon.gov/PublicAccessLogin/login.aspx'
        payload = {'UserName': username, 'Password': password, 'ValidateUser': '1',
                   'dbKeyAuth': 'JusticePA', 'SignOn': 'Sign+On'}
        r = requests.post(url, payload)
        content = r.text
        if "Case Records" in content:
            # success
            return content
        elif "Oregon eCourt is temporarily unavailable due to maintenance" in content:
            raise UnableToReachOECI
        else:
            raise InvalidLoginCreds


if __name__ == "__main__":
    main()