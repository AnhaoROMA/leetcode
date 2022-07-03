"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names
from products after each character of searchWord is typed.
Suggested products should have common prefix with searchWord.
If there are more than three products with a common prefix,
return the three lexicographically minimums products.

Return a list of lists of the suggested products
after each character of searchWord is typed.

Input:
products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]

Input: products = ["havana"], searchWord = "havana"
Output: [["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

Input:
products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
Output:
[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]
"""


def suggest(products: list[str], word: str):
    result = list()
    products.sort()
    # print(products)
    length_products = len(products)
    length_word = len(word)

    i = 0
    k = 0
    while k < length_word:
        tmp = list()
        prefix = word[:k+1]
        # print(prefix)
        while i < length_products and products[i] < prefix:
            i += 1
        j = 0
        while j < 3 and i+j < length_products:
            if products[i+j].startswith(prefix):
                tmp.append(products[i+j])
            else:
                break
            j += 1
        result.append(tmp)
        k += 1
    return result


print(suggest(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"))
print(suggest(["havana"], "havana"))
print(suggest(["bags", "baggage", "banner", "box", "cloths"], "bags"))
