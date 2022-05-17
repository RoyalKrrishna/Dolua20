if [ -z $UPSTREAM_REPO ]
then
  echo "Main Repository"
  git clone https://github.com/RoyalKrrishna/Doluram2.0.git /Doluram
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Doluram2.0
fi
cd /Doluram2.0
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
