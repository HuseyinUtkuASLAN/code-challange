# code-challange
## How to run
- Run docker compose files under docker/postgre and docker/rabbit-mq
- Install required packages
  - flask
  - pika
  - websockets
  - asyncio
  - sqlalchemy
  - psycopg2
- Run all 3 services using '''python main.py'''
- Run src/basic.html
## Architecture

![architecture](https://github.com/HuseyinUtkuASLAN/code-challange/blob/main/emailFlow.drawio.png)

## Missing features
- containers
- single docker-compose
- tests
- implementation of proper dependency injection library
- health checks
- ci/cd
- deployment on k8s
