# -*- coding: utf-8 -*-
# vim: et ts=4 sw=4


def test_get_health(client_swagger):
    ret = client_swagger.demo.get_health().result()
    assert ret['code'] == 'OK'
