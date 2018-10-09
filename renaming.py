#!/usr/bin/env python3
import shutil, os

## Prompt user for what directory we should start in
vardirname = input('What is the directory we should start in?')

## Ensure our program is 'starting' from this location
os.chdir('/home/student/mycode/')

## print the contents of /home/student/mycode/
varmylist = os.listdir(vardirname)

## print list as a string
print('\n *************')
print('                ')
print('\n *************')

## Collect input of file we should move
varfilename = input('What is the file you would like to move from /home/student/mycode/?')

varmoveto = input('What is the new location of the file? You may also include a new filename.')

shutil.move(varfilename, varmoveto)


