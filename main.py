import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "your_account_sid"
# Your Auth Token from twilio.com/console
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos em Excel
lista_meses =['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
# Para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        # Se for maior do q 55000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        message = client.messages.create(
            to="+55***********",#your_number_cel
            from_="+***********",#your_number_twilio
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)