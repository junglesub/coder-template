---
name: Develop with Node in Docker
description: Develop node and client/server ready work environment
tags: [local, docker, node]
icon: /icon/node.svg
---

# docker-node-mysql

This template is used for node development with mysql.

## dev-server

Dev Server is hosted on port `8080` using caddy.

Port `:3000` (client) is reversed proxy by `:8080/` (root directory)  
Port `:3030` (backend) is reversed proxy by `:8080/api/` (api directory)

Also can change access permission using coder parameter (owner, authenticated, public)


## code-server

`code-server` is installed via the `startup_script` argument in the `coder_agent`
resource block. The `coder_app` resource is defined to access `code-server` through
the dashboard UI over `localhost:13337`.
