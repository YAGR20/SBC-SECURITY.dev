from web3 import Web3

# Endpoint de Linea Mainnet
linea_url = "https://linea-mainnet.infura.io/v3/cdf3e4928b1844ada4e143c18eca6240"
w3 = Web3(Web3.HTTPProvider(linea_url))

if w3.is_connected():
    print("Conexión exitosa a Linea Mainnet.")
    latest_block = w3.eth.get_block('latest')
    print("Último bloque:", latest_block)
else:
    print("Error al conectar a Linea Mainnet.")
