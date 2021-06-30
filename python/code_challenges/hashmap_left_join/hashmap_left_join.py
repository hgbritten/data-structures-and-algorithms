from code_challenges.hashtable.hashtable import Hashtable


def left_join(hashmap1, hashmap2):
    joined_tables = []
    for bucket in hashmap1._buckets:
        if bucket:
            current = bucket.head
            while current:
                current_key = current.value[0]
                current_value = current.value[1]
                pairs = [current_key, current_value]
                if hashmap2.contains(current_key):
                    pairs.append(hashmap2.get(current_key))
                else:
                    pairs.append(None)
                joined_tables.append(pairs)
                current = current.next

    return joined_tables
