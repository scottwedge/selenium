#!/bin/bash
#
# Useful script to setup Git colours to all white in 'git setup'
# command to avoid hard-to-read red default colour
#
# To set files to colour white for all git statuses:
git config color.status.added "white bold" --replace-all
git config color.status.untracked "yellow bold blink" --replace-all
git config color.status.changed "white bold blink" --replace-all
git config color.diff.frag yellow
git config color.diff.old white
git config color.diff.new white

# Common .gitignore file settings
#*.pyc
#__pycache__/
