# May Site — WESTY

This folder contains the WESTY Django site and the standalone `index.html`
preview. The Django app keeps profile and link editing in its admin panel.

## Run on Windows (PowerShell)

```powershell
cd "C:\Users\Admin\Desktop\сайт\may site"
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. To edit the profile and links, open
`http://127.0.0.1:8000/admin/` and sign in with the superuser account.

If no admin account exists yet, open another PowerShell window in this folder
and run:

```powershell
python manage.py createsuperuser
```

In **Profile and links**, edit the name, username, Ukrainian quote, and avatar
URL. Add and reorder **Page links**, set their URLs, or toggle whether they are
shown on the page. The `index.html` preview is a separate static copy; its link
URLs are edited directly in that file.

For production, set a secure `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=false`, and
appropriate `DJANGO_ALLOWED_HOSTS` environment variables. Do not publish
`.env`, credentials, or the SQLite database to a public repository.
