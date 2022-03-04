from modul_0 import draw_numbers


def test_draw_numbers():
    # given

    # when
    draw_list = draw_numbers()
    # then
    assert len(draw_list) == 6
    assert sorted(draw_list)[0] > 0
    assert sorted(draw_list)[-1] < 50


