import requests
from fake_useragent import UserAgent

user_agent = UserAgent()

def get_hashrate():

	url = 'https://pool.binance.com/mining-api/v1/public/pool/stat?observerToken=Ns0P0LVoZ0yuTICET88W79jKw3deJqtU7U316k0t0hU02866'

	headers = {
		'authority': 'pool.binance.com',
		"User-Agent": user_agent.random
		}

	r = requests.get(url,  headers=headers)
	if r.status_code ==200:
		data=r.json()
		profitYesterday = data['data']['profitYesterday']['ETH']
		return profitYesterday


def main():
	print(f'Доход за вчерашний день: {get_hashrate()} ETH')

if __name__ == '__main__':
	main()