def solve():
    # Read the number of cows (n) and cards per cow (m) from input
    n, m = map(int, input().split())
    # Initialize a list to store the cards of each cow
    cow_cards_input = []
    # Read the cards for each cow
    for _ in range(n):
        cow_cards_input.append(list(map(int, input().split())))

    # Initialize a list to store the minimum card and index of each cow
    min_cards = []
    # Iterate through each cow
    for i in range(n):
        # Find the minimum card in the cow's hand and store it with the cow's 1-based index
        min_cards.append((min(cow_cards_input[i]), i + 1))

    # Sort the min_cards list based on the minimum card value in ascending order
    # This prioritizes cows with smaller minimum cards to play earlier
    min_cards.sort(key=lambda x: x[0])
    # Create a permutation (p) which is the order of cows based on the sorted min_cards
    p = [cow_index for _, cow_index in min_cards]

    # Define a function to simulate the card game with a given permutation
    def simulate(permutation, initial_cow_cards):
        # Initialize the current top card on the pile to -1
        current_card = -1
        # Sort each cow's initial cards only once at the beginning of simulation
        cow_decks = [sorted(cards) for cards in initial_cow_cards] # Sorting is now outside the rounds loop

        # Simulate m rounds of the game
        for _ in range(m):
            # Iterate through the cows in the order defined by the permutation
            for cow_index_1_based in permutation:
                # Convert 1-based cow index to 0-based index for list access
                cow_index_0_based = cow_index_1_based - 1
                current_cow_deck = cow_decks[cow_index_0_based] # Access cow deck once

                best_card = None # Initialize best_card to None
                # Iterate through the current cow's deck to find the smallest playable card
                for card in current_cow_deck: # Optimized card search: iterate and break early
                    if card > current_card:
                        best_card = card # Found a playable card
                        break # Since deck is sorted, the first valid card is the smallest

                if best_card is not None: # If a playable card was found
                    current_card = best_card
                    current_cow_deck.remove(best_card) # Remove the played card from the cow's deck (in-place removal)
                elif current_cow_deck: # If there are no playable cards but the cow still has cards
                    return False # Game lost for this permutation
        return True # All rounds completed successfully


    # Simulate the game with the generated permutation p
    if simulate(p, cow_cards_input):
        # If simulation is successful, print the permutation p
        print(*(p))
    else:
        # If simulation fails, print -1 indicating no valid permutation found (with this greedy approach)
        print("-1")


# Read the number of test cases
t = int(input())
# Iterate through each test case
for _ in range(t):
    # Solve each test case
    solve()