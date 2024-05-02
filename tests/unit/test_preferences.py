# SPDX-License-Identifier: AGPL-3.0-or-later
# pylint: disable=missing-module-docstring, invalid-name

from searx.locales import locales_initialize
from searx.preferences import (
    EnumStringSetting,
    MapSetting,
    SearchLanguageSetting,
    MultipleChoiceSetting,
    PluginsSetting,
    ValidationException,
)
from tests import SearxTestCase

locales_initialize()


class PluginStub:  # pylint: disable=missing-class-docstring, too-few-public-methods
    def __init__(self, plugin_id, default_on):
        self.id = plugin_id
        self.default_on = default_on


class TestSettings(SearxTestCase):  # pylint: disable=missing-class-docstring
    # map settings

    def test_map_setting_invalid_default_value(self):
        with self.assertRaises(ValidationException):
            MapSetting(3, map={'dog': 1, 'bat': 2})

    def test_map_setting_invalid_choice(self):
        setting = MapSetting(2, map={'dog': 1, 'bat': 2})
        with self.assertRaises(ValidationException):
            setting.parse('cat')

    def test_map_setting_valid_default(self):
        setting = MapSetting(3, map={'dog': 1, 'bat': 2, 'cat': 3})
        self.assertEqual(setting.get_value(), 3)

    def test_map_setting_valid_choice(self):
        setting = MapSetting(3, map={'dog': 1, 'bat': 2, 'cat': 3})
        self.assertEqual(setting.get_value(), 3)
        setting.parse('bat')
        self.assertEqual(setting.get_value(), 2)

    # enum settings

    def test_enum_setting_invalid_default_value(self):
        with self.assertRaises(ValidationException):
            EnumStringSetting(3, choices=[0, 1, 2])

    def test_enum_setting_invalid_choice(self):
        setting = EnumStringSetting(0, choices=[0, 1, 2])
        with self.assertRaises(ValidationException):
            setting.parse(3)

    def test_enum_setting_valid_default(self):
        setting = EnumStringSetting(3, choices=[1, 2, 3])
        self.assertEqual(setting.get_value(), 3)

    def test_enum_setting_valid_choice(self):
        setting = EnumStringSetting(3, choices=[1, 2, 3])
        self.assertEqual(setting.get_value(), 3)
        setting.parse(2)
        self.assertEqual(setting.get_value(), 2)

    # multiple choice settings

    def test_multiple_setting_invalid_default_value(self):
        with self.assertRaises(ValidationException):
            MultipleChoiceSetting(['3', '4'], choices=['0', '1', '2'])

    def test_multiple_setting_invalid_choice(self):
        setting = MultipleChoiceSetting(['1', '2'], choices=['0', '1', '2'])
        with self.assertRaises(ValidationException):
            setting.parse('4, 3')

    def test_multiple_setting_valid_default(self):
        setting = MultipleChoiceSetting(['3'], choices=['1', '2', '3'])
        self.assertEqual(setting.get_value(), ['3'])

    def test_multiple_setting_valid_choice(self):
        setting = MultipleChoiceSetting(['3'], choices=['1', '2', '3'])
        self.assertEqual(setting.get_value(), ['3'])
        setting.parse('2')
        self.assertEqual(setting.get_value(), ['2'])

    # search language settings
    def test_lang_setting_valid_choice(self):
        setting = SearchLanguageSetting('all', choices=['all', 'de', 'en'])
        setting.parse('de')
        self.assertEqual(setting.get_value(), 'de')

    def test_lang_setting_invalid_choice(self):
        setting = SearchLanguageSetting('all', choices=['all', 'de', 'en'])
        setting.parse('xx')
        self.assertEqual(setting.get_value(), 'all')

    def test_lang_setting_old_cookie_choice(self):
        setting = SearchLanguageSetting('all', choices=['all', 'es', 'es-ES'])
        setting.parse('es_XA')
        self.assertEqual(setting.get_value(), 'es')

    def test_lang_setting_old_cookie_format(self):
        setting = SearchLanguageSetting('all', choices=['all', 'es', 'es-ES'])
        setting.parse('es_ES')
        self.assertEqual(setting.get_value(), 'es-ES')

    # plugins settings
    def test_plugins_setting_all_default_enabled(self):
        plugin1 = PluginStub('plugin1', True)
        plugin2 = PluginStub('plugin2', True)
        setting = PluginsSetting(['3'], plugins=[plugin1, plugin2])
        self.assertEqual(set(setting.get_enabled()), set(['plugin1', 'plugin2']))

    def test_plugins_setting_few_default_enabled(self):
        plugin1 = PluginStub('plugin1', True)
        plugin2 = PluginStub('plugin2', False)
        plugin3 = PluginStub('plugin3', True)
        setting = PluginsSetting('name', plugins=[plugin1, plugin2, plugin3])
        self.assertEqual(set(setting.get_enabled()), set(['plugin1', 'plugin3']))


class TestPreferences(SearxTestCase):  # pylint: disable=missing-class-docstring
    def test_encode(self):
        from searx.preferences import Preferences  # pylint: disable=import-outside-toplevel

        pref = Preferences(['simple'], ['general'], {}, [])
        url_params = (
            'eJx1Vk1z4zYM_TXxRZNMd7eddg8-pe21nWnvGoiEJEQkofDDtvzrC1qSRdnbQxQTBA'
            'Hw8eGRCiJ27AnDsUOHHszBgOsSdHjU-Pr7HwfDCkweHCBFVmxHgxGPB7LiU4-eL9Px'
            'TzABDxZjz_r491___HsI0GJA8Ko__nSIPVo8BspLDx5DMjHU7GqH5zpCsyzXTLVMsj'
            'mhPzLI8I19d5iX1SFOUkUu4QD6BE6hrpcE8_LPhH6qydWRonjORnItOYqyXHk2Zs1E'
            'ARojAdB15GTrMA6VJe_Z13VLBsPL1_ccmk5YUajrBRqxNhSbpAaMdU1Rxkqp13iq6x'
            'Np5LxMI15RwtgUSOWx7iqNtyqI3S4Wej6TrmsWfHx2lcD5r-PSa7NWN8glxPxf5r5c'
            'ikGrPedw6wZaj1gFbuMZPFaaPKrIAtFceOvJDQSqCNBRJ7BAiGX6TtCEZt0ta2zQd8'
            'uwY-4MVqOBqYJxDFvucsbyiXLVd4i6kbUuMeqh8ZA_S1yyutlgIQfFYnLykziFH9vW'
            'kB8Uet5iDKQGCEWBhiSln6q80UDlBDch4psPSy1wNZMnVYR2o13m3ASwreQRnceRi2'
            'AjSNqOwsqWmbAZxSp_7kcBFnJBeHez4CKpKqieDQgsQREK5fNcBB_H3HrFIUUeJo4s'
            'Wx7Abekn6HnHpTM10348UMM8hEejdKbY8ncxfCaO-OgVOHn1ZJX2DRSf8px4eqj6y7'
            'dvv162anXS6LYjC3h1YEt_yx-IQ2lxcMo82gw-NVOHdj28EdHH1GDBFYuaQFIMQsrz'
            'GZtiyicrqlAYznyhgd2bHFeYHLvJYlHfy_svL7995bOjofp4ef_55fv36zRANbIJA2'
            'FX0C_v34oE3Es9oHtQIOFFZcilS5WdV_J5YUHRoeAvdCrZ0IDTCuy4sTOvHvMe96rl'
            'usfxs5rcrLuTv1lmOApYmqip6_bEz4eORSyR2xA8tmWxKnkvP3fM0Hgi4bpstFisWR'
            'TWV31adSdvSkPc7SkKbtOOTxgny05ALE6pNdL5vhQ5dFQKhYxjbpJZ0ChuSWcN22nh'
            'rGpPwC32HXSL7Qm8xf6Dzu6XfLfk19dFoZ4li1sRD9fJVVnWYOmiDCe97Uw0RGi4am'
            'o-JJA7IMMYUO7fIvM6N6ZG4ILlotrPhyjXSbSQqQZj7i2d-2pzGntRIHefJS8viwaK'
            '-iW6NN9uyTSuTP88CwtKrG-GPaSz6Qn92fwEtGxVk4QMrAhMdev7m6yMBLMOF86iZN'
            'JIe_xEadXAQuzW8HltyDCkJrmYVqVOI_oU7ijL64W03LLC81jcA8kFuQpDX1R90-b9'
            '_iZOD2J1t9xfE0BGSJ5PqHA7kUUudYuG7HFjz12C2Mz3zNhD8eQgFa_sdiy3InNWHg'
            'pV9OCCkWPUZRivRfA2g3DytC3fnlajSaJs4Zihvrwto7eeQxRVR3noCSDzhbZzYKjn'
            'd-DZy7PtaVp2WgvPBpzCXUL_J1OGex48RVmOXzBU8_N3kqekkefRDzxNK2_Klp9mBJ'
            'wsUnXyRqq1mScHuYalUY7_AZTCR4s=&q='
        )
        pref.parse_encoded_data(url_params)
        self.assertEqual(
            vars(pref.key_value_settings['categories']),
            {'value': ['general'], 'locked': False, 'choices': ['general', 'none']},
        )
