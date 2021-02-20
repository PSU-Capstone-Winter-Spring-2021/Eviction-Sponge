import requests


# attempt login function that takes in a username and password and
# returns a success (0) or failure (1)
# attempts to login to the OECI website

class Crawler:
    @staticmethod
    def attempt_login():
        url = 'https://publicaccess.courts.oregon.gov/PublicAccessLogin/login.aspx'
        payload = {'username': 'QQLMUL01', 'password': 'QQLMUL01'}
        # , 'ValidateUser': '1',
        # 'dbKeyAuth': 'JusticePA', 'SignOn': 'Sign+On'}
        r = requests.post(url, payload)
        content = r.text
        print content

# for testing only
def main():
    Crawler.attempt_login()
    #"Request Rejected"


if __name__ == "__main__":
    main()
