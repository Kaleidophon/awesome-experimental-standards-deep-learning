"""
Produce figures used in papers.
"""

# STD
from datetime import datetime
import json
import os
import re

# EXT
import matplotlib.pyplot as plt
import numpy as np


def timeline():
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.grid(visible=True, axis="both", which="major", linestyle=":", color="grey")
    with open("multiTimeline.csv") as f:
        d = {"time": [], "count": []}
        for line in f:
            t, c = line.strip().split(",")
            year, month = t.split('-')
            d["time"].append(datetime(int(year), int(month), 1))
            d["count"].append(int(c))

        ax.plot(d["time"], d["count"], marker='o', markersize=2, color='darkred')
        ax.set_title('"Deep Learning" by Google Trends (2004-2021)', fontsize=16, alpha=0.6)
        ax.set_ylabel("Popularity (%)", fontsize=14, alpha=0.6)
        ax.set_xlabel("Year", fontsize=14, alpha=0.6)
        plt.setp(ax.get_xticklabels(), rotation=45, ha="center")
        plt.yticks(fontsize=12)
        plt.xticks(fontsize=12)
        plt.tight_layout()
        plt.savefig("trends.pdf", dpi=300)


def peer():
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.grid(visible=True, axis="both", which="major", linestyle=":", color="grey")
    d = {"pub": [10, 12, 14, 17, 20, 22, 25, 30, 34, 33.8, 34, 34.1, 34.9, 35, 40.1, 45, 55, 65, 90, 123]}
    x = np.arange(2000, 2020, 1)

    ax.bar(x, d["pub"], color='slateblue', width=0.6)
    ax.set_title('Development of Peer-Reviewed AI Publications (2000-2019)', fontsize=16, alpha=0.6)
    ax.set_ylabel("Peer-Reviewed AI Pubs. (*1000)", fontsize=12, alpha=0.6)
    ax.set_xlabel("Year", fontsize=14, alpha=0.6)
    plt.yticks(fontsize=12)
    plt.xticks(x, fontsize=12)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="center")
    plt.tight_layout()
    # plt.show()
    plt.savefig("publications.pdf", dpi=300)


def plot_nlp_venues():
    nlp_venues = ["EMNLP", "EMNLP Findings", "TACL", "CL", "CoNLL", "NAACL", "EACL", "ACL", "COLING"]

    # This is extra data I just researched manually through https://aclanthology.org/events/
    extra_data = {
        "ACL": {
            21: 732,
            22: 779
        },
        "EMNLP": {
            21: 848,
            22: 840
        },
        "EMNLP Findings": {
            20: 447,
            21: 419,
            22: 450
        },
        "CL": {
            21: 29
        },
        "TACL": {
            21: 93
        },
        "CoNLL": {
            21: 53
        },
        "EACL": {
            21: 327
        },
        "NAACL": {
            21: 478,
            22: 657
        },
        "COLING": {
            22: 634
        }
    }
    colors_and_markers = {
        "ACL": ("firebrick", "o"),
        "EMNLP": ("forestgreen", "^"),
        "EMNLP Findings": ("limegreen", "^"),
        "CL": ("darkorange", "8"),
        "TACL": ("darkorchid", "s"),
        "CoNLL": ("darkturquoise", "*"),
        "EACL": ("royalblue", "P"),
        "NAACL": ("gold", "p"),
        "COLING": ("darkgrey", "x")
    }

    data_dir = "ml_nlp_paper_data/papers"
    proceeding_files = os.listdir(data_dir)
    proceeding_files = list(
        filter(lambda file_name: any(re.match(fr"^{venue}\d\d", file_name) for venue in nlp_venues), proceeding_files)
    )
    first_year = 12
    last_year = 22

    num_publications = {
        venue: [None] * (last_year - first_year + 1) for venue in nlp_venues
    }

    # Gather data
    for file in proceeding_files:
        venue, year = (
            re.compile(r"(.+?)(\d{2})").match(file).groups()
        )

        with open(f"{data_dir}/{file}", "r") as f:
            num_venue_publications = len(json.load(f))
            num_publications[venue][int(year) - first_year] = num_venue_publications

    for venue in nlp_venues:
        for year, num_venue_publications in extra_data[venue].items():
            num_publications[venue][year - first_year] = num_venue_publications

    # Plot
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.grid(axis="both", which="major", linestyle=":", color="grey")
    x = np.arange(first_year + 2000, last_year + 2001, 1)

    for venue, publication_data in num_publications.items():
        # Use the line below to filter years for which there is no data available
        x_venue, y = tuple(zip(*[(xx, d) for xx, d in zip(x, publication_data) if d is not None]))
        color, marker = colors_and_markers[venue]
        ax.plot(
            x_venue, y, label=venue, marker=marker, color=color, markersize=6
        )

    ax.set_title(f'Development of NLP Publications (20{first_year}-20{last_year})', fontsize=16, alpha=0.6)
    ax.set_ylabel("Publications", fontsize=12, alpha=0.6)
    ax.set_xlabel("Year", fontsize=12, alpha=0.6)
    plt.legend(loc="upper left", ncol=2, fontsize=12)
    plt.yticks(fontsize=12)
    plt.xticks(x, fontsize=12)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="center")
    plt.tight_layout()
    #plt.show()
    plt.savefig("nlp_venues.pdf", dpi=300)


if __name__ == "__main__":
    #timeline()
    #peer()
    plot_nlp_venues()
