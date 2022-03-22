from sqlalchemy import create_engine
from tqdm import tqdm
from config import NETWORKS, BLACK_LIST, POSTGRES_DB_NAME, POSTGRES_DB_PORT, POSTGRES_DB_HOST, POSTGRES_DB_PASSWORD, \
    POSTGRES_USER_NAME, TOKENS, WIN_PERCENT, PRIZE_POOL_ADDRESS

import requests
import pandas as pd
from cyberpy._wallet import address_to_address


def get_delegations(lcd_api: str, validator: str, network: str, black_list: list):
    delegations = []
    url = lcd_api + f'/staking/validators/{validator}/delegations?limit=1000000'
    delegations_raw = requests.get(url).json()['result']
    for delegator in delegations_raw:
        # address = delegator['delegation']['delegator_address']
        # amount = int(delegator['balance']['amount'])
        # if amount >= 10_000_000_000:
        #     print(address, amount)
        temp = (address_to_address(delegator['delegation']['delegator_address'], 'osmo'),
                int(delegator['balance']['amount']))
        delegations.append(temp)
    df = pd.DataFrame(delegations, columns=['address', network]).sort_values(by=network, ascending=False).reset_index(drop=True)
    df = df[~df['address'].isin(black_list)]
    median = df[network].median() / 1.618
    df.drop(df[df[network] < median].index, inplace=True)
    df['rank'] = df[network].rank(ascending=False)
    df[network] = df.apply(lambda x: get_points_df(x['rank']), axis=1)
    return df[['address', network]], median


def get_points_df(value):
    if value <= 10:
        temp = 3
    elif value > 10 and value <= 20:
        temp = 2
    else:
        temp = 1
    return temp


def get_result_table(networks: list, black_list: list = []):
    result_df = pd.DataFrame(columns=['address'])
    medians = []
    for network in tqdm(networks):
        network_df, median = get_delegations(network[0], network[1], network[2], black_list)
        result_df = pd.merge(result_df, network_df, on='address', how='outer')
        if network[2] == 'bostrom':
            medians.append((median / 1_000_000, 'mboot'))
        else:
            medians.append((median / 1_000_000, network[3][1:]))
    result_df['multiplicator'] = result_df.count(axis=1) - 1
    networks = [network[2] for network in networks]
    result_df['total'] = result_df[networks].sum(axis=1) * result_df['multiplicator']
    result_df['win_probability'] = result_df['total'] / result_df['total'].sum() * 100
    result_df = result_df.sort_values(by='total', ascending=False).reset_index(drop=True)
    result_df = result_df[~result_df['address'].isin(black_list)]
    result_df = result_df.reset_index(drop=True)
    medians_df = pd.DataFrame(medians, columns=['amount', 'denom'])
    print(result_df.shape)
    engine = create_engine(
        f'postgresql://{POSTGRES_USER_NAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}')
    result_df.to_sql('participants', engine, if_exists='replace', index=False)
    medians_df.to_sql('min_amount', engine, if_exists='replace', index=False)


def get_current_estimated_prize_pool(networks: list, win_percent: float):
    data = []
    for network in networks:
        balance, denom = get_balance(network[1], network[0], network[3])
        balance = int(balance * win_percent)
        if denom != 'boot':
            data.append((balance / 1_000_000, denom[1:]))
        else:
            data.append((balance, denom))
    df = pd.DataFrame(data, columns=['amount', 'denom'])
    engine = create_engine(
        f'postgresql://{POSTGRES_USER_NAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}')
    df.to_sql('estimated_prize_pool', engine, if_exists='replace', index=False)


def get_balance(validator: str, lcd_api: str, denom: str):
    res = requests.get(lcd_api + f'/cosmos/distribution/v1beta1/validators/{validator}/commission').json()
    token = [x for x in res['commission']['commission'] if x['denom'] == denom][0]
    return (int(float(token['amount'])), denom)


def get_real_pool_prize(address: str, lcd_api: str):
    balances = requests.get(lcd_api + f'/cosmos/bank/v1beta1/balances/{address}').json()['balances']
    data = []
    for balance in balances:
        amount, denom = balance['amount'], TOKENS[balance['denom']]
        if denom != 'boot':
            data.append((int(amount) / 1_000_000, denom[1:]))
        else:
            data.append((amount, denom))
    df = pd.DataFrame(data, columns=['amount', 'denom'])
    engine = create_engine(
        f'postgresql://{POSTGRES_USER_NAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}')
    df.to_sql('current_prize_pool', engine, if_exists='replace', index=False)


def get_black_list(black_list: list):
    black_list = [(x, address_to_address(x, 'osmo')) for x in black_list]
    df = pd.DataFrame(black_list, columns=['original_address', 'osmo_address'])
    engine = create_engine(
        f'postgresql://{POSTGRES_USER_NAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_NAME}')
    df.to_sql('black_list', engine, if_exists='replace', index=False)


if __name__ == "__main__":
    get_result_table(NETWORKS, BLACK_LIST)
    get_current_estimated_prize_pool(NETWORKS, WIN_PERCENT)
    get_real_pool_prize(PRIZE_POOL_ADDRESS, NETWORKS[0][0])
    get_black_list(BLACK_LIST)
