# Pondérations selon les contextes
context_weights = {
    "combat": {
        "attaquer": 3,
        "soigner": 1,
        "fuir": 0.5,
        "négocier": 0.2,
        "observer": 0.3,
    },
    "guérison": {
        "attaquer": 0.5,
        "soigner": 3,
        "fuir": 1,
        "négocier": 0.5,
        "observer": 0.3,
    },
    "fuite": {
        "attaquer": 0.2,
        "soigner": 1,
        "fuir": 3,
        "négocier": 0.7,
        "observer": 0.3,
    },
    "négociation": {
        "attaquer": 0.1,
        "soigner": 0.3,
        "fuir": 1,
        "négocier": 3,
        "observer": 0.5,
    }
}
