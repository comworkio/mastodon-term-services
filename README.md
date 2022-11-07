# Mastodon term of services

This is the terms of services of the [mastodon.comwork.io](https://mastodon.comwork.io) instance.

You'll find the plain html you can adapt for your own instances here: [terms.html](./terms.html)

You'll also find our rules and banned instances here: [config.yaml](./config.yaml)

The source repository is automatically applying the configuration in a gitops way using this [python project](./admin).

## Table of content

[[_TOC_]]

## Git repositories

* Main repo: https://gitlab.comwork.io/oss/mastodon-term-services.git
* Github mirror: https://github.com/idrissneumann/mastodon-term-services.git
* Gitlab mirror: https://gitlab.com/ineumann/mastodon-term-services.git
* Froggit mirror: https://lab.frogg.it/ineumann/mastodon-term-services.git

## Licences

The [terms.html](./terms.html) is under the CC-BY-SA originally adapted from the [Discourse privacy policy](https://github.com/discourse/discourse).

The python [admin](./admin) code is under the apache 2.0 licence.

## Forking this project

You can fork this project and run it with gitlab-ci and docker, all you have to do is:
* Having a gitlab runner hosted in a place that can join your PostgreSQL over TCP
* Docker and docker-compose
* Those [environment variables set](./mastodon.env.dist)

Of course you can decide to use something else than docker to run the Python code, or something else than gitlab-ci if you want to use another git provider. Pretty simple to achieve the same thing with Github Action for example.

The ban domains are under the `ban` key in the [config.yaml](./config.yaml) file:

```yaml
ban:
  - domain: hatefuldomain.com
    comment: Your comment
```

The rules are under:

```yaml
rules:
  - text: No illegal content in France.
    priority: 10
  - text: Do not post hateful content. No discrimination will be tolerated.
    priority: 20
  - text: Do not harass anyone, participate in group harassment of anyone. Any kind of harassment won't be tolerated.
    priority: 30
  - text: Do not post adult content, including pictures containing nudity, or unwelcome sexual attention (including sexualized comments or jokes).
    priority: 40
  - text: "Beware about our term of services: https://mastodon.comwork.io/terms"
    priority: 50
```

You can adapt those following your convictions and obligations.
