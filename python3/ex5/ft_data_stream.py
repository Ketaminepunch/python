# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vsack <vsack@student.42vienna.com>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/04 18:59:58 by vsack             #+#    #+#              #
#    Updated: 2026/05/11 18:21:03 by vsack            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random
import typing


def gen_event() -> typing.Generator:
    players = ["Tom", "Jerry", "Sam", "Clade", "Aurora"]
    actions = [
        "connected",
        "disconnected",
        "leveled up",
        "found a legendary item",
        "died",
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(even_list: list) -> typing.Generator:
    while len(even_list) > 0:
        idx = random.randrange(len(even_list))
        item = even_list[idx]
        del even_list[idx]
        yield item


if __name__ == "__main__":
    eventGen = gen_event()
    print("Streaming 1000 events")
    i = 1
    j = 0
    for _ in range(1000):
        print(f"Event {i}: {next(eventGen)}")
        i += 1
    eventIter = gen_event()
    tupleEvents = [next(eventIter) for _ in range(10)]
    print(f"Built Lost of 10 events: {tupleEvents}")
    for event in consume_event(tupleEvents):
        print(f"Consumed {event}")
        print(f"Remaining in list: {tupleEvents}")
