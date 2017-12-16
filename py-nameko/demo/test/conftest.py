# -*- coding: utf-8 -*-
# vim: et ts=4 sw=4
import re

import pytest
import yaml
from bravado.client import SwaggerClient
from mock import Mock
from nameko.cli.main import setup_yaml_parser
from nameko.constants import WEB_SERVER_CONFIG_KEY
from nameko.extensions import DependencyProvider
from nameko.testing.services import replace_dependencies
from nameko.testing.utils import get_extension
from nameko_consul import DiscoverableWebServer

from service import Service


setup_yaml_parser()


def get_dependency(container, *deps):
    exts = []
    for dep in deps:
        ext = get_extension(container, DependencyProvider, attr_name=dep)
        exts.append(ext.get_dependency({}))
    return exts[0] if len(deps) == 1 else exts


@pytest.fixture
def config():
    return yaml.load(file('conf/config.yaml'))


@pytest.fixture
def web_config(web_config, config):
    web_config.pop('AMQP_URI', None)
    for key, val in config.items():
        web_config.setdefault(key, val)
    return web_config


@pytest.fixture
def container(container_factory, web_config):
    # Mock consul
    # See https://groups.google.com/forum/#!topic/nameko-dev/SvclTULUcSU
    DiscoverableWebServer.consul = Mock()

    container = container_factory(Service, web_config)

    # Mock dependencies
    replace_dependencies(container, 'cache')

    container.start()
    return container


@pytest.fixture
def client_swagger(container, web_config):
    port = web_config[WEB_SERVER_CONFIG_KEY]
    netloc = '127.0.0.1:{0}'.format(port)
    spec = 'http://{0}/v1/{1}/api.json'.format(netloc, container.service_name)
    client = SwaggerClient.from_url(spec, config={"use_models": False})
    api_url = client.swagger_spec.api_url
    client.swagger_spec.api_url = re.sub('(?<=//)[^/]+', netloc, api_url)
    return client


@pytest.fixture
def cache(container):
    return get_dependency(container, 'cache')
