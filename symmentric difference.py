def symmetric_diff():
    element_no1=int(input())
    set1 = set(map(int, input().split()))
    element_no2=int(input())
    set2 = set(map(int, input().split()))
    sym_diff = sorted(set(set1.difference(set2)).union(set2.difference(set1)));
    for x in sym_diff:
        print(x)
