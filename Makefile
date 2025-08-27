install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check brain_games
	uv run ruff format --check
	
lint-fix:
	uv run ruff check --fix brain_games
	uv run ruff format --fix
