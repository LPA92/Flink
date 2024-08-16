cd links
python3.12 -m venv .virtual
source .virtual/bin/activate
python3.12 -m pip install -U pip
pip install reflex --upgrade
pip freeze > requirements.txt
pip install -r requirements.txt
rm -rf public
reflex init
API_URL=https://flink.onrender.com reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate