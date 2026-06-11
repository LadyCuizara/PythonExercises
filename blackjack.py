import random

# ── Data ─────────────────────────────────────────────────

CARDS = [
    {"symbol": "A", "value": (1, 11), "count": 4},   # 0
    {"symbol": "2", "value": 2, "count": 4},          # 1
    {"symbol": "3", "value": 3, "count": 4},          # 2
    {"symbol": "4", "value": 4, "count": 4},          # 3
    {"symbol": "5", "value": 5, "count": 4},          # 4
    {"symbol": "6", "value": 6, "count": 4},          # 5
    {"symbol": "7", "value": 7, "count": 4},          # 6
    {"symbol": "8", "value": 8, "count": 4},          # 7
    {"symbol": "9", "value": 9, "count": 4},          # 8
    {"symbol": "10", "value": 10, "count": 4},        # 9
    {"symbol": "J", "value": 10, "count": 4},         # 10
    {"symbol": "Q", "value": 10, "count": 4},         # 11
    {"symbol": "K", "value": 10, "count": 4},         # 12
]

SUITS = ["♠", "♥", "♦", "♣"]

dealer = []
player = []

# ── Game Logic ───────────────────────────────────────────


def hit_card():
    card_index = random.randint(0, 12)
    CARDS[card_index]["count"] -= 1
    return card_index


def deal_card(hand):
    card_index = hit_card()
    suit = random.choice(SUITS)
    hand.append({
        "symbol": CARDS[card_index]["symbol"],
        "value": CARDS[card_index]["value"],
        "suit": suit,
    })


def start_game():
    for _ in range(2):
        for hand in (player, dealer):
            deal_card(hand)


def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        value = card["value"]
        if isinstance(value, tuple):
            aces += 1
            total += 11
        else:
            total += value
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total


def player_turn():
    while True:
        choice = input("\n[H] Hit  [S] Stand: ").strip().upper()
        if choice == "H":
            deal_card(player)
            show_cards(hide_dealer=True)
            if hand_total(player) > 21:
                return False
        elif choice == "S":
            return True


def dealer_turn():
    show_cards(hide_dealer=False)
    while hand_total(dealer) < 17:
        deal_card(dealer)
        show_cards(hide_dealer=False)


def determine_winner():
    player_total = hand_total(player)
    dealer_total = hand_total(dealer)

    if player_total > 21:
        show_result("BUST! Dealer wins!", player_total, dealer_total)
    elif dealer_total > 21:
        show_result("Dealer busts! You win!", player_total, dealer_total)
    elif player_total > dealer_total:
        show_result("You win!", player_total, dealer_total)
    elif dealer_total > player_total:
        show_result("Dealer wins!", player_total, dealer_total)
    else:
        show_result("It's a tie! Push.", player_total, dealer_total)

# ── Display ──────────────────────────────────────────────


def card_to_lines(card, hidden=False):
    if hidden:
        return [" ___ ", "|## |", "|###|", "|_##|"]
    symbol = card["symbol"]
    suit = card["suit"]
    top = f"|{symbol:<3}|"
    middle = f"| {suit} |"
    bottom = f"|_{symbol:_>2}|"
    return [" ___ ", top, middle, bottom]


def render_hand(hand, hide_first=False):
    all_lines = [
        card_to_lines(card, hidden=(hide_first and i == 0))
        for i, card in enumerate(hand)
    ]
    for row in range(4):
        print("  ".join(lines[row] for lines in all_lines))


def show_cards(hide_dealer=True):
    if hide_dealer:
        print("DEALER: ???")
    else:
        print(f"DEALER: {hand_total(dealer)}")
    render_hand(dealer, hide_first=hide_dealer)
    print()
    print(f"PLAYER: {hand_total(player)}")
    render_hand(player)


def show_result(message, player_total, dealer_total):
    print("\n╔═══════════════════════════════════╗")
    print(f"║  {message:<33}║")
    print(f"║  Player: {player_total:<3}  Dealer: {dealer_total:<13}║")
    print("╚═══════════════════════════════════╝")


def show_title():
    title = """
    ╔═══════════════════════════════════╗
    ║           B L A C K J A C K       ║
    ╚═══════════════════════════════════╝
    """
    print(title)


# ── Main ─────────────────────────────────────────────────

if __name__ == "__main__":
    show_title()
    start_game()
    show_cards()
    player_stands = player_turn()
    if player_stands:
        dealer_turn()
    determine_winner()
