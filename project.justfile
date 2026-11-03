## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Download NVD's modified feed into tmp/nvd-feed/, checking it against the size and
# SHA-256 that the feed's own .meta file gives
[group('model development')]
fetch-nvd-feed:
  uv run scripts/fetch_nvd_feed.py

# Validate every record of NVD's modified feed, one at a time, after fetching it.
# The feed is live, so this fails when NVD starts writing something new.
[group('model development')]
test-nvd-feed: fetch-nvd-feed
  NVD_FEED=1 uv run python -m pytest tests/test_nvd_feed.py
