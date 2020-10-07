from my_dictionary import morphy


def test_convert_lines():
    # setup
    text = """
WASHINGTON — President Trump revealed early Friday morning that he and the first lady, Melania Trump, had tested positive for the coronavirus, throwing the nation’s leadership into uncertainty and escalating the crisis posed by a pandemic that has already killed more than 207,000 Americans and devastated the economy.

Mr. Trump, who for months has played down the seriousness of the virus and hours earlier on Thursday night told an audience that “the end of the pandemic is in sight,” will quarantine in the White House for an unspecified period of time, forcing him to withdraw at least temporarily from the campaign trail only 32 days before the election on Nov. 3.
"""
    # execute
    actual = morphy._convert_lines(text=text)

    # verify
    expect = []
    expect.append('WASHINGTON — President Trump revealed early Friday morning that he and the first lady, Melania Trump, had tested positive for the coronavirus, throwing the nation’s leadership into uncertainty and escalating the crisis posed by a pandemic that has already killed more than 207,000 Americans and devastated the economy.')
    expect.append('Mr. Trump, who for months has played down the seriousness of the virus and hours earlier on Thursday night told an audience that “the end of the pandemic is in sight,” will quarantine in the White House for an unspecified period of time, forcing him to withdraw at least temporarily from the campaign trail only 32 days before the election on Nov. 3.')
    assert actual == expect
