# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_score_analytics.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: mmirdama <mmirdama@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/16 19:13:58 by mmirdama        #+#    #+#               #
#  Updated: 2026/02/16 19:13:59 by mmirdama        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys


def analyze_scores():
    print("=== Player Score Analytics ===")

    if len(sys.argv) < 2:
        print(
            f"No scores provided. "
            f"Usage: {sys.argv[0]} <score1> <score2> ...")
        return

    raw_scores = sys.argv[1:]
    clean_scores = []
    try:
        for score in raw_scores:
            clean_scores.append(int(score))
    except ValueError:
        print("Error: all scores must be valid integers!")
        return

    total = sum(clean_scores)
    count = len(clean_scores)
    print(f"Scores processed: {clean_scores}")
    print(f"Total players: {count}")
    print(f"Total score: {total}")
    print(f"Average score: {(total/count):.1f}")
    print(f"High score: {max(clean_scores)}")
    print(f"Low score: {min(clean_scores)}")
    print(f"Score range: {max(clean_scores) - min(clean_scores)}")
    print()


if __name__ == "__main__":
    analyze_scores()
