football_stats = {
    'Chislo stran': 48,
    'Uchastniki': ['Australia', 'Sweden', 'Argentina, Switzerland','Japan', 'Germany', '42 more countries'],
    'Rewards': {
        'Golden ball': 'Leonel Messi',
        'Silver ball': 'Mbappe',
        'Golden boot': 'Mbappe',
        'Silver boot': 'Mbappe',
        'Most goals ': {
            'Player': 'Mbappe - team captain',
            'Count goals': 8
        }
    }
}
def test_read_value():
    count = football_stats['Chislo stran']
    assert count == 48

def test_write_stats():
    football_stats['Chislo stran'] = 50
    count = football_stats['Chislo stran']
    assert count == 50
def test_new_value_stats():
    len_before = len(football_stats)
    football_stats['Pobeditel'] = 'Argentine'
    winner = football_stats['Pobeditel']
    len_after = len(football_stats)
    assert winner == 'Argentine'
    assert len_before + 1 == len_after
def test_read_list():
    participants = football_stats['Uchastniki']
    aus = participants[1]
    assert aus == 'Sweden'
    assert len(participants) > 0

def test_read_dict():
    awards = football_stats['Rewards']['Most goals ']['Count goals']
    assert awards == 8

def test_save_dict():
    awards = football_stats['Rewards']
    player = awards['Most goals ']['Player']
    assert player == 'Mbappe - team captain'