def top_scores():
    with open('results.csv') as file:
        read_file = csv.reader(file)
        scores = []
        for line in read_file:
            name, score = line
            scores.append((name,score))
    scores.sort(key=lambda tup: tup[1], reverse=True)
    place = ["First", "Second", "Third", "Fourth", "Fifth"]
    for i in range(0,min(len(scores), 5)):
        print(place[i] + ":\n" + scores[i][0] + " - " +  str(scores[i][1]))