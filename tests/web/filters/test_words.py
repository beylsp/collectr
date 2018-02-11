from collectr.web.filters import words


def test_pluralize_singular_default_arg():
    assert words.pluralize(1) == ''


def test_pluralize_plural_default_arg():
    assert words.pluralize(2) == 's'


def test_pluralize_singular_arg():
    assert words.pluralize(1, singular='ium') == 'ium'


def test_pluralize_singular_arg__plural():
    assert words.pluralize(5, singular='ium') == 's'


def test_pluralize_plural_arg():
    assert words.pluralize(5, plural='ia') == 'ia'


def test_pluralize_plural_arg__single():
    assert words.pluralize(1, plural='ia') == ''


def test_pluralize_singular_and_plural_arg__single():
    assert words.pluralize(1, singular='ium', plural='ia') == 'ium'


def test_pluralize_singular_and_plural_arg__plural():
    assert words.pluralize(5, singular='ium', plural='ia') == 'ia'
