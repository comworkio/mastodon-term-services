# Mastodon term of services

This is the terms of services of the [mastodon.comwork.io](https://mastodon.comwork.io) instance.

You'll find the plain html you can adapt for your own instances here: [terms.html](./terms.html)

You'll also find our rules and banned instances here: [config.yaml](./config.yaml)

The source repository is automatically applying the configuration in a gitops way using this [python project](./admin).

## Table of content

[[_TOC_]]

## Licence

The [terms.html](./terms.html) is under the CC-BY-SA originally adapted from the [Discourse privacy policy](https://github.com/discourse/discourse).

The python [admin](./admin) code is under the apache 2.0 licence.

## Forking this project

You can fork this project and run it with gitlab-ci and docker, all you have to do is:
* Having a gitlab runner hosted in a place that can join your PostgreSQL over TCP
* Those [environment variables set](./mastodon.env.dist)

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/mastodon-term-services.git
* Github mirror: https://github.com/idrissneumann/mastodon-term-services.git
* Gitlab mirror: https://gitlab.com/ineumann/mastodon-term-services.git
* Froggit mirror: https://lab.frogg.it/ineumann/mastodon-term-services.git
