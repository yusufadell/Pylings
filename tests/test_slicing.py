from exercises.slicing import data, slice_subscriptable_dict


def test_slicing_subscriptable_dict():
    assert [
        ("name", "ACME"),
        ("shares", 100),
        ("price", 542.23),
    ] == slice_subscriptable_dict(data)
