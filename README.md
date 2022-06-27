# Brownie Repo

## Setups

### Setup envs

```
poetry install

poetry run brownie compile

poetry run brownie networks add Ethereum ganache-local host=http://127.0.0.1:8545 chainid=5777
poetry run brownie networks add Ethereum mainnet-fork host=http://127.0.0.1:8546 chainid=5778
```

### Setup Eth local blockchains

```
docker-compose up
```

### Remove set networks

```
poetry run brownie networks delete ganache-local 
poetry run brownie networks delete mainnet-fork
```

### Running Tests

```
poetry run brownie test --network ganache-local -vs
poetry run brownie test --network mainnet-fork -vs
```

### Clean repo (remove previous deployment artefacts)

```
make clean
```

