def reverse(st):
    word = st.split()
    return ' '.join(reversed(word))

st = 'Hello World!'
result = reverse(st)
print(result)
