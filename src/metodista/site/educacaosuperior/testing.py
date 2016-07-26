# -*- coding: utf-8 -*-

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing.z2 import installProduct


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import Products.PloneFormGen
        self.loadZCML(package=Products.PloneFormGen)
        installProduct(app, 'Products.PloneFormGen')
        # Load ZCML
        import metodista.site.educacaosuperior
        self.loadZCML(package=metodista.site.educacaosuperior)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'metodista.site.educacaosuperior:default')


FIXTURE = Fixture()


INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name='metodista.site.educacaosuperior:Integration',
)

FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name='metodista.site.educacaosuperior:Functional',
)
