# Confusing HA terms

_Home Automation, Home Assistant, Hassio, HassOS, HA, Hass, WTF?_

# Home Automation

There are a lot of systems that offer Home Automation capabilities, Home Assistant is just on of them.

Other popular systems in this space are:

- [Domoticz](https://www.domoticz.com/)
- [Alexa](https://en.wikipedia.org/wiki/Amazon_Alexa)
- [Google Assistant](https://assistant.google.com/)
- [openHAB](https://www.openhab.org/)
- [Homey](https://homey.app/)
- [SmartThings](https://www.smartthings.com/)

_And many many many more, as a base part of their core they allow you control/moitor your smart home or make your dumb home smarter._

# Home Assistant

_Let's start with an easy one._

Home Assistant is the automation platform (software) that we all run.
This is where you have your integrations, do automations and create awesome Lovelace views.

Some popular abbrevations of Home Assistant:

- **H**ome **A**ssistant (HA)
- **H**ome **Ass**istant (Hass)

To add to the confusion, HA is also used as an abbrevation for "Home Automation" so... sorry?

[More information about Home Assistant](https://www.home-assistant.io/)

## Hassio / Hass.io

_Now things can get a little tricky._

Hassio is not Home Assistant, and Home Assistant is not Hassio.

Hassio is a way of installing Home Assistant (similar to `pip install homeassistant` and docker).

When you use one of the Hassio installers (HassOS/Generic linux) you get a set of docker containers in addition to the main part (Home Assistant)

**Base set of containers for Hassio:**

- Home Assistant
- Hassio Supervisor
- DNS

**Some key aspects:**

- _Every_ Hassio installation uses Docker.
- Hassio can be installed on _any_ linux OS.
- Hassio does not have automations
- Hassio does not have integrations
- The add-on store is _only_ available _if_ you installed Home Assistant with Hassio.

[More information about Hassio](https://www.home-assistant.io/hassio/)

## HassOS

HassOS is a OS based on buildroot, that ships with Hassio (and therefore also Home Assistant).

[More information about HassOS](https://github.com/home-assistant/hassos)

There are images available for many boards, as well as hypervisors.

## Hassbian

_Bonus round._

Hassbian was the first OS that came with Home Assistant pre installed in a python venv., it is (was) a customized version of Raspbian lite.


## Compararable to

Part | comparable to
-- | --
Home Assistant | Word, Excel, Chrome (Software)
Hassio | Office, Adobe (Suites of software)
HassOS / Hassbian | Windows, MacOS, Ubuntu (OS (Operating Systems))

# One last thing

_You can add some stuff to your system._

## Add-ons

_Wait... What now?_

Add-ons are (for the most part) pre exsisting software wrapped in a spesial way so Hassio know how to run them.
These are all standalone containers (docker lingo), and as noted earlier Add-ons are **only** available on Hassio installations.

_Although_ the add-ons are only available for Hassio installation, these (again, for the most part) are "just" wrappers for software you can install manually if Hassio is not your cup of tea.

_NB!: This is not integrations_

[More information about Add-ons and some examples of ones](https://addons.community/)

## Integrations

_Flavor with sparkels and rainbows._

Integrations allow you to add additional functions/data to your Home Assistant installation.
**Every** Installation of Home Assistant have integrations, this is the things you add to your `configuration.yaml` and/or in the UI of Home Assistant under "Integrations"

Earlier this was called "Components", cummunity managed integrations are still refered to as custom_component(s).

_NB!: This is not add-ons_

[A list of Integrations in Home Assistant](https://www.home-assistant.io/integrations/)


## Compararable to

Part | comparable to
-- | --
Add-ons | Word, Excel, Chrome (Software)
Integrations | I don't know, the save/print function in Word maybe?
