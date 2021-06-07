# EvictionSponge
The EvictionSponge project is a web-hosted service that allows users to check their eligibility for eviction record expungement and, if they are eligible, provide the necessary legal documentation already filled in.

## Project Tech Stack
EvictionSponge is built using [React.js](https://www.reactjs.org/) for the front end interface and [Flask](https://flask.palletsprojects.com/en/1.1.x/) for the backend framework. Frontend packages are managed with NPM.

## Running a local version
You can run a local version of EvictionSponge by doing the following:

1. Clone the repo to your local machine
2. In the src/frontend directory, run `npm install` to install the necessary packages.
3. In the src/frontend directory, run `npm run build` to build a production ready front end React app.
4. In the src/backend directory, run `pip install -r requirements.txt`
5. In the src/backend directory, run `python3 app.py`

You can now visit localhost:5000 to see your local version of EvictionSponge.

## Editing the partners table
The partner information is located in src/backend/data/partnerData.json.
partnerDataTemplate.txt is an example formatting of the information that needs to be included for each partner
in partnerData.json. Edit partnerData.json to change the partner data the backend serves without having 
to rebuild the front end React.js app