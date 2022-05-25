def merge_sort(arr):
    result = []
    for ith_result in merge_sort_gen(arr):
        result = ith_result

    return result


def merge_sort_gen(arr):
    def merge_sort_rec(start, end):
        if end - start > 1:
            middle = (start + end) // 2

            yield from merge_sort_rec(start, middle)  # don't provide slice, but index range
            yield from merge_sort_rec(middle, end)
            left = arr[start:middle]
            right = arr[middle:end]

            a = 0
            b = 0
            c = start

            while a < len(left) and b < len(right):
                if left[a] < right[b]:
                    arr[c] = left[a]
                    a += 1
                else:
                    arr[c] = right[b]
                    b += 1
                c += 1

            while a < len(left):
                arr[c] = left[a]
                a += 1
                c += 1

            while b < len(right):
                arr[c] = right[b]
                b += 1
                c += 1

            yield arr

    yield from merge_sort_rec(0, len(arr))
