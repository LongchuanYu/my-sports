# coding: utf-8
action_lib_presets = [
    # chest
    {
        'name': 'chest_press_machine',
        'label': '坐姿推胸',
        'category': 'chest',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'butterfly',
        'label': '蝴蝶夹胸',
        'category': 'chest',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'reverse_machine_flyes',
        'label': '反向器械飞鸟',
        'category': 'chest',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'smith_machine_squat',
        'label': '史密斯机深蹲',
        'category': 'chest',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'smith_machine_bench_press',
        'label': '史密斯机卧推',
        'category': 'chest',
        'values': [{'weight': 0, 'numbers': 0}],
    },

    # Back
    {
        'name': 'lat_pull_down',
        'label': '高位下拉',
        'category': 'back',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'seated_row_machine',
        'label': '坐姿划船',
        'category': 'chest',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'axle_deadlift',
        'label': '坐姿划船',
        'category': 'chest',
        'values': [{'weight': 0, 'numbers': 0}],
    },

    # leg 
    {
        'name': 'leg_press',
        'label': '腿部推蹬机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'leg_extension',
        'label': '腿部伸展机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'outer_thigh_abductor_machine',
        'label': '腿部外弯机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'inner_thigh_adductor_machine',
        'label': '腿部内弯机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },

    {
        'name': 'leg_press',
        'label': '腿部推蹬机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'leg_extension',
        'label': '腿部伸展机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'outer_thigh_abductor_machine',
        'label': '腿部外弯机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },
    {
        'name': 'inner_thigh_adductor_machine',
        'label': '腿部内弯机',
        'category': 'leg',
        'values': [{'weight': 0, 'numbers': 0}],
    },
]


def get_label_by_name(name):
    for action in action_lib_presets:
        if name == action.get('name'):
            return action.get('label')
    return 'Unknown'
