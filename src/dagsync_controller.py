import kopf

@kopf.on.create('operators.rolanddb.github.io', 'v1', 'airflowdags')
def on_create(namespace, spec, body, **kwargs):
    print(f"An AirflowDag object has been created: {body}")
    
    # # extracting the requested currency out of the ExchangeRate object
    # currency = spec['currency']
    #
    # # querying the current exchange rate for this currency
    # exchange_rates_url = 'https://api.exchangeratesapi.io/latest?symbols='
    # rate = requests.get(f"{exchange_rates_url}{currency}").json()['rates'][currency]
    #
    # # creating a new ConfigMap containing the exchange rate
    # k8s_client.CoreV1Api().create_namespaced_config_map(namespace,
    #  {
    #    'data': {
    #        'rate': str(rate)
    #    }
    #  }
    # )