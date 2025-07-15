from web3 import Web3

# Можно заменить другим RPC-провайдером, например Infura или Alchemy
INFURA_URL = "https://cloudflare-eth.com"

def get_eth_balance(address: str):
    if not Web3.isAddress(address):
        print("❌ Некорректный адрес Ethereum.")
        return

    w3 = Web3(Web3.HTTPProvider(INFURA_URL))

    try:
        balance_wei = w3.eth.get_balance(address)
        balance_eth = w3.fromWei(balance_wei, 'ether')
        print(f"💰 Баланс {address}: {balance_eth:.6f} ETH")
    except Exception as e:
        print(f"❌ Ошибка при получении баланса: {e}")

if __name__ == "__main__":
    user_address = input("🔗 Введите адрес Ethereum-кошелька: ").strip()
    get_eth_balance(user_address)
