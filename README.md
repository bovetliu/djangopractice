
### Prepare
1. Clone the project;
2. `./create-env-if-not-exist.sh`
3. `source .venv/bin/activate` to enter the virtual env;
4. `pip install -r requirements.txt` if you haven't done so;

### Code
1. Go into `./src` and add new app through `./manage.py startapp <namespace>` (see details in [doc](https://docs.djangoproject.com/en/1.10/ref/django-admin/))
2. Follow Django or platform apis to create new models/services/tasks;
3. `./manage.py makemigrations` then `./manage.py migrate`;
4. Run the Django dev server with `./manage.py runserver 0.0.0.0:8000`; 
5. Finish with `deactivate` to exit the virtual env;
