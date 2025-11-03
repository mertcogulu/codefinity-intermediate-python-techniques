def announcements(team_a, team_b, team_c, team_d):
    print(f"The teams that move to the next round are {team_a} and {team_b}.\n"
        f"The team that will play in the Europa League group stage is {team_c}.\n"
        f"{team_d} is out of the Champions League.")


group_c = ["Bayern", "Inter", "Barcelona", "Viktoria Plzen"]
announcements(*group_c)