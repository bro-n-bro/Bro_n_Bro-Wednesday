from config import OSMO_LCD, OSMO_RPC, PRIZE_POOL_ADDRESS, PRIZE_POOL_ADDRESS_MNEMONIC, PRIZE_POOL_ADDRESS_NUMBER
from db import generate_tx, get_winners, write_winners_to_db, get_rewards, distribute_rewards, get_winners_table



def main():
    memo = input("Enter memo please: ")
    winners = get_winners()
    [print(w) for w in winners]
    write_winners_to_db(winners)
    rewards = get_rewards(OSMO_LCD, PRIZE_POOL_ADDRESS)
    distribution_df = distribute_rewards(winners, rewards)
    print('the resulting tx:')
    get_winners_table(winners, distribution_df)
    tx = generate_tx(PRIZE_POOL_ADDRESS_MNEMONIC, 2_000_000, memo, PRIZE_POOL_ADDRESS_NUMBER)
    for index, row in distribution_df.iterrows():
        tx.add_transfer(row['address'], row['payout'], row['denom'])
    conf = input("Do you want to broadcast this transaction? (y/n): ")
    if conf == 'y' or conf == 'Y':
        tx.broadcast(OSMO_RPC)
        print('brodcasted')
    elif conf == 'n' or conf == 'N':
        print('declined')
    else:
        print('declined')


if __name__ == "__main__":
    main()