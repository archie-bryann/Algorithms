# A greedy algorithm is simple: at each step, pick the optimal move 
# Approximation algorithm is a greedy algorithm

# Suppose you’re starting a radio show. You want to
# reach listeners in all 50 states. You have to decide what
# stations to play on to reach all those listeners. It costs
# money to be on each station, so you’re trying to minimize the
# number of stations you play on. You have a list of stations.

# Each station covers a region, and
# there’s overlap.
# How do you figure out the smallest set of
# stations you can play on to cover all 50
# states?

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {
    "kone": set(["id", "nv", "ut"]),
    "ktwo": set(["wa", "id", "mt"]),
    "kthree": set(["or", "nv", "ca"]),
    "kfour": set(["nv", "ut"]),
    "kfive": set(["ca", "az"])
}

final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()

    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # finds the intersection betw. states_for_station & states needed
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            states_needed -= states_covered
            final_stations.add(best_station)

print(final_stations)

