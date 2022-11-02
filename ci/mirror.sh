#!/usr/bin/env bash

REPO_PATH="${PROJECT_HOME}/mastodon-term-services/"

cd "${REPO_PATH}" && git pull origin main || :

git config --global user.email "${GIT_EMAIL}"
git config --global user.name "${GIT_EMAIL}"

current_date="$(date +%Y-%m-%d-T%H:%M:%S%z)"
sed -i "s/\(Last update: \)[^\.]*\./\1${current_date}./g" terms.html
git add .
git commit -m "Update date terms.html: ${current_date}"

git push origin main
git push github main -f
git push pgitlab main -f
git push froggit main -f
exit 0
