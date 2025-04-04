def get_num_words(book):
    return len(book.split())

def get_count_chars(book):
    counts = {}
    for char in book:
        char = char.lower()
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def get_sorted_count_chars(count_chars):
    sorted_list = []
    for line in count_chars:
        simple_dict = {}
        simple_dict["Character"] = line
        simple_dict["Count"] = count_chars[line]
        sorted_list.append(simple_dict)
    
    def sort_on(dict):
        return dict["Count"]
    
    sorted_list.sort(reverse = True, key = sort_on)

    return sorted_list

