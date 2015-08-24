#!/usr/bin/env python
#-*- coding:utf-8 -*-
from fabric.api import env, run, cd, hide, sudo
from project.local_settings import *


def pull():
    git("pull --rebase origin master")

def git(cmd):
    with cd(project_path):
        run("git %s" % cmd)

def server():
    env.server = server
    env.hosts = [user + '@' + host +':'+ port]
    #env.CLONE_PATH = u'/home/intipfaction/webapps/crm/crm'
    env.PROJECT_PATH = project_path
    #env.PYTHON_BIN = u'/home/intipfaction/.virtualenvs/crm/bin/python'
    #env.PIP_BIN = u'/home/intipfaction/.virtualenvs/crm/bin/pip'
    ##env.WEBSERVER = u'httpd'
    #env.SETTINGS = u'--settings=deploy.webfaction.settings'
    #env.DB_NAME = u'crm'
    #env.USER_DB = u'crm_webfaction'
    #env.PASS_DB = u'postgres'