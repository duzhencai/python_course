#!/usr/bin/python2
#-*- coding: UTF-8 -*- 
import os
import shutil


p = os.path.realpath(__file__)
workspace = os.path.split(p)[0]
backup_dir = os.path.join(workspace, 'backup')

if os.path.exists(backup_dir):
     shutil.rmtree(backup_dir)

os.mkdir(backup_dir)
shutil.copy(p, backup_dir)
