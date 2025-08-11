install:
	uv sync
	
brain-games:
	uv run brain-games

build:
	uv build

WHEEL := $(shell ls dist/*.whl | head -n 1)

package-install:
	uv pip install $(WHEEL)
