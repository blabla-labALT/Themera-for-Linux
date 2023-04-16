"""
d888888P dP
   88    88
   88    88d888b. .d8888b. 88d8b.d8b. .d8888b. 88d888b. .d8888b.
   88    88'  `88 88ooood8 88'`88'`88 88ooood8 88'  `88 88'  `88
   88    88    88 88.  ... 88  88  88 88.  ... 88       88.  .88
   dP    dP    dP `88888P' dP  dP  dP `88888P' dP       `88888P8

Themera Independent Constants File
PySimpleGUI Theme Code Generator
Copyright 2023 Divine Afam-Ifediogor
"""

# IMPORTS ______________________________________________________________________________________________________________
from darkdetect import isLight
from PySimpleGUI import running_mac, running_windows, LOOK_AND_FEEL_TABLE
from version_and_copyright import __version__

# CONSTANTS ____________________________________________________________________________________________________________
APP_ID = f'divineafamifediogor.themera.v{__version__.split(".", 1)[0]}'  # Major version only

DEFAULT_SETTINGS_PATH = f'./.themerasettings'
THEMES = ['Themera Light', 'Themera Dark'] + \
         sorted(
             [theme for theme in LOOK_AND_FEEL_TABLE.keys() if '1234567890' not in LOOK_AND_FEEL_TABLE[theme].values()]
         )
DEFAULT_THEME = (THEMES[0] if isLight() else THEMES[1]) if isLight() is not None else THEMES[0]
EXTERNAL_LINK_ICON = '⇗'  # '🔗'
GEAR_ICON = '⚙'
DOWN_ICON = '▼'
UP_ICON = '▲'
PENCIL_ICON = '✎'
WARNING_ICON = '⚠'
BORDER_UPPER_LIMIT = 100001
BATCH_ACTIONS = [
    '-- Choose an action --',
    'Select Color',
    'Shuffle',
    'Interpolate',
    'Random Color (All)',
    'Random Color (Individual)',
    'Brighten Colors',
    'Darken Colors',
]
LAST_USED_BATCH_ACTION = BATCH_ACTIONS[0]
DISPLAY_TO_THEMEDICT = {
    'Background': 'BACKGROUND',
    'Text': 'TEXT',
    'Input Background': 'INPUT',
    'Input Text': 'TEXT_INPUT',
    'Button Background': 'BUTTON[1]',
    'Button Text': 'BUTTON[0]',
    'Slider': 'SCROLL',
    'Progress Bar Trough': 'PROGRESS[1]',
    'Progress Bar Indicator': 'PROGRESS[0]',
    'Border': 'BORDER',
    'Slider Border': 'SLIDER_DEPTH',
    'Progress Bar Border': 'PROGRESS_DEPTH',
    'Accent 1': 'ACCENT1',
    'Accent 2': 'ACCENT2',
    'Accent 3': 'ACCENT3',
    'Accent 4': 'ACCENT4',
}
SAFE_TO_EXPAND = ['BUTTON', 'PROGRESS']
EXPANSION_FORMAT = '[<index>]'
INDEX_MARKERS = EXPANSION_FORMAT.split('<index>')
THEMEDICT_TO_DISPLAY = {value: key for key, value in DISPLAY_TO_THEMEDICT.items()}
CTRL = 'Cmd' if running_mac() else 'Ctrl'
CTRL_EVENT = 'Command' if running_mac() else 'Control'
ALT = 'Option' if running_mac() else 'Alt'
IMAGE_PREVIEW_SIZE = (320, 130)
CREATE_BUTTON_PADDING = ((3, 2), 3)
BACK_BUTTON_PADDING = ((2, 5), 3)
IMAGE_FILETYPES = [
    ('All Images', ('*.png', '*.jpg', '*.jpeg', '*.gif', '*.webp', '*.bmp', '*.ico', '*.icns')),
    ('PNG Images', ('*.png')),
    ('JPEG Images', ('*.jpg', '*.jpeg')),
    ('GIF Images', ('*.gif')),
    ('WEBP Images', ('*.webp')),
    ('Bitmaps', ('*.bmp')),
    ('Windows Icons', ('*.ico')) if running_windows() else ('Mac Icons', ('*.icns')),
]
DEFAULT_COLOR_THEME_FIELDS = [key for key in THEMEDICT_TO_DISPLAY.keys() if 'Border' not in THEMEDICT_TO_DISPLAY[key]]
DEFAULT_NON_COLOR_THEME_FIELDS = {
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0,
}

IMAGE_INDEX = [.3, 1, .7, .1, .2, 0, .6, .4, .5, .3, .7, .8, .6]
AUTOCONTRAST_INDEX_DARK = [.99, .8, .2, .1, .99, .7, .8, .3, .5, .6, .2, .4]
AUTOCONTRAST_INDEX_LIGHT = [.3, .7, .3, .8, .23, .3, .4, .7, .2, .9, .1, .6]
DARK_MODE_INDEX = [.1, .9, .8, .1, .3, .2, .7, .8, .3, .2, .4, .6, .8]
LIGHT_MODE_INDEX = [.9, .1, .3, .8, 1, .9, .4, .6, .2, .8, .6, .4, .2]

DEFAULT_ALIAS = 'sg'
DEFAULT_SETTINGS_DICT = {
    'psg_alias': DEFAULT_ALIAS,
    'theme': DEFAULT_THEME,
    'colorboxes': True,
    'image_index': IMAGE_INDEX,
    'autocontrast_index_dark': AUTOCONTRAST_INDEX_DARK,
    'autocontrast_index_light': AUTOCONTRAST_INDEX_LIGHT,
    'dark_mode_index': DARK_MODE_INDEX,
    'light_mode_index': LIGHT_MODE_INDEX,
}

CONTRAST_THRESHOLD = 0.5
CONTRAST_THRESHOLD_MULTIPLIER = 3

CRASH_REPORT_TITLE_PREFIX = '[Crash]'

LINK_DEVELOPER = 'https://github.com/definite-d'
LINK_GITHUB_REPO = f'{LINK_DEVELOPER}/themera'
LINK_GITHUB_ISSUES = f'{LINK_GITHUB_REPO}/issues'
LINK_NEW_GITHUB_ISSUE = f'{LINK_GITHUB_ISSUES}/new'
LINK_PYSIMPLEGUI_SITE = 'https://pysimplegui.org/'
LINK_PYSIMPLEGUI_REPO = 'https://github.com/pysimplegui/pysimplegui/'
LINK_DOCS_DL = f'{LINK_GITHUB_REPO}/blob/main/src/help/help.rtf'

HELP_PATH = 'help/help.rtf'