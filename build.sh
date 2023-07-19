pip3 install -r deps.txt

python manage.py collectstatic --no-input

python3 manage.py migrate user_accounts
python3 manage.py migrate admin
python3 manage.py migrate save_files
python3 manage.py migrate admin