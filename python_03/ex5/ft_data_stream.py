import time

# Event Generator (Deterministic)
def game_event_stream(num_events):
    players = ['alice', 'bob', 'charlie', 'dave', 'eve']
    actions = ['killed monster', 'found treasure', 'leveled up']
    levels = [5, 12, 8, 15, 3]  # deterministic player levels

    for i in range(num_events):
        player = players[i % len(players)]
        level = levels[i % len(levels)]
        action = actions[i % len(actions)]
        yield (f"Event {i+1}: Player {player} "
               f"(level {level}) {action}"), player, level, action


# Event Processing and Stats
def process_events(num_events):
    print("=== Game Data Stream Processor ===")
    print(f"Processing {num_events} game events...")
    total_events = 0
    high_level = 0
    treasure_count = 0
    level_up_count = 0
    start_time = time.time()  # start timing
    for event_str, player, level, action in game_event_stream(num_events):
        print(event_str)
        total_events += 1
        if level >= 10:
            high_level += 1
        if action == 'found treasure':
            treasure_count += 1
        if action == 'leveled up':
            level_up_count += 1

    end_time = time.time()  # end timing
    elapsed = end_time - start_time

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"Players level 10 or above: {high_level}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}")
    print("Memory usage: constant (streaming)")
    print(f"Processing time: {elapsed:.3f} seconds")


# Fibonacci Generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


# Prime Number Generator
def primes(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1


process_events(1000)
print("\n=== Generator Demonstration ===")
print("Fibonacci sequence (first 10):")
for value in fibonacci(10):
    print(value, end=' ')
print()

print("Prime numbers (first 5):")
for value in primes(5):
    print(value, end=' ')
