# leetcode

Auto-synced LeetCode submissions. A GitHub Action fetches my accepted solutions
from LeetCode on a schedule and commits each one here, so solving problems shows
up as contributions — similar to how NeetCode syncs.

Powered by [joshcai/leetcode-sync](https://github.com/joshcai/leetcode-sync).

## Setup (one-time secrets)

This repo needs three Actions secrets (Settings → Secrets and variables → Actions):

| Secret | What it is |
|--------|-----------|
| `LEETCODE_SESSION` | the `LEETCODE_SESSION` cookie from leetcode.com |
| `LEETCODE_CSRF_TOKEN` | the `csrftoken` cookie from leetcode.com |
| `LEETCODE_GH_TOKEN` | a GitHub personal access token with `repo` scope (so commits are attributed to me and count as contributions) |

The workflow runs hourly and can also be triggered manually from the Actions tab.
