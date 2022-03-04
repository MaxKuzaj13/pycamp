from modul_0 import draw_numbers, iterate_until_equal


def test_draw_numbers():
    # given
    my_set = {1, 13, 17, 9, 49, 21}

    def my_firs_lucky_try():
        return [1, 13, 17, 9, 49, 21]
    # when
    draw_list = draw_numbers()

    # then
    assert iterate_until_equal(my_set, my_firs_lucky_try) == 1
    assert len(draw_list) == 6
    assert sorted(draw_list)[0] > 0
    assert sorted(draw_list)[-1] < 50


