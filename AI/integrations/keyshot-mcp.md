# Optional KeyShot MCP integration (model-agnostic)

**Status:** Integration guidance only. This repository does not install or operate an MCP server. The documentation-first KeyShot Python Scripting Assistant works with **no MCP connection**.

## Project and compatibility

- Independent upstream project: [lfoletti/keyshot-mcp](https://github.com/lfoletti/keyshot-mcp), MIT licensed, a working **prototype** maintained by its author.
- The upstream `1.1.1` release (2026-10-24) describes **33 MCP tools** for scene state, cameras, environments, materials and graphs, rendering, screenshots, plus bridge inspection.
- The author reports Windows and KeyShot Studio **2026.2 Pro** testing. KeyShot **2026.3 beta is not validated by that report**. Do not claim compatibility until tested in that build.
- Architecture: an **external Python 3.12+ stdio MCP server** speaks to a **separately installed bridge inside KeyShot** via a token-protected, localhost-only (`127.0.0.1:1998` by default) TCP connection. The server and bridge need to run on the same Windows host. This is **not** a cloud-accessible MCP service by default.
- The upstream project currently documents a Claude Code setup; MCP is a protocol, not a guarantee that another agent host can connect to this local stdio server. Follow the upstream README for installation; adapt client configuration only for hosts that explicitly support local MCP.

## Agent integration contract

1. Discover **actual** host-exposed MCP tools and their schemas. Do not assume a tool exists because it is named in this document. A repository or skill link is not an MCP connection.
2. Start with read-only `keyshot_status`. Verify the bridge responds and report the detected KeyShot and bridge versions. If unavailable, use the ordinary documentation-only workflow.
3. For inspection, prefer only the read tools needed: `get_scene_info`, `get_scene_tree`, `list_objects`, `list_materials`, `get_material`, `list_cameras`, `list_environments`, `lux_functions`. Read the actual tool schema and result. Do not infer a supported field or setting from a tool name.
4. Treat `lux_functions` as **live introspection evidence**, not an automatic override of the saved `lux/KeyShot_lux_API.md` or `lux/KeyShot_luxmath_API.md`. A discrepancy calls for a report and a deliberate versioned reference update.
5. Before a mutating tool, confirm the user's exact scene target and scope. Handle unsaved work, backups, references, side effects, permissions and limitations. Never assume material-change undo covers all state changes.
6. Never enable `execute_python` automatically. Upstream disables it by default. Enable only with explicit permission after considering the broader arbitrary-code risk and verifying code against the same source constraints.
7. Do not expose the localhost bridge or its token on a public endpoint, include the token in prompts/logs, or copy secrets into source control.
8. Distinguish declaration/static/mock tests from verified **GUI runtime**, **headless runtime**, **rendering**, and **visual** tests. An upstream test suite is not evidence of a test run on the user's machine.

## GitHub knowledge retrieval is separate

- [Current 2026.3 beta API and working materials](https://github.com/donaldtuttle/Unofficial_KeyShot_Python) provide the scripting knowledge. Access via a **connected GitHub tool** or packaged local files.
- [Original KPSA archive](https://github.com/donaldtuttle/KeyShot-Python-AI-Knowledge) provides historical documentation and audits when authorized and accessible.
- MCP and GitHub serve distinct roles: **GitHub for reference documents**, **KeyShot MCP for the running application**. A skill may describe both without providing either integration itself.

## Test procedure before enabling scene writes

- Confirm the actual KeyShot version and that the local bridge starts and stops cleanly.
- Read status, scene tree, current camera, environment and one material without modifications.
- Compare `lux_functions` declarations to the pinned 2026.3 dumps, logging differences for review.
- Use a disposable scene to test one scoped material adjustment and its rollback semantics.
- Separately verify render and save operations only after explicit permission.
- If any step fails, disable write tools and use documentation-only mode.

See the [core agent skill](../skill.md) and [platform adapters](../skills/README.md).
