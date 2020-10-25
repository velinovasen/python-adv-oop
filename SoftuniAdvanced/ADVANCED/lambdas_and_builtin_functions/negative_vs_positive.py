nums = list(map(lambda x: int(x), input().split()))
negative_nums = list(filter(lambda x: x < 0, nums))
positive_nums = list(filter(lambda x: x > 0, nums))
print(sum(negative_nums))
print(sum(positive_nums))
if abs(sum(negative_nums)) > abs(sum(positive_nums)):
    print(f'The negatives are stronger than the positives')

else:
    print(f'The positives are stronger than the negatives')