---
id: spirit-ent-console-wifi-bandwidth-for-a-facility
title: The WiFi bandwidth a room of machines needs, and the access users must be given
kind: policy
question: How much WiFi bandwidth does a room of Spirit CT800ENT-2022 or CT850ENT-2022
  treadmills need?
asked_as:
- how much internet speed do the treadmills need
- how many machines can i put on one wifi
- do i have to give members the wifi password
- the streaming apps buffer on the treadmills
keywords:
- wifi bandwidth
- mbps
- network planning
- facility
- open network
- wifi password
- streaming
- multiple machines
facets:
  brand:
  - spirit
  product_line: treadmill
  model: '*'
  applies_to:
  - ct800ent-2022
  - ct850ent-2022
  section: console
  code: '*'
authority: 2
not_to_be_confused_with: []
see_also:
- spirit-ent-console-wifi-setup
- spirit-ent-console-screen-mirroring-limits
source:
  ref: spirit-ent-console-internet-connection-tip
  locator: '"Connecting to the Internet", one page support note, revision 07.01.2024,
    p. 1, the three bullets beside the Maintenance screenshot'
  extracted_at: '2026-09-09'
---

- **WiFi bandwidth of 1.5 Mbps or greater for every 4 units is recommended**, to ensure proper
  bandwidth to support the use of streaming apps across multiple machines.
- **For screen mirroring, the machine and the user's phone must be connected to the same WiFi
  signal.**
- **To allow screen mirroring, the WiFi signal must be accessible to users** - either by
  facilitating an **open network** or by **providing the WiFi password** to potential users.

The second and third bullets together are the practical consequence: a facility that keeps its WiFi
password private has disabled screen mirroring for its members, whatever the console is set to.

The note gives no figure for a single machine on its own, no guidance on access point count or
placement, and no minimum for the console's own app use as distinct from mirroring.

**Ethernet does not solve the bandwidth question**, because a wired machine cannot be mirrored to at
all: `spirit-ent-console-screen-mirroring-limits`.
