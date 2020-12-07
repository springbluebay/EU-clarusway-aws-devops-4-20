lst = ["A", "A", "A", "B", "C", "C", "A", "D", "D", "D", "D", "D"]


def majority_vote(xx):
    for i in lst:
        if lst.count(i) > len(lst)/2:
            return i

print(majority_vote(lst))