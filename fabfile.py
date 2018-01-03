import os  
from contextlib import contextmanager  
from fabric.api import cd, env, prefix, run, sudo, task

# don't changed
SYSTEM_NAME = 'dapi'

PROJECT_NAME = '<replace_this>' 
REPOSITORY_URL = '<url_repository_git>'



PROJECT_ROOT = '<replace_this>' 
VENV_DIR = os.path.join(PROJECT_ROOT, '../env3')  
REPO = '<replace_this>' 

host_dev = ['<remplace for your IP SERVER']

@task
def dev():  
    env.hosts = host_dev
    env.environment = 'dev'
    env.forward_agent = True

 
@contextmanager
def source_virtualenv():  
    with prefix('source ' + os.path.join(VENV_DIR, 'bin/activate')):
        yield


def clean():  
    """Cleans Python bytecode"""
    sudo('find . -name \'*.py?\' -exec rm -rf {} \;')


def chown():  
    """Sets proper permissions"""
    sudo('chown -R www-data:www-data %s' % PROJECT_ROOT)


def restart():  
    sudo('service nginx restart')


   

@task
def deploy():  
    """
    Deploys the latest tag to the dev server
    """
    sudo('chown -R %s:%s %s' % (env.user, env.user, PROJECT_ROOT))

    with cd(PROJECT_ROOT):
        run('git pull origin master')
        with source_virtualenv():
            with prefix('export DJANGO_SETTINGS_MODULE={}.settings'.format(SYSTEM_NAME,)):
                run('pwd')
                run('source ../env3/bin/activate')
                run('pip3 install -r requirements/staging.txt')
                run('./migratelocal.py')
                run('./runlocal.sh')
          

    chown()
    restart()

 