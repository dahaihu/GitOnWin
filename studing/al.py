# a = [(1, 2), (2, 5), (6, 9), (9.5, 20)]
# b = [(1.5, 2.5), (3, 10)]
a = [(1, 3), (5, 6)]
b = [(0, 1), (2, 5), (7, 8)]
def func(a, b):
    a.extend(b)
    a.sort(key=lambda x:x[0])
    print(a)
    inter = 0
    union = 0
    # 长度为1 就不需要计算了
    if len(a) <= 1:
        return
    # print("len(a) is {}".format(len(a)))
    i, j = 0, 1
    while i <= len(a)-1 and j <= len(a) - 1:
        # print("i is {}, j is {}".format(i, j))
        if a[i][1] < a[j][0]:
            union += a[i][1] - a[i][0]
            i, j = j, j+1
            # print("*")
            # print("{} => {}".format(i, j))
            continue
        elif a[i][1] >= a[j][0]:
            if a[i][1] < a[j][1]:
                union += a[i][1] - a[i][0]
                inter += a[i][1] - a[j][0]
                a[j] = (a[i][1], a[j][1])
                i, j = j, j+1
                # print("**")
                # print("union is {}".format(union))
                # print('inter is {}'.format(inter))
                # print("{} => {}".format(i, j))
                # print("a[i] is {}".format(a[i]))
            else:
                inter += a[j][1] - a[j][0]
                union += a[j][1] - a[i][0]
                a[i] = (a[j][1], a[i][1])
                i, j = i, j+1
    #             print("***")
    #             print("union is {}".format(union))
    #             print('inter is {}'.format(inter))
    #             print("{} => {}".format(i, j))
    #             print("a[i] is {}".format(a[i]))
    # print("i is {}".format(i))
    # print("j is {}".format(j))
    if i <= len(a)-1:
        union += a[i][1] - a[i][0]
    if j <= len(a) - 1:
        union += a[j][1] - a[j][0]
    print(f'intersection:{inter}, union:{union}')
    # # union += a[-1][1] - a[-1][0]
    # print("a[-1] is {}".format(a[-1]))
    # print('union {}'.format(union))
    # print('inter {}'.format(inter))

def _audio_time_iou(pre_time, post_time):
    """
    音频转文本的时间相似度，iou代表intersection over union
    :param pre_time: [(start time, end time) ...]
    :param post_time: [(start time, end time) ...]
    :return:
    """

    def _time_next(time_sequence, cur=None):
        """
        获取下一个pointer
        :param time_sequence: 传入要找到指针的time sequence
        :param cur: 当前指针位置，例如(0,0)，第一个数字代表list的index，第二个数字代表tuple的index
        :return: pointer_time, list_index, tuple_index
        """
        if cur is None:
            return time_sequence[0][0], (0, 0)
        list_pos = cur[0]
        tuple_pos = cur[1]
        if tuple_pos == 0:
            return time_sequence[list_pos][1], (list_pos, 1)
        elif list_pos != len(time_sequence) - 1:
            return time_sequence[list_pos + 1][0], (list_pos + 1, 0)
        else:
            return None, None

    time_counter, counter = [], 0
    pre_cur, pre_seq = _time_next(pre_time)
    post_cur, post_seq = _time_next(post_time)

    def _time_counter(cur, seq, cur_time):
        nonlocal counter, time_counter
        counter = counter + 1 if not seq[1] else counter - 1
        time_counter.append((cur, counter))
        return _time_next(cur_time, seq)

    while pre_cur is not None or post_cur is not None:
        if pre_cur is not None and post_cur is not None:
            if pre_cur <= post_cur:
                pre_cur, pre_seq = _time_counter(pre_cur, pre_seq, pre_time)
            else:
                post_cur, post_seq = _time_counter(post_cur, post_seq, post_time)
        elif pre_cur:
            pre_cur, pre_seq = _time_counter(pre_cur, pre_seq, pre_time)
        else:
            post_cur, post_seq = _time_counter(post_cur, post_seq, post_time)

    print(f'time_counter:{time_counter}')

    union, intersection = 0, 0
    for index, e in enumerate(time_counter):
        if e[1] == 1:  # 两个集合只有一个
            union += time_counter[index + 1][0] - e[0]
        elif e[1] == 2:  # 两个集合都有
            intersection += time_counter[index + 1][0] - e[0]

    print(f'intersection:{intersection}, union:{union+intersection}')

    return intersection / (union + intersection)


func(a, b)
#
_audio_time_iou(a, b)