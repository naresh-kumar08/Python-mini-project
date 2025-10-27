
while True:
    def get_amount():
        while True:
            try:
                amount = float(input("Enter your amount: "))
                if amount <=0:
                    raise ValueError
                else:
                    return amount
            except ValueError:
                print("Invailed syntex")

    def get_currency(label):
        currencies = ('USD','RUPE','AUD')
        while True:
            currency = input(f'{label} currency(USD,AUD,RUPE): ').upper()
            if currency not in currencies:
                print("Invalid value")
            else:
                return currency

    def convert(amount,target_money,source_money):
        exchange = {
            'USD': {'RUPE':87.71,'AUD':1.54},
            'AUD': {'USD': 0.65,'RUPE':57.12},
            'RUPE':{'USD':0.011,'AUD':0.018} 
        }   
        if source_money == target_money:    
            return amount
        return amount * exchange[target_money][source_money]    

    def main():
        amount = get_amount()
        source_money = get_currency('surce')
        target_money = get_currency('target')
        converted = convert(amount,source_money,target_money)
        print(f'{amount} {source_money} is equal to {converted:.2f}')

    if __name__ == "__main__":
        main()

    cout = input("You are continue for transection(yas/no)").lower()
    if cout!='yas':
        break