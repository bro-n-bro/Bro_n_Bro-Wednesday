import requests
import random
import pandas as pd


from itertools import chain
from sqlalchemy import create_engine
from osmopy._wallet import seed_to_privkey, privkey_to_address
from osmopy import Transaction
from config import GRAPHQL_API, HEADERS, POSTGRES_USER_NAME, POSTGRES_DB_PASSWORD, POSTGRES_DB_HOST, POSTGRES_DB_PORT, \
    POSTGRES_DB_NAME, OSMO_LCD, DISTRIBUTION_SHARES


def run_query(query):  # A simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(GRAPHQL_API, json={'query': query}, headers=HEADERS)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))


def get_sample() -> list:
    query = '''{
                    participants {
                        address
                        total
                    }
                }'''
    result = run_query(query)['data']['participants']
    return list(chain.from_iterable([[x['address']] * x['total'] for x in result]))


def get_winners():
    sample = get_sample()
    return random.choices(sample, k=10)


def write_winners_to_db(winners: list):
    df = pd.DataFrame(winners, columns=['address'])
    engine = create_engine(
        f'postgresql://{POSTGRES_USER_NAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}')
    df.to_sql('winners', engine, if_exists='replace', index=False)


def get_rewards(lcd_api: str, address: str):
    balances = requests.get(lcd_api + f'/cosmos/bank/v1beta1/balances/{address}').json()['balances']
    return [(int(balance['amount']), balance['denom']) for balance in balances]


def distribute_rewards(winners: list, rewards: list):
    df = pd.DataFrame(columns=['address', 'payout', 'denom'])
    for asset in rewards:
        payouts = [int(x * asset[0]) for x in DISTRIBUTION_SHARES]
        denoms = [asset[1]] * 10
        data = list(zip(winners, payouts, denoms))
        _df = pd.DataFrame(data, columns=['address', 'payout', 'denom'])
        df = pd.concat([df, _df])
    df = df.reset_index(drop=True)
    return df


def generate_tx(seed, gas, memo, number):
    sequence = get_sequence(seed)
    return Transaction(
        privkey=seed_to_privkey(seed),
        account_num=number,
        sequence=sequence,
        fee=0,
        gas=gas,
        memo=memo,
        chain_id="osmosis-1",
        sync_mode="broadcast_tx_sync",
    )


def get_sequence(seed):
    address = privkey_to_address(seed_to_privkey(seed))
    res = requests.get(OSMO_LCD + f'/cosmos/auth/v1beta1/accounts/{address}')
    result = res.json()['account']['sequence']
    return int(result)





