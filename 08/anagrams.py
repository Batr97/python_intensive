def anagramms(text: str, pattern: str):
    if len(pattern) > len(text):
        return []
    patt_s = {}
    text_s = {}
    for i, patt in enumerate(pattern):
        patt_s[patt] = 1 + patt_s.get(patt, 0)
        text_s[text[i]] = 1 + text_s.get(text[i], 0)
    res = [0] if patt_s == text_s else []
    left = 0
    for right in range(len(pattern), len(text)):
        text_s[text[right]] = 1 + text_s.get(text[right], 0)
        text_s[text[left]] -= 1
        if text_s[text[left]] == 0:
            text_s.pop(text[left])
        left += 1
        if text_s == patt_s:
            res.append(left)
    return res
