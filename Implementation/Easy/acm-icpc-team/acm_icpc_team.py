if __name__ == "__main__":
    num_people, num_topics = list(map(int, input().split()))
    people = []
    
    for ii in range(num_people):
        people.append(int(input(), base=2))
    
    max_topics = 0
    num_teams = 0
    
    for ii in range(len(people)):
        for jj in range(ii+1, len(people)):
            team = people[ii] | people[jj]
            topics = bin(team)[2:].count("1")
            if topics > max_topics:
                max_topics = topics
                num_teams = 1
            elif topics == max_topics:
                num_teams += 1
    
    print(max_topics)
    print(num_teams)