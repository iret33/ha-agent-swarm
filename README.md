# Agent Swarm

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub Release](https://img.shields.io/github/release/iret33/ha-agent-swarm.svg)](https://github.com/iret33/ha-agent-swarm/releases)

Home Assistant integration for managing agent swarms via API.

## Installation

### HACS (Recommended)

1. Open HACS
2. Click "Integrations"
3. Click menu (3 dots) → "Custom repositories"
4. Add `https://github.com/iret33/ha-agent-swarm`
5. Install and restart Home Assistant

### Manual

1. Copy `custom_components/agent_swarm` to your Home Assistant `config/custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to Settings → Devices & Services
2. Click "Add Integration"
3. Search for "Agent Swarm"
4. Enter your API URL and API Key

## Entities

### Sensors

| Entity | Description |
|--------|-------------|
| `sensor.total_agents` | Number of registered agents |
| `sensor.active_tasks` | Total active tasks |
| `sensor.completed_tasks` | Completed tasks count |

### Binary Sensors

| Entity | Description |
|--------|-------------|
| `binary_sensor.api_online` | API connectivity status |

## Services

- `agent_swarm.refresh` - Force refresh data from API

## Support

For issues and feature requests, please use [GitHub Issues](https://github.com/iret33/ha-agent-swarm/issues).

## License

MIT
