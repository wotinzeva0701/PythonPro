
s = "Ежевику для ежат принесли два ежа. Ежевику ели-ели ежата возле ели съели."
words = s.split()
count = 0
for word in words:
    if word[0].lower() == 'е':
        count += 1

print("Количество слов:", count)


