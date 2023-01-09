from art import logo

print(logo)

bids = {}
bidding_finish = False


def find_highest(bidding_record):
    highest_bid = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}.\n')


while not bidding_finish:
    name = input('What is your name? ')
    price = int(input('What is yout bid? $'))
    bids[name] = price
    should_continue = input(
        'Are there any other bidders? Typer "yes" or "no".\n')
    #clear()
    if should_continue == 'no':
        bidding_finish = True
        find_highest(bids)
