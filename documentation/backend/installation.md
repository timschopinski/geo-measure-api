## Preparation



## Running locally with docker-compose 

### Installation
1. Clone repository `[...]` 

    (or with HTTPS `git clone [...]`)
 
2. Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) and [docker-compose](https://docs.docker.com/compose/install/).
3. Then add .env file in backend/config/settings (You can copy dotenv.example contents for local development)


### Setup githooks 
Set git hooks config path to use hooks from the repository:

`git config core.hooksPath .githooks`

### Prepare local env for pre-commit checks

Create venv and install dev dependencies:

1. `python3.10 -m venv venv`
2. `source /venv/bin/activate`
3. `pip install -r backend/dependencies/dev.txt`

### Run application
6. Run `./reset.sh`. This will initialize default data
7. Run `docker compose up`
