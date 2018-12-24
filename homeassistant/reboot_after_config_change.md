# Reboot after config change.

_/rant\_start_

**NO DO NOT DO THIS!**

For some obscure reason there are someone out there that belive that you need to reboot the host after making a configuration change, this _is_ a **lie**!

For each change to the configuration a restart of Home Assistant (And **only** Home Assistant, **NOT** the host.) is needed.

But that is not entirely true.
You _can_ "Reload" some parts without needing to restart Home Assistant.
You can find these options here `https://my-ha-domain.duckdns.org/config/core`

There are 4 things you can reload.

- Core (Customizations)
- Groups
- Automations
- Scripts

Hitting these buttons **will** reload configurations for that part.
All other changes needs a restart of Home Assistant, **NOT** the host...

Components/platfoms that are configured with "Integrations" here `https://my-ha-domain.duckdns.org/config/integrations/dashboard` does **NOT** need a restart.

_/rant\_end_