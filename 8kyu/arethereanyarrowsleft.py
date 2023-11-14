def anyArrows(arrows):
    for arrow in arrows:
        if 'damaged' not in arrow or not arrow['damaged']:
            return True
    return False

quiver = [{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}]
result = anyArrows(quiver)
print(result)
